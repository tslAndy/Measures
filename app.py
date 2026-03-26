from flask import Flask, request, Response, render_template
import json 
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
socketio = SocketIO(app)


measurements = []

@cross_origin
@app.route('/api/measurements')
def showmeas():
    isolista = []
    for mittausolio in measurements:
        row = [] 
        row.append(mittausolio["time"])
        row.append(mittausolio["pressure"])
        row.append(mittausolio["temperature"])
        row.append(mittausolio["humidity"])
        isolista.append(row)

    #sarjallistetaan
    s = json.dumps(measurements, indent=True)
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)

@app.route('/api/meas2')
def showmeas2():
    chartmeas = []

    for row in measurements:
        chartrow = []
        chartrow.append(row["time"])
        chartrow.append(row["pressure"])
        chartrow.append(row["temperature"])
        chartrow.append(row["humidity"])
        chartmeas.append(chartrow)

    s = json.dumps(chartmeas, indent=True)
    resp = Response(s, status=200, mimetype='application/json')
    return (resp)


#@cross_origin
@app.route('/')
def showpage():
    return render_template('measurements.html')


@app.route('/api/measurements', methods = ['POST'])
def newmeas():
    meas = request.get_json()
    measurements.append(meas)
    resp = Response("", status=200, mimetype='application/json')
    return (resp)

if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app, debug=True)