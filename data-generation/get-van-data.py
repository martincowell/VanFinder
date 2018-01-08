import json
import urllib.request
import time
from selenium import webdriver
from operator import itemgetter
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re
from random import randint

def get_temp_vals(td):
    return list(map(lambda x: int(x.get_text().strip().replace('\xa0°F', '')), td.find_all('td')[1:]))

def get_prec_vals(td):
    vals = list(map(lambda x: x.get_text().strip().replace('\xa0in', ''), td.find_all('td')[1:]))[:-1]
    return list(map(lambda x: 0 if x == '-' else float(x), vals))

car_id = 'd2219'
zip = 90278
distance = 50000
page = 1

driver = webdriver.Firefox()

def get_cargurus(car_id, zip, distance, page):
    # url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=' \
    #       'carGurusHomePage_false_0&' \
    #       'newSearchFromOverviewPage=true&' \
    #       'inventorySearchWidgetType=AUTO&' \
    #       'entitySelectingHelper.selectedEntity=' + str(car_id) + '&' \
    #       'entitySelectingHelper.selectedEntity2=&' \
    #       'zip=' + str(zip) + '&' \
    #       'distance=' + str(distance) + '&' \
    #       'searchChanged=true&' \
    #       'trimNames=2500+144+WB+Cargo+Van&' \
    #       'modelChanged=false&' \
    #       'filtersModified=true' \
    #       '#resultsPage=' + str(page)

    # Sprinter 2500 Cargo 144
    url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&entitySelectingHelper.selectedEntity=d2219&entitySelectingHelper.selectedEntity2=&zip=90278&distance=50000&searchChanged=true&trimNames=2500+144+WB+Cargo+Van&modelChanged=false&filtersModified=true' \
          '#resultsPage=' + str(page)

    # Sprinter 2500 Crew 144
    url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&entitySelectingHelper.selectedEntity=d1830&entitySelectingHelper.selectedEntity2=&zip=90278&distance=50000&searchChanged=true&trimNames=2500+144+WB+Crew+Van&modelChanged=false&filtersModified=true' \
         '#resultsPage=' + str(page)

    print(url)

    driver.get(url)
    # if page == 1:
    time.sleep(randint(5, 8))
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

        # response = urllib.request.urlopen(url)
        # bs = BeautifulSoup(response.read(), 'html.parser')

    #time.sleep(randint(5, 10))
    reg_exp = re.compile('listing_[0-9]+')
    results = bs.find(id='listingsDiv').find_all('div', id=reg_exp)
    print('---got all listings')
    print(results)
    # print(list(results))

    # get price data
    for res in results:
        price_tag = res.find(string='Price:')
        price = 0
        if price_tag is not None:
            price = int(price_tag.find_parent('p').find('span').find_all('span')[0].get_text().strip().replace('$', '').replace(',', '').replace('No Price Listed','0'))
        prices.append(price)
    print(prices)

    # get mileage data
    for res in results:
        mile_tag = res.find(string='Mileage:')
        mileage = 0
        if mile_tag is not None:
            mileage = int(mile_tag.find_parent('p').get_text().strip().replace('Mileage: ', '').replace(' mi', '').replace(',', '').replace('N/A', '0'))
        mileages.append(mileage)
    print(mileages)

    # # get IMV data
    # for res in results:
    #     IMV_tag = res.find(string='cg-dealfinder-result-deal-imv ')
    #     IMV = 0
    #     if IMV_tag is not None:
    #         IMV = int(IMV_tag.find_parent('p').get_text().strip().replace('CarGurus IMV of ', '').replace('$', '').replace(',', ''))
    #     IMVs.append(IMV)
    # print(IMVs)

    #return dict(mileages=mileages, prices=prices, IMVs=IMVs)
    return dict(mileages=mileages, prices=prices)


def get_carscom(car_id, zip, distance, page):
    url = 'https://www.cars.com/for-sale/searchresults.action/?mdId=22183&' \
        'mkId=20028&' \
        'page=1&' \
        'perPage=100&' \
        'rd=99999&' \
        'searchSource=PAGINATION&' \
        'sort=relevance&' \
        'stkTypId=28881&' \
        'trId=22711&' \
        'zc=90278'

    print(url)

    driver.get(url)
    # if page == 1:
    #time.sleep(randint(5, 8))
    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')

    reg_exp = re.compile('listing-[0-9]+')
    results = bs.find(id='listings').find_all('div', id=reg_exp)
    print('---got all listings')
    #   print(results)

    # get price data
    for res in results:
        price_tag = res.find('span', 'listing-row__price')
        #print(price_tag)
        price = 0
        if price_tag is not None:
            price = int(price_tag.get_text().strip().replace('$', '').replace(',', '').replace('Not Priced','0'))
        prices.append(price)
    print(prices)

    # get mileage data
    for res in results:
        mile_tag = res.find('span', 'listing-row__mileage')
        mileage = 0
        if mile_tag is not None:
            mileage = int(mile_tag.get_text().strip().replace(' mi.', '').replace(',', '').replace('N/A', '0'))
        mileages.append(mileage)
    print(mileages)

    return dict(mileages=mileages, prices=prices)

def save_as_json(fname, data):
    file = open('csv/' + fname +'.json', 'w', encoding='utf8')
    json_data = json.dumps(data, ensure_ascii=False)
    file.write(json_data)
    file.close()

prices = []
mileages = []

if 1:
    fname = 'cargurus'
    for i in range(1, 3 + 1):
        data = get_cargurus(car_id, zip, distance, i)
        save_as_json(fname, data)
        print('page ' + str(i))

if 0:
    fname = 'carscom'
    for i in range(1, 1+1):
        data = get_carscom(car_id, zip, distance, i)
        save_as_json(fname, data)
        print('page ' + str(i))
