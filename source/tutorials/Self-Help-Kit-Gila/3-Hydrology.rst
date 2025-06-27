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

In this lesson, we assign rainfall to a FLO-2D project. You will learn how to use the **Rain Editor**, apply **uniform rainfall**, and optionally sample **spatially variable rainfall** from NOAA Atlas data.

Step 1: Open the Rain Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Collapse all QGIS dock widgets to reduce clutter.
- Go to **Plugins > FLO-2D > Rain Editor**.
- Check **Simulate Rainfall**.
- Set the **Total Rainfall Depth** to ``2.65 in`` (this example uses a 6-hour, 100-year event).
- Check **Apply Building Rain**.

.. note::
   Leave **Rainfall Abstraction** at ``0.0`` for now. This is set elsewhere.

Step 2: Add a Storm Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Open** next to the storm pattern.
- Navigate to the **FLO-2D documentation folder** and find the **6-hour event distribution**.
- Choose the **first pattern** from the list.
- Confirm the time-percent curve was imported correctly.

.. important::
   The rainfall distribution table has:
   - **Time (hours)** on the left
   - **Cumulative rainfall (0–1)** on the right  
   The percent values must **start at time = 0 and rainfall = 0**.

Step 3: Understanding Rain on Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Rainfall is applied **uniformly** across all grid elements.
- Every element receives **2.65 inches** following the selected pattern.
- This is called **"rain on grid"**, and it is different from assigning rainfall to subcatchments.

.. tip::
   Rain on grid works well for small projects. For large areas, use **spatial variability** (see below).

Step 4: Sample a Rainfall Raster (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use a **NOAA Atlas 14 rainfall raster** to apply **spatially variable rainfall**.

- Drag your **24-hour rainfall raster** into QGIS.
- Right-click the layer > **Zoom to Layer**.
- Check the data: it should be in inches and match your coordinate system.

To apply the raster:
- Go to the **Rain Editor**.
- Check **Sample from Raster**.
- Select your raster file.
- Leave **"Fill NoData"** unchecked if not needed.
- Click **OK** and confirm.
- QGIS will now **sample rainfall values** from the raster to each grid element based on spatial location.

.. note::
   The sampling uses the centroid of each grid element and computes a **point reduction factor** based on the maximum raster value. It is **not** a depth-area reduction, but rather a **point-based** rainfall adjustment.

Step 5: Export Rainfall Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to **Plugins > FLO-2D > Export DAT Files**.
- This will generate a ``RAIN.DAT`` file in your export folder.

Check `Control Parameters`:
- The rainfall switch is turned on automatically when you check **Simulate Rainfall**.

.. tip::
   If ``RAIN.DAT`` is missing an asterisk, your data has been successfully exported.

Inside the ``RAIN.DAT`` file:
- ``0`` = uniform rainfall  
- ``1`` = rain-on-building (not used here)  
- Total rainfall is listed  
- A distribution pattern is defined  
- Each grid element gets a **reduction factor** based on the raster (e.g., ``0.999``)

.. note::
   Raster values are sampled, warped to match the grid, and averaged by pixel intersection. A **ratio** is calculated between each grid cell's rainfall and the maximum value, generating a point reduction factor.

Wrap-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You’ve now assigned both **uniform** and **spatially variable** rainfall to your project. When ready, run your model to simulate rainfall input across the grid.


Infiltration - Assign SCS Curve Number
-------------------------------------------

Curve Number Infiltration Method
=================================

This lesson walks through how to generate and apply Curve Number infiltration data in FLO-2D. You will learn how to pull Curve Number values from land cover and soil data, manipulate those values, and apply them to your grid using either vector or raster formats.

.. note::
   Only complete **one** of the three infiltration methods. This tutorial covers **Curve Number**.

Step 1: Generate Curve Number Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **Curve Number Generator** from the **Toolbox**.
- This downloads and intersects:
  - **NLCD** land cover data
  - **SSURGO** soil data
- Set outputs to **Temporary Layers**, except save the final Curve Number layer.
- Click **Run** to create your composite Curve Number layer.

Step 2: Inspect Generated Layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- You’ll see several layers:
  - **Soils layer** (SSURGO)
  - **Impervious surface raster** from NLCD
  - **Land cover classification**
  - **Final Curve Number layer**

.. tip::
   Use the **Identify Features** tool to inspect pixel values, such as percent impervious or land class (e.g., “Developed, Open Space”).

Step 3: Edit Curve Number Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **Attribute Table** of the Curve Number layer.
- Use **field calculator** or manual selection to edit curve numbers.
- Example: Select polygons with Curve Number < 63 and update to 63.
- Save edits and close the attribute table.

Step 4: Apply Curve Number to Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open **Infiltration Editor** > **Global Infiltration**.
- Choose **Curve Number** as your method.
- Click **OK**.
- Now go to **Calculate Curve Number**:
  - Select the **Curve Number layer**
  - Choose the correct field
  - Apply values to the grid.

Step 5: Export Infiltration Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Enable the **Infiltration Switch** in **Control Parameters**.
- Save your control settings.
- Go to **Export DAT Files**.
- Select only **Infiltration** and export.

.. note::
   ``INFIL.DAT`` will include:
   - Switch = ``2`` for Curve Number method
   - Global values (optional)
   - Local values per grid element

Step 6: Optional - Rasterize Curve Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If your Curve Number polygon layer is too complex or fragmented:

- Open **Rasterize Vector to Raster** from the **Processing Toolbox**.
- Input:
  - Layer: Curve Number shapefile
  - Field: Curve Number
  - Cell size: ``30 x 30``
  - Extent: Match your FLO-2D grid layer
  - No Data value: ``9999``
- Save output raster and click **Run**.

Step 7: Use Raster Calculator (Alternative Method)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open **Infiltration Editor** > **Curve Number from Raster**.
- Select your rasterized Curve Number layer.
- Run the same sampling calculator used for elevation/N values.
- Click **OK** to apply sampled values.

.. note::
   Raster sampling uses the **centroid** of each grid element to pull the value and applies a **point-based reduction**.

Wrap-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You now know two ways to assign Curve Number infiltration data:
1. Using vector polygon data
2. Using rasterized grid sampling

Only one method is needed for your project.


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

