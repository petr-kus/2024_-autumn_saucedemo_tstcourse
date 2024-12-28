python3 -m pip install --upgrade pip
python3 -m venv venv
#TODO Lektor - tady je dle me chyba. me funguje... 
#python -m pip install --upgrade pip
#python -m venv venv
# ./venv/Scripts/activate.ps1
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
