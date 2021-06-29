<br/>
<p align="center"> 
  <img src="images/header.png">
</p>

# Power Analytics

Toolkit for power consumption analysis for the manufacturer of woodworking tools

## Table of Contents

- [Introduction](#introduction)
  - [What is Power Analytics?](#what-is-power-analytics)
  - [What can Power Analytics do?](#what-can-power-analytics-do)
- [Installation](#installation)
- [Getting started](#getting-started)
- [Overview](#overview)
  - [Main view](#main-view)
  - [Import view](#import-view)
  - [Parameters view](#parameters-view)
- [Troubleshooting](#troubleshooting)
- [Acknowledgements](#acknowledgements)

## Introduction

### What is Power Analytics?

The application was developed to enable knowledge extraction from data produced during wood and wood-based material cutting experiments. The application is connected to a local database in which all the performed measurements are stored. Each record stores the parameters and the dependent variable, which is the power consumption of the woodworking machine. The parameters can be divided into three subgroups:

- parameters related to the material being cut itself,
- parameters related to the cutting process,
- parameters related to the cutting tool.

Due to the multitude of parameters, multivariate analysis and - in the long term - tool optimization are possible.

### What can Power Analytics do?

Some of the features of the software are as follows:

- modern and user-friendly graphic interface
- storage of all measurements in a database allowing for gradual increase of knowledge
- storing tools in the database and tracking and saving the changes made, which prevents the loss of data when updating the database with new data from the main enterprise system
- database records can be customized
- available data can be exported in CSV format for further analysis (both data from the database and data from the charts)
- available graphs can be saved in a variety of formats, including vector graphics formats; the range of graphs can be manually adjusted, saving only the interesting parts
- after each measurement a report is generated in PDF format, containing used parameters, graphs and basic statistics
- it is possible to view historical reports - the reports are saved by default, so that access to them is guaranteed at any time
- intuitive graphical interface for multi-parameter data visualization enables easy browsing of available measurements and searching for potential correlations

## Installation

### Tested on 64-bit version of Windows 10

To install the software, follow the bulleted steps:

- download the installer [here](https://github.com/daniellechowicz/power-analytics/raw/main/Power%20Analytics.exe)
- run the installer and follow the instructions displayed in the installer window
- if the Python interpreter (version 3.9.0) is not installed on your computer, make sure that the installation of this program is checked
- after the installation is complete, go to the _bin_ folder and launch the application by double clicking on the icon

<p align="center"> 
  <img src="images/path/python.png">
  <p align="center">
    Fig. 1. Make sure that Python 3.9.0 will be added to system's <i>PATH</i> variable; if admin rights are unavailable, then <i>Install launcher for all users (recommended)</i> must be unchecked
  </p>
</p>

## Getting started

This chapter describes an example use of the software and the procedure to analyze the data. A detailed description of the various functionalities is described in the next section.

### Main window

After launching the application, you will see the main window from which you can navigate to the various functionalities of the software. The tabs shown on the left are:

- data import and parameter entry,
- cutting and idle range selection and signal analysis including spectrum visualization,
- database and multi-parameter data visualization,
- reporting,
- settings.

<p align="center"> 
  <img src="images/main.png">
  <p align="center">
    Fig. 2. Main window of Power Analytics
  </p>
</p>

### Importing data and entering parameters

Head to the first tab and then enter the path to the measurement file. If you do not have any measurement files in TDMS format, go to the _samples_ folder, which contains sample files. Confirm your selection. The next step is to enter the measurement parameters, including:

- author,
- material,
- material moisture content,
- rotational speed,
- feed speed,
- cutting width,
- cutting depth,
- tool ID,
- comment.

Mandatory fields are marked with an asterisk. Once the parameters have been entered, it is necessary to confirm them and then move on to the next tab by clicking the confirm button located on the right side of the window.

<p align="center"> 
  <img src="images/import.png">
  <p align="center">
    Fig. 3. Import page of Power Analytics
  </p>
</p>

<p align="center"> 
  <img src="images/parameters.png">
  <p align="center">
    Fig. 4. Parameters widget of Power Analytics
  </p>
</p>

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

1. group name - the name that is given to the measurement file group name when it is saved (avoid special characters)
2. channel name - the name that is given to the measurement file channel name when it is saved (avoid special characters)
3. sampling frequency - the sampling frequency used during the measurement specified in Hz
4. resampling factor - the factor by which the number of samples will be reduced (e.g. for a resampling factor of 10, the original number of samples of 1 MS will be 1 kS)
5. window size - the number of samples from which the moving average is calculated (the larger the window size, the less sensitive to noise and the more generalized the result)
6. idle start index - the default setting for the first measured value of the idle
7. idle stop index - the default setting for the last measured value of the idle
8. cutting start index - the default setting for the first measured value of the cutting
9. cutting stop index - the default setting for the last measured value of the cutting
10. CSV tools filename - the name of the CSV file that will contain the description of the tool parameters

### Troubleshooting

Error logs are saved in the _logs_ folder with the appropriate date. In case of any errors, please send the file to _d.lechowicz@wood-kplus.at_.

### Acknowledgements

The icons used in the software are property of _www.flaticon.com_.
