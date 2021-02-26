from script import get_allotted_stock_from_boid
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/allotment-check')
def allotment_check():
    boid_list = request.args.get('boid').split(",")
    print(boid_list)
    return render_template('result.html', data=get_allotted_stock_from_boid(boid_list))
    # return jsonify(get_allotted_stock_from_boid(boid_list))


if __name__ == '__main__':
    app.run()
