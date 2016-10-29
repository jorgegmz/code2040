#!/usr/bin/env python
import requests
import json

#API Token for authentication
token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

#github repository for code2040
repo = "https://github.com/jorgegmz/code2040"

#the API endpoint for registration
api_endpoint = "http://challenge.code2040.org/api/register"

#two dictionary keys with token and github repo
json = {"token": token, "github": repo}

#response acquired from posting endpoint and json
response = requests.post(api_endpoint, data=json)

#Response, We're good to go!
print "Response: " + response.content

