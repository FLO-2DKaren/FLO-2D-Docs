Hydrology
========================

Learn how to set up rainfall and infiltration using QGIS and the FLO-2D Gila Plugin.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

Load the Project
-------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/w7iFEWItUyA?si=Fyuii5QSBomqkTWH"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



This lesson shows how to load a FLO-2D project in QGIS, manage paths, and handle GeoPackage data. It also highlights improvements from version 0.10.115 to Build 25 regarding project portability.

Step 1: Launch QGIS
-------------------
- Open the **QGIS application**.
- You can pin QGIS to your Start Menu for quicker access.

.. tip::
   To avoid searching for QGIS every time, right-click the QGIS icon and select **"Pin to Start."**

Step 2: Open Your Project
-------------------------
- If QGIS opens your most recent project, simply click on it in the **Recent Projects** list.
- If the project was moved and no longer loads:
  - Go to **Plugins > FLO-2D > Open FLO-2D Project**.
  - Navigate to your project `.gpkg` file (GeoPackage) and select it.

.. note::
   The GeoPackage contains your entire project, including the `.qgz` file.

Step 3: Remove Data from the GeoPackage
---------------------------------------
- To remove data:
  - Go to **Plugins > FLO-2D > GeoPackage Management**.
  - Check the layer you want to remove (e.g., `mannings.dat`) and click **Delete**.
  - Click **Cancel** if you don't want to delete anything.

.. warning::
   Do not right-click and remove layers from the Layers panel. That does **not** remove them from the GeoPackage.

Step 4: Browse GeoPackage Contents
-----------------------------------
- Open the **Browser** panel in QGIS.
- If it's in an awkward location, drag it beside the Layers panel until the layout is comfortable.

****Need Image Here**** browser_panel_layout.png
   :alt: Example layout of QGIS Layers and Browser panels side by side

- Right-click on **GeoPackage** and select **New Connection**.
- Browse to your project `.gpkg` file and open it.
- You will now see all layers and tables contained within the GeoPackage.

Step 5: Understand the GeoPackage Structure
-------------------------------------------
- The GeoPackage is a spatial database built on SQLite.
- It contains:
  - Vector data (points, lines, polygons)
  - Raster data (elevation layers)
  - Attribute tables (e.g., `RAINCELL.DAT`, `MANNINGS_N.DAT`)
  - The `.qgz` project file itself

.. note::
   In older versions like 0.10.115, the `.qgz` file was separate. In Build 25, it is embedded inside the GeoPackage for easier file sharing and portability.

Summary
-------
- Use the FLO-2D Plugin to open and manage your project.
- GeoPackage management allows data cleanup without risking data loss.
- The embedded `.qgz` file ensures seamless project transfer across devices and folders.




Assign an Inflow Node
--------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/YoYULnJ-0U0?si=OT2AiswXQdgwaTcF"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Set a Boundary Condition with an Inflow Node
This lesson covers how to define an upstream inflow boundary condition at the edge of your grid, using Cave Creek as an example. The inflow point corresponds to a culvert outfall structure at the edge of the basin.

Step 1: Navigate to the Boundary Location
Use the mouse scroll wheel to zoom in and out.

Click and hold the scroll wheel to pan across the map.

.. note::
This navigation method is similar to Civil 3D, ArcGIS, and Google Earth.

Step 2: Open the Boundary Editor
Collapse other plugin tools to reduce clutter.

Open the Boundary Editor from the FLO-2D plugin.

Select Inflow Node.

Click Add Point, then click on the map at the outlet location.

.. image:: boundary_add_point.png
:alt: Adding an inflow point to the map

Click OK to place the inflow node.

Click the Save icon.

Step 3: Name the Inflow Point
Click Rename and set the name to:

.. code-block::

Grover Basin Inflow

Step 4: Create Time Series Data
Open the Time Series Editor.

Click New and name the time series:

.. code-block::

GroverIn_100y6h

This is a 100-year, 6-hour inflow hydrograph from a previous project.

Set the inflow type to Floodplain.

.. note::
Use Floodplain for storm drain or basin flows. Use Channel for stream-based inflows.

Step 5: Paste Hydrograph Data
Open the lesson data file for hydrographs.

Choose the 100y_6hr inflow file.

.. tip::
Use Ctrl + A to select all, Ctrl + C to copy, and Ctrl + W to close the file.

In the time series editor:

Click the first cell.

Paste using Ctrl + V.

.. image:: paste_hydrograph_data.png
:alt: Time-discharge data pasted into FLO-2D plugin

Time is in hours, discharge is in cubic feet per second (cfs).

Step 6: Schematize the Inflow
Click Schematize to convert the time series to FLO-2D format.

This creates the necessary internal format for simulation.

Step 7: Export the Inflow Data
Right-click the project folder and select Export Data.

Select only the Inflow Element option.

Choose your Export Folder.

.. image:: export_inflow.png
:alt: Exporting inflow element to .DAT file

Open INFLOW.DAT in Notepad++ to review the structure:

F indicates floodplain inflow.

Grid element ID is listed.

Data is in graphical mode format.

Starts at time 0 with discharge 0.

.. code-block::

F 1562
h 0.00 0.00
h 0.10 4.50
...

.. tip::
Always start hydrographs at zero discharge. Ramp up over 0.1 to 0.5 hours for realistic transition.

Summary
You created an inflow boundary at the project edge.

You imported and schematized a time series hydrograph.

You exported it to the INFLOW.DAT file for FLO-2D simulation.

Assign Rainfall
-----------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/IKeZAli-2yA?si=ACNEjxC64o8Ltyq9"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Infiltration - Assign SCS Curve Number
-------------------------------------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/thLVZaBdGT0?si=xrzdoZUKB4fLUB7m"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Infiltration - Assign Horton
-----------------------------------------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/SgvLq0CCJFc?si=SnC1Au5xSzV6C_QQ"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Infiltration - Assign Green and Ampt
----------------------------------------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/PE9vvuW7p-A?si=O2bP9jhPCbZUWS10"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Save Export and Run
-----------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/nOPr9G2UmQA?si=BhGrr7CuclE_UC4Q"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

