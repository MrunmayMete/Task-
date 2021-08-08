#second python project

import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX = 3

for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div" , {"class": "hotelcardlisting"})
    scrapped_info_list = []

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHoteldescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAdress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text 
        #tray... except block
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        
        parent_amrneties_element = hotel.find("div", {"class":"amenityWrapper"})
        
        ammenities__list = []

        for amenity in parent_amrneties_element.find_all("div", {"class":"amenityWrapper__amenity"}):
            ammenities__list.append(amenity.find("span", {"class": "d-body-smd-textEllipsis"}).text.strip())

        hotel_dict["amenities"] = ",".join(ammenities__list[:-1])

        #print(hote_name, hotel_adress, hotel_price, hotel_rating,ammenities__list)

        scrapped_info_list.append(hotel_dict)

    dataFrame = pandas.DataFrame(scrapped_info_list)
    dataFrame.to_csv("Oyo.csv")