if exist env (
  echo Virtual environment already exists 
) else (
  py -3 -m venv env
  pip install -r requirements.txt
)