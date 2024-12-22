python.exe -m pip install --upgrade pip
#Lektor - zde je chybejejici vytvoreni virtualniho prostredi... .
python -m venv venv
./venv/Scripts/Activate.ps1
#Lektor - na rakdu vyse jsem ti opravil activaci virtualniho prostredi... .
pip install -r requirements.txt
pip freeze > requirements.txt
rfbrowser init
playwright install
