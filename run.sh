#!/bin/bash

FLASK_APP=scivi.py PYTHONPATH=$PYTHONPATH:scivi.web python3 -m flask run --host=0.0.0.0 --port=5555
if [ $? -ne 0 ]; then
    echo "Maybe you are out of python virtual environment"
    echo "Try:"
    echo "./setup.sh"
    echo "source .venv/bin/activate"
fi
