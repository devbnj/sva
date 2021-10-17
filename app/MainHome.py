from os import listdir
from os.path import isfile, join
import json
import re

# def
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
# end def

# def
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
# end def

'''
Starts Here
'''

# def
def dprint(txt):
    if txt is not None:
        print(txt)
# enddef

# def
def homerun(tchar):
    mypath = './static/homeo/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles.sort()
    cumdata = []
    for file in onlyfiles:
        if file.endswith(".json"):
            if file.startswith(tchar):
                filename = join(mypath, file)
                with open(filename) as home_file:
                    tdata = json.load(home_file)
                    cumdata.append(tdata.copy())
    return cumdata
# end def

# def
def homesrch(phr):
    mypath = './static/homeo/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles.sort()
    cumdata = []
    for file in onlyfiles:
        if file.endswith(".json"):
            filename = join(mypath, file)
            with open(filename) as home_file:
                tdata = json.load(home_file)
                if checkPhrase(phr, tdata):
                    rdata = replacePhrase(phr, tdata, 'yellow')
                    cumdata.append(rdata.copy())
    return cumdata    
# end def

# def
def homeMultiSrch(phr, cond1, phx):
    mypath = './static/homeo/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles.sort()
    cumdata = []
    for file in onlyfiles:
        if file.endswith(".json"):
            filename = join(mypath, file)
            with open(filename) as home_file:
                tdata = json.load(home_file)
                if checkPhrase(phr, tdata) and (cond1 != 'AND'):
                    rdata = replacePhrase(phr, tdata, 'yellow')
                    cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata) and checkPhrase(phr, tdata) and (cond1 == 'AND'):
                        rdata = replacePhrase(phx, tdata, 'yellow')
                        rdata = replacePhrase(phr, rdata, 'green')
                        cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata) and (cond1 == 'OR'):
                        rdata = replacePhrase(phx, tdata, 'green')
                        cumdata.append(rdata.copy())
    return cumdata    
# end def

satt = [
    'Mind', 'Head', 'Eyes','Face', 'Nose','Ears','Burn','Eye',
    'Mouth','Respiratory','Throat','Stomach','Chest', 'Abdomen',
    'Gastric','Heart','Male','Female','Extremities','Back','Hip',
    'Fever','Sleep','Skin','Rectum','Urine','Stool','Modalities',
    'Toe','Finger','Jaws','Lips','Feet','Foot','Tooth','Teeth',
    'Bowels',
    'Relationships'
]

# import re
def replacePhrase(phrase, djson, color):
    rson = djson
    ns = '<span class="w3-' + color + '">' + phrase + '</span>'
    try:
        # print ('rson', rson['details'])
        rstr = str(rson['details'])
        nr = re.sub(phrase, ns, rstr, flags=re.IGNORECASE)
        # print ('replaced', nr)
        rson["details"] = nr
    except:
        # do nothing
        print("An exception occurred")

    r = deep_get(djson, 'symptoms')
    if r is not None:
        for i in range(len(satt)):
            if satt[i] in djson['symptoms']:
                rstr = str(djson['symptoms'].get(satt[i]))
                if re.search(phrase, rstr, re.IGNORECASE):
                    nr = re.sub(phrase, ns, rstr, flags=re.IGNORECASE)
                    rson['symptoms'][satt[i]] = nr
    return rson

# def
def checkPhrase(phrase, djson):
    result = False
    r = deep_get(djson, 'details')
    if r is not None:
        # print(r)
        if re.search(phrase, r, re.IGNORECASE):
            result = True
    if not result:
        r = deep_get(djson, 'symptoms')
        if r is not None:
            for i in range(len(satt)):
                if satt[i] in djson['symptoms']:
                    if re.search(phrase, str(djson['symptoms'].get(satt[i])), re.IGNORECASE):
                        result = True
    return result
# end def

# def
def homeThreeSrch(phr, cond1, phx, cond2, phy):
    mypath = './static/homeo/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles.sort()
    cumdata = []
    for file in onlyfiles:
        if file.endswith(".json"):
            filename = join(mypath, file)
            with open(filename) as home_file:
                tdata = json.load(home_file)
                if checkPhrase(phr, tdata) and (cond1 != 'AND'):
                    rdata = replacePhrase(phr, tdata, 'yellow')
                    cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata) and checkPhrase(phr, tdata) and (cond1 == 'AND') and (cond2 != 'AND'):
                        rdata = replacePhrase(phx, tdata, 'yellow')
                        rdata = replacePhrase(phr, rdata, 'green')
                        cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata) and checkPhrase(phr, tdata) and checkPhrase(phy, tdata) \
                    and (cond1 == 'AND') and (cond2 == 'AND'):
                        rdata = replacePhrase(phx, tdata, 'yellow')
                        rdata = replacePhrase(phr, rdata, 'green')
                        rdata = replacePhrase(phy, rdata, 'blue')
                        cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata) and (cond1 == 'OR'):
                        rdata = replacePhrase(phx, tdata, 'green')
                        cumdata.append(rdata.copy())
    return cumdata    
# end def

