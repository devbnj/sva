from os import listdir
from os.path import isfile, join
import json
import re

def ayutrt(a, h):
    rpath = './static/ayur/'
    flname = a + "_" + h + ".json"
    with open(join(rpath, flname)) as afile:
        tdata = json.load(afile)
    return tdata.copy() 



