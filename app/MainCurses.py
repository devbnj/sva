'''
MainCurses.py
'''
import swisseph as swe
import datetime
swe.set_ephe_path('/home/dev/nodejs/swisseph2_7/ephe') # set path to ephemeris files
import json

# def
def checkNak(value_to_check, y):
    max_rank = len(y)
    for ii in range(len(y)-1,0,-1):
        if (y[ii] >= value_to_check >= y[ii-1]) or (y[ii] <= value_to_check <= y[ii-1]):
            max_rank = ii
            break
    return max_rank - 1
# undef

# def
def printHdr():
    print ('Gra', 
        '{:^6}'.format('Long.'),
        '{:^2}'.format('Sn'),
        '{:^2}'.format('Hs'),
        '{:^2}'.format('Nv'),
        '{:^15}'.format('Naks-28'), 
        '{:^15}'.format('Naks-27'),
        '{:^2}'.format('Pd')
    )
# undef

# def
def printNak(dstr, dlong, asc):
    d2 = 13.3333333333
    d1 = 3.33333333333

    print (dstr, 
        '{:06.2f}'.format(dlong),
        '{:2d}'.format(getSign(dlong)),
        '{:2d}'.format(getHouse(dlong, asc)),
        '{:2d}'.format(getNavamsa(dlong)),
        '{:^15}'.format(naks28[checkNak(dlong, nakdegs)]), 
        '{:^15}'.format(naks27[int(dlong/d2)]),
        '{:1d}'.format(int(dlong / d1) % 4 + 1))
    return
# undef

# def
def getSign(dlong):
    return int(dlong / 30.0) + 1
# undef

# def
def getNavamsa(dlong):
    nvm = int(dlong / 3.333333) % 12 + 1
    if nvm == 0:
        nvm = 12
    return nvm
# undef

# def
def getHouse(dlong, asc):
    sgn = getSign(dlong)
    diff = sgn - asc + 1
    if diff > 12:
        diff = 12 - diff + 1
    elif diff < 0:
        diff = 12 + diff
    elif diff == 0:
        diff = 12
    return diff
# undef

# def
def lordOf(house):
	# get the Rasi from the house
    asc = getSign(lag)
    dsign = house + asc - 1
    if (dsign > 12):
        dsign = dsign - 12
	# get the lordship from the sign
	return iruler[sign - 1]
# undef

# def
def computeAstro(yy, mm, dd, hr, mi, tz, lng, lat, isTransit=False):
    swe.set_topo(lng, lat, 0)
    dob = datetime.datetime(yy, mm, dd)
    u = swe.utc_time_zone(yy, mm, dd, hr, mi, 0, tz) # minu
    weekday = dob.strftime("%w")
    jdt = swe.utc_to_jd(u[0], u[1], u[2], u[3], u[4], u[5], swe.GREG_CAL)
    jd = jdt[1]

    # --- set lahiri ayanamsa
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    houses = swe.houses_ex(jd, lat, lng, b'I', swe.FLG_SIDEREAL)
    # --- debug ---
    # print (houses)
    lag = houses[0]

    aya = swe.get_ayanamsa(jd)
    # --- debug ---
    # print ('aya', aya)
    sun = swe.calc_ut(jd, swe.SUN, flag)
    moo = swe.calc_ut(jd, swe.MOON, flag)
    mer = swe.calc_ut(jd, swe.MERCURY, flag)
    ven = swe.calc_ut(jd, swe.VENUS, flag)
    mar = swe.calc_ut(jd, swe.MARS, flag)
    jup = swe.calc_ut(jd, swe.JUPITER, flag)
    sat = swe.calc_ut(jd, swe.SATURN, flag)
    rah = swe.calc_ut(jd, swe.MEAN_NODE, flag)
    # ketu is calculated from rahu
    kl = rah[0][0] + 180.0
    if kl > 360: 
        kl -= 360
    ket = kl
    
    asc = getSign(lag[0])
    # print (getSign(sun[0][0]))
    lagd = swe.split_deg(houses[0][0], flag)
    sund = swe.split_deg(sun[0][0], flag)
        
    # print (json.dumps(houses))
    # print (sun)
    # print (lagd)
    # print (sund)
    return [houses[0][0], sun[0][0], moo[0][0], mer[0][0], ven[0][0], 
            mar[0][0], jup[0][0], sat[0][0], rah[0][0], ket[0][0]]
# undef

# def 
def findCurses():
    # RULE 1

# undef

# main
graha = ['Sun','Moon','Merc','Venus','Mars','Jup','Sat']
signs = ['Ari','Tau','Gem','Can','Leo','Vir','Lib','Sco','Sag','Cap','Aqu','Pis']
rlord = ["Ma", "Ve", "Me", "Mo", "Su", "Me", "Ve", "Ma", "Ju", "Sa", "Sa", "Ju"]
ruler = [ 4,     3,    2,    1,    0,    2,    3,    4,    5,    6,    6,    5]
exalX = ["Su", "Mo", "Ra", "Ju", "Ne", "Me", "Sa", "Ur", "Ke", "Ma", ".", "Ve"]
exalt = [ 0,     1,   -1,    5,   -1,    2,    6,   -1,   -1,    4,   -1,   3 ]
fall  = ["Sa", "Ur", "Ke", "Ma", ".", "Ve", "Su", "Mo", "Ra", "Ju", "Ne", "Me"]
ifall = [ 6,    -1,   -1,    4,   -1,   3,    0,    1,    -1,    5,   -1,   2 ]


flag = swe.FLG_SPEED + swe.FLG_SWIEPH + swe.FLG_SIDEREAL
rgh = computeAstro(1959, 11, 12, 13, 30, +5.5, 88.3639, 22.5726, False)
lag = rgh[0]

