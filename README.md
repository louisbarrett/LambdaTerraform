# Lambda 🌍 Terraform
This is a proof of concept for running Terraform from inside an AWS lambda. I created this POC as a means of demonstrating webhook based infrastructure deployments without the use of a traditional CI system.

## Overview
The Terraform version is pinned at v0.11.11, and a single `main.tf` file must be included in the `Lambdaform.zip` file in order to plan and apply. Terraform state is not maintained between lambda runs, therefore this method is best suited to one time deployments.

TF_ACTION environment variable controls terraform runtime behavior (plan, apply, init)

TF_CLI_ARGS can be used to pass in terraform inputs for TF_VARS


```
          TF_ACTION: apply
          TF_CLI_ARGS: '-input=false'
          TF_CLI_CONFIG_FILE: ''
          TF_IN_AUTOMATION: '1'
          TF_LOG: ERROR
          TF_PLUGIN_CACHE_DIR: /tmp/plugin-cache/
```

Available TF Providers:

AWS - terraform-provider-aws_v2.21.1_x4

Local - terraform-provider-local_v1.3.0_x4

Null - terraform-provider-null_v2.1.2_x4

TLS - terraform-provider-tls_v2.0.1_x4

## Usage

1. Add *your* `main.tf` along with the provided `main.py` to a zip archive
2. Create a new AWS Lambda function using the python runtime, and upload the zip
3. Add the TF enviroment variables to your Lambda (see lambdaform.yaml)
4. Profit

## To-Do

1. Allow download of terraform plans via S3 bucket, HTTP URI, pastebin etc...
2. Allow remote state via methods above
