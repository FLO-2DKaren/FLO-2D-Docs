Hydrology
==========

Learn how to set up rainfall and infiltration using QGIS and the FLO-2D Gila Plugin.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

   The videos are more detailed whereas the text gives the minimum steps needed
   to complete the project.

Load the Project
-----------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/w7iFEWItUyA?si=Fyuii5QSBomqkTWH"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



This lesson shows how to load a FLO-2D project in QGIS, manage paths, and handle GeoPackage data.

Step 1: Launch QGIS
~~~~~~~~~~~~~~~~~~~~
- Open the **QGIS application**.

.. image:: ../img/shg/3/shg_hydro001.png

- You can pin QGIS to your Start Menu for quicker access.

.. tip::
   To avoid searching for QGIS every time, right-click the QGIS icon and select **"Pin to Start."**

Step 2: Open Your Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- If QGIS opens your most recent project, simply click on it in the **Recent Projects** list.

.. image:: ../img/shg/3/shg_hydro002.png

- If the project was moved and no longer loads:
  - Go to **Plugins > FLO-2D > Open FLO-2D Project**.
  - Navigate to your project `.gpkg` file (GeoPackage) and select it.

.. image:: ../img/shg/3/shg_hydro003.png

.. note::
   The GeoPackage contains your entire project, including the `.qgz` file.

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

Step 2: Add an Inflow Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- In **FLO-2D Panel**, click **Collapse All** to clear any open panels.

.. image:: ../img/shg/3/shg_hydro004.png

- Expand **Boundary Condition Editor**.

.. image:: ../img/shg/3/shg_hydro005.png

- Choose the **Inflow Node** option.

.. image:: ../img/shg/3/shg_hydro006.png

- Click **Add Point**, then click on the map at the outlet of the structure (culvert with dissipator and grate).

.. image:: ../img/shg/3/shg_hydro007.png

- Click **OK** to create the inflow point, and then
  click the **Add Point** button again to save it.

.. image:: ../img/shg/3/shg_hydro008.png

Step 3: Rename the Inflow Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Rename**, and rename to "Grover Basin Inflow"

.. image:: ../img/shg/3/shg_hydro009.png

Step 4: Create a Time Series
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to the **Time Series Editor**.
- Click **Rename**, and rename "Time Series 1" to "GroverIn 100yr 6hr"

.. image:: ../img/shg/3/shg_hydro010.png

- This is a 100-year, 6-hour inflow hydrograph taken from the original larger project.
- Set the **Type** to: `Floodplain`

.. image:: ../img/shg/3/shg_hydro011.png

.. warning::
   Do not select **Channel** unless modeling a direct stream. This is surface runoff entering the basin.

Step 5: Paste Hydrograph Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the provided hydrograph data file from **Lesson 1 Data**.
  - Choose the `100yr 6hr` inflow file.

  .. image:: ../img/shg/3/shg_hydro012.png

  - Time should be in hours on the **left** and discharge (cfs) on the **right**.
- Select all data with **Ctrl+A**, then copy with **Ctrl+C**.
- Close the file with **Ctrl+W**.
- In the QGIS Time Series Editor, click the first cell and paste using **Ctrl+V**.

.. image:: ../img/shg/3/shg_hydro013.png

.. note::
   FLO-2D automatically uses **cubic feet per second** for discharge. Use metric units only if your model is in metric.

Step 6: Schematize the Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Schematize** to convert the pasted user input into FLO-2D schema data.

.. image:: ../img/shg/3/shg_hydro014.png

Step 7: Export the Inflow File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Right-click the inflow node and choose **Export > Data**.
- Set the export folder and confirm.

.. image:: ../img/shg/3/shg_hydro015.png

- Select only the **Inflow Elements**, not all files.

.. image:: ../img/shg/3/shg_hydro016.png

You will now have a file called `INFLOW.DAT`.

.. image:: ../img/shg/3/shg_hydro017.png


Assign Rainfall
-----------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/IKeZAli-2yA?si=ACNEjxC64o8Ltyq9"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In this lesson, we assign rainfall to a FLO-2D project.
You will learn how to use the **Rain Editor**, apply **uniform rainfall**, and optionally sample **spatially
variable rainfall** from NOAA Atlas data.

Step 1: Open the Rain Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- In **FLO-2D Panel**, click **Collapse All** to clear any open panels.
- Expand **Rain Editor**.

.. image:: ../img/shg/3/shg_hydro018.png

- Check **Simulate Rainfall**.
- Set the **Total Rainfall Depth** to ``2.65 in`` (this example uses a 6-hour, 100-year event).
- Leave **Rainfall Abstraction** at ``0.0`` for now. This is set elsewhere.
- Check **Apply Building Rain**.

.. image:: ../img/shg/3/shg_hydro019.png

Step 2: Add a Storm Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Open** next to the storm pattern.

.. image:: ../img/shg/3/shg_hydro020.png

- Navigate to the **FLO-2D documentation folder** and find the **6-hour event distribution**.
  Choose the **first pattern** from the list.

.. image:: ../img/shg/3/shg_hydro021.png

- Confirm the time-percent curve was imported correctly.

.. image:: ../img/shg/3/shg_hydro022.png

.. important::

   The rainfall distribution table has:

   - **Time (hours)** on the left.
   - **Cumulative rainfall (0–1)** on the right.

   The percent values must **start at time = 0 and rainfall = 0**.

Step 3: Understanding Rain on Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Rainfall is applied **uniformly** across all grid elements.
- Every element receives **2.65 inches** following the selected pattern.
- This is called **"rain on grid"**, and it is different from assigning rainfall to subcatchments.

.. tip::
   Rain on grid works well for small projects. For large areas, continue to **Step 4**.

Step 4: Sample a Rainfall Raster (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use a **NOAA Atlas 14 rainfall raster** to apply **spatially variable rainfall**.

- Drag your **24-hour rainfall raster** into QGIS.

- Right-click the layer > **Zoom to Layer**.

- Check the data: it should be in inches and match your coordinate system.

.. image:: ../img/shg/3/shg_hydro023.png

To apply the raster:

- Go to the **Rain Editor**.

- Check **Sample from Raster**.

.. image:: ../img/shg/3/shg_hydro024.png

- Select your raster file.

- Leave **"Fill NoData"** unchecked if not needed.

- Click **OK** and confirm.

.. image:: ../img/shg/3/shg_hydro025.png

- QGIS will now **sample rainfall values** from the raster to each grid element based on spatial location.

.. image:: ../img/shg/3/shg_hydro026.png

.. note::
   The sampling uses the centroid of each grid element and computes a **point reduction factor**
   based on the maximum raster value. It is **not** a depth-area reduction, but rather a **point-based**
   rainfall adjustment.

Step 5: Export Rainfall Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Check `Control Parameters`:

- The rainfall switch is turned on automatically when you check **Simulate Rainfall**. Click **Save**.

.. image:: ../img/shg/3/shg_hydro027.png

- Export **DAT Files**.

.. image:: ../img/shg/3/shg_hydro028.png

- This will generate a ``RAIN.DAT`` file in your export folder.

.. image:: ../img/shg/3/shg_hydro029.png

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















Infiltration
---------------

.. toggle::

   **Infiltration - Assign Horton**

   This lesson walks through the **Horton infiltration method** in FLO-2D.
   You’ll learn how to estimate Horton parameters, join infiltration attributes, and prepare data for export.













Infiltration
---------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

Infiltration - Assign SCS Curve Number
-------------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/thLVZaBdGT0?si=xrzdoZUKB4fLUB7m"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


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


Infiltration - Assign Horton
-----------------------------------------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/SgvLq0CCJFc?si=SnC1Au5xSzV6C_QQ"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson walks through the **Horton infiltration method** in FLO-2D. You’ll learn how to estimate Horton parameters, join infiltration attributes, and prepare data for export.

Step 1: Prepare Horton Shapefile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- If you don't have Horton data, you can estimate it by comparing with SCS Curve Number values.
- Create a shapefile with estimated Horton parameters.
- Add this shapefile to QGIS and place it in the **External Layers** group.

Step 2: Add Unique Name Field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **Attribute Table** and toggle editing.
- Add a new field named ``name`` (type: String).
- Use the **Expression Editor** to generate unique IDs:
  - Use `concat('Horton-', @row_number)` to fill the field.
- Click **Update All**, save edits, and stop editing.

Step 3: Copy Features to GeoPackage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Select all features in the shapefile.
- Press ``Ctrl+C`` to copy.
- Edit the **infiltration areas** layer in your GeoPackage.
- Paste the features and save.

.. note::
   Attributes are not copied. You will perform a **table join** next.

Step 4: Perform Table Join
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Right-click **infiltration areas** > **Properties** > **Joins**.
- Add a join to the Horton shapefile using the ``name`` field.
- Select only required fields: ``initial``, ``final``, ``decay``.
- Add a prefix like ``Horton_`` for clarity.

Step 5: Copy Joined Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Reopen the attribute table for infiltration areas.
- Toggle editing and update:
  - Set ``Horton Initial`` = ``Horton_initial``
  - Set ``Horton Final`` = ``Horton_final``
  - Set ``Decay`` = ``Horton_decay``
- Click **Update All**, save edits, and turn off editing.

.. important::
   Joined fields are read-only. You must copy them to editable fields.

Step 6: Delete the Join
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go back to **Layer Properties > Joins**.
- Remove the join to improve performance.

Step 7: Global Horton Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open **Infiltration Editor > Global Infiltration**.
- Check **Horton** and enter generic global values (used only for missing cells).
- Click **OK**.

Step 8: Schematize and Export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Schematize** to sample Horton values to the grid.
- Enable **Infiltration Switch** in **Control Parameters**.
- Save your project.

Then:
- Go to **Export DAT Files**.
- Select only ``INFILTRATION`` and ``CONT.DAT``.
- Click **OK** to export.

Step 9: Edit Initial Abstraction (Manual Step)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open ``INFIL.DAT`` in Notepad++.
- Add **initial abstraction** manually, if needed (e.g., ``0.2``).
- Save and do not forget to reapply this if you re-export later.

.. note::
   This value offsets rainfall before infiltration starts. It may be added to the plugin in the future.

Troubleshooting: Missing Grid Elements
--------------------------------------
- If some cells don’t receive infiltration data, verify **complete polygon coverage**.
- Use the **Vertex Tool** to stretch polygon boundaries over missing cells.
- Save and re-run **Schematize**.

Infiltration - Assign Green and Ampt
----------------------------------------------

.. Important:: FLO-2D uses three infiltration types. Choose one lesson and skip the other two.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/PE9vvuW7p-A?si=O2bP9jhPCbZUWS10"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson walks through the **Green-Ampt infiltration method** in FLO-2D, including the 2018 and 2023 Flood Control District methods and the SERGO/OSM-based method. You'll learn how to set global parameters, apply land use and soil data, and export Green-Ampt data files.

Step 1: Set Global Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the **Global Infiltration** tool.
- Check **Green-Ampt**.
- Recommended default values (inches/hour, inches):
  - Initial Abstraction: ``0``
  - Porosity: ``0.4``
  - Hydraulic Conductivity: ``0.1``
  - Initial Saturation: ``0.3``
  - Final Saturation: ``1.0``
  - Soil Suction: ``4``
  - Soil Depth: Set to ``1`` for limited depth (set to ``0`` for unlimited).
- Click **OK**.

Step 2: Load Land Use and Soil Shapefiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Add land use and soil shapefiles (e.g., 2018 or 2023 Maricopa County).
- Inspect attributes such as:
  - ``initial abstraction``, ``impervious``, ``initial saturation``
  - ``hydraulic conductivity (XKsat)``, ``soil depth``
  - ``DTheta dry``, ``DTheta normal``, ``Psif``

Step 3: Use the 2018 Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Run **Green-Ampt Calculator** (2018 version).
- Input Fields:
  - Soil Layer: ``XKsat``, ``RockOutcrop``, ``SoilDepth``
  - Land Use: ``Initial Saturation``, ``Initial Abstraction``, ``Impervious``
- Leave ``Vegetative Cover`` unchecked.
- Click **OK** to calculate.

Step 4: Review the 2018 Manual Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 2018 method derives ``Psif`` and ``DTheta`` from XKsat.
- Uses area-weighted averages (no log scaling).
- Global and local infiltration data will be stored in ``INFIL.DAT``.

Step 5: Export Infiltration Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Ensure **Infiltration Switch** is ON in **Control Parameters**.
- Click **Export DAT Files**.
- Export only ``INFILTRATION`` and ``CONT.DAT``.

Step 6: Use the 2023 Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Switch calculator to use 2023 soil shapefile.
- Input Fields:
  - Soil Layer: ``XKsat``, ``RockOutcrop``, ``SoilDepth``, ``DTheta Normal``, ``DTheta Dry``, ``Psif``
  - Land Use: ``Initial Saturation``, ``Initial Abstraction``, ``Impervious``
- Leave ``Vegetative Cover`` unchecked.
- 2023 method uses:
  - Log area average for XKsat and Psif
  - Intersected DTheta from land use-soil overlay
  - Maximum impervious value from both layers

Step 7: Use SERGO and OpenStreetMap Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use **SERGO Downloader** to get soil components:
  - Horizon, Fragmentation, Component layers
- Use **OSM Downloader** to generate land use polygons:
  - Raster images are vectorized based on color mapping.
- Calculator reads attributes:
  - Land Use: ``Initial Saturation``, ``Impervious``, ``Initial Abstraction``
  - Soil: ``XKsat``, ``Soil Depth``, ``DTheta``, ``Psif``

Step 8: Verify Infiltration Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Enable **Advanced Layers** in **FLO-2D Settings**.
- Review attributes in **infiltration_results**:
  - ``Hydraulic Conductivity``
  - ``Soil Suction``
  - ``DTheta``
  - ``Initial Abstraction``
  - ``Impervious``
  - ``Soil Depth``

.. note::
   Always **re-sort by FID** before export to avoid misaligned data rows.

Save Export and Run
-----------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/nOPr9G2UmQA?si=BhGrr7CuclE_UC4Q"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson covers the final steps before running your FLO-2D simulation. You will learn how to save your project, export model data, and run the simulation using the **Quick Run** tool.

Step 1: Save Your Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Remove unneeded scratch layers:
  - Right-click any temporary layers you no longer need and select **Remove**.
- Click the **Save Project** button.
- When prompted, click **Yes** to save scratch layers into the **GeoPackage**.
  - This ensures they are committed and safely stored with your project file.

.. tip::
   Scratch layers must be saved to preserve your data across sessions.

Step 2: Export Data Using Quick Run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use **Quick Run** to export and simulate in one step.
- Quick Run is only available **if your project does not include storm drains**.

To use Quick Run:
- Click **Quick Run** from the FLO-2D toolbar.
- Create a new folder (e.g., ``quick_run``) for the export.
- Select this folder when prompted.

The plugin will:
- Export all required `.DAT` files
- Automatically launch the simulation upon successful export

Step 3: Wait for Simulation to Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Once data is exported, the model will begin running.
- Watch for early rainfall values in the results window.
  - Rainfall accumulation (e.g., ~0.1 in) will appear first.
  - Ponded water will start appearing on the grid.
  - Water will flow down streets and terrain according to the grid and infiltration settings.

.. note::
   Simulation results should show flow routing from rainfall across your modeled surface and toward low-lying areas.

Wrap-up
----------
You’ve now saved your project, exported model inputs, and initiated a run using **Quick Run**. The next lesson will guide you through reviewing and visualizing your simulation results.

