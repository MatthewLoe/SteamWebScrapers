from contextlib import closing
from requests import get
from requests.exceptions import RequestException

import json
import re

"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Scrapes person's wishlist and returns the data on all wishlisted items
"""

def get_wishlist(url):
    #Attempts to get wishlist of specified user 
    
    response = get_text(url)

    if response is not None:
        wishlist_url = json.loads( re.findall(r'g_strWishlistBaseURL = (".*?");', get_text(url))[0] )
        
        data = get(wishlist_url + 'wishlistdata/?p=0').json()

        return data

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def get_text(url):
    #Retrieves HTML text of url

    try:
        with closing(get(url, stream=True)) as response:
            if is_good_response(response):
                return response.text
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    #Returns True if response seems to be HTML

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    #Logs error to command line

    print(e)
