import boto3
import json
import sys

region = 'us-west-1'
ec2c = boto3.client('ec2',  region)
resp = ec2c.describe_subnets()
vpcid = resp['Subnets'][0]['VpcId']
subnetlist = ec2c.describe_subnets(Filters = [{'Name':'vpc-id','Values':[vpcid] }])
subnetid = subnetlist['Subnets'][0]['SubnetId']


if __name__ == '__main__':

   print('subnetid > ', subnetid)
   print('vpcid > ', vpcid)
