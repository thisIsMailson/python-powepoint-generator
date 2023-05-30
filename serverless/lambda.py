import requests

def handler(evt, context):
    res = {
        message: "Hello World!", 
        event: evt,
        context: context
    }
    print(res)
    return res