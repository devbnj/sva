# main.py

from flask import Blueprint, render_template, json, request, session
from flask_login import login_required, current_user
# import os
from flask import current_app as app
from . import db
from .models import Vivek
from .MainEvents import run as moonrun
from .MainHome import homerun

pagecount = 1
maxpage = 1
advpg = 0
advmax = 70
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/resort/')
def resort():
    return render_template('resinput.html')

@main.route('/travel/')
@login_required
def travel():
    return render_template('travelinput.html', name=current_user.name, rigved=current_user.bgcode)

@main.route('/mind/')
@login_required
def mind():
    return render_template('mindinput.html')

@main.route('/mind/', methods=['POST'])
@login_required
def mindpost():
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
    mooner, minder = moonrun(yr, mo, dy, hr, mi, tz, ln, lt, sy, ey)
    # mooner, minder = moonrun(1959, 11, 12, 13, 30, +5.5, 88.3639, 22.5726, 2020, 2022)
    return render_template('mind.html', name=current_user.name, rigved=current_user.bgcode, posts=minder, mpost=mooner)

@main.route('/body/')
@login_required
def body():
    return render_template('homeoinput.html')

@main.route('/body/', methods=['POST'])
@login_required
def bodypost():
    # print ("Got Hit")
    tc = request.form.get('tchar')
    f = homerun(tc)
    return render_template('homeo.html', name=current_user.name, hpost=f)

@main.route('/profile/')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, rigved=current_user.bgcode)

'''
# def
def commonClass(pg):
    if pg == 0:
        pg = 1
    if 'page' in session:
        pg = session['page']
    filename = os.path.join(app.static_folder, ('class%d.json') % pg)
    actdata = {}
    with open(filename) as scriptures_file:
        tdata = json.load(scriptures_file)
        # print (tdata)
        actdata = tdata["data"]
    return render_template('class.html', name=current_user.name, page=pg, posts=actdata)
# end def

# def
def vivekDb(page=0, page_size=None):
    gc = db.session.query(Vivek)
    if page_size:
        gc = gc.limit(page_size)
    if page: 
        gc = gc.offset(page*page_size)    
    return render_template('class2.html', name=current_user.name, post1=gc)
# end def

# def
@main.route('/sankara/')
@login_required
def sankarclass():
    global pagecount
    pagecount = 1
    return commonClass(pagecount)
# end def

# def
@main.route('/vivek/')
@login_required
def vivekclass():
    global pagecount
    return vivekDb(0, 1)
# end def

# def
@main.route('/auro/')
@login_required
def auroclass():
    global pagecount
    pagecount = 1
    return commonClass(pagecount)
# end def

# def
@main.route('/yuktes/')
@login_required
def yuktesclass():
    global pagecount
    return vivekDb(0, 1)
# end def

# def
@main.route('/prevclass/')
@login_required
def prevclass():
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
# end def

# def
@main.route('/advprev/')
@login_required
def advprev():
    global advpg
    advpg = advpg - 1
    if (advpg < 0):
        advpg = 0
    return vivekDb(advpg, 1)
# end def

# def
@main.route('/advnext/')
@login_required
def advnext():
    global advpg
    advpg = advpg + 1
    if advpg > advmax:
        advpg = advmax
    return vivekDb(advpg, 1)
# end def

@main.route('/nextclass/')
@login_required
def nextclass():
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

'''

@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500