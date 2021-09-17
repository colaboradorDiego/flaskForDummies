from flask import jsonify
from flask import request
from flask import render_template
from flask import Flask

import json

app = Flask(__name__)


@app.route('/pie')
def google_pie_chart():
    data = {'Task': 'Hours per Day', 'Work': 11, 'Eat': 2, 'Commute': 2, 'Watching TV': 2, 'Sleeping': 7}
    # print(data)
    return render_template('pie.html', data=data)

@app.route('/statictable')
def google_staticTable_chart():
    return render_template('staticTable.html')

@app.route('/ajaxtable')
def google_ajaxtable():
    return render_template('ajaxTable.html')



@app.route('/semistatictable')
def google_semiStaticTable_chart():
    covid = {"countries":{
        "USA":{
            "country_name":"USA",
            "total_cases":1735029,
            "total_recovered":481988,
            "total_deaths":101285},
        "Brazil":{
            "country_name":"Brazil",
            "total_cases":394507,
            "total_recovered":158593,
            "total_deaths":24600},
        "Russia":{
            "country_name":"Russia",
            "total_cases":370680,
            "total_recovered":142208,
            "total_deaths":3968},
        "Spain":{
            "country_name":"Spain",
            "total_cases":283339,
            "total_recovered":196958,
            "total_deaths":27117},
        "UK":{
            "country_name":"UK",
            "total_cases":267240,
            "total_recovered":0,
            "total_deaths":37460},
        "China":{
            "country_name":"China",
            "total_cases":82993,
            "total_recovered":78280,
            "total_deaths":4634}
    }}
    return render_template('semiStaticTable.html', data=covid)


if __name__ == "__main__":
    app.run(debug=True)