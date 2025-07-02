Buildings and Walls
========================

Setup up Buildings and Walls using Open Street Map Downloader, QGIS, and the FLO-2D Plugin.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

Load and Assign Data
-----------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/lljO4niOWdQ?si=zBzN_ocXETMYlLGd"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson explains how to import and assign buildings in your FLO-2D model, including visualization tips and parameter configurations.

Step 1: Import Building Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Locate the **buildings** shapefile from the **Lesson 4 Tutorial** folder.
- Drag and drop the shapefile onto the map canvas in QGIS.

.. tip::
   Move the buildings layer into the **External Layers** group for better organization.

Step 2: Change Building Appearance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Double-click the **buildings** layer.
- To remove the black outline:
  - Set the **Stroke style** to **No Pen**.
- Change the fill color (e.g., Violet) for visibility.

Step 3: Check Building Attribute Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Open the attribute table to confirm the following required fields:
- ``collapse``: whether a building collapses during simulation (used in dam breach or large river simulations).
- ``ARF`` (Area Reduction Factor): adjusts flow for shallow overland flow.
- ``WRF`` (Width Reduction Factor): adjusts channel width for flow routing (rarely used).

.. note::
   For urban simulations, only ``ARF`` is typically required.

Step 4: Assign Buildings Using Grid Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Open **Grid Tools**.
2. Click the **Assign Buildings** button.
3. Set the following parameters:
   - **Layer**: buildings
   - **Collapse Field**: ``collapse``
   - **Area Reduction Field**: ``ARF``
   - **Width Reduction Field**: ``WRF``

- Click **OK** to apply.

This process will:
- Create a blocked areas layer representing building footprints.
- Update the **schematized data** to reflect buildings in the model.

Step 5: Building Rain Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ensure your rainfall setup includes the **Building Rain Switch**.
This makes rain that falls on buildings flow into the grid per assigned elevation.

- Turn on the **Building Switch** (ARF switch) in the FLO-2D Controls.
- Click **Save Components**.

.. important::
   If you forget to activate the building switch, buildings may act as sinks instead of obstructions.

Summary
--------
- Buildings are assigned as blocked areas.
- The ARF forces water to flow around buildings.
- Turn on building-related switches in the control parameters.


Download Building Polygons
------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/h-mN4m8rJnw?si=ieWhEVt5BZDst-AM"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

   
This tutorial covers how to obtain building data using OpenStreetMap (OSM) and prepare it for FLO-2D modeling. This process is useful when client-provided data is unavailable.

Step 1: Install the OSM Downloader Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to **Plugins > Manage and Install Plugins**.
- Search for **OSM Downloader**.
- Click **Install**.

.. tip::
   The OSM Downloader button is nearly transparent. Toggle it on/off to locate it in your toolbar.

Step 2: Prepare the Layer Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Right-click in the Layers panel and **Add Group**.
- Name it ``osm_download``.

Step 3: Download Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Activate the **OSM Downloader tool**.
- Draw a rectangle around your project area.
- Save the file with a clear name like ``osm_file.geojson``.
- The data is downloaded in EPSG:4326 and will be reprojected later.

Step 4: Export Polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Turn off unnecessary OSM sublayers (e.g., roads).
- Right-click the **polygons** layer > **Export > Save Features As...**
- Save as ``osm_buildings``.
- Change the CRS to your project CRS (e.g., EPSG:2223).
- Remove irrelevant fields before exporting.

Step 5: Filter for Buildings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open the attribute table.
- Sort by the ``building`` field.
- Select rows where ``building`` is null or empty and delete them.
- Save your edits.

Step 6: Crop to Project Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use **Select by Location**:
  - Select features from ``osm_buildings``.
  - Where the feature is **within** the computational domain layer.
- Delete unselected features (those outside your project area).

Step 7: Clean Building Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Review building types.
- Delete features such as ``carports``, ``gas islands``, etc., which don’t obstruct flow.

Step 8: Add Required Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Add the following integer fields:
  - ``collapse``
  - ``ARF`` (Area Reduction Factor)
  - ``WORF`` (Width Reduction Factor)
- Use the **Field Calculator** to:
  - Set ``collapse = 0``
  - Set ``ARF = 1``
  - Set ``WORF = 0``

Step 9: Fill in Missing Buildings (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Turn on a satellite basemap (e.g., Google Satellite).
- Use the **Add Polygon tool** or **Shape Digitizing Toolbar** to:
  - Digitize missing buildings.
  - Use ``Rectangle from Extent`` for fast creation.
  - Use ``Digitize with Segment`` for complex shapes.

Step 10: Export the Final Building Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Save your edited buildings as a new layer if desired.
- This layer can now be used with the **Grid Tools > Assign Buildings** tool.

Step 11: Review the `ARF.DAT` File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- After exporting building reductions, open ``arf.dat`` in Notepad++.
- Key sections:
  - ``G`` line: global reduction factor (e.g., set to 0.5 to reduce all T lines to 50%).
  - ``T`` lines: fully blocked cells.
  - ``P`` lines: partial blocks with ARF values < 1.0.

.. tip::
   The model will automatically convert cells with high ARF values (e.g., > 0.95) to fully blocked.


Review and Assign Walls
------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/EZGEPQZEs6A?si=RiECh45qLXuRhdHO"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This lesson reviews check files and model behavior after a full simulation including walls and buildings.
We focus on understanding outputs and interpreting any warnings or adjustments made by FLO-2D after the simulation.

Check File Review
-----------------------------

After running the model:

- Check for the presence of updated `error.check` files. Some older ones may persist if not overwritten.
- Confirm that levies are correctly defined. Messages in the check files may warn of adjustments or missing values.

.. note::
   If a `.check` file was not updated with a current timestamp, it's likely outdated.

Review of Specific Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**rf.dat**:
- T-lines indicate total blockage by walls or buildings.
- Reduction factor warnings may appear if `RIMP` (imperviousness) is less than the area reduction factor (ARF).
- FLO-2D will adjust this internally to avoid instability.

**levy.doap**:
- Warns if grid elevation differences across walls or levies exceed 1 ft.
- Often not critical unless you're modeling shallow Overland flow.

**levy.fail**:
- Lists grid elements where levies failed.
- Failure can result from water depth exceeding threshold on a wall cell.

**evacuated_fp.out**:
- Identifies cells that dried out completely over time steps.
- Check surrounding slope and surface conditions. May require adjusting Manning's `n` or assigning a spatial tolerance.

**chan.elevation.check**:
- Shows mismatches between bank elevation and floodplain elevation.
- Positive values: channel bank is higher.
- Negative values: floodplain is higher (may indicate perched banks).

Interpreting Failures
-----------------------------

- Failures near project boundaries often result from unrealistic collection of water in corners or poorly placed walls.
- Review in QGIS using the FLO-2D profile tool to inspect cross-sections.
- Use street view if necessary to confirm if structures are above ground or have relief features.

Tips
~~~~~~~

- Walls along the boundary may fail due to limited discharge options. Consider removing or adjusting them.
- Buildings sitting higher than surrounding terrain (due to lidar artifacts) may affect wall performance.
- Use elevation profile plots to determine validity of outliers.
- Check the `levy_deficit.it.out` and `levy_do.out` for failure times and flow conditions.
- The model may self-correct minor inconsistencies during runtime.

.. tip::
   Only take corrective action if errors are persistent or affect flood routing.

Next Steps
----------------

We now move on to the **Mapping** lesson where simulation outputs like maximum depth and velocity vectors are imported and analyzed.

Save Export and Run
------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/gdzmKSlocsE?si=uyVPzthJHeAiQ6iS"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson walks through saving the FLO-2D project, exporting the required data, troubleshooting errors, and running the simulation.

Step 1: Clean the Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Right-click and remove temporary or unused layers before saving.
- If data hasn’t been committed to the GeoPackage, you can remove it by **Right-click > Remove Group**.

Step 2: Save Your Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click the **Save Project** button to preserve edits and store current data in the `.gpkg`.

.. note::
   If you already saved the project earlier, some data might already be in the GeoPackage.

Step 3: Export and Run the Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Export the Project Data**
   - Click the **Export** button.
   - Confirm export of the **IMP** file when prompted.

2. **Run the Model**
   - After export, the path should be set automatically.
   - Click **Run** to begin simulation.

.. warning::
   If you receive an error on run, open the `error.check` files to investigate.

Step 4: Troubleshoot Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Example Error: “Channel extends through a levy at Bank 5528”
- Solution:
  1. Use the **Vertex Editor** to reposition the levy line so it does not overlap the channel.
  2. Click **Save**.
  3. Recalculate the levy using the **Levy Tool**.

Step 5: Re-export and Rerun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use **Export > Select only Levy data** to replace the corrected `.dat` file.
- Click **Run** again to verify the error is resolved.

.. tip::
   Once the model runs successfully, you can proceed to the summary and data review steps.

Final Notes
-----------------------------
- This step completes the build-and-run process for the current project.
- Always check `.check` files if errors occur.
- Focus first on correcting spatial data (like levies or channels) rather than complex rebuilds.
