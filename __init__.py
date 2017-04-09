#!/usr/bin/env python

from flask import Flask, render_template

import logging

app = Flask(__name__)

'''
log_dir = '/tmp'
logging.basicConfig(filename='{0}/log_ilmnuri'.format(log_dir),
                    format='%(asctime)s  %(funcName)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
'''

log = logging.getLogger(__name__)


@app.route('/')
def index():
    # log.debug('index page rendered.')
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
