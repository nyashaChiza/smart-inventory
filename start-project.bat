@echo off
rem Change the path to your virtual environment's activate script
set VENV_PATH=C:\Users\usr\Documents\projects\smart-inventory\inv-env\Scripts\activate

rem Activate the virtual environment
call "%VENV_PATH%"

rem Change the directory to your Django project directory
cd /d "C:\Users\usr\Documents\projects\smart-inventory\"

rem Run the Django development server
python manage.py runserver
