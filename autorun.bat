::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCuDJGuB5E0jFCtbWwGQcUq0B7kF/OH4/NaXrVoYRq8+do7Xw6CHI/Mv/0zYfJUi2GlmlMILBA9RcBXlZww7yQ==
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSTk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCuDJGuB5E0jFCtbWwGQcUq0B7kF/OH4/NaFq0MhZO0ofZ2b+7qPLPkH40b3O5M10xo=
::YB416Ek+Zm8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off

cd ..

if not exist logs (
  mkdir logs 
)

CALL env\Scripts\activate.bat
cd power-analytics
python main.py 2>> ..\logs\LOGS_%date:~-4,4%_%date:~-7,2%_%date:~-10,2%.log