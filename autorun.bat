@echo off

cd ..

if not exist logs (
  mkdir logs 
)

CALL env\Scripts\activate.bat
cd src
python main.py 2>> ..\logs\LOGS_%date:~-4,4%_%date:~-7,2%_%date:~-10,2%.log