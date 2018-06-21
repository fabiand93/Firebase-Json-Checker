#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Fabian Diaz"
__email__       ="fabiandiaz@protonmail.com"
"""
------------------------------------------------------------------------------
	Firebase json Checker  - 20.06.18 - Fabian Diaz (@otraarroba)
------------------------------------------------------------------------------
"""
import requests
import os

version = str(1.0)

def banner():
    print('Firebase json Checker \nVersion '+ version +' \nMade by Fabian Diaz (@otraarroba)')

def main():
    banner()
    with open('sites.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    lines = sum(1 for line in open('sites.txt'))
    i=0
    # Define amount of lines that your file has
    while i < lines:
        requestURL = 'https://'+content[i]+'.firebaseio.com/.json'
        requestURL = str(requestURL)
        request = requests.get(requestURL)
        if request.status_code == 200:
            print ('Website exists and probably it\'s vulnerable with the url: ', requestURL)
            print (request.json())
        elif request.status_code == 404:
            print ('Website: '+ requestURL +' doesn\'t exists' )
            print ('Status Code: '+ str(request.status_code))
        else:
            print ('Website: '+ requestURL +' is safe')
            print ('Status Code: '+ str(request.status_code))
        i = i+1
main()
