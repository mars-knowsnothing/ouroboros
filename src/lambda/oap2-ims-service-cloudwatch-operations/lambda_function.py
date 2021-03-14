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

def uri_to_arn(Arn):
    return Arn.replace('-','/')

def arn_to_uri(Arn):
    return Arn.replace('/','-')

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

def describe_alarms_for_metric(payLoad):
    _params_describe_alarms_for_metric = dict(
        MetricName = payLoad.get('MetricName'),
        Namespace = payLoad.get('Namespace'),
        Statistic = payLoad.get('Statistic'),
        ExtendedStatistic = payLoad.get('ExtendedStatistic'),
        Dimensions = payLoad.get('Dimensions'),
        Period = payLoad.get('Period'),
        Unit = payLoad.get('Unit'),
    )
    _params_describe_alarms_for_metric = {k:v for k,v in _params_describe_alarms_for_metric.items() if v!=None}
    print(_params_describe_alarms_for_metric)

    Fields=payLoad.get("Fields",None)
    DefaultFields=["AlarmArn"]
    _alarms_raw = cloudwatch_client.describe_alarms_for_metric(**_params_describe_alarms)
    return _alarms_raw["MetricAlarms"]

def uri_to_func(uri):
    funcName = uri.replace('-','_')
    return globals()[funcName]

def lambda_handler(event, context):
    # TODO implement
    print(event)
    pathParameters=event.get("pathParameters")
    if not pathParameters:
        pathParameters=dict()
    payLoad = json.loads(event["body"]) if event["body"]!=None else dict()
    print(payLoad)
    # queryStringParameters=event.get("queryStringParameters")
    # if not queryStringParameters:
    #     queryStringParameters=dict()

    ss = switch_role_to_account(accountId=pathParameters["accountid"],roleName="ims-service-role")
    cloudwatch_client = ss.client('cloudwatch')
    func = uri_to_func(pathParameters["operationid"])
    print(func,dir(func))
    result = func(payLoad)
    # try:
    #     print(_params_describe_alarms)
    #     _Alarms=list()
    #     _alarms_raw = cloudwatch_client.describe_alarms(**_params_describe_alarms)
    #     print(_alarms_raw)
    #     if Fields:
    #         _Alarms.extend([{key:d.get(key) for key in Fields.split(',')+DefaultFields} for d in _alarms_raw["MetricAlarms"]+_alarms_raw["CompositeAlarms"]])
    #     else:
    #         _Alarms.extend(_alarms_raw["MetricAlarms"])
    #     while "NextToken" in _alarms_raw:
    #         _alarms_raw = cloudwatch_client.describe_alarms(
    #             NextToken=_alarms_raw["NextToken"],
    #             **_params_describe_alarms)
    #         if Fields:
    #             _Alarms.extend([{key:d.get(key) for key in Fields.split(',')+DefaultFields} for d in _alarms_raw["MetricAlarms"]+_alarms_raw["CompositeAlarms"]])
    #         else:
    #             _Alarms.extend(_alarms_raw["MetricAlarms"])
    # except Exception as e:
    #     print(e)
    #     return {
    #         'statusCode': 400,
    #         'body': json.dumps({"message":"failed to describe instances in {account_id}".format(account_id=pathParameters["accountid"])})
    #     }
    resp = dict(
        data = result # _Alarms
    )
    return {
        'statusCode': 200,
        'body': json.dumps(resp,cls=ComplexEncoder)
    }
