'''
MainChart.py
'''
import swisseph as swe
import datetime
swe.set_ephe_path('/home/devbnjhp/nodejs/swisseph2_7/ephe') # set path to ephemeris files
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
        '{:^18}'.format('Naks-28'), 
        '{:^18}'.format('Naks-27'),
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
        '{:^18}'.format(naks28[checkNak(dlong, nakdegs)]), 
        '{:^18}'.format(naks27[int(dlong/d2)]),
        '{:1d}'.format(int(dlong / d1) % 4 + 1))
    return
# undef

# def
def printHdr2():
    print ('{:^51}'.format('NATAL'),
           '{:^48}'.format('TRANSITING')
           )
    print ('Gra', 
        '{:^6}'.format('Long.'),
        '{:^2}'.format('Sn'),
        '{:^2}'.format('Hs'),
        '{:^2}'.format('Nv'),
        '{:^18}'.format('Naks-28'), 
        '{:^18}'.format('Naks-27'),
        '{:^2}'.format('Pd'),
        '{:^1}'.format('|'),
        '{:^6}'.format('Long.'),
        '{:^2}'.format('Sn'),
        '{:^2}'.format('Hs'),
        '{:^2}'.format('Nv'),
        '{:^18}'.format('Naks-28'), 
        '{:^18}'.format('Naks-27'),
        '{:^2}'.format('Pd')
    )
# undef

# def
def printNak2(dstr, dlong, asc, dlong1):
    d2 = 13.3333333333
    d1 = 3.33333333333

    print (dstr, 
        '{:06.2f}'.format(dlong),
        '{:2d}'.format(getSign(dlong)),
        '{:2d}'.format(getHouse(dlong, asc)),
        '{:2d}'.format(getNavamsa(dlong)),
        '{:^18}'.format(naks28[checkNak(dlong, nakdegs)]), 
        '{:^18}'.format(naks27[int(dlong/d2)]),
        '{:2d}'.format(int(dlong / d1) % 4 + 1),
        '{:^1}'.format('|'),
        '{:06.2f}'.format(dlong1),
        '{:2d}'.format(getSign(dlong1)),
        '{:2d}'.format(getHouse(dlong1, asc)),
        '{:2d}'.format(getNavamsa(dlong1)),
        '{:^18}'.format(naks28[checkNak(dlong1, nakdegs)]), 
        '{:^18}'.format(naks27[int(dlong1/d2)]),
        '{:1d}'.format(int(dlong1 / d1) % 4 + 1))
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
def sarvartabhadra(lg, su, mon, me, ve, ma, ju, sa, ra, ke, wk):
    dnak = ['-'] * 29
    dsgn = ['-'] * 12
    dday = ['-'] * 7
    lag = int(lg / 30.0)
    nak = int(mon / 13.333333333)
    if (nak > 21):
        nak = nak + 1
    if (nak == 21 and (mon >= 293.333 and mon <= 297.333)):
        nak = nak + 1
    # nak = nak + 1
    print ('nak', nak)
    dnak[nak] = '[*]'
    dsgn[lag] = '[*]'
    dday[wk] = '[*]'
    
    print ('NW --------------------------------- NORTH --------------------------------- NE')
    print ('   |EE ई   |Dhanis |ShatBh |P.Bhad |U.Bhad |Revati |Asvini |Bharan |a अ    |')
    print ('   |       |       |       |       |       |       |       |       |       |')
    xstr = '   |       |'
    for i in range(23, 28):
        xstr = xstr + '{:^6}'.format(dnak[i]) + ' |'
        
    for i in range(0, 2):
        xstr = xstr + '{:^6}'.format(dnak[i]) + ' |'

    xstr = xstr + '       |'
    
    print (xstr)
    print ('   -------------------------------------------------------------------------')
    print ('   |Sravan |Ri ऋ   |Ga ग   |Sa स   |दda tha|Cha च  |La ल   |U उ    |Kritik |')
    print ('   |       |       |       |       |jha na |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[22])) + ' '
    xstr = xstr + '|       |       |       |       |       |       |       |'
    xstr = xstr + ('{:^6}'.format(dnak[2])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |Abhijt |Kha ख  |Ai ऐ   |Aquars |Pisces |Aries  |Lu लृ   |a अ    |Rohini |')
    print ('   |       |       |       |       |       |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[21])) + ' |'
    xstr = xstr + '       |       |'
    for i in range (10, 12):
        xstr = xstr + ('{:^6}'.format(dsgn[i])) + ' |'
    xstr = xstr + ('{:^6}'.format(dsgn[0])) + ' |'    
    xstr = xstr + '       |       |'
    xstr = xstr + ('{:^6}'.format(dnak[3])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |U.Shad |Ja ज   |Capric |Ah अः  |Friday |O ओ    |Taurus |Va व   |Mrigas |')
    print ('   |       |       |       |       |Ritka  |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[20])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dsgn[9])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dday[5])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dsgn[1])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dnak[4])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('WES|P.Shad |भbh dha|Sagitr |Thursd |Saturd |Sun Tue|Gemini |कKa gha|Ardra  |EAST')
    print ('   |       |pha dha|       |Jaya   |Purna  |Nanda  |       |na cha |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[19])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dsgn[8])) + ' |'
    xstr = xstr + ('{:^6}'.format(dday[4])) + ' |'
    xstr = xstr + ('{:^6}'.format(dday[6])) + ' |'
    xstr = xstr + ('{:^6}'.format(dday[0]+dday[2])) + ' |'
    xstr = xstr + ('{:^6}'.format(dsgn[2])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dnak[5])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |Moola  |Ya य   |Scorpo |Am अं   |Mon wed|Au औ   |Cancer |ha ह   |Punarv |')
    print ('   |       |       |       |       |Bhadra |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[18])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dsgn[7])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dday[1]+dday[3])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dsgn[3])) + ' |'
    xstr = xstr + '       |'
    xstr = xstr + ('{:^6}'.format(dnak[6])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |Jyesta |Na न   |Ae ए   |Libra  |Virgo  |Leo    |Lu लृ   |da ड   |Pushya |')
    print ('   |       |       |       |       |       |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[17])) + ' |'
    xstr = xstr + '       |       |'    
    xstr = xstr + ('{:^6}'.format(dsgn[6])) + ' |'
    xstr = xstr + ('{:^6}'.format(dsgn[5])) + ' |'
    xstr = xstr + ('{:^6}'.format(dsgn[4])) + ' |'
    xstr = xstr + '       |       |'    
    xstr = xstr + ('{:^6}'.format(dnak[7])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |Anurda |Ri ऋ   |Ta त   |Ra र   |प Pa sa|Ta ट   |Ma म   |Uu ऊ   |Ashles |')
    print ('   |       |       |       |       |na tha |       |       |       |       |')

    xstr = '   |'
    xstr = xstr + ('{:^6}'.format(dnak[16])) + ' '
    xstr = xstr + '|       |       |       |       |       |       |       |'
    xstr = xstr + ('{:^6}'.format(dnak[8])) + ' |'
    print (xstr)

    print ('   -------------------------------------------------------------------------')
    print ('   |i इ    |Vishak |Swati  |Chitra |Hasta  |U.Phal |P.Phal |Magha  |Aa आ   |')
    print ('   |       |       |       |       |       |       |       |       |       |')

    xstr = '   |       |'
    for i in range(15, 9, -1):
        xstr = xstr + '{:^6}'.format(dnak[i]) + ' |'
    xstr = xstr + '       |'
      
    print (xstr)

    print ('SW --------------------------------- SOUTH --------------------------------- SE')

# undef

'''
Runtime stuff
'''

naks28 = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu',
'Pushya', 'Aslesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra',
'Svati', 'Visakha', 'Anuradha', 'Jyestha', 'Mula', 'Purva Ashada', 'Uttara Ashada',
'Abhijit', 'Sravana', 'Dhanista', 'Sata Bhisag', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati']

naks27 = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu',
'Pushya', 'Aslesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra',
'Svati', 'Visakha', 'Anuradha', 'Jyestha', 'Mula', 'Purva Ashada', 'Uttara Ashada',
'Sravana', 'Dhanista', 'Sata Bhisag', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati']

nakdegs = [0, 13.00, 25.99, 38.99, 58.48, 71.48, 77.98, 97.47, 110.47, 123.47, 136.46, 149.46,
168.95, 181.95, 194.95, 201.44, 220.94, 233.94, 240.43, 253.43, 259.93, 279.42, 282.02,
295.02, 308.01, 314.51, 327.51, 347.00, 360.00]

# def
def computeAstro(yy, mm, dd, hr, mi, tz, lng, lat, isTransit=False):

    # now = swe.julday(2007,3,3) # get Julian day number
    # res = swe.lun_eclipse_when(now) # find next lunar eclipse (from now on)
    # ecltime = swe.revjul(res[1][0]) # get date UTC
    # ecltime(2007, 3, 3, 23.347975596785545)
    
    swe.set_topo(lng, lat, 0)
    dob = datetime.datetime(yy, mm, dd)
    u = swe.utc_time_zone(yy, mm, dd, hr, mi, 0, tz) # minu
    weekday = dob.strftime("%w")
    jdt = swe.utc_to_jd(u[0], u[1], u[2], u[3], u[4], u[5], swe.GREG_CAL)
    # --- debug ---
    # print('jdt', jdt) 
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
    
    if (not(isTransit)):
        printHdr()
        printNak ('lag', lag[0], asc)
        printNak ('sun', sun[0][0], asc)
        printNak ('moo', moo[0][0], asc)
        printNak ('mar', mar[0][0], asc)
        printNak ('ven', ven[0][0], asc)
        printNak ('mer', mer[0][0], asc)
        printNak ('jup', jup[0][0], asc)
        printNak ('sat', sat[0][0], asc)
        printNak ('rah', rah[0][0], asc)
        printNak ('ket', ket, asc)
        
    sarvartabhadra(lag[0], sun[0][0], moo[0][0], 
               mer[0][0], ven[0][0], mar[0][0], 
               jup[0][0], sat[0][0], rah[0][0], 
               ket, int(weekday))
    return
# undef

# def
def computeAstro2(yy, mm, dd, hr, mi, tz, lng, lat, yy1, mm1, dd1, hr1, mi1, tz1, lng1, lat1):
   
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
    
    # now do it for the transits
    swe.set_topo(lng1, lat1, 0)
    dot = datetime.datetime(yy1, mm1, dd1)
    u1 = swe.utc_time_zone(yy1, mm1, dd1, hr1, mi1, 0, tz1) 
    weekday = dot.strftime("%w")
    jdt1 = swe.utc_to_jd(u1[0], u1[1], u1[2], u1[3], u1[4], u1[5], swe.GREG_CAL)
    jd1 = jdt1[1]

    # --- set lahiri ayanamsa
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    houses1 = swe.houses_ex(jd1, lat1, lng1, b'I', swe.FLG_SIDEREAL)

    aya1 = swe.get_ayanamsa(jd1)
    # --- debug ---
    # print ('aya', aya)
    tsun = swe.calc_ut(jd1, swe.SUN, flag)
    tmoo = swe.calc_ut(jd1, swe.MOON, flag)
    tmer = swe.calc_ut(jd1, swe.MERCURY, flag)
    tven = swe.calc_ut(jd1, swe.VENUS, flag)
    tmar = swe.calc_ut(jd1, swe.MARS, flag)
    tjup = swe.calc_ut(jd1, swe.JUPITER, flag)
    tsat = swe.calc_ut(jd1, swe.SATURN, flag)
    trah = swe.calc_ut(jd1, swe.MEAN_NODE, flag)
    tkl = trah[0][0] + 180.0
    if tkl > 360: 
        tkl -= 360
    tket = tkl
    
    # transits done
   
    printHdr2()
    printNak2 ('lag', lag[0], asc, lag[0])
    printNak2 ('sun', sun[0][0], asc, tsun[0][0])
    printNak2 ('moo', moo[0][0], asc, tmoo[0][0])
    printNak2 ('mar', mar[0][0], asc, tmar[0][0])
    printNak2 ('ven', ven[0][0], asc, tven[0][0])
    printNak2 ('mer', mer[0][0], asc, tmer[0][0])
    printNak2 ('jup', jup[0][0], asc, tjup[0][0])
    printNak2 ('sat', sat[0][0], asc, tsat[0][0])
    printNak2 ('rah', rah[0][0], asc, trah[0][0])
    printNak2 ('ket', ket, asc, tket)
        
    return
# undef

'''
Main Program
'''

flag = swe.FLG_SPEED + swe.FLG_SWIEPH + swe.FLG_SIDEREAL # + swe.FLG_TOPOCTR

computeAstro(1959, 11, 12, 13, 30, +5.5, 88.3639, 22.5726, False)
computeAstro(2020, 12, 11, 1, 0, -5.00, -73.98661, 40.73065, True)

computeAstro2(1959, 11, 12, 13, 30, +5.5, 88.3639, 22.5726, 2021, 6, 19, 21, 0, -5.0, -73.98661, 40.73065) 

'''
# native longitude, latitude
lng = 88.3639 # kolkata
lat = 22.5726 # kolkata

# transit longitude, latitude
lngt = -73.98661 # nyc
latt = 40.73065

# lng = 77.20227 # new delhi
# lat = 28.61418

# lat = 39.9500 # philly
# lng = -75.1667 # philly

# lng = 80.26726 # sripuram
# lat = 13.04520 # sripuram

# lng = 87.66016 # ramakrishna
# lat = 22.89546

# lng = 77.81250 # satya sai baba
# lat = 14.16368

# lng = -73.98661 # donald trump
# lat = 40.73065

# u = swe.utc_time_zone(1959, 11, 12, 13, 30, 0, 5.5) # minu
# u = swe.utc_time_zone(1962, 11, 11, 7, 20, 0, 5.5) # mithoo
# u = swe.utc_time_zone(1988, 10, 3, 21, 35, 0, 5.5) # dea
# u = swe.utc_time_zone(2008, 2, 14, 21, 6, 0, -5.0) # kam
# u = swe.utc_time_zone(1990, 6, 24, 16, 30, 0, 5.5) # sonne
# u = swe.utc_time_zone(1976, 1, 3, 8, 0, 0, 5.5) # amma
# u = swe.utc_time_zone(1960, 7, 15, 12, 40, 0, 5.5) # p talwar
# u = swe.utc_time_zone(1863, 1, 12, 6, 20, 0, 5.5) # vivekananda
# u = swe.utc_time_zone(1836, 2, 13, 22, 20, 0, 5.5) # ramakrishna
# u = swe.utc_time_zone(1926, 11, 23, 11, 0, 0, 5.5) # satya sai baba
# u = swe.utc_time_zone(1946, 6, 14, 10, 54, 0, -5.0) # donald trump

# --- debug ---
# print('u', u) 
'''

# help(swe)