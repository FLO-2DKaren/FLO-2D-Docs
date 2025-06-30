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

.. image:: /images/hydraulic_structures_labels.png
   :alt: Example of labeled hydraulic structures with arrows.

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


.. _correct_elevation:

Correct Elevation
---------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/u41PNLBt8mk?si=0f7P3iE_7gwMFfuu"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Save Export and Run Pre Elevation Change
-----------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/oPha4GTRnQ0?si=e3hM3dhDYahu69bN"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



Create Culverts with Culvert Equations
----------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rACaKUlcFKU?si=yJCouGxFaV-GE5CI"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Summary and Review Project
-------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/Guo0N85qZlk?si=oQcqSHB5RVxrgQm5"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>