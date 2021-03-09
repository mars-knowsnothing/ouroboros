import json
import boto3
import time
from datetime import datetime,date


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def get_ts():
	ts = time.time()
	st = datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
	return st

def switch_role_to_account(accountId,roleName,**kwargs):
    roleArn = "arn:aws-cn:iam::{accountId}:role/{roleName}".format(
        accountId=accountId,
        roleName=roleName
    )
    sts_client = boto3.client('sts')
    response = sts_client.assume_role(
        RoleArn=roleArn,
        RoleSessionName=kwargs.get('RoleSessionName','role-session-'+get_ts()),
    )
    switch_role_session = boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken']
    )
    return switch_role_session

def filters(queryStringParameters):
    _available_filters = ["tag","instance-id","instance-state-name","instance-type","private-ip-address"]
    _filters = list()
    for k,v in queryStringParameters.items():
        if k not in _available_filters and k.split(":")[0] not in _available_filters:
            continue
        _filters.append({
            'Name': k,
            'Values': v.split(',')
        })
    return _filters

def lambda_handler(event, context):
    # TODO implement
    print(event)
    pathParameters=event.get("pathParameters")
    if not pathParameters:
        pathParameters=dict()

    queryStringParameters=event.get("queryStringParameters")
    if not queryStringParameters:
        queryStringParameters=dict()
    _params_describe_instances = dict(
        Filters=filters(queryStringParameters),
        MaxResults=queryStringParameters.pop("MaxResults",50)
    )
    NextToken=queryStringParameters.pop("NextToken",None)
    if NextToken:
        _params_describe_instances["NextToken"]=NextToken

    Fields=queryStringParameters.pop("Fields",None)
    DefaultFields=["InstanceId"]
    ss = switch_role_to_account(accountId=pathParameters["accountid"],roleName="ims-service-role")
    ec2_client = ss.client('ec2')
    print(_params_describe_instances)
    _instances =list()
    try:
        _instances_raw = ec2_client.describe_instances(**_params_describe_instances)
        for Reservation in _instances_raw["Reservations"]:
            if Fields:
                _instances.extend([{key:d.get(key) for key in Fields.split(',')+DefaultFields} for d in Reservation["Instances"]])
            else:
                _instances.extend(Reservation["Instances"])
        while "NextToken" in _instances_raw:
            _instances_raw = ec2_client.describe_instances(
                NextToken=_instances_raw["NextToken"],
                **_params_describe_instances)
            for Reservation in _instances_raw["Reservations"]:
                if Fields:
                    _instances.extend([{key:d.get(key) for key in Fields.split(',')+DefaultFields} for d in Reservation["Instances"]])
                else:
                    _instances.extend(Reservation["Instances"])
    except Exception as e:
        print(_instances_raw.json())
        return {
            'statusCode': 400,
            'body': json.dumps({"message":"failed to describe instances in {account_id}".format(account_id=pathParameters["accountid"])})
        }
    resp = dict(
        data = _instances
    )
    return {
        'statusCode': 200,
        'body': json.dumps(resp,cls=ComplexEncoder)
    }
