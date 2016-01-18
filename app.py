#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from flask import Flask,request,Response
import yasik, conference, sadari

app = Flask(__name__)

def make_bot(name, handler):
    def handler_wrapper():
        command = request.form['command']
        text = request.form['text']
        print command

        msg="""{
        "response_type" : "in_channel",
        "text" : "%s"
        }
        """ % handler(text)
        print msg

        return msg, 200, {"Content-Type":"application/json"}
    app.add_url_rule("/"+name,name,handler_wrapper, methods=['GET','POST'])

if __name__ == '__main__':
    # make bots with command and handler
    make_bot("yasik", yasik.get_yasik)
    make_bot("conf", conference.get_Confer_Info)
    make_bot("sadari", sadari.sadari)
    app.run( host='0.0.0.0', port=10000, threaded=True, debug=False)

