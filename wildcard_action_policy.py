import json
import boto3
import os

iam = boto3.client('iam')
sns = boto3.client('sns')

snsarn = os.environ['TOPIC_ARN']

## send mail
def sendemail(subject, message):
    response = sns.publish(
        TopicArn=snsarn,
        Message=message,
        Subject=subject
    )
    
def lambda_handler(event, context):
    ## get all policies only attached
    response = iam.list_policies(
        Scope='All',
        OnlyAttached=True,
        )
    arns=[]
    for i in response["Policies"]:
        arn = i["Arn"]
        pol_d = iam.get_policy_version(
            PolicyArn=arn,
            VersionId = i["DefaultVersionId"]
            )
        for x in pol_d["PolicyVersion"]["Document"]["Statement"]:
            perm = x["Action"]
            if isinstance(perm, list):
                for p in perm:
                    ## condition to end with wildcard in action
                    if p.endswith("*"):
                        if arn not in arns:
                            arns.append(str(arn))
            else:
                ## condition to end with wildcard in action
                if perm.endswith("*"):
                    if arn not in arns:
                        arns.append(str(arn))
    msg="\n".join(arns)
    sub="List of policies with wildcard in Action"
    sendemail(sub, msg)
    

