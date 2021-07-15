from os import listdir
from os.path import isfile, join
import json
# import os

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

def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

'''
Starts Here
'''

# def
def dprint(txt):
    if txt is not None:
        print(txt)
# enddef

def homerun(tchar):
    mypath = './static/'
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

'''
for c in cumdata:
    # print (deep_get(person, "person.name.first"))
    print (c['name']) 
    dprint (deep_get(c, 'common_names'))

        deep_get(c, 'details'),
        deep_get(c, 'dosage'), 
        deep_get(c, 'symptoms.Mind'),
        deep_get(c, 'symptoms.Head'),
        deep_get(c, 'symptoms.Eyes'),
        deep_get(c, 'symptoms.Nose'),
        deep_get(c, 'symptoms.Ears'),

        deep_get(c, 'symptoms.Mouth'),
        deep_get(c, 'symptoms.Respiratory'),
        deep_get(c, 'symptoms.Throat'),

        deep_get(c, 'symptoms.Stomach'),
        deep_get(c, 'symptoms.Abdomen'),

        deep_get(c, 'symptoms.Heart'),
        deep_get(c, 'symptoms.Male'),
        deep_get(c, 'symptoms.Female'),
        deep_get(c, 'symptoms.Extremities'),
        deep_get(c, 'symptoms.Back'),
        deep_get(c, 'symptoms.Fever'),
        deep_get(c, 'symptoms.Sleep'),
        deep_get(c, 'symptoms.Skin'),

        deep_get(c, 'symptoms.Urine'),
        deep_get(c, 'symptoms.Stool'),

        deep_get(c, 'symptoms.Modalities')
    '''
