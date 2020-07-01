from WishlistScraper.ScrapeWishlist import get_wishlist
from WishlistScraper.ProcessDiscounted import processData

"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Script for running scrape
"""

data = get_wishlist()
processData(data)