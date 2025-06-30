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


Review and Assign Walls
------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/EZGEPQZEs6A?si=RiECh45qLXuRhdHO"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Save Export and Run
------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/gdzmKSlocsE?si=uyVPzthJHeAiQ6iS"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
