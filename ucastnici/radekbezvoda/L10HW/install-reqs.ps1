python -m venv venv
python.exe -m pip install --upgrade pip
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt