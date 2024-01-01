import requests

def headers_json(url,headers,data):
    headers['Content-Type']="application/json; charset=UTF-8"
    response =requests.put(url,headers=headers,json=data)
    return response