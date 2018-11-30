from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import urllib3
import json

def call_api(url,fields={}):
    http = urllib3.PoolManager()
    r = http.request('GET',
        url,
        fields=fields,
        headers={
                 'Private-Token':'YourPrivateToken'
                })
        
    response = json.loads(r.data.decode('utf-8'))
    return response