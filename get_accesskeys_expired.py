import json
import os
import boto3

iam = boto3.client('iam')

def lambda_handler(event, context):
    all_users = iam.list_users()
    for user in all_users['Users']:
        u = user['UserName']
        all_accesskeys = iam.list_access_keys(
            UserName=u,
        )
        print(all_accesskeys)
