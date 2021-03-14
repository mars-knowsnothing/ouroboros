# VPC
# 1 Internet GW
# N * NAT GW Subnets (N=num of AZs)
# N Transit GW Subnets
# 1 Public Route Table
#   Default Route -> Internet GW
# N Private Route Table
#   Default Route -> NAT GW of the AZ
#   S3 Endpoint Route -> S3 Endpoint
# 1 Transit GW
# 1 Transit GW Route Table

# N * NAT GWs
