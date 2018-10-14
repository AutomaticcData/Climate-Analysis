

#-------DEPENDENCIES--------------------------------
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify
from datetime import datetime, timedelta





#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)




#------------Precipitation dates setup ------------------------
#master_ds = session.query()
max_md = engine.execute('SELECT MAX(date) FROM measurement').first()
#print(max_md)
min_md = engine.execute('SELECT MIN(date) FROM measurement').first()
#print(min_md)
max_md = max_md[0]
min_md = min_md[0]

#calculate the start date from 12 months ago
months_ago = datetime.strptime(max_md,'%Y-%m-%d')
months_ago = months_ago - timedelta(days=365)

q_months_ago = months_ago.strftime("%Y-%m-%d")

#-----------Stations dates setup ----------------------------
"""
max_station_md = engine.execute("SELECT MAX(date) FROM measurement WHERE station = '" + mostactiveid + "'").first()
max_station_md = max_station_md[0]
#print(max_station_md)
#2017-08-18

#calculate the start date from 12 months ago
station_months_ago = datetime.strptime(max_station_md,'%Y-%m-%d')
station_months_ago = station_months_ago - timedelta(days=365)
#print(f'months_ago = {months_ago}')
#months_ago = 2016-08-23 00:00:00

q_station_months_ago = station_months_ago.strftime("%Y-%m-%d")
#print(f'q_station_months_ago = {q_station_months_ago}')
#q_station_months_ago = 2016-08-18
"""

#################################################
# Flask Routes
#################################################

'''
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes <hr>"
        #f"/api/v1.0/names<br/>"
        #f"/api/v1.0/passengers"
        "<a href='http://localhost:5000/api/v1.0/precipitation'>/api/v1.0/precipitation</a>"
        "<br>"
        "<a href='http://localhost:5000/api/v1.0/stations'>/api/v1.0/stations</a>"
        "<br>"
        "<a href='http://localhost:5000/api/v1.0/tobs'>/api/v1.0/tobs</a>"
        "<br>"
        "<a href='http://localhost:5000/api/v1.0/begindate/'>/api/v1.0/begindate"
        "<br>"
        "<a href='http://localhost:5000/api/v1.0/begindate/'>/api/v1.0/begindate/enddate"
        "<br>"
    )
'''


@app.route("/")
def welcome():
    html =        '<!DOCTYPE html>																																									  '
    html = html + '<html lang="en-us">																																								  '
    html = html + '<head>																																											  '
    html = html + '  <meta charset="UTF-8">																																							  '
    html = html + '    <title>Climate Analysis</title>																																				  '
    html = html + '    <style type="text/css">																																						  '
    html = html + '            p {																																									  '
    html = html + '                font-size: 30px;																																					  '
    html = html + '            }																																									  '
    html = html + '            li {																																									  '
    html = html + '                font-size: 25px;																																					  '
    html = html + '            }																																									  '
    html = html + '            h1 {																																									  '
    html = html + '                background-color: black;																																			  '
    html = html + '                color: yellow;																																					  '
    html = html + '            }																																									  '
    html = html + '            .shadow{																																								  '
    html = html + '                box-shadow: 5px 10px #888888;																																	  '
    html = html + '            }																																									  '
    html = html + '            .sectionback{																																						  '
    html = html + '                background-color: tomato;																																		  '
    html = html + '            }																																									  '
    html = html + '            .font2{																																								  '
    html = html + '                font-size: 25px																																					  '
    html = html + '            }																																									  '
    html = html + '            .whiteback{																																							  '
    html = html + '                background-color: whitesmoke;																																	  '
    html = html + '                color: black;																																					  '
    html = html + '            }																																									  '
    html = html + '																																													  '
    html = html + '            ul {																																									  '
    html = html + '                border: 1px solid whitesmoke;																																	  '
    html = html + '                }																																								  '
    html = html + '    </style>																																										  '
    html = html + '</head>																																											  '
    html = html + '<body background="http://localhost:5000/Resources/Hawaii.jpg">																																			  '
    html = html + '<h1>Climate Analysis Project and API</h1>																																		  '
    html = html + '<h3>Grab your board shorts. Surfs up dudes!</h3>																																	  '
    html = html + '<img class="shadow" src="https://uci.bootcampcontent.com/UCI-Coding-Bootcamp/UCIRV201807DATA4-2/raw/master/02-Homework/11-Advanced-Data-Storage-and-Retrieval/Instructions/Images/surfs-up.jpeg" height="200" width="400"/>																										  '
    html = html + '<section>																																										  '
    html = html + '	<p class="font2">																																								  '
    html = html + '            Hooray! We''ve decided to treat ourselves to a long holiday vacation in Honolulu, Hawaii! 																			  '
    html = html + '            <br>																																									  '
    html = html + '            To help with your trip planning, we have prepared some insightful API entry points.																					  '
    html = html + '    </p>																																											  '
    html = html + '    <div id="7" width="200"><p class="border1 whiteback shadow">Available Routes</p></div>																						  '
    html = html + '	<ul class="shadow">																																								  '
    html = html + '		<li><a href="http://localhost:5000/api/v1.0/precipitation" target="_blank">/api/v1.0/precipitation</a></li>																	  '
    html = html + '        <li><a href="http://localhost:5000/api/v1.0/stations" target="_blank">/api/v1.0/stations</a></li>																		  '
    html = html + '        <li><a href="http://localhost:5000/api/v1.0/tobs" target="_blank">/api/v1.0/tobs</a></li>																				  '
    html = html + '        <li><a href="http://localhost:5000/api/v1.0/begindate/" target="_blank" onclick="javascript:alert(''Use date format of 2016-08-19'')">/api/v1.0/begindate</a></li>			  '
    html = html + '        <li><a href="http://localhost:5000/api/v1.0/begindate/" target="_blank" onclick="javascript:alert(''Use date format of 2016-08-19'')">/api/v1.0/begindate/enddate</a></li>   '
    html = html + '    </ul>																																										  '
    html = html + '</section>																																										  '
    html = html + '</body>																																											  '
    html = html + '</html>																																											  '

    return html

@app.route("/api/v1.0/precipitation")
def rainfalls():
    #query rainfall
    rainfall = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > q_months_ago).group_by(Measurement.date).order_by(Measurement.date).all()

    #create a dictionary to hold key values for jsonification
    rainfall_dict = {}
    for value in rainfall:
        #print(value[0])
        #print('done')
        
        
        #get key/value pairs
        thedate = value[0]
        
        #deal with null values
        if value[1] == None:
            prcp = 0
        else:
            prcp = value[1]
        
        #add key/values to dictionary
        rainfall_dict[thedate] = prcp
        results = rainfall_dict

    return jsonify(results)
    #return value[0] + str(value[1])
#----------------------------------



@app.route("/api/v1.0/stations")
def stations():
    xunique_stations = engine.execute("SELECT id,station,name FROM station ORDER BY id DESC").fetchall()
    xus_df = pd.DataFrame(xunique_stations)
    xus_df = xus_df.rename(columns={0:"id",1:"Station",2:"Name"})
    results = xus_df.to_dict()

    #results = {"Date":datetime.today()}
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def temperatures():
    #!---------------------------------NOTE-------------------------------------------------------------------->
    #using session query here creates a separate thread for execution and then causes subsequent entry point errors
    #<--------------------------------------------------------------------------------------------------------!!!!
    
    #temperature = session.query(Measurement.date, Measurement.tobs).\
    #            filter(Measurement.date > q_months_ago).group_by(Measurement.date).order_by(Measurement.date).all()

    xt_df = pd.DataFrame(engine.execute("SELECT date, tobs from Measurement WHERE date>'" + q_months_ago + "' GROUP BY Measurement.date").fetchall())                
                
                
    #xt_df = pd.DataFrame(temperature)
    xt_df = xt_df.rename(columns={0:"date",1:"tobs"})
    results = xt_df.to_dict()
 
    
    #results = {"Date":datetime.today()}
    return jsonify(results)


@app.route("/api/v1.0/<begindate>/", defaults = {'enddate': None})
@app.route("/api/v1.0/<begindate>/<enddate>/")
def datesearch(begindate, enddate): 
    if enddate == None:
        ds_df = pd.DataFrame(engine.execute("SELECT MIN(tobs), MAX(tobs), AVG(tobs) from Measurement\
                                        WHERE date ='" + begindate + "'").fetchall())  
    else:
        ds_df = pd.DataFrame(engine.execute("SELECT MIN(tobs), MAX(tobs), AVG(tobs) from Measurement\
                                        WHERE date>'" + begindate + "' \
                                        AND date<='" + enddate + "' ").fetchall())  
        
             
    ds_df = ds_df.rename(columns={0:"TMIN",1:"TMAX",2:"TAVG"})
    results = ds_df.to_dict()
    
    #results = {"Date":"Enter a Valid Start Date"}
    #results = {"Date":datetime.today()}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

