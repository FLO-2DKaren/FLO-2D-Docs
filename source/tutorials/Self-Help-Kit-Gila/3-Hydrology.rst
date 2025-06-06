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

This guide outlines how to load and manage a FLO-2D project in QGIS using a GeoPackage format. It follows the step-by-step instructions covered in the video tutorial.

0:00 – Introduction: Why Use a GeoPackage?
--------------------------------------------
Projects can break if files are moved and paths are lost. Storing everything in a GeoPackage allows you to move or share your QGIS project without losing linked data.

0:39 – Launching QGIS Efficiently
-----------------------------------
1. Open Windows search and type ``QGIS``.
2. Right-click the QGIS icon and choose ``Pin to Start``.
3. Use the Start Menu to quickly launch QGIS next time.

1:03 – Opening a Project
--------------------------
1. When QGIS opens, you may see the last loaded project listed. Click it to reopen.
2. If the project is missing (e.g., moved location), do the following:
   - Click ``FLO-2D Project`` > ``Open FLO-2D Project``.
   - If QGIS remembers the file path, select your GeoPackage and click ``OK``.
   - Otherwise, browse manually to the ``.gpkg`` file and open it.

1:44 – Managing GeoPackage Layers
-----------------------------------
To properly remove layers embedded in the GeoPackage:
1. Open the ``FLO-2D GeoPackage Management`` tool.
2. Check the layer you want to delete (e.g., ``Manning data``).
3. Click ``Delete`` to remove it from the GeoPackage.
4. If you do not want to delete anything, click ``Cancel``.

2:48 – Organizing the QGIS Interface
--------------------------------------
1. Go to the ``Browser`` tab.
2. If panels are misaligned, drag the Browser panel until the ``Layers Panel`` turns blue, then release to dock them together.

3:33 – Connecting to the GeoPackage
-------------------------------------
1. In the ``Browser`` panel, right-click ``GeoPackage`` and choose ``New Connection``.
2. Navigate to your project’s ``.gpkg`` file.
3. Expand the connection to view all spatial and tabular layers.

   Layers may include:
   - Polygons, Points, Polylines
   - Elevation raster
   - Table data (non-spatial)

4:33 – Embedded QGZ Project File
-----------------------------------
Earlier FLO-2D versions (e.g., v115) stored the ``.qgz`` project file externally, requiring it to be kept with the data. This created issues when transferring between folders or computers.

In the current setup, the project is embedded *within* the GeoPackage:
- Easier project portability
- No broken data paths

5:17 – Conclusion
--------------------
This approach simplifies managing, transferring, and editing FLO-2D projects in QGIS. All data and the project file are embedded in one portable GeoPackage file.


Assign an Inflow Node
--------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/YoYULnJ-0U0?si=OT2AiswXQdgwaTcF"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

