# main.py

from flask import Blueprint, render_template, request, session
from flask import current_app as app
from .MainEvents import run as moonrun, sunrun
from .MainHome import homerun, homesrch, homeMultiSrch, homeThreeSrch
from .MainAyur import ayutrt
import sqlite3, os, json
from sqlite3 import dbapi2 as sqlite

pagecount = 1
maxpage = 17
main = Blueprint('main', __name__)

# def
def commonClass(pg):
    if pg == 0:
        pg = 1
    if 'page' in session:
        pg = session['page']
    filename = os.path.join(app.static_folder, ('ayur/ayur%d.json') % pg)
    hdr, bdy, pg1, pg2, note, cav = {}, {}, {}, {}, {}, {}
    with open(filename) as ayur_file:
        tdata = json.load(ayur_file)
        hdr = tdata["header"]
        bdy = tdata['body']
        pg1 = tdata["para1"]
        pg2 = tdata["para2"]
        if "notes" in tdata:
            note = tdata["notes"]
        if "caveat" in tdata:
            cav = tdata["caveat"]
    return render_template('ayur01.html', hding=hdr, bdy=bdy, pg1=pg1, pg2=pg2, nt=note, cv=cav, pg=pg, mx=maxpage)
# end def

@main.route('/prev/')
def prev():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    # page decrement
    pg = pg - 1
    if pg < 1:
        pg = 1
    session['page'] = pg
    return commonClass(pg)

@main.route('/next/')
def nextc():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    if pg < maxpage:
        pg = pg + 1
    session['page'] = pg
    return commonClass(pg)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/resort/')
def resort():
    return render_template('resinput.html')

@main.route('/travel/')
def travel():
    return render_template('travelinput.html')

@main.route('/const/')
def constitute():
    return render_template('ayur02.html', hding="Constitution Physical Questions")

@main.route('/ayursrch/')
def asrch():
    return render_template('ayurinput.html')

@main.route('/ayurtreat/')
def tsrch():
    return render_template('atinput.html')

@main.route('/ayurtreat1/', methods=['POST'])
def atreatfound():
    h = request.form.get('humor')
    p = request.form.get('area')
    result = ayutrt(p, h)
    hd = result["header"]
    bd = result["body"]
    sy1 = result["sy1"]
    sy2 = result["sy2"]
    sy3 = result["sy3"]
    tr1 = result["tr1"]
    tr2 = result["tr2"]
    tr3 = result["tr3"]
    tr4 = result["tr4"]
    tr5 = result["tr5"]
    tr6 = result["tr6"]
    return render_template('atfnd.html', hd=hd, bd=bd, sy1=sy1, sy2=sy2, sy3=sy3, \
         tr1=tr1, tr2=tr2, tr3=tr3, tr4=tr4, tr5=tr5, tr6=tr6,)


@main.route('/ayur2/', methods=['POST'])
def ahfound():
    s = request.form.get('asymp')
    filename = os.path.join(app.static_folder, ('awsym/' + s + '.json'))
    nm, v, p, k, desc, vd, pd, kd = "", "", "", "", "","","",""
    with open(filename) as ayur_file:
        tdata = json.load(ayur_file)
        try:
            nm = tdata["name"]
            v = tdata["V"]
            p = tdata['P']
            k = tdata["K"]
            desc = tdata["desc"]
            vd = tdata["vdesc"]
            pd = tdata["pdesc"]
            kd = tdata["kdesc"]
        except:
            # ignore
            print ("error in traversing")

    return render_template('ayurfnd.html', nm=nm, v=v, p=p, k=k, d=desc, vd=vd, pd=pd, kd=kd)


vsum, psum, ksum = 0, 0, 0
def summit(st, vs, ps, ks):
    if (st == 'v'): vs = vs + 1 
    if (st == 'p'): ps = ps + 1 
    if (st == 'k'): ks = ks + 1
    return vs, ps, ks

@main.route('/const01/', methods=['POST'])
def pconstitute():
    global vsum, psum, ksum
    vsum, psum, ksum = 0, 0, 0
    s = request.form.get('selbuild')
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selweight")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selweightmngt")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selskin")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selhair")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selteeth")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("seleyes")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("sellips")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selchin")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selcheeks")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selneck")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selnails")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selchest")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selbelly")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selnavel")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selhips")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    return render_template('ayur03.html', hding="Constitution Physical Questions", vs=vsum, ps=psum, ks=ksum)

@main.route('/const02/', methods=['POST'])
def tconstitute():
    global vsum, psum, ksum
    s = request.form.get("seljoints")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selappetite")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("seltaste")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("seldigest")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selevacuate")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selthirst")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selperspire")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selactivity")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selmental")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selstamina")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selsleep")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selemotion")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("seltemperament")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selintellect")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selspeech")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selfaith")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selspiritual")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("seldream")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selsex")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    s = request.form.get("selfinance")
    vsum, psum, ksum = summit(s, vsum, psum, ksum)
    chk = ''
    if max(vsum, psum, ksum) == vsum:
        chk = 'Vata'
    elif max(vsum, psum, ksum) == psum:
        chk = 'Pitta'
    else:
        chk = 'Kapha'
    return render_template('ayur04.html', hding="Constitution Questions Concluded", \
        vs=vsum, ps=psum, ks=ksum, chk=chk)
	    
@main.route('/ayur/')
def ayur():
    global pagecount
    session['page'] = 1
    return commonClass(pagecount)

@main.route('/mind/')
def mind():
    con = sqlite3.connect('atlas.db')
    cur = con.cursor()
    res = []
    res2 = []
    for row in cur.execute('select iso, country from CountryInfo'):
        res.append({'iso':row[0], 'country': row[0] + ' | ' + row[1]})
    return render_template('placeinput.html', postcountry=res)

@main.route('/mind0/', methods=['POST'])
def mind0():
    con = sqlite3.connect('atlas.db')
    cur = con.cursor()
    iso = request.form.get('iso')
    ctr = '%' + request.form.get('place') + '%'
    rst = []
    res = {}

    xsql = "SELECT A._idx, A.name, A.asciiname, A.alternatenames, B.iso, A.latitude, A.longitude, A.elevation, C.timezoneid, C.gmtoffset, C.dstoffset, C.rawoffset FROM GeoNames as A, CountryInfo AS B, Timezones AS C WHERE B.iso = (?) AND B._idx = A.country AND (A.name LIKE (?)) AND A.timezone = C._idx ORDER BY A.name"
    for row in cur.execute(xsql, (iso, ctr)):
        res['id'] = row[0]
        res['name'] = str(row[1]) + "|Alt:" + str(row[3]) +"|Lat: "+ str(row[5]) + "|Lng: " + str(row[6]) + "|TZ:"+ str(row[8])
        rst.append(res.copy())
    # print ('res', rst)
    return render_template('placeinter.html', postplace=rst, iso=iso, ctr=ctr)    

@main.route('/mind1/', methods=['POST'])
def mind1():
    con = sqlite3.connect('atlas.db')
    cur = con.cursor()
    iso = request.form.get('iso')
    ctr = '%' + request.form.get('ctr') + '%'
    plc = request.form.get('plc')
    res = {}

    xsql = "SELECT A._idx, A.name, A.asciiname, A.alternatenames, B.iso, A.latitude, A.longitude, A.elevation, C.timezoneid, C.gmtoffset, C.dstoffset, C.rawoffset FROM GeoNames as A, CountryInfo AS B, Timezones AS C WHERE A._idx = (?) AND B.iso = (?) AND B._idx = A.country AND (A.name LIKE (?)) AND A.timezone = C._idx ORDER BY A.name"
    for row in cur.execute(xsql, (plc, iso, ctr)):
        res['name'] = str(row[1]) + ', ' + str(row[4])
        res['lng'] = str(row[6]) 
        res['lat'] = str(row[5]) 
        res['gmt'] = str(row[9]) 
        res['dst'] = str(row[10]) 
    print ('res', res)
    return render_template('mindinput.html', postplace=res)    

@main.route('/mind/', methods=['POST'])
def mindpost():
    zt = {}
    yr = int(request.form.get('yr'))
    mo = int(request.form.get('mo'))
    dy = int(request.form.get('dy'))
    hr = int(request.form.get('hr'))
    mi = int(request.form.get('mn'))
    tz = float(request.form.get('tz'))
    ln = float(request.form.get('ln'))
    lt = float(request.form.get('lt'))
    sy = int(request.form.get('sy'))
    ey = int(request.form.get('ey'))
    zt['yr'] = yr
    zt['mo'] = mo
    zt['dy'] = dy
    zt['hr'] = hr
    zt['mn'] = mi
    zt['tz'] = tz
    zt['ln'] = ln
    zt['lt'] = lt
    zt['sy'] = sy
    zt['ey'] = ey
    mooner, minder = moonrun(yr, mo, dy, hr, mi, tz, ln, lt, sy, ey)
    # mooner, minder = moonrun(1959, 11, 12, 13, 30, +5.5, 88.3639, 22.5726, 2020, 2022)
    return render_template('mind.html', posts=minder, mpost=mooner, mdt=zt)

@main.route('/spirit/', methods=['POST'])
def spiritpost():
    zt = {}
    yr = int(request.form.get('yr'))
    mo = int(request.form.get('mo'))
    dy = int(request.form.get('dy'))
    hr = int(request.form.get('hr'))
    mi = int(request.form.get('mn'))
    tz = float(request.form.get('tz'))
    ln = float(request.form.get('ln'))
    lt = float(request.form.get('lt'))
    sy = int(request.form.get('sy'))
    ey = int(request.form.get('ey'))
    zt['yr'] = yr
    zt['mo'] = mo
    zt['dy'] = dy
    zt['hr'] = hr
    zt['mn'] = mi
    zt['tz'] = tz
    zt['ln'] = ln
    zt['lt'] = lt
    zt['sy'] = sy
    zt['ey'] = ey
    suner, sunder = sunrun(yr, mo, dy, hr, mi, tz, ln, lt, sy, ey)
    return render_template('spirit.html', posts=sunder, mpost=suner, mdt=zt)

@main.route('/body/')
def body():
    return render_template('homeoinput.html')

@main.route('/body/', methods=['POST'])
def bodypost():
    tc = request.form.get('tchar')
    f = homerun(tc)
    return render_template('homeo.html', hpost=f, tpost='List Alphabetically')

@main.route('/body2/', methods=['POST'])
def body2post():
    tc = request.form.get('tchar2')
    f = homesrch(tc)
    return render_template('homeo.html', hpost=f, tpost='Search by '+tc)    

@main.route('/body3/', methods=['POST'])
def body3post():
    tc1 = request.form.get('symp1').lower()
    tc2 = request.form.get('symp2').lower()
    ta1 = request.form.get('cond1')
    f = homeMultiSrch(tc1, ta1, tc2)
    strtc = tc1 + ' ' + ta1 + ' [' + tc2 + '] '
    return render_template('homeo.html', hpost=f, tpost='Search by '+strtc, tc1=tc1, ta1=ta1, tc2=tc2)

@main.route('/body4/', methods=['POST'])
def body4post():
    tc1 = request.form.get('symp1').lower()
    tc2 = request.form.get('symp2').lower()
    tc3 = request.form.get('symp3').lower()
    ta1 = request.form.get('cond1')
    ta2 = request.form.get('cond2')
    f = homeThreeSrch(tc1, ta1, tc2, ta2, tc3)
    strtc = tc1 + ' ' + ta1 + ' [' + tc2 + '] ' + ta2 + ' [' + tc3 + '] '
    return render_template('homeo.html', hpost=f, tpost='Search by '+strtc, tc1=tc1, ta1=ta1, tc2=tc2,
            ta2=ta2, tc3=tc3)

@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500