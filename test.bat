cd src

echo "[INFO] unit test execution started"
timeout 3 >nul

echo "[INFO] currently testing: calculate_parameters.py"
timeout 1 >nul
python -m unittest tests.tests_helpers.test_calculate_parameters.Testing

echo "[INFO] currently testing: helpers.py"
timeout 1 >nul
python -m unittest tests.tests_helpers.test_helpers.Testing

echo "[INFO] unit test execution finished"

cd ..