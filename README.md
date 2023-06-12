# This project contains automated scripts to perform security checks on AWS IAM and VPC.

All scripts are written for AWS lambda function, to make it easier for execution. If your requirement exceeds execution more then 15mins, please modify the script and run on machine.
List of scripts:

- getpublic_sgs.py - Gets the list of security groups which are open to public.
- wildcard_action_policy.py - Fetches list of policies which have Action has a wildcard in the policy, instead of providing specific permissions.
- get_accesskeys_expired.py - List of IAM users with access keys and check their date of usage, it is recommended to rotate access keys regularly.(in progress)
