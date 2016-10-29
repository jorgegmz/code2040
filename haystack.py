#!/bin/bash/env python
import requests
import json

#API authentication token
token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

#endpoint for haystack challenge
endpoint_haystack = "http://challenge.code2040.org/api/haystack"

#endpoint to validate code
endpoint_validate = "http://challenge.code2040.org/api/haystack/validate"

#json token
json = {"token": token}

#dict of needle keyword and list of strings with keyword needle
response = requests.post(endpoint_haystack, data=json)

#testing to see output
#print response.content

#used to parse dict
dict_needle = response.json()

#testing to see parsed dict
#print dict_needle

#obtain keyword for key needle and only view values from this key
needle = dict_needle["needle"]

#testing to view values from key, needle
#print needle

#obtain keyword for key haystack and only view values from this key
haystack = dict_needle["haystack"]

#testing to view values from key, haystack
#print haystack

#iterate through values from key haystack and initiate a counter
#to obtain the index of where the value is located if the value
#from key needle is equal to the value from key haystack
for i in range(0, len(haystack)):
    if needle == haystack[i]:
       # print i
        idx = i

#json token with index from found value
json_res = {"token": token, "needle": idx}

#validate response from post requests to api endpoint
validate_res = requests.post(endpoint_validate, data=json_res)

#response printed. We're good to go!!
print "Response " + validate_res.content
