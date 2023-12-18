import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("A hello request has been completed!")

