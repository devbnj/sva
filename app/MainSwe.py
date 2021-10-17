import swisseph as swe
swe.set_ephe_path('/home/dev/nodejs/swisseph2_7/ephe') # set path to ephemeris files

flag = swe.FLG_SPEED + swe.FLG_SWIEPH + swe.FLG_SIDEREAL # + swe.FLG_TOPOCTR
lng = 88.3639 # kolkata
lat = 22.5726 # kolkata

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

swe.set_topo(lng, lat, 0)

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
def checkNak(value_to_check, y):
    max_rank = len(y)
    for ii in range(len(y)-1,0,-1):
        if (y[ii] >= value_to_check >= y[ii-1]) or (y[ii] <= value_to_check <= y[ii-1]):
            max_rank = ii
            break

    return max_rank - 1
# undef

# def
def printNak(dstr, dlong):
    print (dstr, 
        '{:06.2f}'.format(dlong), 
        '{:^15}'.format(naks28[checkNak(dlong, nakdegs)]), 
        '{:^15}'.format(naks27[int(dlong/13.33333)]))

# undef

# now = swe.julday(2007,3,3) # get Julian day number
# res = swe.lun_eclipse_when(now) # find next lunar eclipse (from now on)
# ecltime = swe.revjul(res[1][0]) # get date UTC
# ecltime(2007, 3, 3, 23.347975596785545)

u = swe.utc_time_zone(1959, 11, 12, 13, 30, 0, 5.5) # minu
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
jdt = swe.utc_to_jd(u[0], u[1], u[2], u[3], u[4], u[5], swe.GREG_CAL)
# --- debug ---
# print('jdt', jdt) 
jd = jdt[1]

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

printNak ('lag', lag[0])
# Longitude, Latitude, Distance in AU, Speed in longitude (deg/day), Speed in latitude (deg/day)
# Speed in distance (AU/day)

# printNak ('sun', sun[0][0])
print ('1 sun', sun)
print ('2 sun', sun[0][0], sun[0][3])

printNak ('moo', moo[0][0])
# printNak ('mar', mar[0][0])
# printNak ('ven', ven[0][0])
print ('mar', mar)
print ('ven', ven)
printNak ('mer', mer[0][0])
printNak ('jup', jup[0][0])
printNak ('sat', sat[0][0])
# printNak ('rah', rah[0][0])
print ('rah', rah)
printNak ('ket', ket)


# help(swe)