import requests
import json
from random import *
from datetime import datetime

status = {'status': randint(0, 2), 'date': datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

r = requests.post("http://127.0.0.1:5000/status-page/update", json.dumps(status))
print status
print r.json