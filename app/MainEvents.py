"""
MainEvents.py
"""
import swisseph as swe
import datetime
import math

swe.set_ephe_path(
    "/home/devbnjhp/nodejs/swisseph2_7/ephe"
)  # set path to ephemeris files
import json

flag = swe.FLG_SPEED + swe.FLG_SWIEPH + swe.FLG_SIDEREAL  # + swe.FLG_TOPOCTR

# def
def checkNak(value_to_check, y):
    max_rank = len(y)
    for ii in range(len(y) - 1, 0, -1):
        if (y[ii] >= value_to_check >= y[ii - 1]) or (
            y[ii] <= value_to_check <= y[ii - 1]
        ):
            max_rank = ii
            break
    return max_rank - 1


# undef

# def
def printHdr():
    print(
        "Gra",
        "{:^6}".format("Long."),
        "{:^2}".format("Sn"),
        "{:^2}".format("Hs"),
        "{:^2}".format("Nv"),
        "{:^18}".format("Naks-28"),
        "{:^18}".format("Naks-27"),
        "{:^2}".format("Pd"),
    )


# undef

# def
def printNak(dstr, dlong, asc):
    d2 = 13.3333333333
    d1 = 3.33333333333

    print(
        dstr,
        "{:06.2f}".format(dlong),
        "{:2d}".format(getSign(dlong)),
        "{:2d}".format(getHouse(dlong, asc)),
        "{:2d}".format(getNavamsa(dlong)),
        "{:^18}".format(naks28[checkNak(dlong, nakdegs)]),
        "{:^18}".format(naks27[int(dlong / d2)]),
        "{:1d}".format(int(dlong / d1) % 4 + 1),
    )
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

"""
Runtime stuff
"""

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
def computeAstro(yy, mm, dd, hr, mi, tz, lng, lat):
    res = {}
    swe.set_topo(lng, lat, 0)
    dob = datetime.datetime(yy, mm, dd)
    u = swe.utc_time_zone(yy, mm, dd, hr, mi, 0, tz)
    weekday = dob.strftime("%w")
    jdt = swe.utc_to_jd(u[0], u[1], u[2], u[3], u[4], u[5], swe.GREG_CAL)
    jd = jdt[1]

    # --- set lahiri ayanamsa
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    houses = swe.houses_ex(jd, lat, lng, b"I", swe.FLG_SIDEREAL)
    # --- debug ---
    lag = houses[0]

    aya = swe.get_ayanamsa(jd)
    # --- debug ---
    res["yr"] = yy
    res["mo"] = mm
    sun = swe.calc_ut(jd, swe.SUN, flag)
    res["sun"] = sun[0][0]
    moo = swe.calc_ut(jd, swe.MOON, flag)
    res["moo"] = moo[0][0]
    mer = swe.calc_ut(jd, swe.MERCURY, flag)
    res["mer"] = mer[0][0]
    ven = swe.calc_ut(jd, swe.VENUS, flag)
    res["ven"] = ven[0][0]
    mar = swe.calc_ut(jd, swe.MARS, flag)
    res["mar"] = mar[0][0]
    jup = swe.calc_ut(jd, swe.JUPITER, flag)
    res["jup"] = jup[0][0]
    sat = swe.calc_ut(jd, swe.SATURN, flag)
    res["sat"] = sat[0][0]
    rah = swe.calc_ut(jd, swe.MEAN_NODE, flag)
    res["rah"] = rah[0][0]
    # ketu is calculated from rahu
    kl = rah[0][0] + 180.0
    if kl > 360:
        kl -= 360
    ket = kl
    res["ket"] = ket
    asc = getSign(lag[0])
    res["Asc"] = asc
    res['lag'] = lag[0]
    return res


# undef

# def
def add_one_month(yy, mm):
    # advance year and month by one month
    new_year = yy
    new_month = mm + 1
    # note: in datetime.date, months go from 1 to 12
    if new_month > 12:
        new_year += 1
        new_month -= 12

    return new_year, new_month
# undef

d2 = 13.3333333333

# def
def getRec(name, plnt1, natmoon, asc, year, month, atk):
    drec = {}
    drec["Collision"] = name
    drec["Naks1"] = naks27[int(plnt1 / d2)]
    # drec["Naks2"] = naks27[int(natmoon / d2)]
    drec["Sign1"] = getSign(plnt1)
    # drec["Sign2"] = getSign(natmoon)
    drec["House"] = getHouse(plnt1, asc)
    drec["Nav1"] = getNavamsa(plnt1)
    # drec["Nav2"] = getNavamsa(natmoon)
    drec["ash"] = atk
    drec["Year"] = year
    drec["Month"] = month
    return drec
# enddef

"""
Main Program
"""
# def
def run(yr, mo, dy, hr, mi, tz, ln, lt, styr, enyr):
    orb = 8  # assuming influence within 8 degrees

    natData = computeAstro(yr, mo, dy, hr, mi, tz, ln, lt)
    ma = findAshtakVarga(natData)

    # benchmark against the moon
    msign = math.floor(natData["moo"] / 30 + 1)
    mAstemp = ma['moo']
    mAstak = mAstemp[msign - 1]
    
    # print('msign', msign, 'mastak', mAstak)
    mResult = {}
    mResult["sign"] = msign
    mResult["astak"] = mAstak
    mResult["nak"] = naks27[int(natData["moo"] / d2)]
    mResult['nav'] = getNavamsa(int(natData["moo"]))

    colls = []
    yr1 = yr
    mo1 = mo
    result = []
    rec = {}

    colls.append(natData.copy())

    for i in range(1, 1440):
        yr1, mo1 = add_one_month(yr1, mo1)
        rdata = computeAstro(yr1, mo1, dy, hr, mi, tz, ln, lt)
        colls.append(rdata.copy())

    whyear1 = styr
    whyear2 = enyr
    dlower = natData["moo"] - orb
    # if dlower < 0:
    #    dlower += 360
    dhigher = natData["moo"] + orb
    # if dhigher > 360:
    #    dhigher = dhigher - 360
    """
    if dlower > dhigher:
        dtemp = dhigher
        dhigher = dlower
        dlower = dtemp
    """
    print(dhigher, dlower)

    for i in range(1, 1440):
        # set a small year range
        if colls[i]["yr"] >= whyear1 and colls[i]["yr"] <= whyear2:
            # Sade Sathi - Saturn over Natal Moon
            if colls[i]["sat"] >= dlower and colls[i]["sat"] <= dhigher:
                mAstemp = ma['sat']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Saturn/Moon",
                    colls[i]["sat"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Delays. Loneliness. Negative Health"
                result.append(rec.copy())
            # Jup over moon, good tidings
            if colls[i]["jup"] >= dlower and colls[i]["jup"] <= dhigher:
                mAstemp = ma['jup']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Jupiter/Moon",
                    colls[i]["jup"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Hurdles. Mental tensions. Fear and anxiety"
                result.append(rec.copy())
            # Ven, sun, mars, merc over moon
            if colls[i]["ven"] >= dlower and colls[i]["ven"] <= dhigher:
                mAstemp = ma['ven']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Venus/Moon",
                    colls[i]["ven"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Good prospects, finances and uplifted mind. Meet new people"
                result.append(rec.copy())
            if colls[i]["sun"] >= dlower and colls[i]["sun"] <= dhigher:
                mAstemp = ma['sun']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Sun/Moon",
                    colls[i]["sun"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Health concerns. Heart, BP and eyes affected. Financial Instability. No peace of mind"
                result.append(rec.copy())
            if colls[i]["mar"] >= dlower and colls[i]["mar"] <= dhigher:
                mAstemp = ma['mar']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Mars/Moon",
                    colls[i]["mar"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Unwanted expenses. Fever, blood related issues."
                result.append(rec.copy())
            if colls[i]["mer"] >= dlower and colls[i]["mer"] <= dhigher:
                mAstemp = ma['mer']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Mercury/Moon",
                    colls[i]["mer"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Stress level up. Financial Hiccups. Confidence and courage down. Travel discouraged"
                result.append(rec.copy())

            # Rah over moo, health
            if colls[i]["rah"] >= dlower and colls[i]["rah"] <= dhigher:
                mAstemp = ma['rah']
                mAstak = mAstemp[msign - 1]
                rec = getRec(
                    "Rahu/Moon",
                    colls[i]["rah"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    mAstak
                )
                rec["result"] = "Squandering Money. Careless. Mentally disturbed. Lack of peace of mind"
                result.append(rec.copy())
            if colls[i]["ket"] >= dlower and colls[i]["ket"] <= dhigher:
                rec = getRec(
                    "Ketu/Moon",
                    colls[i]["ket"],
                    natData["moo"],
                    natData["Asc"],
                    colls[i]["yr"],
                    colls[i]["mo"],
                    -1,
                )
                rec["result"] = "Mental tensions. Health is down. Loss of reputation"
                result.append(rec.copy())

    return mResult, result
# endef

# DEF void ashtakCompute
def ashtakCompute(a, b, c, d, e, f, g, h, i, j, k, l, n):
    p = 0
    q = 0
    k2 = [0] * 13
    ash2 = [0] * 12

    k2[1] = a
    k2[2] = b
    k2[3] = c
    k2[4] = d
    k2[5] = e
    k2[6] = f
    k2[7] = g
    k2[8] = h
    k2[9] = i
    k2[10] = j
    k2[11] = k
    k2[12] = l
    for q in range(1, 12):
        p = n + q - 1
        if p > 12:
            p = p - 12
        ash2[int(p)-1] = ash2[int(p)-1] + k2[q]
    # end for
    return ash2
# UNDEF ashtakCompute

# DEF findAshtakVarga
def findAshtakVarga(plnt):
    csun = math.floor(plnt['sun'] / 30 + 1)
    dmoon = math.floor(plnt['moo'] / 30 + 1)
    emars = math.floor(plnt['mar'] / 30 + 1)
    fmercury = math.floor(plnt['mer'] / 30 + 1)
    gjupiter = math.floor(plnt['jup'] / 30 + 1)
    hvenus = math.floor(plnt['ven'] / 30 + 1)
    isaturn = math.floor(plnt['sat'] / 30 + 1)
    jlagna = math.floor(plnt['lag'] / 30 + 1)
    ashObj = {}

    # Rules for Bindu / Rekha for Sun / Surya
    a1 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, csun)
    a2 = ashtakCompute(0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, dmoon)
    a3 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, emars)
    a4 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, fmercury)
    a5 = ashtakCompute(0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, gjupiter)
    a6 = ashtakCompute(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, hvenus)
    a7 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, isaturn)
    a8 = ashtakCompute(0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['sun'] = [sum(x) for x in zip(*temp)]

    # Next is Moon or Chandra
    a1 = ashtakCompute(0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, csun)
    a2 = ashtakCompute(1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, dmoon)
    a3 = ashtakCompute(0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, emars)
    a4 = ashtakCompute(1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, fmercury)
    a5 = ashtakCompute(1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, gjupiter)
    a6 = ashtakCompute(0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, hvenus)
    a7 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, isaturn)
    a8 = ashtakCompute(0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['moo'] = [sum(x) for x in zip(*temp)]
    
    # Mars
    a1 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, csun)
    a2 = ashtakCompute(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, dmoon)
    a3 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, emars)
    a4 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, fmercury)
    a5 = ashtakCompute(0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, gjupiter)
    a6 = ashtakCompute(0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, hvenus)
    a7 = ashtakCompute(1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, isaturn)
    a8 = ashtakCompute(1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['mar'] = [sum(x) for x in zip(*temp)]

    # Mercury
    a1 = ashtakCompute(0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, csun)
    a2 = ashtakCompute(0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, dmoon)
    a3 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, emars)
    a4 = ashtakCompute(1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, fmercury)
    a5 = ashtakCompute(0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, gjupiter)
    a6 = ashtakCompute(1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, hvenus)
    a7 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, isaturn)
    a8 = ashtakCompute(1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['mer'] = [sum(x) for x in zip(*temp)]

    # Jupiter
    a1 = ashtakCompute(1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, csun)
    a2 = ashtakCompute(0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, dmoon)
    a3 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, emars)
    a4 = ashtakCompute(1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, fmercury)
    a5 = ashtakCompute(1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, gjupiter)
    a6 = ashtakCompute(0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, hvenus)
    a7 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, isaturn)
    a8 = ashtakCompute(1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['jup'] = [sum(x) for x in zip(*temp)]

    # Venus
    a1 = ashtakCompute(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, csun)
    a2 = ashtakCompute(1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, dmoon)
    a3 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, emars)
    a4 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, fmercury)
    a5 = ashtakCompute(0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, gjupiter)
    a6 = ashtakCompute(1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, hvenus)
    a7 = ashtakCompute(0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, isaturn)
    a8 = ashtakCompute(1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['ven'] = [sum(x) for x in zip(*temp)]

    # Saturn
    a1 = ashtakCompute(1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, csun)
    a2 = ashtakCompute(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, dmoon)
    a3 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, emars)
    a4 = ashtakCompute(0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, fmercury)
    a5 = ashtakCompute(0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, gjupiter)
    a6 = ashtakCompute(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, hvenus)
    a7 = ashtakCompute(0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, isaturn)
    a8 = ashtakCompute(1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['sat'] = [sum(x) for x in zip(*temp)]
    
    a1 = ashtakCompute(1,1,1,1,0,0,1,1,0,1,0,0,csun)
    a2 = ashtakCompute(1,0,1,0,1,0,1,1,1,1,0,0,dmoon)
    a3 = ashtakCompute(0,1,1,0,1,0,0,0,0,0,0,1,emars)
    a4 = ashtakCompute(0,1,0,1,0,0,1,1,0,0,0,1,fmercury)
    a5 = ashtakCompute(1,0,1,1,0,1,0,1,0,0,0,0,gjupiter)
    a6 = ashtakCompute(0,0,0,0,0,1,1,0,0,0,1,1,hvenus)
    a7 = ashtakCompute(0,0,1,0,1,0,1,0,0,1,1,1,isaturn)
    a8 = ashtakCompute(0,0,1,1,1,0,0,0,1,0,0,1,jlagna)
    temp = [a1, a2, a3, a4, a5, a6, a7, a8]
    ashObj['rah'] = [sum(x) for x in zip(*temp)]
    print ('ashObj', ashObj)

    return ashObj