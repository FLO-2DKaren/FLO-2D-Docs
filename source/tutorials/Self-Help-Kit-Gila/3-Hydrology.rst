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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **QGIS application**.
- You can pin QGIS to your Start Menu for quicker access.

.. tip::
   To avoid searching for QGIS every time, right-click the QGIS icon and select **"Pin to Start."**

Step 2: Open Your Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- If QGIS opens your most recent project, simply click on it in the **Recent Projects** list.
- If the project was moved and no longer loads:
  - Go to **Plugins > FLO-2D > Open FLO-2D Project**.
  - Navigate to your project `.gpkg` file (GeoPackage) and select it.

.. note::
   The GeoPackage contains your entire project, including the `.qgz` file.

Step 3: Remove Data from the GeoPackage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- To remove data:
  - Go to **Plugins > FLO-2D > GeoPackage Management**.
  - Check the layer you want to remove (e.g., `mannings.dat`) and click **Delete**.
  - Click **Cancel** if you don't want to delete anything.

.. warning::
   Do not right-click and remove layers from the Layers panel. That does **not** remove them from the GeoPackage.

Step 4: Browse GeoPackage Contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **Browser** panel in QGIS.
- If it's in an awkward location, drag it beside the Layers panel until the layout is comfortable.

****Need Image Here**** browser_panel_layout.png
   :alt: Example layout of QGIS Layers and Browser panels side by side

- Right-click on **GeoPackage** and select **New Connection**.
- Browse to your project `.gpkg` file and open it.
- You will now see all layers and tables contained within the GeoPackage.

Step 5: Understand the GeoPackage Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- The GeoPackage is a spatial database built on SQLite.
- It contains:
  - Vector data (points, lines, polygons)
  - Raster data (elevation layers)
  - Attribute tables (e.g., `RAINCELL.DAT`, `MANNINGS_N.DAT`)
  - The `.qgz` project file itself

.. note::
   In older versions like 0.10.115, the `.qgz` file was separate. In Build 25, it is embedded inside the GeoPackage for easier file sharing and portability.

Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use the FLO-2D Plugin to open and manage your project.
- GeoPackage management allows data cleanup without risking data loss.
- The embedded `.qgz` file ensures seamless project transfer across devices and folders.




Assign an Inflow Node
--------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/YoYULnJ-0U0?si=OT2AiswXQdgwaTcF"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This tutorial shows how to create an **inflow boundary condition** at a project edge where an upstream channel—**Cave Creek**—enters the basin. This is useful when modeling runoff entering the system from offsite.

Step 1: Navigate the Map
~~~~~~~~~~~~~~~~~~~~~~~~
- Use your **mouse scroll wheel** to zoom in and out.
- Click and drag with the **middle mouse button (wheel)** to pan the map view.

.. note::
   This navigation style is similar to Civil 3D, ArcGIS, and Google Earth.

Step 2: Add an Inflow Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
- In QGIS, go to **Plugins > FLO-2D > Boundary Editor**.
- Click **Collapse All** to clear any open panels.
- Choose the **Inflow Node** option.
- Click **Add Point**, then click on the map at the outlet of the structure (culvert with dissipator and grate).
- Click **OK** to create the inflow point.
- Click the **Save** button (floppy disk icon) to save it.

Step 3: Rename the Inflow Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Rename**, and enter:

  `Grover Basin Inflow`

Step 4: Create a Time Series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to the **Time Series Editor**.
- Click **New**, and name it:

  `GroverIn_100yr_6hr`

- This is a 100-year, 6-hour inflow hydrograph taken from the original larger project.
- Set the **Type** to: `Floodplain`

.. warning::
   Do not select **Channel** unless modeling a direct stream. This is surface runoff entering the basin.

Step 5: Paste Hydrograph Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the provided hydrograph data file from **Lesson 1 Data**.
  - Choose the `100yr_6hr` inflow file.
  - Time should be in hours on the **left** and discharge (cfs) on the **right**.
- Select all data with **Ctrl+A**, then copy with **Ctrl+C**.
- Close the file with **Ctrl+W**.
- In the QGIS Time Series Editor, click the first cell and paste using **Ctrl+V**.

.. note::
   FLO-2D automatically uses **cubic feet per second** for discharge. Use metric units only if your model is in metric.

Step 6: Schematize the Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Schematize** to convert the pasted user input into FLO-2D schema data.

Step 7: Export the Inflow File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Right-click the inflow node and choose **Export > Data**.
- Select only the **Inflow Elements**, not all files.
- Set the export folder and confirm.

You will now have a file called `INFLOW.DAT`.

Understanding the INFLOW.DAT File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Open `INFLOW.DAT` in **Notepad++** or any plain text editor. It will look like this::

   f   [Floodplain flag]
   ####  [Grid element number]
   h   [Time-series line]
   0.0  0.0
   0.1  2.4
   ...

- `f` means **floodplain** (use `c` for channel inflow).
- The number is the grid element where the inflow enters.
- `h` starts a new hydrograph.
- The table represents **time (hr)** and **discharge (cfs)**.
- Always start at time `0` with `0` discharge.
- Ramp up gradually in the first interval.

.. tip::
   For **tailings dams** or Flash like flows, ramp up more quickly (e.g., within 0.5 hour). For regular runoff, 1–2 hours may be appropriate.




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

