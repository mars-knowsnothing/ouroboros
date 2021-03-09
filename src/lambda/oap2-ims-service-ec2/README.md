## Sample Event
### AWS API Gateway - HTTP Requests
```python
{
  'resource': '/accouns/{accountid}/services/{serviceid}/instances',
  'path': '/accouns/843064179036/services/ec2/instances',
  'httpMethod': 'GET',
  'headers': {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Host': 'aqu5oyrzna.execute-api.cn-north-1.amazonaws.com.cn',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'X-Amzn-Trace-Id': 'Root=1-603f527f-0155d50f150cc8b952cbe1f6',
    'X-Forwarded-For': '223.104.39.93',
    'X-Forwarded-Port': '443',
    'X-Forwarded-Proto': 'https'
  },
  'multiValueHeaders': {
    'accept': [
      'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ],
    'accept-encoding': [
      'gzip, deflate, br'
    ],
    'accept-language': [
      'zh-CN,zh;q=0.9'
    ],
    'Host': [
      'aqu5oyrzna.execute-api.cn-north-1.amazonaws.com.cn'
    ],
    'sec-fetch-dest': [
      'document'
    ],
    'sec-fetch-mode': [
      'navigate'
    ],
    'sec-fetch-site': [
      'none'
    ],
    'sec-fetch-user': [
      '?1'
    ],
    'upgrade-insecure-requests': [
      '1'
    ],
    'User-Agent': [
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    ],
    'X-Amzn-Trace-Id': [
      'Root=1-603f527f-0155d50f150cc8b952cbe1f6'
    ],
    'X-Forwarded-For': [
      '223.104.39.93'
    ],
    'X-Forwarded-Port': [
      '443'
    ],
    'X-Forwarded-Proto': [
      'https'
    ]
  },
  'queryStringParameters': None,
  'multiValueQueryStringParameters': None,
  'pathParameters': {
    'serviceid': 'ec2',
    'accountid': '843064179036'
  },
  'stageVariables': None,
  'requestContext': {
    'resourceId': 'wt1ru4',
    'resourcePath': '/accouns/{accountid}/services/{serviceid}/instances',
    'httpMethod': 'GET',
    'extendedRequestId': 'bmnT7E8SBTIFZkw=',
    'requestTime': '03/Mar/2021:09:10:23 +0000',
    'path': '/dev/accouns/843064179036/services/ec2/instances',
    'accountId': '843403612003',
    'protocol': 'HTTP/1.1',
    'stage': 'dev',
    'domainPrefix': 'aqu5oyrzna',
    'requestTimeEpoch': 1614762623428,
    'requestId': '38458a02-f42e-43dd-bde5-9373ab3cbeba',
    'identity': {
      'cognitoIdentityPoolId': None,
      'accountId': None,
      'cognitoIdentityId': None,
      'caller': None,
      'sourceIp': '223.104.39.93',
      'principalOrgId': None,
      'accessKey': None,
      'cognitoAuthenticationType': None,
      'cognitoAuthenticationProvider': None,
      'userArn': None,
      'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
      'user': None
    },
    'domainName': 'aqu5oyrzna.execute-api.cn-north-1.amazonaws.com.cn',
    'apiId': 'aqu5oyrzna'
  },
  'body': None,
  'isBase64Encoded': False
}
```
