#!/bin/bash
python3 -m pip install --upgrade pip

# Lektor: zde chybi vytvoreni virtualniho enviromentu 
#(nezminil jsem na lekci priomo kod - ale pozornemu pozorovateli to mohlo i dojit)
# doplnuji... probereme na lekci
python3 -m venv .venv

source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt