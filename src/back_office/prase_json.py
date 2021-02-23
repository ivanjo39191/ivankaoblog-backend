#!/usr/bin/env python
# coding: utf-8

import datetime, os, sys, re

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
site_packages = os.path.join(PROJECT_ROOT, '../libs')
if site_packages not in sys.path:
    sys.path.insert(0, site_packages)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('..')
import dotenv
dotenv.load_dotenv(os.path.join(os.path.dirname(PROJECT_ROOT), '../.env'), True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import pymysql
pymysql.install_as_MySQLdb()

from django.db.utils import DatabaseError,IntegrityError
from django.db.models.fields import TextField
from django.conf import settings
import django
django.setup()
import requests, json
import django.db.backends.utils
from django.db import OperationalError
from django.core.files import File
from travel.models import *


def writedb():
    responese = requests.get('http://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json')
    results = responese.json()['XML_Head']['Infos']['Info']
    count = 0
    for result in results[0:1000]:
        count+=1
        print(count)
        json_d = result["Id"] if "Id" in result else ''
        name = result["Name"] if "Name" in result else ''
        zone = result["Zone"] if "Zone" in result else ''
        toldescribe = result["Toldescribe"] if "Toldescribe" in result else ''
        description = result["Description"] if "Description" in result else ''
        add = result["Add"] if "Add" in result else ''
        zipcode = result["Zipcode"] if "Zipcode" in result else ''
        region = result["Region"] if "Region" in result else ''
        town = result["Town"] if "Town" in result else ''
        tel = result["Tel"] if "Tel" in result else ''
        travellinginfo = result["Travellinginfo"] if "Travellinginfo" in result else ''
        opentime = result["Opentime"] if "Opentime" in result else ''
        website = result["Website"] if "Website" in result else ''
        picture1 = result["Picture1"] if "Picture1" in result else ''
        picdescribe1 = result["Picdescribe1"] if "Picdescribe1" in result else ''
        picture2 = result["Picture2"] if "Picture2" in result else ''
        picdescribe2 = result["Picdescribe2"] if "Picdescribe2" in result else ''
        picture3 = result["Picture3"] if "Picture3" in result else ''
        picdescribe3 = result["Picdescribe3"] if "Picdescribe3" in result else ''
        gov = result["Gov"] if "Gov" in result else ''
        px = result["Px"] if "Px" in result else ''
        py = result["Py"] if "Py" in result else ''
        orgpclass = result["Orgclass"] if "Orgclass" in result else ''
        pclass = result["Class"] if "Class" in result else ''
        pclass1 = result["Class1"] if "Class1" in result else ''
        pclass2 = result["Class2"] if "Class2" in result else ''
        pclass3 = result["Class3"] if "Class3" in result else ''
        map = result["Map"] if "Map" in result else ''
        parkinginfo = result["Parkinginfo"] if "Parkinginfo" in result else ''
        parkinginfo_px = result["Parkinginfo_Px"] if "Parkinginfo_Px" in result else ''
        parkinginfo_py = result["Parkinginfo_Py"] if "Parkinginfo_Py" in result else ''
        ticketinfo = result["Ticketinfo"] if "Ticketinfo" in result else ''
        remarks = result["Remarks"] if "Remarks" in result else ''
        keyword = result["Keyword"] if "Keyword" in result else ''
        changetime = result["Changetime"] if "Changetime" in result else ''
        place = Place.objects.filter(json_d=json_d)
        if len(place)==0 and picture1:
            place = Place.objects.create(
                json_d=json_d,
                name=name,
                zone=zone,
                toldescribe=toldescribe,description=description,
                add=add,zipcode=zipcode,
                region=region,town=town,tel=tel,
                travellinginfo=travellinginfo,
                opentime=opentime,website=website,
                picture1=picture1 ,picdescribe1= picdescribe1,picture2=picture2,
                picdescribe2=picdescribe2,picture3=picture3,picdescribe3=picdescribe3,
                gov=gov,px=px,py=py,orgpclass=orgpclass,
                pclass1=pclass1,pclass2=pclass2,pclass3=pclass3,
                map=map,parkinginfo=parkinginfo,parkinginfo_px=parkinginfo_px,parkinginfo_py=parkinginfo_py,
                ticketinfo= ticketinfo,remarks=remarks,keyword=keyword,changetime=changetime)

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv):
        print ("Write to db")
        writedb()
    else:
        print('error')