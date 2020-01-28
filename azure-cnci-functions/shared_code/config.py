AZURE_PIPELINE_BUILD_RESULT_URL = "https://dev.azure.com/azurecnci/azure-cnci/_build/results?buildId={build_id}&view=results"
AZURE_PERSONAL_ACCESS_TOKEN = "wlcnlx5skscqmbukst462zjpvjbgrswygaamz5fmjwkpzmeabhlq"
ORGANIZATION_URL = "https://dev.azure.com/azurecnci"
AZURE_DEVOPS_PROJECT_NAME = 'azure-cnci'
MERGE_BUILD_PIPELINE_NAME = 'yuganshmarwah.azure-cnci (1)'
# CICD_BOT_TOKEN = "xoxb-2169257353-776335030674-quuqnlpTZQogvOIR82Mxo4Xq"
CICD_BOT_TOKEN = "xoxp-904796246228-907111961575-895894997697-fbf04caa72c4c6ff45097be88ad650c5"
REPO_NAME = "azure-cnci"
GITHUM_ORG = "yuganshmarwah"
GIT_PR_LINK = "https://github.com/{org}/{repo_name}/pull/{pull_number}"
GIT_PR_TEXT = "{repo_name}/pull/{pull_number}"
STAGE_BUILD_PIPELINE = "build-deploy-stage"
PROD_BUILD_PIPELINE = "build-deploy-prod"
STAGE_ENV_URL = "http://52.149.174.38"
PROD_ENV_URL = "http://52.149.174.38"
SLACK_CHANNEL = "#testchannelhcc1"
SLACK_RES_COLORS = {
                        "SUCCESS": "#28c72a",
                        "FAILURE": "#eb0011",
                        "QUEUED": "#0083cc",
                        "WORKING": "#07b5ff",
                        "INTERNAL_ERROR": "#eb0011",
                        "TIMEOUT": "#f40072",
                        "CANCELLED": "#3a4247"
                    }