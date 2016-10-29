#!/bin/bash/env/ python
import requests
import json

#API token for authentication
token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

#url endpoint of string to reverse
endpoint_reverse = "http://challenge.code2040.org/api/reverse"

#url endpoint to validate string reverse
endpoint_validate = "http://challenge.code2040.org/api/reverse/validate"

#json dict
json = {"token": token}

#assigns string to response if post was successful
response = requests.post(endpoint_reverse, data=json)

#temporary variable of string
tmp = response.text

#testing tmp
#print tmp

#reversing string
rev = tmp[::-1]

#testing if string was reversed
#print rev

#json dict with two keys: first is auth token and second string reversed
json_val = {"token": token, "string": rev}

#assign string to validate_res if post was successful with endpoint_validate
validate_res = requests.post(endpoint_validate, data=json_val)

#print response from post: We're good to go!
print "Response " + validate_res.content
