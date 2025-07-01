.. _structure_example:

Hydraulic Structures - Culverts
==================================

Set up culverts using Rating Tables and Culvert Equations using QGIS and the FLO-2D Plugin.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

Import and Review Culvert Data
-------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ebIFoGUuQcI?si=XMiARpQIkzIPD5Es"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In this lesson, we begin setting up hydraulic structures (culverts, weirs) in the FLO-2D project using QGIS. The workflow involves importing a shapefile, adjusting symbology, verifying flow direction, and preparing the geometry and elevation data.

Add the Hydraulic Structures Layer
----------------------------------
- Drag the ``hydraulic_structures.shp`` into the QGIS map.
- Change the symbology to **arrow** style to visualize the flow direction.
- Optionally, change the fill color for visibility.

.. tip::
   The arrow is drawn from the first to last vertex of each polyline—first is **inlet**, last is **outlet**.

Flow Direction and Invert Elevation
-----------------------------------
- Each hydraulic structure moves flow from inlet to outlet.
- Verify and correct elevation to reflect true invert elevation of the structure.
- Use **ID tool** to check elevation of individual grid cells and surrounding terrain.

.. note::
   The grid cell elevation is an average, but for culverts we need the **lowest** point (invert) for both inlet and outlet.

Elevation Correction Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Example 1:
  - Upstream: 1409 → Invert needed: 1405
  - Use elevation correction tools to align DEM with true invert.
- Example 2:
  - A weir is used to filter sediment before reaching a stilling basin.
  - Identify inlet (1390) and downstream invert (1385) and correct grid elevation accordingly.

Scuppers and Elevation Transitions
----------------------------------
- Some inlets capture runoff from streets via scuppers.
- Adjust elevation across roadways and localized channel segments so water reaches inlets correctly.

Shared Culverts Between Floodplain and Channels
-----------------------------------------------
- When flow is routed to a **channel**, always assign the **left bank**.
- This ensures proper mapping to the **cross-section**, not just the bank cell.
- Right banks can contain multiple grid cells, which may lead to ambiguity.

Labeling Hydraulic Structures
-----------------------------
- Open layer properties and go to **Labels**.
- Choose the field ``structure_name`` to display.
- Adjust font size and color for better visibility.

**Put Image Here**

Understanding Structure Types
-----------------------------
Each structure is categorized by flow type:
- **Floodplain to Floodplain**
- **Floodplain to Channel** (requires assignment to left bank)
- **Channel to Channel** (handled earlier in the channel lesson)

Switches and Advanced Setup
---------------------------
- Set all structures initially to use a **rating table**.
- Tailwater switch: set to ``0`` by default, unless needed otherwise.
- Head reference elevation and geometry parameters will be handled in the advanced culvert setup.

Next Steps
----------
In the next video, we'll learn how to assign hydraulic structure attributes into the project database.


Set-up Culvert Structures
-------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/WKjd-FG0ZUM?si=VVumLcmUz5gq9NSg"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This part of the lesson shows how to import and configure hydraulic structures in your FLO-2D project using QGIS.

.. note::
   Covert (culvert) data rarely comes as pre-formatted GIS line features. Most often, site surveys or as-built drawings are needed.

Step 1: Import the Hydraulic Structure Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Open **QGIS Lesson 6** project.
- Drag and drop the ``hydraulic_structures.shp`` file from the lesson data folder onto the map.
- Change symbology:
  - Set to **Arrow symbol** to show flow direction.
  - Optionally brighten the line color.

.. tip::
   The arrowhead marks the **Outlet**, and the first vertex is the **Inlet**.

Step 2: Copy from Template Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Select features from the template layer:
  - Use **Select Features** tool or ``Ctrl+A``.
  - Copy with ``Ctrl+C``.
- Activate the **Structure** layer from the **FLO-2D widget** editor.
  - Ensure editing mode is on.
  - Paste with ``Ctrl+V``.
- Save the edits.

Step 3: Name and Review Each Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use the **Center on structure** button to step through.
- Rename each one based on the provided naming convention (e.g., ``CLV001`` to ``CLV012``).
- Set labels to ``structure_name`` field with 12pt font for visibility.

Step 4: Assign Structure Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Identify structure types:
  - **Floodplain to Floodplain**
  - **Floodplain to Channel** (must be on a **Left Bank node**)
  - **Channel to Channel** (usually already handled in the channel lesson)
- Set the type to **Rating Table** using the drop-down menu.

.. note::
   For grouped culverts (e.g., simple storm drain systems), assign a **storm drain capacity** in CFS.

Step 5: Schematic Correction and Recheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- After assigning types:
  - Save and click **Schematize** to update geometry.
  - Check and re-validate structure assignments one more time.
  - Use the Center button to cycle through and verify again.

Step 6: Import Rating Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- From the ``ct_tables`` folder, select all files and import.
- Only rating tables that match existing structure names will be applied.

Step 7: Manually Modify a Rating Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Example: reduce max headwater for ``129A``, ``129B``, ``129C`` to approx. 3 feet.
- Delete rows from 3.0+ ft.
- Copy and paste modified table to the other two structures.

.. note::
   Use ``Ctrl+C`` and ``Ctrl+V`` or **Copy/Paste** buttons.

Next Step
---------

The next step is to **Save, Export, and Run** the model. This is covered in the following video.


.. _correct_elevation:

Correct Elevation
---------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/u41PNLBt8mk?si=0f7P3iE_7gwMFfuu"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson covers how to make elevation corrections for hydraulic structures, set up minimum elevations, apply levees, and prepare the model for export and run.

Step 1: Copy Elevation Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use the **Identify Features** tool to get the elevation at the required location.
- Right-click the value in the Identify panel and choose **Copy Attribute Value**.

Step 2: Create Elevation Polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to the **Elevation Polygons** layer.
- Start editing and click **Add Polygon**.
- Draw a polygon around the **centroid** of the grid element you want to modify.
- Set the elevation using the previously copied value.
- Set the correction method to ``grid`` and give the polygon a name like ``head wall``.

Step 3: Setup Minimum Elevation Polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- For complex corrections, select multiple grid cells and draw a polygon.
- Set the name to ``min from elev raster`` or similar.
- Set method to ``grid``; leave other values ``null``.

Step 4: Apply a Levy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use the **Levy Line** tool to draw a line where flow should be restricted.
- Assign the crest elevation based on sampled raster value (e.g., 1396.5).
- Reprocess the levies using:
  ``Plugins > FLO-2D > Create Schematic Layers from User Layers`` with ``Levy Lines`` checked only.

Step 5: Adjust Hydraulic Structure Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use the **Vertex Tool** to move hydraulic structure endpoints to correct elevations or grid elements.
- After adjustment, save and **Schematize** the structure lines to update the schema.

Step 6: Apply Grid Element Corrections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- For polygons with assigned elevation values:
  - Use **Grid Element Correction Tool**
  - Select: ``Elevation polygon attributes``
  - Check: ``Only selected polygons``

- For polygons pulling from raster values:
  - Use **External Layer Mode**
  - Set layer: ``Elevation Polygons``
  - Check: ``Centroids within polygons``
  - Select: ``Statistics from raster``
  - Choose ``Minimum elevation``
  - Check: ``Statistics per grid element`` and ``Only selected features``

Step 7: Export and Run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Export DAT files with a name like: ``post_elevation_change_and_correction.dat``
- Run the model.

.. note::
   These steps ensure correct invert elevations, allow headwalls to collect water properly, and ensure flow can pass over levees or into hydraulic structures.

.. tip::
   After corrections, verify grid elevations with the Identify tool to confirm changes.


Save Export and Run Pre Elevation Change
-----------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/oPha4GTRnQ0?si=e3hM3dhDYahu69bN"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This short lesson walks through saving hydraulic structures, exporting the data, and running the model. It is part of the final steps for preparing your model.

Step 1: Save the Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click the **Save** button to commit your hydraulic structures to the layer in the GeoPackage.

.. note::
   You do not need to turn on the export switch again if it was already activated when setting up channel hydraulic structures.

Step 2: Export Data Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Go to the **Import/Export** button.
- Select **Option 3** to export data files.
- Create a new folder inside your ``lesson6`` directory called:

  ::

    pre-elevation-change

  This helps distinguish the export prior to making elevation corrections.

- First, the D-series data files are exported.
- Then, the Storm Drain files are exported.
- You should now see a complete set of exported files inside the folder.

Step 3: Run the Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click **Run FLO-2D** to initiate the simulation.

.. note::
   If there is **no error.check** file generated, it means your data was set up correctly.

.. warning::
   Although the model runs, the results may still be inaccurate due to elevation issues. These will be addressed in the next lesson.

What's Next?
----------------------------
Now that we have run the model using the current elevations, we will compare it to a corrected version. Proceed to the next video to apply **elevation corrections** and re-run the model.


Create Culverts with Culvert Equations
----------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rACaKUlcFKU?si=yJCouGxFaV-GE5CI"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson walks through how to convert culverts from rating tables to generalized culvert equations (GCE) in FLO-2D, and then run the model to compare the results.

Convert a Culvert to GCE
------------------------

We are updating culvert **CL-009** from a rating table to a generalized culvert equation.

1. **Change the Structure Type**:
   - Open the structure editor.
   - Set type to `Culvert Equation`.

2. **Set GCE Parameters**:
   - Diameter: 48 in (convert to 4 ft).
   - Barrels: 3
   - Conduit Length: Measured to be 250 ft (headwall to headwall).
   - Entrance Type: 1 (square edge with headwall)
   - Culvert Type (CType): 2 (circular)
   - Manning's n: 0.018
   - Entrance Loss Coefficient (K): 0.5
   - Base: 0

.. note::
   These values are based on as-built drawings and Table C2 from HDS-5, 3rd Edition.

Convert Another Culvert to GCE
------------------------------

Now convert **CL-122**:

1. **Update Parameters**:
   - Set to `Culvert Equation`
   - Height: 5 ft (Box Culvert)
   - Length: 100–110 ft
   - Entrance Type: 1 (wing wall 30°–75°)
   - Culvert Type: 1 (box)
   - Barrels: 1
   - Base: 8 ft
   - Manning's n: 0.018
   - Entrance Loss Coefficient (K): 0.4

2. **Justification**:
   - From highway design manuals and HY-8 documentation
   - Image review confirms structure shape and inlet type

Apply and Export
----------------

- Click **Schematize** to update the structure layer.
- Verify values are correctly saved.
- Save and close prior runs if necessary.

3. **Export Files**:
   - Go to **Import/Export > Export .DAT files**
   - Create new folder:
     ``Generalized CT with Elevation Correction``
   - Export project and storm drain layers

Run the Model
-------------

- Click **Run FLO-2D**
- Ensure no errors are reported.
- Compare results with earlier model using rating tables.

.. tip::
   Always back up your project after making changes.

Next Steps
----------

Proceed to the **Summary** lesson, where the differences between rating tables and generalized culvert equation results will be reviewed.

Summary and Review Project
-------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/Guo0N85qZlk?si=oQcqSHB5RVxrgQm5"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>