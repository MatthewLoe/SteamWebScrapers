from WishlistScraper.ScrapeWishlist import get_wishlist
from WishlistScraper.ProcessDiscounted import processData

"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Script for running scrape
"""
#Edit url, replacing USERNAME with the user wishlist to be scraped  
url = 'https://store.steampowered.com/wishlist/id/USERNAME/#sort=order'

data = get_wishlist(url)
processData(data)
