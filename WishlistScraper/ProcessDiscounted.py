"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Processes scraped data to only discounted items
"""

def processData(data):
    #Filters out non discounted items
    
    for key in data:
        game_dict = data[key]
        subs = game_dict['subs']
        if subs:
            subs = subs[0]
            if not "no_discount" in subs['discount_block']:
                print(subs)





