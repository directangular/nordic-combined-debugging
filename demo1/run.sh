#!/bin/bash

[[ -x env/bin/flask ]] || {
    echo "Please init a virtualenv first"
    exit 1
}

FLASK_APP=app.py env/bin/flask run
