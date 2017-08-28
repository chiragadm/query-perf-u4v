#!/usr/bin/python
###################################################################################################
# Author: Chirag Patel
# Purpose: This python script demonstrates example on querying Unisphere database
# for performance metrics. It uses REST API call to query information. This code has adopted from
# code dellemc pyu4v.
# Notes: You will need to set following variables to successfully run this script. 
#        unimaxURI = "you unisphere DNS with port with /univmax/restapi added at the end"
#                    "for example: https://unisphere.abc.com:8443/univmax/restapi"
#        username = "unisphere username with perfmonitor and monitor RBAC."
#        password = "user password"
#        symmId = "12 digit vmax serial number that is managed by above unisphere server."
#
###################################################################################################


###################################################################################################
# Import Statements
###################################################################################################
import requests
import json
import time
from requests.auth import HTTPBasicAuth
#import urllib3
#urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning # It disable ssl warnings

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # It disable ssl warnings
 
 
###################################################################################################
# Variables
###################################################################################################
#unimaxURI = 'https://unisphere.abc.com:8443/univmax/restapi'
#username = 'username'
#password = 'password'
#symmId = '000196700000'
# Following generates epoch time range for last 24 hours.
endDate = int(time.time()) * 1000
startDate = endDate - 86400000
 
 
###################################################################################################
# REST API Class That Does GET & POST Methods
###################################################################################################
class u4vmaxRest:
        # Define basic of this class
        def __init__(self, u4vmaxURL, username, password):
                self.headers = {'Content-Type' : 'application/json' }
                self.URL = u4vmaxURL
                self.username = username
                self.password = password
                self.symID = ""
                self.payload = {}

        def doGet(self,restURI):
                # Following will construct URL by combining base URI with passed path.
                url = "%s/%s" % (self.URL,restURI)
 
 
                # verify=False will let us ignore the SSL Cert error
                r_info = requests.get(url,headers=self.headers, verify=False, auth=HTTPBasicAuth(self.username,self.password))
                # Following will convert JSON into python dict.
                data = r_info.json()
                return data
 
        def doPost(self,restURI,payload):
                # Following will construct URL by combining base URI with passed path.
                url = "%s/%s" % (self.URL,restURI)
                # verify=False will let us ignore the SSL Cert error
                r_info = requests.post(url,headers=self.headers, data=json.dumps(payload),verify=False, auth=HTTPBasicAuth(self.username,self.password))
                # Following will convert JSON into python dict.
                print (type(r_info))
                data = r_info.json()
                return data
 
 
###################################################################################################
# Instantiate the class
###################################################################################################
u4vmax = u4vmaxRest(unimaxURI,username, password)
 
###################################################################################################
# Get Method:
###################################################################################################
 
###################################################################################################
# Example of getting Unisphere runtime info (not important)
###################################################################################################
#data = u4vmax.doGet('management/RuntimeUsage/read')
#print (json.dumps(data,indent=4))
 
 
###################################################################################################
# Example of getting list of frames and first and last available metrics dates.
###################################################################################################
#data = u4vmax.doGet('performance/Array/keys')
#print (json.dumps(data,indent=4))
 
###################################################################################################
# Example to get list of all directors (FA,DA,RF,EDS,)
###################################################################################################
#new_ur="sloprovisioning/symmetrix/" + symmId + "/director"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))
 
###################################################################################################
# Example to get list of storage groups
###################################################################################################
#new_ur="sloprovisioning/symmetrix/" + symmId + "/storagegroup"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))
 
###################################################################################################
# Example to get list of all ports (FA,DA,RF)
###################################################################################################
#new_ur="sloprovisioning/symmetrix/" + symmId + "/port"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to get list of all initiators
###################################################################################################
# all hba that once discovered on frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/initiator"
# hba that are login to frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/initiator?logged_in=true"
# hba that has masking views
#new_ur="sloprovisioning/symmetrix/" + symmId + "/initiator?num_of_masking_views>1"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to get info on initiator	
###################################################################################################
# all hba that once discovered on frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/initiator/FA-4D:28:20024c00000000df"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to get info on initiator group
###################################################################################################
# all hba that once discovered on frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/hostgroup/IG_LNXDB-PRD-201-205-209_PSA"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to list masking view
###################################################################################################
# all hba that once discovered on frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/maskingview"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to get detail info on masking view
###################################################################################################
# all hba that once discovered on frame
#new_ur="sloprovisioning/symmetrix/" + symmId + "/maskingview/MV_DBC-PRD1-2101_A"
#data = u4vmax.doGet(new_ur)
#print (json.dumps(data,indent=4))

###################################################################################################
# POST Method: A POST requires a payload. We build a dict with the values corresponding to the
# schema. The start and end Date are the same so we aren't going to get anything interesting.
###################################################################################################
 
###################################################################################################
# Example to query Storage Group Matrics
###################################################################################################
#payload = { 
#  "startDate" : startDate,
#  "endDate" : endDate,
#  "symmetrixId" : symmId,
#  "storageGroupId" : "SG_CTSPRD_DT01_SA",
#  "dataFormat" : "Average",
#  "metrics" : [ "HostIOs", "ResponseTime", "HostMBs"]
#}
 
#data = u4vmax.doPost('performance/StorageGroup/metrics',payload)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to query List of FE Director 
###################################################################################################
payload = { 
  "symmetrixId" : symmId,
}
 
data = u4vmax.doPost('performance/FEDirector/keys',payload)
#print (data)
print (json.dumps(data, indent=4))

###################################################################################################
# Example to query FE Director Matrics
###################################################################################################
#payload = { 
#  "startDate" : startDate,
#  "endDate" : endDate,
#  "symmetrixId" : symmId,
#  "directorId" : "FA-1D",
#  "dataFormat" : "Average",
#  "metrics" : [ "PercentBusy", "HostIOs", "HostMBs"]
#}
 
#data = u4vmax.doPost('performance/FEDirector/metrics',payload)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to query FA Port Matrics
###################################################################################################
#payload = { 
#  "startDate" : startDate,
#  "endDate" : endDate,
#  "symmetrixId" : symmId,
#  "directorId" : "FA-1D",
#  "portId" : "24",
#  "dataFormat" : "Average",
#  "metrics" : [ "IOs", "MBs", "AvgIOSize", "PercentBusy"]
#}
 
#data = u4vmax.doPost('performance/FEPort/metrics',payload)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to query BE Director Matrics
###################################################################################################
#payload = { 
#  "startDate" : startDate,
#  "endDate" : endDate,
#  "symmetrixId" : symmId,
#  "directorId" : "DF-1C",
#  "dataFormat" : "Average",
#  "metrics" : [ "PercentBusy"]
#}
 
#data = u4vmax.doPost('performance/BEDirector/metrics',payload)
#print (json.dumps(data,indent=4))

###################################################################################################
# Example to query EDS Director Matrics
###################################################################################################
payload = { 
  "startDate" : startDate,
  "endDate" : endDate,
  "symmetrixId" : symmId,
  "directorId" : "ED-1B",
  "dataFormat" : "Average",
  "metrics" : ["PercentBusy"]
}
 
data = u4vmax.doPost('performance/EDSDirector/metrics',payload)
print (json.dumps(data,indent=4))

###################################################################################################
# Example to query Cache Usage
###################################################################################################
#payload = { 
#  "startDate" : startDate,
#  "endDate" : endDate,
#  "symmetrixId" : symmId,
#  "dataFormat" : "Average",
#  "metrics" : ["PercentCacheWP"]
#}

#data = u4vmax.doPost('performance/Array/metrics',payload)
#print (json.dumps(data,indent=4))


