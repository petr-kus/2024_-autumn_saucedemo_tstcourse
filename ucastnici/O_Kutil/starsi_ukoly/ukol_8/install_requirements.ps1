#Lektor: prihazuji si svuj skript :-) na windows... at muzu kontrolovat ulohu :-)
python.exe -m pip install --upgrade pip
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt