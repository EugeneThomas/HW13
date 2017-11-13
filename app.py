# Eugene Thomas
# SoftDev1 pd7
# HW13 -- A RESTful Journey Skyward
# 2017-11-08


from flask import Flask, request, render_template, session, redirect, url_for, flash
import os
import urllib2, json

app = Flask(__name__) #create instance of class
app.secret_key = os.urandom(32)

### while my api reading isnt working optimally....

LIST = [{"borough_code":"X","fromstreetname":"CRESTON AVENUE","onstreetname":"EAST BURNSIDE AVENUE","purpose":"OCCUPANCY OF SIDEWALK AS STIPULATED","segmentid":"175855","tostreetname":"GRAND CONCOURSE","work_end_date":"2017-05-16T23:58:59.000","work_start_date":"2017-04-14T00:00:00.000"}
,{"borough_code":"Q","fromstreetname":"SUNBURY ROAD","onstreetname":"IRWIN PLACE","purpose":"DEP CONTRACTOR MAJOR INSTALLATION SEWER","segmentid":"129283","tostreetname":"TROUTVILLE ROAD","work_end_date":"2017-06-02T23:58:59.000","work_start_date":"2017-04-06T11:54:47.000"}
,{"borough_code":"S","fromstreetname":"BAYONNE BRIDGE","onstreetname":"RICHMOND TERRACE","purpose":"CROSSING SIDEWALK","segmentid":"160201","tostreetname":"BAYONNE BRIDGE","work_end_date":"2017-05-02T23:58:59.000","work_start_date":"2017-04-24T00:00:00.000"}
,{"borough_code":"Q","fromstreetname":"DAVIS COURT","onstreetname":"49 AVENUE","purpose":"DOT IN-HOUSE PAVING","segmentid":"35732","tostreetname":"LONG ISLAND RAILROAD","work_end_date":"2017-05-15T23:59:59.000","work_start_date":"2017-04-10T00:00:00.000"}
,{"borough_code":"S","fromstreetname":"PARK STREET","onstreetname":"SHADOW LANE","purpose":"D.D.C. CONTRACTOR MAJOR RECONSTRUCTION","segmentid":"7419","tostreetname":"TYSENS LANE","work_end_date":"2017-06-05T23:58:59.000","work_start_date":"2017-03-08T00:00:00.000"}
,{"borough_code":"S","fromstreetname":"KOREAN WAR VETS PARKWAY","onstreetname":"DRUMGOOLE ROAD WEST","purpose":"DOT IN-HOUSE PAVING","segmentid":"159627","tostreetname":"WATKINS AVENUE","work_end_date":"2017-05-08T23:59:59.000","work_start_date":"2017-04-19T07:44:25.000"}
,{"borough_code":"Q","fromstreetname":"GLENMORE AVENUE","onstreetname":"76 STREET","purpose":"PLACE CRANE OR SHOVEL ON STREET","segmentid":"120839","tostreetname":"NYCTA","work_end_date":"2017-05-08T23:58:59.000","work_start_date":"2017-04-28T00:00:00.000"}
,{"borough_code":"B","fromstreetname":"BOERUM STREET","onstreetname":"BOGART STREET","purpose":"OCCUPANCY OF ROADWAY AS STIPULATED","segmentid":"44463","tostreetname":"JOHNSON AVENUE","work_end_date":"2017-05-22T23:58:59.000","work_start_date":"2017-04-20T00:00:00.000"}
,{"borough_code":"B","fromstreetname":"BEDFORD AVENUE","onstreetname":"RUTLEDGE STREET","purpose":"OCCUPANCY OF ROADWAY AS STIPULATED","segmentid":"30695","tostreetname":"LEE AVENUE","work_end_date":"2017-05-04T23:58:59.000","work_start_date":"2017-02-03T00:00:00.000"}
,{"borough_code":"Q","fromstreetname":"43 AVENUE","onstreetname":"9 STREET","purpose":"PLACE CRANE OR SHOVEL ON STREET","segmentid":"36859","tostreetname":"43 ROAD","work_end_date":"2017-05-21T23:58:59.000","work_start_date":"2017-04-19T13:27:11.000"}
,{"borough_code":"Q","fromstreetname":"128 STREET","onstreetname":"20 AVENUE","purpose":"DOT IN-HOUSE PAVING","segmentid":"84946","tostreetname":"129 STREET","work_end_date":"2017-06-12T23:59:59.000","work_start_date":"2017-05-08T00:00:00.000"}
,{"borough_code":"B","fromstreetname":"FLATBUSH AVENUE","onstreetname":"NEVINS STREET","purpose":"OCCUPANCY OF ROADWAY AS STIPULATED","segmentid":"192287","tostreetname":"LIVINGSTON STREET","work_end_date":"2017-05-01T23:58:59.000","work_start_date":"2017-03-23T15:33:12.000"}
,{"borough_code":"X","fromstreetname":"EAST  192 STREET","onstreetname":"GRAND CONCOURSE","purpose":"OCCUPANCY OF SIDEWALK AS STIPULATED","segmentid":"176301","tostreetname":"EAST  193 STREET","work_end_date":"2017-05-28T23:58:59.000","work_start_date":"2017-04-26T00:00:00.000"}
,{"borough_code":"M","fromstreetname":"SOUTH STREET","onstreetname":"BATTERY PARK VIADUCT","purpose":"NYCDOT-BRIDGES RECONSTRUCTION","segmentid":"258232","tostreetname":"BKLYN BATTERY TUNNEL","work_end_date":"2017-07-12T23:58:59.000","work_start_date":"2017-04-17T11:58:56.000"}
,{"borough_code":"Q","fromstreetname":"COLLEGE POINT BOULEVARD","onstreetname":"39 AVENUE","purpose":"OCCUPANCY OF ROADWAY AS STIPULATED","segmentid":"91052","tostreetname":"PRINCE STREET","work_end_date":"2017-05-11T23:58:59.000","work_start_date":"2017-04-02T00:00:00.000"}
,{"borough_code":"M","fromstreetname":"BEND","onstreetname":"5 AVENUE","purpose":"D.D.C. CONTRACTOR MAJOR RECONSTRUCTION","segmentid":"33006","tostreetname":"EAST   23 STREET","work_end_date":"2017-05-14T23:58:59.000","work_start_date":"2017-04-21T12:08:52.000"}
,{"borough_code":"S","fromstreetname":"SOUTH RAILROAD AVENUE","onstreetname":"PETER AVENUE","purpose":"D.D.C. CONTRACTOR MAJOR RECONSTRUCTION","segmentid":"7516","tostreetname":"8 STREET","work_end_date":"2017-06-30T23:58:59.000","work_start_date":"2017-04-01T00:00:00.000"}
,{"borough_code":"X","fromstreetname":"BRONX BOULEVARD","onstreetname":"EAST  226 STREET","purpose":"DOT IN-HOUSE PAVING","segmentid":"88917","tostreetname":"CARPENTER AVENUE","work_end_date":"2017-07-05T23:59:59.000","work_start_date":"2017-04-07T07:52:21.000"}
,{"borough_code":"X","fromstreetname":"COSTER STREET","onstreetname":"HUNTS POINT AVENUE","purpose":"DOT IN-HOUSE PAVING","segmentid":"9002149","tostreetname":"GILBERT PLACE","work_end_date":"2017-07-15T23:59:59.000","work_start_date":"2017-04-17T14:59:23.000"}]

#data = urllib2.request.urlopen("https://data.cityofnewyork.us/resource/p9yb-iscp.json")
#string = data.read()
#d = json.loads(string)


### The Root Route:

@app.route('/')
def hello():
    retList = []
    for l in LIST:
        d = {}
        d["borough"] = code_to_borough(l["borough_code"])
        d["fromS"] = l["fromstreetname"]
        d["toS"] = l["tostreetname"]
        d["onS"] = l["onstreetname"]
        d["purpose"] = l["purpose"]
        retList.append(d)
    return render_template("data.html", l = retList)

def code_to_borough(code):
    if code == "X":
        return "the Bronx"
    if code == "Q":
        return "Queens"
    if code == "S":
        return "Staten Island"
    if code == "M":
        return "Manhattan"
    if code == "B":
        return "Brooklyn"

if __name__=="__main__":
    app.debug = True
    app.run()
