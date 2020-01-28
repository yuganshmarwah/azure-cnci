import logging

import azure.functions as func
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v6_0.pipelines import models
from __app__.shared_code import config

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    pipeline_id = None
    buil_run_result_url = None
    pipeline_name = config.MERGE_BUILD_PIPELINE_NAME
    project_name = config.AZURE_DEVOPS_PROJECT_NAME

    # Create a connection to the org
    credentials = BasicAuthentication('', config.AZURE_PERSONAL_ACCESS_TOKEN)
    connection = Connection(base_url=config.ORGANIZATION_URL, creds=credentials)
    try:
        # Create pipeline client for azure devops
        pipelines_client_v6_0 = connection.clients_v6_0.get_pipelines_client()

        # Find the pipeline id on the basis of given pipeline name
        pipelines = pipelines_client_v6_0.list_pipelines(project=project_name)
        for pipeline in pipelines:
            logging.info("Pipeline name:"+str(pipeline.name))
            if pipeline.name == pipeline_name:
                pipeline_id = pipeline.id
        logging.info("Pipeline id:"+str(pipeline_id))

        # Creating empty run params
        run_parameters = models.RunPipelineParameters()

        # Inititate pipeline run
        buil_run_result_url = pipelines_client_v6_0.run_pipeline(run_parameters=run_parameters,project=project_name,pipeline_id=pipeline_id)._links.additional_properties.get("web").get("href")
    except Exception as e:
        logging.error("Error due to exception: {error}".format(error=e))

    return func.HttpResponse(buil_run_result_url)        

