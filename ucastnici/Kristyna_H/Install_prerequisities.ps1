python.exe -m pip install --upgrade pip
#Lektor - zde je chybejejici vytvoreni virtualniho prostredi... .
python -m venv venv
./venv/Scripts/Activate.ps1
#Lektor - na rakdu vyse jsem ti opravil activaci virtualniho prostredi... .
# Student - jen pro info - ve windows opravena aktivace nefunguje. Funguje toto .\/.venv/Scripts/Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt
rfbrowser init
playwright install
#Lektor - super je ze jsi to sama rozsirila o ten playwright. Uz zacinas chapat vyznam tohto skriptu :-)
