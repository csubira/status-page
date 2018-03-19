#!flask/bin/python
from flask import Flask, g, session, jsonify, render_template, request, redirect, url_for, json, flash
from forms import StatusForm
from datetime import datetime


app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['AUTO_MODE'] = True
MODES = dict([(True, "Automatic"), (False, "Manual")])
STATUS_TEXT = {0: "The platform is down", 1: "The platform is healty", 2: "The platform is having some issues"}
STATUS_LIST=[
 {
 'status': 1,
 'message': STATUS_TEXT[1],
 'date': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
 'auto_mode': True
 }
]

def save_status(status):
    file = open('status.log', 'a')
    status_log = "%s %s %s \n" % (MODES[status['auto_mode']], status['date'], status['message'])
    file.write(status_log)
    file.close()

save_status(STATUS_LIST[0])


# Routes
@app.route('/change_mode', methods=['POST'])
def change_mode():
    app.config['AUTO_MODE'] = not app.config['AUTO_MODE']
    flash('You are now on ' + MODES[app.config['AUTO_MODE']] + ' mode')
    return redirect(url_for('get_all_status'))


@app.route('/status-page',methods=['GET'])
def get_all_status():
    g._mode = {'auto': app.config['AUTO_MODE'], 'text': MODES[app.config['AUTO_MODE']] }
    return render_template('main.html', status_list=reversed(STATUS_LIST))

@app.route('/status-page/update', methods=['POST'])
def update():
    if app.config['AUTO_MODE']:
        r = json.loads(request.data)
        status_num = r['status']

        current_status = {
        'status': r['status'],
        'message': STATUS_TEXT[status_num],
        'date': r['date'],
        'auto_mode': True
        }

        STATUS_LIST.append(current_status)
        save_status(current_status)
    return jsonify({'response':'Success'})


@app.route('/status-page/manual-update', methods=['GET', 'POST'])
def manual_update():
    if app.config['AUTO_MODE']:
        flash('You cannot update an status in Automatic Mode!')
        return redirect(url_for('get_all_status'))

    form = StatusForm()
    if form.is_submitted():
        new_status = {
            'status': int(form.status.data),
            'message': str(form.message.data),
            'date': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'auto_mode': False
        }
        STATUS_LIST.append(new_status)
        save_status(new_status)
        return redirect(url_for('get_all_status'))
 
    return render_template('manual_update.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
