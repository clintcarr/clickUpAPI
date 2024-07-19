# !/usr/bin/env python
""" 
Small script to generate a basic view of a Clickup Hierarchy
Version: 0.1
Date: 16/07/24
Author: Clint Carr
"""
import json, requests
from apis.get import clGet



if __name__ == '__main__':
    clSpace = clGet.get_space()


    print(clSpace)