python.exe -m pip install --upgrade pip
python -m venv venv

# Aktivace prost�ed�
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#chvalim hodne za pridani si tohoto prikazu! - v podtsate to znamena ze jsi pochopila princip a vyplivajici problemy a aspekty!
.\venv\Scripts\Activate.ps1

# Instalace bal��k�
pip install -r requirements.txt
pip freeze > requirements.txt
