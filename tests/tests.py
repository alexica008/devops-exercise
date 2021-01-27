#!/usr/bin/python3

import requests

page1 = requests.get('http://10.0.0.11')
page2 = requests.get('http://10.0.0.11:')

if ("httpd_1" in page1.text or "httpd_2" in page1.text) and ("httpd_1" in page2.text or "httpd_2" in page2.text):
  print ("da")
else:
  print ("nu")
