CALL env\Scripts\activate.bat
cd src
python -m unittest tests.tests_helpers.test_calculate_parameters.Testing
python -m unittest tests.tests_helpers.test_helpers.Testing
python -m unittest tests.tests_windows.test_settings_window.SettingsWindowTest
pause