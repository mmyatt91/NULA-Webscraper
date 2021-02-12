import json
import requests
import urllib.request
import time

from bs4 import BeautifulSoup
from forms import ResourceMenuForm

# class ResourceHandler:
"""Access the NULA Resource Page via BeautifulSoup"""

URL = 'https://www.namiurbanla.org/resources'
CATEGORIES = ['Crisis Support, Helplines & Warmlines',
            'Organizations & Campaigns',
            'Mental Health, Rehab & Counseling Services',
            'Psychiatric Inpatient Services',
            'Outpatient Clinics & Wellness Centers',
            'Urgent Care Centers',
            'Support Groups & Education Classes',
            'Transitional Age Youth Drop-In Centers & Services',
            'Benefits Assistance, Housing, Shelters & Food',
            'Peer Centers & Respites',
            'Apps',
            'Holistic Health']

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
    
    # for resource in resources:
    #     links = resource.find_all('a')
    #     for link in links:
    #         a_tags = link['href']
    #         for a_tag in a_tags:
    #             weblink = a_tag
    #             print(weblink)
    #             resourceList.append(weblink)

    return '\n'.join(resourceList)




