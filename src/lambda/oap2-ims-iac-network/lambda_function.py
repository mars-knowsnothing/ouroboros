import json
import troposphere
import requests

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


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


class Network(object):
    def __init__(self, metadata, spec, **context):
        self.Environment = context['Environment']
        self.Template = Template()
        self.outputs = []
        self.spec = spec
        self.context = context
        self.metadata = metadata
        self.AZs = ['cn-north-1a', 'cn-north-1b']
        self.Netmask = spec.get('Netmask', 28)
        self.name = metadata['name']

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
