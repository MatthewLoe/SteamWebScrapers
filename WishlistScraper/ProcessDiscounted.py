from decimal import Decimal

"""
Author: Matthew Loe
Date Last Modified: 1/7/2020
Description: Processes scraped data to only discounted items
"""

def processData(data):
    #Filters out non discounted items
    
    items = list()

    for key in data:
        game_dict = data[key]
        subs = game_dict['subs']
        if subs:
            subs = subs[0]
            text = subs['discount_block']
            if not "no_discount" in text:
                item = {
                    "name" : game_dict['name'],
                    "appid" : key,
                    "discount" : subs['discount_pct'],
                }

                #Find original price
                result = text.find('A$')
                item["original_price"] = text[result: result + 8]

                #Find discount price
                result = text.rfind('A$')
                item["discount_price"] = text[result: result + 8]

                items.append(item)

    return items





