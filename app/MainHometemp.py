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

satt = ['details', 'symptoms["Mind"]', 'symptoms["Head"]', 'symptoms["Eyes"]','symptoms["Nose"]','symptoms["Ears"]',
        'symptoms["Mouth"]','symptoms["Respiratory"]','symptoms["Throat"]','symptoms["Stomach"]','symptoms["Abdomen"]',
        'symptoms["Heart"]','symptoms["Male"]','symptoms["Female"]','symptoms["Extremities"]','symptoms["Back"]',
        'symptoms["Fever"]','symptoms["Sleep"]','symptoms["Skin"]','symptoms["Urine"]','symptoms["Stool"]',
        'symptoms["Modalities"]', 'symptoms["Limbs/Extremities"]'
]
rsatt = [
'details', 'symptoms.Mind', 'symptoms.Head', 'symptoms.Eyes','symptoms.Nose','symptoms.Ears',
'symptoms.Mouth','symptoms.Respiratory','symptoms.Throat','symptoms.Stomach','symptoms.Abdomen',
'symptoms.Heart','symptoms.Male','symptoms.Female','symptoms.Extremities','symptoms.Back',
'symptoms.Fever','symptoms.Sleep','symptoms.Skin','symptoms.Urine','symptoms.Stool','symptoms.Modalities',
'symptoms.Limbs\/Extremities'
]

# import re
def replacePhrase(phrase, djson, n, color):
    rson = djson
    rstr = rson.get(satt[n])
    ns = '<span class="w3-' + color + '">' + phrase + '</span>'
    nr = re.sub(phrase, ns, str(rstr), flags=re.IGNORECASE)
    rson[str(rsatt[n])] = nr
    return rson

# def
def checkPhrase(phrase, djson, n):
    result = False
    r = deep_get(djson, rsatt[n])
    # if rsatt[n] in djson.keys():
    if r is not None:
        # r = djson.get(rsatt[n])
        if (rsatt[n] == 'symptoms.Heart'): 
            print(r)
        if re.search(phrase, str(r), re.IGNORECASE):
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
                for i in range(len(satt)):
                    if checkPhrase(phr, tdata, i) and (cond1 != 'AND'):
                        rdata = replacePhrase(phr, tdata, i, 'yellow')
                        cumdata.append(rdata.copy())
                    if checkPhrase(phx, tdata, i) and checkPhrase(phr, tdata, i) and \
                        (cond1 == 'AND') and (cond2 != 'AND'):
                        rdata = replacePhrase(phx, tdata, i, 'yellow')
                        rdata = replacePhrase(phr, rdata, i, 'green')
                        cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata, i) and checkPhrase(phr, tdata, i) \
                    and checkPhrase(phy, tdata, satt[i]) and (cond1 == 'AND') and (cond2 == 'AND'):
                        rdata = replacePhrase(phx, tdata, i, 'yellow')
                        rdata = replacePhrase(phr, rdata, i, 'green')
                        rdata = replacePhrase(phy, rdata, i, 'blue')
                        cumdata.append(rdata.copy())
                if checkPhrase(phx, tdata, i) and (cond1 == 'OR'):
                        rdata = replacePhrase(phx, tdata, i, 'green')
                        cumdata.append(rdata.copy())
    return cumdata    
# end def

