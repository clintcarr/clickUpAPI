#!/usr/bin/env python
""" 
Get API calls
Version: 0.1
Date: 19/07/24
Author: Clint Carr
"""
import requests

# Use the Clickup console to create a personal token
token = 'pk_####'
# Get your teamId from the url
teamId = "####"
url = "https://api.clickup.com/api/v2/team/" + teamId + "/space"
headers = {"Authorization": token}
query = {"archived": "false"}

def get_space():
    """
    Function that performs GET to collect spaces. Samplle
    """
    response = requests.get(url.format (teamId),headers=headers, params=query)
    data = response.json()
    clSpaces = {}
    for i in data['spaces']:
        clSpaces.update({i['id']: i['name']})
    return(clSpaces)

def get_folders():
    """
    Function to return folders from clickup space
    """
    sapces = get_space()
    clFolders = {}
    for spaceId, spaceName in spaces.items():
        url = "https://api.clickup.com/api/v2/space/" + spaceId + "/folder"
        response = requests.get(url, headers=headers, params=query)
        data = response.json()
        for i in data['folders']:
            clFolders.update({i['id']: i['name']})
    return(clFolders)