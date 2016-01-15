# -*- coding: utf-8 -*-
from flask import Flask,request,Response
import urllib2
import re
import random
import time
import yasik, conference

app = Flask(__name__)




@app.route('/yasik', methods=['GET','POST'])
def yasik_bot():
    print request.form
    command = request.form['command']
    text = request.form['text']
    print command

    msg="""{
    "response_type" : "in_channel",
    "text" : "%s"
    }
    """ % yasik.get_yasik(text)
    print msg

    return msg, 200, {"Content-Type":"application/json"}


@app.route('/conf', methods=['GET','POST'])
def conf_bot():
    print request.form
    command = request.form['command']
    text = request.form['text']
    print command
    msg="""{
    "response_type" : "in_channel",
    "text" : "%s"
    }
    """ % conference.get_Confer_Info(text)
    print msg

    return msg, 200, {"Content-Type":"application/json"}

if __name__ == '__main__':
    conference.init()
    app.run(debug=True, host='0.0.0.0', port=8080)

