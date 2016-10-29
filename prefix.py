#!/bin/bash/env python
import requests
import json

#API authentication
token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

#code2040 endpoint for prefix challenge
endpoint_prefix = "http://challenge.code2040.org/api/prefix"

#code2040 endpoint for validating output
endpoint_validate = "http://challenge.code2040.org/api/prefix/validate"

#json with token API auth
json = {"token": token}

#response containing dictionary of prefix and list of strings
response = requests.post(endpoint_prefix, data=json)

#testing to see dict
#print response.content #\n

#parse response and store in dict_res
dict_res = response.json()

#assign prefix string to variable prefix
prefix = dict_res["prefix"]

#testing to see prefix variable
#print prefix #\n

#assign list of string to variable dict_array
dict_array = dict_res["array"]

#testing to visualize list of strings
#print dict_array #\n

#initialize empty array in variable array
array = []

#iterate through dict_array and append to variable array
#strings that do not have prefix in string
for i in range(0, len(dict_array)):
    if not dict_array[i].startswith(prefix):
        array.append(dict_array[i])

#testing to see output of array
#print array #\n

#json response containing token and array
json_res = {"token": token, "array[]": array}

#assign resquests post response to  validate_res
validate_res = requests.post(endpoint_validate, data=json_res)

#print Response: We're good to go!!
print "Response " + validate_res.content
