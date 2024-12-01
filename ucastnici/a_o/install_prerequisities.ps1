python.exe -m pip install --upgrade pip
python -m venv venv

# Aktivace prostøedí
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# Instalace balíèkù
pip install -r requirements.txt
pip freeze > requirements.txt
