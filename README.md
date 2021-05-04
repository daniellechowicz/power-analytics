# Power Analytics
Toolkit for power consumption analysis for the manufacturer of woodworking tools

## Installation
1) navigate to the folder
2) execute the following commands:
```
pip install -m pynsist 
```
```
pynsist install.cfg
```
3) run the installer and follow the instructions
4) double-click the file _Power_Analytics.launch.pyw_

## Software functionalities
Accordingly to the customer's requirements, the software has the following features:
1) working with National Instruments TDMS format
2) integration of applied parameters with existing database by tool ID number
3) manual selection of idle mode and cutting regions
4) noise compensation with moving average
5) spectral representation of analysed signal
6) integration of SQLite database
7) visualization of data available in the database
8) possibility to export the database in CSV format
9) generation of measurement reports in PDF format
10) possitibility to change default settings
11) possibility to edit parameters of available tools
12) possibility to add new tools
13) possibility to replace CSV file containing tools' parameters without losing the information collected over time

## Manual

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
When you get to the last tab, you can change the software settings and add or edit tools and their parameters. It is also possible to replace a file in CSV format without losing the changes made.
<p align="center">
  <figure>
    <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/settings.png" width="30%">
    <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
  </figure>
  <figure>
    <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/edit.png" width="30%">
    <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
  </figure> 
  <figure>
    <img src="https://github.com/daniellechowicz/Power-Analytics/blob/main/img/add.png" width="30%">
    <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
  </figure> 
</p>
