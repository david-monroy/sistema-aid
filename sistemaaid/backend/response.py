import json
from rest_framework import status

def error_response(message,error):
    response = dict()
    response["error"] = error
    response["detail"]= message
    response ["status"] = status.HTTP_400_BAD_REQUEST

    return json.dumps(response)

def response(message):
    response = dict()
    response["error"] = ""
    response["detail"]= message
    response ["status"] = status.HTTP_200_OK

    return json.dumps(response)