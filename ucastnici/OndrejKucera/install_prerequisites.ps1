python.exe -m pip install --upgrade pip
python.exe -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt