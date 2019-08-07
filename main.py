import os
import json
import subprocess 

def lambda_handler(event, context):
    # TODO implement

    subprocess.check_output(["cp","/var/task/terraform","/tmp/terraform"])
    subprocess.check_output(["cp","/var/task/main.tf","/tmp/main.tf"])

## Manually initialize terraform
    #AWS Provider
    subprocess.check_output(["curl","https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-aws_v2.21.1_x4","--output","/tmp/terraform-provider-aws_v2.21.1_x4"])
    subprocess.check_output(["chmod","+x","/tmp/terraform-provider-aws_v2.21.1_x4"])
    
    #Local Provider
    subprocess.check_output(["curl","https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-local_v1.3.0_x4","--output","/tmp/terraform-provider-local_v1.3.0_x4"])
    subprocess.check_output(["chmod","+x","/tmp/terraform-provider-local_v1.3.0_x4"])

    #https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-null_v2.1.2_x4

    #Null Provider
    subprocess.check_output(["curl","https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-null_v2.1.2_x4","--output","/tmp/terraform-provider-null_v2.1.2_x4"])
    subprocess.check_output(["chmod","+x","/tmp/terraform-provider-null_v2.1.2_x4"])


    #https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-tls_v2.0.1_x4
    subprocess.check_output(["curl","https://terraform-providers-test.s3-us-west-2.amazonaws.com/terraform-provider-tls_v2.0.1_x4","--output","/tmp/terraform-provider-tls_v2.0.1_x4"])
    subprocess.check_output(["chmod","+x","/tmp/terraform-provider-tls_v2.0.1_x4"])

## Finish initializing terraform
    os.chdir("/tmp")
    # print(subprocess.check_output(["/tmp/terraform","init"]))
    Action = os.environ["TF_ACTION"]
    print(subprocess.check_output(["/tmp/terraform",Action]))
    # print(event)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
