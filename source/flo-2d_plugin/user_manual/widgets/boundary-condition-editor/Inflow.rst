.. _inflow_editor:

Inflow Editor
==================

Any number of inflow hydrographs can be assigned to the channel, floodplain, or 1D street components 
in the FLO-2D model. These hydrographs represent off-site flood inflows entering the simulation domain.

.. image:: ../../img/Boundary-Condition-Editor/newbc002.png

.. |bctraining| raw:: html

    <a href="https://flo-2d.com/product/boundary-conditions/" target="_blank" rel="noopener">BC Training Package</a>

.. note:: Get a |bctraining| to learn how to correctly define boundaries for FLO-2D projects.

.. contents:: Contents
   :local: 
   :depth: 2
   :backlinks: entry


Create Inflow Point
-----------------------------

1. To create a point of inflow, click the Add Point BC button on the Boundary Condition
   Editor widget.

.. image:: ../../img/Boundary-Condition-Editor/newbc004.png

2. Digitize the inflow node by left clicking the location of the inflow node on the map.
   In this example, the inflow node is a channel inflow node.
   It is not necessary to enter the fid.
   Click OK to create the feature.

.. image:: ../../img/Boundary-Condition-Editor/newbc005.png

3. Click the Add Point button again to save the feature and load the data.

.. image:: ../../img/Boundary-Condition-Editor/newbc006.png

4. The data is now updated in the editor.

.. image:: ../../img/Boundary-Condition-Editor/newbc008.png

Create Inflow Line
-----------------------------

.. warning:: The Inflow Boundary Condition Line has been modified.  The hydrograph is now distributed
   to the cells that are intersected by the line.  Previously, the hydrograph was assigned to each cell
   intersected by the line.  The hydrograph will be distributed by dividing the discharge cells by the 
   number of cells intersected by the line.

1. To create a line of inflow, click the Add Line BC button on the Boundary Condition
   Editor widget.

.. image:: ../../img/Boundary-Condition-Editor/newbc004a.png

2. Digitize the line by left clicking the start of the line on the map. Continue to left click 
   the line to finish it.  Right click to close the line.

.. image:: ../../img/Boundary-Condition-Editor/newbc005a.png

3. Click the Add **Line** button again to save the feature and load the data.

.. image:: ../../img/Boundary-Condition-Editor/newbc006a.png

4. Click the Schematize button to create the schematized data.

.. image:: ../../img/Boundary-Condition-Editor/newbc007a.png

Import an Inflow Data File
-----------------------------

This button allows the user to load an INFLOW.DAT file into the Boundary Condition layers and add it to a project.

.. warning:: Importing the INFLOW.DAT file may take longer than expected if schematized inflow boundary data already exists. 
   To speed up the process, click the Delete Schematized Inflow Boundary Condition button before loading the file.

1. Start by clicking the Delete Schematized Inflow Boundary Condition button to delete the schematized data.

.. image:: ../../img/Boundary-Condition-Editor/newbc007b.png

2. Click on the Open INFLOW.DAT button.

.. image:: ../../img/Boundary-Condition-Editor/newbc014.png

2. Navigate to the folder containing the INFLOW.DAT file and select it.

.. image:: ../../img/Boundary-Condition-Editor/newbc015.png

3. A message on the QGIS toolbar will appear, indicating that the importing was successful.

.. image:: ../../img/Boundary-Condition-Editor/newbc016.png

4. Finish the process by clicking the Schematize button to create the schematized data.

.. note:: When you load the INFLOW.DAT file, the data is appended to the Boundary Condition layers and tables. If any cells already have boundary conditions assigned, they will be updated.

   All imported data is also added to the Boundary Condition Points User Layer.

   To speed up the import and schematization process, delete any existing schematized data before loading the INFLOW.DAT file.

Assign Inflow Attributes Hydrographs
----------------------------------------

1. Assign the conditions to the inflow node as seen in the following image. 

.. image:: ../../img/Boundary-Condition-Editor/newbc009.png

2. The time series inflow hydrograph is assigned in the table editor where time is in hours and discharge is cfs or cms.
   This is a clear water inflow hydrograph and no sediment concentration is assigned.

.. image:: ../../img/Boundary-Condition-Editor/newbc010.png

3. Repeat the process to add additional inflow hydrographs.
   Use the Add data series/table for current BC button to create a new hydrograph.

.. image:: ../../img/Boundary-Condition-Editor/newbc011.png

Zoom and Pan to Inflow Boundary Condition
-----------------------------------------

1. Use they eye button to pan and zoom to the selected Inflow Boundary Condition.

.. image:: ../../img/Boundary-Condition-Editor/newbc017.png


Delete Selected Inflow Boundary Condition
--------------------------------------------

1. To delete an Inflow Boundary Condition, click on the Delete Inflow Boundary Condition button.

.. image:: ../../img/Boundary-Condition-Editor/newbc018.png

2. Click the Schematize button to update the schematized data.


Schematize the Data
---------------------

1. Use the Schematize button to save the data to the Schematic Layers and click Yes to overwrite the layers.

.. image:: ../../img/Boundary-Condition-Editor/newbc012.png


.. image:: ../../img/Boundary-Condition-Editor/newbc013.png

Delete Schematized Data
------------------------

1. To delete all schematized Inflow Boundary Conditions, click on the Delete Schematized Inflow Boundary Condition button
   and click Yes to delete all schematized Inflow Boundary Conditions.

.. important:: This button removes all schematized Inflow Boundary Conditions data. It will not delete the time series data.
   Use this button if before importing the INFLOW.DAT file.  It will speed up the import and schematization process.

.. image:: ../../img/Boundary-Condition-Editor/newbc019.png

.. image:: ../../img/Boundary-Condition-Editor/newbc020.png
