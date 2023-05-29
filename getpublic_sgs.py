import json
import boto3


ec2 = boto3.client('ec2')

def sendemail(subject, message):
    response = sns.publish(
        TopicArn=snsarn,
        Message=message,
        Subject=subject
    )
    
pub_sgs=[]

def lambda_handler(event, context):
    sg_resp = ec2.describe_security_groups()
    for i in sg_resp["SecurityGroups"]:
        for x in i["IpPermissions"]:
            if len(x["IpRanges"]) != 0:
                if x["IpRanges"][0]["CidrIp"] == "0.0.0.0/0":
                    pubsg= str(x["FromPort"]) + " port is open to public for security group " + i["GroupId"]
                    pub_sgs.append(pubsg)
    
    msg="\n".join(pub_sgs)
    sub="List of public security groups open to any port"
