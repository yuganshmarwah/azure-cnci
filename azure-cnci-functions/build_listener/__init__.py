import logging
import re

import azure.functions as func
from __app__.shared_code import config, slack_utils


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    slack_message = {}
    message = ""
    try:
        event = req.get_json()
        event_type =  event.get("eventType")

        if event_type == "build.complete":
            resource = event.get("resource")
            status = resource.get("status")
            build_id = resource.get("id")
            reason = resource.get("reason")
            build_pipeline = resource.get("definition").get("name")
        elif event_type == "ms.vss-pipelines.run-state-changed-event":
            event_message = event.get("message").get("text")
            regex = r"buildId=([0-9]{2})"
            build_id_search = re.search(regex, event.get("message").get("html"), re.IGNORECASE)

            if build_id_search:
                build_id = build_id_search.group(1)
            else:
                raise Exception("BuildId not found in event {event_type}".format(event_type=event_type))

            if "in progress" in event_message:
                status = "inprogress"
            elif "cancelled" in event_message:
                status = "cancelled"
            else:
                raise Exception("No other event to he handled with event type {event_type}".format(event_type=event_type))

        LOG = "<"+config.AZURE_PIPELINE_BUILD_RESULT_URL.format(build_id=build_id)+"| `Build Number: {build_id}`>".format(build_id=build_id)

        if status == "succeeded":
            message = "Build `successfull` for {log_url}".format(log_url=LOG)
            if reason == "validateShelveset":
                message += " ready to merge."
            elif reason == "individualCI" and build_pipeline == config.STAGE_BUILD_PIPELINE:
                message += "\n Click <"+config.STAGE_ENV_URL+"| here to go to staging environment"
            elif build_pipeline == config.PROD_BUILD_PIPELINE:
                message += "\n Click <"+config.PROD_ENV_URL+"| here to go to production environment"
        elif status == "failed":
            message = "Build `failed` for {log_url}".format(log_url=LOG)
        elif status == "inprogress":
            message = "Build `in progress` for {log_url}".format(log_url=LOG)
        elif status == "cancelled":
            message = "Build `cancelled` for {log_url}".format(log_url=LOG)

        slack_client = slack_utils.get_client(access_token = config.CICD_BOT_TOKEN)
        slack_message.update( {"attachments": [{"fallback": message,
                                                "text":message}]} )
        slack_utils.send_message(client = slack_client, message = message, channel = config.SLACK_CHANNEL)
    except Exception as e:
        logging.error("Error occured due to exception: {error}".format(error=e))

    return func.HttpResponse(
            "Event successfully served!!",
            status_code=200
    )
