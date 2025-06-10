.. _pre_processing_tools:

Pre-Processing Tools
========================

The Pre-Processing Tools are tools designed to modify Digital Elevation Models (DEMs) for various applications.
These tools provide efficient pre-processing solutions for removing artificial barriers such as dams, bridges, and
levees, allowing users to create more realistic and valuable terrain representations.

.. image:: ../../img/Widgets/preprocessing.png

.. note:: To date, the only available tool is the Dam Removal.
          Bridge & Levee removal tools are expected in future updates.


Dam and Reservoir Removal
--------------------------

The Dam Removal Tool is a specialized utility designed to process Digital Elevation Models (DEMs) and remove the
representation of dams or artificial barriers within the elevation data.

1.  Click on Dam area.

.. image:: ../../img/Pre-Processing-Tools/Prepro001.png

2.  Draw the dam area

.. image:: ../../img/Pre-Processing-Tools/Prepro002.png

3.  Click on Save dam area to save the shapefile.

.. image:: ../../img/Pre-Processing-Tools/Prepro003.png

4.  Fill the Side slope, Dam elevation, Dam invert elevation, and Intervals.

.. image:: ../../img/Pre-Processing-Tools/Prepro004.png

5.  Click on Estimate Reservoir.

.. image:: ../../img/Pre-Processing-Tools/Prepro005.png

Downstream of Dam
___________________

Open a path for the water to leave the dam on the downstream edge of the dam.  Lower the elevation using the channel
polygon.

6.  Click on Add Channel.

.. image:: ../../img/Pre-Processing-Tools/Prepro006.png

7.  Draw the channel.

.. image:: ../../img/Pre-Processing-Tools/Prepro007.png

8.  Click on Save channel.

.. image:: ../../img/Pre-Processing-Tools/Prepro008.png

9. Select the Input Raster.

.. image:: ../../img/Pre-Processing-Tools/Prepro009.png

10.  Click on Remove Dam and save or not the intermediate calculation shapefiles (Dam Area & Channel).

.. image:: ../../img/Pre-Processing-Tools/Prepro010.png

11. Check the modified DEM for any bad data and redo the process until the DEM is satisfactory.

.. image:: ../../img/Pre-Processing-Tools/Prepro011.png


Dam Removal Troubleshooting
_______________________________

Estimate the side slopes based on the dam banks or design data.
The connection between the channel and the reservoir is usually steep, check for potential bad data there.
Check the area and the volume removed from the DEM to match the design volume.
The number of intervals equal 10 is a good estimation, but it can be modified.

Raster Unit Converter
--------------------------

The unit converter was developed to convert the USGS elevation data from meters to ft. Download the USGS DEM data
from a 3DEP layer and convert it to feet using the unit converter.

1.  Click on the Raster Converter editor.
2.  Load the raster file. 
3.  Define the file name and path to save the converted file.
4.  Click the convert button.

.. image:: ../../img/Pre-Processing-Tools/prepro030.png

5. The new layer will be added to the map with the converted data.

.. image:: ../../img/Pre-Processing-Tools/prepro031.png

Download 3DEP DEM Data
--------------------------

The 3DEP (3D Elevation Program) provides high-resolution elevation data for the United States.
To download 3DEP DEM data, follow these steps:

1. Open the Data Source Manager.
2. Load the WCS tab.
   
.. image:: ../../img/Pre-Processing-Tools/prepro031.png

3. Create a new connection to the 3DEP WCS server.
4. Name the Connection.  In this case the name 3DEP is used.
5. Add the URL to the dataset: 
   
`https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WCSServer`

.. image:: ../../img/Pre-Processing-Tools/prepro031.png

6. Click connect to connect to the server.
7. Select the first layer in the list.
8. Click the Add button to add the layer to the map.

.. image:: ../../img/Pre-Processing-Tools/prepro031.png

9.  The downloaded layer may have a broken link.
10.  Right click the layer and click Repair Data Source.

.. image:: ../../img/Pre-Processing-Tools/prepro034.png

11. Use the dialog to fix the data source as shown below.

.. image:: ../../img/Pre-Processing-Tools/prepro034.png

12.  Once the layer loads, uncheck it so the data won't load every time the map is refreshed.

.. image:: ../../img/Pre-Processing-Tools/prepro036.png

13.  To use the data, download a raster file by Exporting the layer. 

.. image:: ../../img/Pre-Processing-Tools/prepro037.png

14.  Don't forget to set the layer extent to the area of interest.

.. image:: ../../img/Pre-Processing-Tools/prepro038.png

