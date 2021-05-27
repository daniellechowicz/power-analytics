<br/>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/header.png">
</p>

# Power Analytics
Toolkit for power consumption analysis for the manufacturer of woodworking tools

## Installation (tested on 64-bit version of Windows 10)
1) download the _Power Analytics.exe_ installer (_https://github.com/daniellechowicz/power-analytics/raw/main/Power%20Analytics.exe_)
2) run the _Power Analytics.exe_ installer and follow the instructions
3) allow the interpreter _Python 3.9.0_ to be installed (see the figure below)
4) allow the external module _wkhtmltopdf_ for HTML to PDF conversion to be installed (see the figure below)
5) allow the application _Power Analytics 1.0_ to be installed
6) add _wkhtmltopdf_'s path to the environment variables (see _Adding wkhtmltopdf's path to PATH_)
7) go to the _bin_ folder and double-click the _Power Analytics.exe_ to start the application

<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/python.png">
  <p align="center">
    Ad 4) | Make sure Python 3.9 will be added to system's _PATH_ variable
  </p>
</p>

<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/wkhtmltopdf.png">
  <p align="center">
    Ad 5) | Do not change the default path of the _wkhtmltopdf_ module
  </p>
</p>

## Adding wkhtmltopdf's path to PATH
Type _System_ in the taskbar search engine. When the window opens, go to _Advanced system settings_.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/path_1.png">
</p>

When the next window appears, press the _Environment variables_ button.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/path_2.png">
</p>

In the next window you will see two groups: user variables and system variables. In the system variables, find the _Path_ variable and then select it by double-clicking.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/path_3.png">
</p>

When the window opens, select the _New_ button and then add the following path: _C:\Program Files\wkhtmltopdf\bin\\_. 
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/path/path_4.png">
</p>

Confirm the changes. To be sure, it is advisable to restart the computer.

## Software functionalities
Accordingly to the customer's requirements, the software has the following features:
1) working with the National Instruments TDMS format
2) integration with the database that stores all measurements taken
3) integration of applied parameters into the database via tool ID number
4) manual selection of idle and cutting regions
5) noise compensation with moving average filter
6) spectral representation of analysed signal
7) interactive visualization of data available in the database
8) possibility of editing the data present in the database, as well as deleting individual records
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
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/main.png">
</p>

### Import view
After pressing the _Data import_ button, the import view is visible. Select the measurement file in the TDMS format and then specify the parameters that were used during the measurement by clicking the _Parameters_ icon. After indicating the path to the measurement file and filling in the parameters, confirm your choices by pressing the _Confirm_ icon.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/import.png">
</p>

### Parameters view
Moving to the parameters view, complete all fields as instructed. User has the possibility to clean the fields at once by pressing the _Remove_ button. The process will only complete successfully if all fields are completed. If the tool ID number provided does not match any of the ID numbers present in the CSV file containing all tools, the user will be asked to enter the tool into the database. Once the tool has been entered into the database, fill in the parameters' fields again. <b>NOTE: There are only two choices in the correlating field to the cutting direction: GGL (ggl) or GLL (ggl).</b>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/parameters.png">
</p>

### Analysis view
Once data import carried out properly, you are automatically taken to the data analysis tab. You will see three graphs - the first corresponds to the entire file, the second to the range corresponding to idling, and the third to the cutting process. Select the appropriate ranges by manually moving the green (cutting) and red (idle) rectangles, and adjust their borders. Before validating your selections, indicate whether you want the data to be added to the database. If ready, press the blue button below the charts.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/range_selection.png">
</p>

### Filters view
Digital signal processing functionality has also been made available to the user. A moving average filter can be used, as well as a frequency spectrum. The cards are visible at the top of the window. The visible ranges are automatically truncated for the cutting process only (green rectangle).
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/moving_average.png">
  <p align="center">
    Filters view | Moving average
  </p>
</p>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/psd.png">
  <p align="center">
    Filters view | Power Spectral Density (PSD)
  </p>
</p>

### Database view
Moving to the third tab, database-related functionalities will appear. The functionalities are as follows: viewing the database and the measurements taken, multi-parameter data visualization using a graphical interface (relative comparison to the last measurement), and exporting the database in CSV format. You can edit the data in the database. Two options are available: editing individual values or completely deleting a record from the database.
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/main_database.png">
</p>

<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/database.png">
  <p align="center">
    Database view | Visualization of measurements taken with corresponding metadata and statistics
  </p>
</p>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/database_edit.png">
  <p align="center">
    Database view | Edition of values present in the database
  </p>
</p>
<p align="center"> 
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/visualization.png">
  <p align="center">
    Database view | Multiparameter data visualization using a graphical interface
  </p>
</p>

### Settings view
When you navigate to the last tab, you can change the software settings and add or edit tools and their parameters. It is also possible to replace a file in CSV format without losing the changes made. The individual functionalities are self-explanatory - follow the instructions. The following are the default software settings window, the edit window, and the add new tool window, respectively.
<p align="center">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/settings.png" width="30%">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/edit.png" width="30%">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/add.png" width="30%">
</p>

### Report
The software has the functionality of generating reports. To generate a report with a summary of the parameters used in the measurement, as well as basic statistics, press the fourth button from the main menu. The report can only be generated if measurement data has been imported, parameters entered, and idle and cutting process ranges defined. A sample auto-generated report is shown below.
<p align="center">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/report_1.png">
  <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/images/report_2.png">
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

### Troubleshooting
Error logs are saved in the _logs_ folder with the appropriate date. In case of any errors, please send the file to _d.lechowicz@wood-kplus.at_.

### Acknowledgements
The icons used in the software are property of _www.flaticon.com_.