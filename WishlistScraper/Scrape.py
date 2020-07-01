from . import get_wishlist
from . import scrape_wishlist

"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Script for running scrape
"""

data = get_wishlist()
scrape_wishlist(data)