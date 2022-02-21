# encoding: utf-8

from flask import jsonify, request
from flask_script import Manager
from flask_cors import CORS, cross_origin

from project.app import create_app
from project.services import calc

app = create_app()
myCalc = calc.CalcVBT();
CORS(app, resources={r'*': {'origins': '*'}})


manager = Manager(app)

@app.route("/get_vbt_value")
def get_ohlcv():    
    print ('#################################')
    print  (request.args.get('k'))
    print ('#################################')
    
    return jsonify({'k':myCalc.get_vbt_value(request.args.get('ticker'), 2, float(request.args.get('k')))})
    


if __name__ == '__main__':
    manager.run()
