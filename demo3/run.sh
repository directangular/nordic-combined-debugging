#!/bin/bash

[[ -x env/bin/flask ]] || {
    echo "Please init a virtualenv first"
    exit 1
}

env/bin/python app.py
