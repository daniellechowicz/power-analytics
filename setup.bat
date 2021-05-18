if exist env (
  echo Virtual environment already exists 
) else (
  py -3 -m venv env
  CALL env\Scripts\activate.bat
  pip install -r requirements.txt
)