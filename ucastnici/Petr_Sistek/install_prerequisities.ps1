python.exe -m pip install --upgrade pip
#TODO Lektor - zde jsem ti pridal vytvoreni virtualniho enviromentu. Je to potreba bez toho neni s cim pracovat.
#u tebe uz existuje ale jinde ne neexistuje...
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt
