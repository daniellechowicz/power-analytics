@echo off
if exist env (
  echo Virtual environment already exists 
) else (
  @echo on
  echo [INSTALL] Setting up...
  echo [INSTALL] Please be patient, it might take a while...
  echo [INSTALL] Creating virtual environment...
  py -3 -m venv env
  CALL env\Scripts\activate.bat
  echo [INSTALL] Installing required modules...
  pip install -r requirements.txt
)