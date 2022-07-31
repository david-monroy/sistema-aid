import json

def error_response(message,error, status):
    response = dict()
    response["error"] = error
    response["detail"]= message
    response ["status"] = status

    return json.dumps(response)