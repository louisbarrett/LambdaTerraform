# LambdaTerraform
Run Terraform from inside an AWS lambda

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
