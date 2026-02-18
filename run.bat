@echo off
mode con: cols=20 lines=5
call venv\scripts\activate

python run.py
pause