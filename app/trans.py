#!/usr/bin/env python3.7
 
import faulthandler
faulthandler.enable()

import swisseph as swe
swe.set_ephe_path('/home/devb/nodejs/swisseph2_7/ephe') 
# set path to ephemeris files

flag = swe.FLG_SWIEPH # + swe.FLG_SIDEREAL
# lng = 88.3639 # kolkata
# lat = 22.5726 # kolkata

year = -200
lng = 77.20227 # new delhi
lat = 28.61418

swe.set_topo(lng, lat, 0)

# kerb aries aswini
# hamal taurus 
# alcyone pleiades krittika
# aldeberan rohini
# bellatrix
# mintaka 
# polaris
# betelgeuse - ardra
# castor/polux twins - punarvasu
# 22 vega - abhijit

stars = ['Kerb', 'Hamal', 'Alcyone', 'Aldebaran', 'Bellatrix', 'Mintaka', 
    'Polaris', 'Betelgeuse', 'Castor', 'Pollux', 'Sirius', 'Regulus', 'Denebola', 
    'Spica', 'Vega', 'Fomalhaut']

# def
def checkTransit(jd_start, dstar, lon, lat):
    result = swe.rise_trans(jd_start,
        dstar, 0.0, 0.0, 0.0, 0, 
        swe.CALC_RISE)
    return result
# undef

# vernal equinox 20th march
u = swe.utc_time_zone(year, 3, 20, 6, 0, 0, 0)
jdt = swe.utc_to_jd(u[0], u[1], u[2], u[3], u[4], u[5], swe.GREG_CAL)
jd = jdt[1]

try:
    for s in stars:
        xtuple = checkTransit(jd, s, lng, lat)
        tm = list(zip(*xtuple))[0][1]
        dt = swe.jdet_to_utc(tm, swe.GREG_CAL)
        dtd = list(dt)
        print (s, dtd)
    swe.close()
except:
    pass
finally:
    swe.close()

