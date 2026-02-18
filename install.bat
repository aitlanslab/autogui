@echo off

if not exist venv (
    python -m venv venv
)

call venv\scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
echo .
echo Installation successful.
pause