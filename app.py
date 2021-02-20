from script import get_allotted_stock_from_boid
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('template.html')


@app.route('/allotment-check')
def allotment_check():
    boid_list = request.args.get('boid').split(",")
    print(boid_list)
    return jsonify(get_allotted_stock_from_boid(boid_list))
