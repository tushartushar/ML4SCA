from data import DataClassPaper, HomePageData, childc, parentc, root,Absdata
from dataclasses import dataclass
import jsonpickle
import os 
from pathlib import Path



__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
wpathdir = Path(__location__)
wpath = os.path.join(os.path.join(
    wpathdir.parent.parent.absolute(), "assets"), "JSON")

jsonpath=os.path.join(wpath, "paperdata.json")
print(jsonpath)


with open(jsonpath, 'r') as f:
    jsondata = f.read()



data = jsonpickle.decode(jsondata)

dg = {}
for dt in data:
    if dt.Category not in dg:
        dg[dt.Category] = {}
    if dt.Venue in dg[dt.Category].keys():
        dg[dt.Category][dt.Venue] = dg[dt.Category][dt.Venue] + 1
    else:
        dg[dt.Category][dt.Venue] = 1

sbdict = []
for key, value in dg.items():
    chlist = []
    for key1, value1 in value.items():
        chlist.append(childc(key1, value1))
    sbdict.append(parentc(key, chlist))



rootobj = root("ML4SE", sbdict)
json_object = jsonpickle.encode(rootobj, unpicklable=False)
file1 = open(os.path.join(wpath, "flare-2.json"), "w")
file1.write(json_object)
file1.close()