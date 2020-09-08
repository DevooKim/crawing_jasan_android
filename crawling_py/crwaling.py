from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

total_list = [] #모든 자산의 리스트

def recvJson():

    cred = credentials.Certificate('mykey.json')
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'https://craw-cd4be.firebaseio.com/'
    })

    ref = db.reference('PC')
    return ref.get()

def jsonParsing(json_file):
    
    return json_file.values()


def crawling(url_tuple):

    for url in url_tuple:
        object_list = ["PC"]
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")

        for tr in bsObject.find_all('tr'):
            num_value,spec_value = None, None

            for td in tr.find_all('td'):
                tr_list = []
                tr_list = tr.find_all(text=True)

                if(td.string == "물품번호"):
                    num_value = tr_list[3]
                    object_list.append(num_value)
                    break

                elif(td.string == "규격"):
                    spec_value = tr_list[3]
                    
                    #CPU, Ram, HDD - 구분
                    cpu, ram, hdd = None, None, None
                    spec = spec_value.split(',')
                    if len(spec) == 1:
                        cpu = spec[0]
                        ram = "X"
                        hdd = "X"
                    elif len(spec) == 2:
                        cpu = spec[0]
                        ram = spec[1]
                        hdd = "X"
                    elif len(spec) >= 3:
                        cpu = spec[0]
                        ram = spec[1]
                        hdd = spec[2]
                    #cpu, ram, hdd = spec[0], spec[1], spec[2]

                    object_list.append(cpu)
                    object_list.append(ram)
                    object_list.append(hdd)
                    break

                elif(td.string == "취득가액"):
                    price = tr_list[3]
                    object_list.append(price)
                    
        total_list.append(object_list)
         
    return total_list
    
def toCSV(asset_list):
    file = open('test.csv', 'w', encoding='cp949', newline='')
    csvfile = csv.writer(file)
    for row in asset_list:
        csvfile.writerow(row)
    file.close()
    print("수행완료")

json_file = recvJson()
value = jsonParsing(json_file)
craw = crawling(value)
toCSV(craw)
