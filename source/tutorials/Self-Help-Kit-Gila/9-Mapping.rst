Project Review and Mapping
==================================

Set up culverts using Rating Tables and Culvert Equations using QGIS and the FLO-2D Plugin.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

Load Results and Maps
-------------------------------

.. note:: Place holder video.  Final version not ready.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ebIFoGUuQcI?si=XMiARpQIkzIPD5Es"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson introduces the setup of hydraulic structures in FLO-2D using QGIS. It includes visual styling, elevation considerations, and labeling, preparing the dataset for modeling.

Step 1: Load Hydraulic Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Load the **hydraulic_structures.shp** shapefile into your QGIS project.
- Modify the layer style:
  - Change the symbol to an **arrow line** for visualizing flow direction.
  - Adjust the **color** to make structures more visible.

.. note::
   Arrows indicate the direction of flow: inlet is the first vertex, outlet is the last.

Step 2: Understand Elevation Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Each hydraulic structure must move flow from an **inlet** to an **outlet** grid element.
- Elevations must match the **invert elevations** of culverts and connected features.

.. tip::
   Use the **Identify Features** tool on your elevation raster and grid layers to find elevation mismatches.

Common adjustments:
~~~~~~~~~~~~~~~~~~~
- **Move** the inlet/outlet point to the nearest correct elevation cell.
- Use **elevation correction polygons** where necessary to model invert slopes and street flow paths.
- Consider **stilling basins** or **weirs** where sediment control is necessary.

Step 3: Examples of Flow Adjustments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Evaluate upstream/downstream cells:
  - Example: Move from a 1428 ft grid cell to a 1425 ft cell to match invert.
- Ensure continuity along **trapezoidal channels** feeding culverts.

Step 4: Assign Structures to Cross-Sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- For culverts connecting to channels:
  - Always assign outlet to the **left bank** of the cross-section.
  - FLO-2D exchanges discharge to cross-sections, not grid elements.

.. note::
   Right bank assignments can cause ambiguity. Use left bank consistently.

Step 5: Label the Hydraulic Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open **Layer Properties > Labels** tab.
- Label each structure with the **structure_name** field.
- Recommended settings:
  - Font size: **12 pt**
  - Font color: **white** or a visible contrast color

Step 6: Check Attribute Table Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Ensure the attribute table contains:
  - ``structure_name``
  - ``structure_type`` (floodplain-to-floodplain, floodplain-to-channel, etc.)
  - ``tailwater_switch`` (default = 0)
  - ``head_reference_elevation``
  - Additional culvert parameters (used in the advanced setup)

Structure Types:
~~~~~~~~~~~~~~~~
- **Floodplain to Floodplain**: Flow between two grid cells
- **Floodplain to Channel**: Connect to left bank of a cross-section
- **Channel to Channel**: Set up previously in the Channel lesson

Next Step
---------
In the next lesson, you'll learn how to define hydraulic structure parameters in the layer attribute table and export your model data.

Review a Project Run
-------------------------------

.. note:: Place holder video.  Final version not ready.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ebIFoGUuQcI?si=XMiARpQIkzIPD5Es"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
