#!/usr/bin/python3
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/bill")
print(response.json())
