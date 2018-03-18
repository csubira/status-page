#!flask/bin/python
from flask import Flask, g, session, jsonify, render_template, request, redirect, url_for, json, flash
from forms import StatusForm
from datetime import datetime
import logging


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['AUTO_MODE'] = True
MODES = dict([(True, "Automatic"), (False, "Manual")])

# logger = logging.getLogger('myapp')
# hdlr = logging.FileHandler('myapp.log')
# logging.basicConfig(filename='example.log')
# hdlr.setFormatter(formatter)
# app.config['WTF_CSRF_ENABLED'] = False
statusList=[
 {
 'status': 1,
 'message':'Working',
 'date':'Today',
 'auto_mode': True
 },
 {
 'status': 0,
 'message':'Not Working',
 'date':'Today',
 'auto_mode': True
 },{
 'status': 2,
 'message':'Psa',
 'date':'Today',
 'auto_mode': True
 },{
 'status': 1,
 'message':'Not Working',
 'date':'Today',
 'auto_mode': True
 }
]


@app.route('/change_mode', methods=['POST'])
def change_mode():
    app.config['AUTO_MODE'] = not app.config['AUTO_MODE']
    flash('You are now on ' + MODES[app.config['AUTO_MODE']] + ' mode')
    return redirect(url_for('get_all_status'))


@app.route('/status-page',methods=['GET'])
def get_all_status():
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')
    # logger = logging.getLogger('INFO')
    # get_mode()
    # logger = logging.getLogger('myapp')
    # hdlr = logging.FileHandler('myapp.log')
    # formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # hdlr.setFormatter(formatter)
    # logger.addHandler(hdlr) 
    # logger.setLevel(logging.WARNING)
    # logger.error('We have a problem')
    # logger.info('While this is just chatty')
    g._mode = {'auto': app.config['AUTO_MODE'], 'text': MODES[app.config['AUTO_MODE']] }
    return render_template('main.html', status_list=reversed(statusList))

@app.route('/status-page/update', methods=['POST'])
def update():
    if app.config['AUTO_MODE']:
        r = json.loads(request.data)

        dat = {
        'status': r['status'],
        'message':r['message'],
        'date': r['date'],
        'auto_mode': True
        }

        statusList.append(dat)
        # return jsonify({'response':'Success'})
        # file = open("testfile.txt","w") 
        # file.write(''.join(statusList))
        # file.close() 

        # print statusList
        # return render_template('main.html', status_list=statusList)
    return jsonify({'response':'Success'})


@app.route('/status-page/manual-update', methods=['GET', 'POST'])
def manual_update():
    if app.config['AUTO_MODE']:
        flash('You cannot update an status in Automatic Mode!')
        return redirect(url_for('get_all_status'))
    form = StatusForm()
    print 'hello'    
    print form.errors

    if form.is_submitted():
        dat = {
            'status': int(form.status.data),
            'message': str(form.message.data),
            'date': str(datetime.now()),
            'auto_mode': False
        }
        print dat
        statusList.append(dat)

        return redirect(url_for('get_all_status'))

    # if form.validate():
    #     print "valid"

    # if form.validate_on_submit():
 
    #     # Check the password and log the user in
    #     # [...]
    #     print 'estamos aqui'
    #     print form.status
 
    return render_template('manual_update.html', form=form)
# @app.route('/')
# def index():
#     return "Hello, World!"

# @app.route('/empdb/employee',methods=['GET'])
# def getAllEmp():
#     # return jsonify({'emps':empDB})
#     return render_template('main.html', status_list=empDB)

# @app.route('/empdb/employee/<empId>',methods=['GET'])
# def getEmp(empId):
#     usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
#     return jsonify({'emp':usr})

# @app.route('/empdb/employee/<empId>',methods=['PUT'])
# def updateEmp(empId): 
#     em = [ emp for emp in empDB if (emp['id'] == empId) ] 
#     if 'name' in request.json : 
#         em[0]['name'] = request.json['name'] 
#     if 'title' in request.json:
#         em[0]['title'] = request.json['title'] 
#     return jsonify({'emp':em[0]})

# @app.route('/empdb/employee',methods=['POST'])
# def createEmp(): 
#     dat = {
#     'id':request.json['id'],
#     'name':request.json['name'],
#     'title':request.json['title']
#     }
#     empDB.append(dat)
#     return jsonify(dat)

# @app.route('/empdb/employee/<empId>',methods=['DELETE'])
# def deleteEmp(empId): 
#     em = [ emp for emp in empDB if (emp['id'] == empId) ] 
#     if len(em) == 0:
#         abort(404) 
#     empDB.remove(em[0])
#     return jsonify({'response':'Success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
