import json
import requests
import urllib.request
import time

from bs4 import BeautifulSoup
from forms import ResourceMenuForm

# class ResourceHandler:
"""Access the NULA Resource Page via BeautifulSoup"""

URL = 'https://www.namiurbanla.org/resources'

def get_resources(category_id):

    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, "html.parser")

    resourceList = []

    i = category_id

    resources = soup.find_all('div', 's-item-text-group')[i]

    for resource in resources:
        links = resource.find_all('a')
        for link in links:
            a_tags = link['href']
            print(a_tags)
            resourceList.append(a_tags)

    return resourceList




