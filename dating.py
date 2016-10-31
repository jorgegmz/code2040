#!/bin/bash/env python
import requests
import json
import datetime

#API authorization token
token = "92126c5c427966f9f5e8e7dcdb6d7a3b"

#endpoint to receive dictionary
endpoint_dating = "http://challenge.code2040.org/api/dating"

#endpoint which is used to validate assignment
endpoint_validate = "http://challenge.code2040.org/api/dating/validate"

#json with token
json = {"token": token}

#assign dictionary to response
response = requests.post(endpoint_dating, data=json)

#testing to view elements of dictionary
#print response.content

#assign dictionary to dict_arr with key value pairs
dict_arr = response.json()

#assign key datestamp to dict_date with value being date and time
dict_date = dict_arr["datestamp"]


#assign key interval to dict_interval with value interval to be added to datestamp
dict_interval = dict_arr["interval"]

#testing to view element of key interval
#print dict_interval

#parse each element in array. This will help for later use
#when having to add interval to date
yr = dict_date[:4]
mnth = dict_date[5:7]
day = dict_date[8:10]
hr = dict_date[11:13]
minute = dict_date[14:16]
sec = dict_date[17:19]

#datetime is a module for manipulating dates and times
time = datetime.datetime(int(yr), int(mnth), int(day), int(hr), int(minute), int(sec))

#this adds the dict_interval to time
updated_time = time + datetime.timedelta(seconds=dict_interval)

#testing to view correct output
#print updated_time

#here response_time is formatted and 'Z' and appended to time
response_time = updated_time.isoformat()+'Z'

#testing to verify correct output
#print response_time

#json dictionary with token and updated time
json_res = {"token": token, "datestamp": response_time}

#assign output from updated response time to validate_res
validate_res = requests.post(endpoint_validate, data=json_res)

#Response to step 5: We're good to go!!
print "Response " + validate_res.content
