import json
import boto3
import os


ec2 = boto3.client('ec2')
sns = boto3.client('sns')

snsarn = os.environ['TOPIC_ARN']

def sendemail(subject, message):
    response = sns.publish(
        TopicArn=snsarn,
        Message=message,
        Subject=subject
    )
    
    
def lambda_handler(event, context):
    sg_resp = ec2.describe_security_groups()
    pub_sgs=[]
    for i in sg_resp["SecurityGroups"]:
        for x in i["IpPermissions"]:
            if len(x["IpRanges"]) != 0:
                if x["IpRanges"][0]["CidrIp"] == "0.0.0.0/0":
                    pubsg= str(x["FromPort"]) + " port is open to public for security group " + i["GroupId"]
                    pub_sgs.append(pubsg)
                    
    msg="\n".join(pub_sgs)
    print(msg)
    sub="List of public security groups open to any port"
    sendemail(sub, msg)
