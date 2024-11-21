python.exe -m pip install --upgrade pip

# Lektor: zde chybi vytvoreni virtualniho enviromentu 
#(nezminil jsem na lekci priomo kod - ale pozornemu pozorovateli to mohlo i dojit)
# doplnuji... probereme na lekci
python -m venv venv

.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt  