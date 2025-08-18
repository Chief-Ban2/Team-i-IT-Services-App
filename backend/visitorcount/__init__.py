import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function processed a request.')
    return func.HttpResponse('{"count":0}', mimetype="application/json")
