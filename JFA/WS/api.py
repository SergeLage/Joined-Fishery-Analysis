from Models.vms_records import VMSRecords
from DAL.vms_recordsDAL import VMSRecordsDAL
from AS.register_core import RegisterCore
from datetime import datetime
from flask import render_template
from flask import Flask, jsonify
from flask import request
from WS import app
from threading import Thread

hello = {
    "language" : "Python",
    "framework" : "Flask",
    'name' : 'JFA API',
    'version' : 0.1
    }
#READ
@app.route('/')
@app.route('/home')
def getHome():
    return jsonify({'description': hello})

#CREATE
@app.route('/api/vms/newdata',methods=['POST'])
def newVMSData():
    vesselid = request.form.get('vesselid')
    utc = request.form.get('utc')
    gps_id = request.form.get('gps_id')
    fix = request.form.get('fix')
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    cog = request.form.get('cog')
    sog = request.form.get('sog')
    fix2 = request.form.get('fix2')
    lat2 = request.form.get('lat2')
    lon2 = request.form.get('lon2')
    isFishing = request.form.get('isFishing')
    data = VMSRecords(vesselid,utc, gps_id, fix, lat, lon, cog, sog, fix2, lat2,lon2, isFishing  )
    #RegisterCore.newEntry(data)
    thread = Thread(target = RegisterCore.newEntry, args = (data, ))
    thread.start()
    return jsonify({'description': data.serialize()})
    

#UPDATE