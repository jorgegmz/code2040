#!/bin/bash/env python
import requests
import json

token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

endpoint_dating = "http://challenge.code2040.org/api/dating"

endpoint_validate = "http://challenge.code2040.org/api/dating/validate"

json = {"token": token}

response = requests.post(endpoint_dating, data=json)

print response.content

#assign dictionary to dict_arr with key value pairs
dict_arr = response.json()

#assign key datestamp to dict_date with value being date and time
dict_date = dict_arr["datestamp"]

print dict_date

#assign key interval to dict_interval with value interval to be added to datestamp
dict_interval = dict_arr["interval"]

print dict_interval


