import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

vacunaspty = [
    {'id':0,
     'year': 1990,
     'cantidad': 73
     },
    {'id':1,
     'year': 2000,
     'cantidad': 97
     },
    {'id':2,
     'year': 2011,
     'cantidad': 97
     },
    {'id':3,
     'year': 2012,
     'cantidad': 98
     },
    {'id':4,
     'year': 2013,
     'cantidad': 92
     },
    {'id':5,
     'year': 2014,
     'cantidad': 90
     },
    {'id':6,
     'year': 2015,
     'cantidad': 93
     },
    {'id':7,
     'year': 2016,
     'cantidad': 95
     },
    {'id':8,
     'year': 2017,
     'cantidad': 98
     },
    {'id':9,
     'year': 2018,
     'cantidad': 98
     },
    {'id':10,
     'year': 2019,
     'cantidad': 98
     },
    {'id':11,
     'year': 2020,
     'cantidad': 97
     }


]


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/api/all', methods=['GET'])
def api_all():
    return jsonify(vacunaspty)

@app.route('/api/', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: id no ingresado. Por favpr, especificar un id."

    results = []

    for vacuna in vacunaspty:
        if vacuna['id'] == id:
            results.append(vacuna)

    return jsonify(results)

app.run()
