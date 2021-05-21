<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/logo.png">
</p>

# Power Analytics
Toolkit for power consumption analysis for the manufacturer of woodworking tools

## Installation
1) navigate to the folder
2) run the installer _Power Analytics.exe_ and follow the instructions
3) allow the interpreter _Python 3.9.0_ to be installed
4) allow the external module _wkhtmltopdf_ for HTML to PDF conversion to be installed
5) allow the application _Power Analytics 1.0_ to be installed 
3) go to the _bin_ folder and double-click the _Power Analytics.exe_ to start the application

## Software functionalities
Accordingly to the customer's requirements, the software has the following features:
1) working with National Instruments TDMS format
2) integration of applied parameters with existing database by tool ID number
3) manual selection of idle mode and cutting regions
4) noise compensation with moving average
5) spectral representation of analysed signal
6) integration of SQLite database
7) visualization of data available in the database
8) possibility to the database
9) possibility to export the database in CSV format
10) generation of measurement reports in PDF format
11) possitibility to change default settings
12) possibility to edit parameters of available tools
13) possibility to add new tools
14) possibility to replace CSV file containing tools' parameters without losing the information collected over time

## Overview

### Main view
After launching the application, you will see the main view of the application from where you can navigate to the various functionalities of the application. On the left you can see tabs leading to data import, analysis, database, reporting and settings, respectively.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/main.png">
</p>

### Import view
After pressing the first button, the data import view is visible. Select the measurement file in TDMS format and then specify the parameters that were used during the measurement by clicking the second icon. After indicating the path to the measurement file and filling in the used parameters, confirm your choices by pressing the third icon.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/import.png">
</p>

### Parameters view
Moving to the parameters view, complete all fields as instructed. The parameter view is shown in the following image.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/parameters.png">
</p>

### Analysis view
Once you confirm your selections, you are automatically taken to the data analysis tab. You will see three graphs - the first corresponds to the entire file, the second to the range corresponding to idling, and the third to the cutting process. Select the appropriate ranges by manually moving the green and red rectangles, and adjust their borders. Before validating your selections, indicate whether you want the data to be added to the database. If ready, press the blue button below the charts.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/range_selection.png">
</p>

### Filters view
Digital signal processing functionality has also been made available to the user. A moving average filter can be used, as well as a frequency spectrum. The cards are visible at the top of the window. The visible ranges are automatically truncated for the cutting process only (green rectangle).
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/moving_average.png">
  <p align="center">
    Filters view | Moving average
  </p>
</p>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/psd.png">
  <p align="center">
    Filters view | Power Spectral Density (PSD)
  </p>
</p>

### Database view
Moving to the third tab, database-related functionalities will appear. The functionalities are as follows: viewing the database and the measurements taken, multi-parameter data visualization using a graphical interface, and exporting the database in CSV format.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/main_database.png">
</p>

<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/database.png">
  <p align="center">
    Database view | Visualization of measurements taken with corresponding metadata and statistics
  </p>
</p>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/visualization.png">
  <p align="center">
    Database view | Multiparameter data visualization using a graphical interface
  </p>
</p>

### Settings view
When you navigate to the last tab, you can change the software settings and add or edit tools and their parameters. It is also possible to replace a file in CSV format without losing the changes made. The individual functionalities are self-explanatory - follow the instructions. The following are the default software settings window, the edit window, and the add new tool window, respectively.
<p align="center">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/settings.png" width="30%">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/edit.png" width="30%">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/add.png" width="30%">
</p>

### Report
The software has the functionality of generating reports. To generate a report with a summary of the parameters used in the measurement, as well as basic statistics, press the fourth button from the main menu. The report can only be generated if measurement data has been imported, parameters entered, and idle and cutting process ranges defined. A sample auto-generated report is shown below.
<p align="center">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/report_1.png">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/report_2.png">
</p>

### Settings
The user has access to some software settings. The settings can be accessed from the _Settings_ tab. The settings that can be changed are as follows:
1) group name - the name that is given to the measurement file group name when it is saved (avoid special characters)
2) channel name - the name that is given to the measurement file channel name when it is saved (avoid special characters)
3) sampling frequency - the sampling frequency used during the measurement specified in Hz
4) resampling factor - the factor by which the number of samples will be reduced (e.g. for a resampling factor of 10, the original number of samples of 1 MS will be 1 kS)
5) window size - the number of samples from which the moving average is calculated (the larger the window size, the less sensitive to noise and the more generalized the result)
6) idle start index - the default setting for the first measured value of the idle
7) idle stop index - the default setting for the last measured value of the idle
8) cutting start index - the default setting for the first measured value of the cutting
9) cutting stop index - the default setting for the last measured value of the cutting
10) CSV tools filename - the name of the CSV file that will contain the description of the tool parameters
