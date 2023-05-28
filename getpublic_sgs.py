import json
import boto3


ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    sg_resp = ec2.describe_security_groups()
    for i in sg_resp["SecurityGroups"]:
        print("---")
        print(i)
