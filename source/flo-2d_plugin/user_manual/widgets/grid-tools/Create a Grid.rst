.. _create_grid:
1. Create Grid
===============

.. image:: ../../img/gridtools/Create-a-Grid/create006.png

The create a grid processing tool can only be applied to one polygon.
The limits of the grid are defined by a single polygon.
The polygon can be digitized in the Computational Domain layer or an external layer such as an Area of Interest.
Both methods are described below.

Method 1: Computational Domain
---------------------------------------------

1. Select the Computational
   Domain layer in the Layers Panel>User Layers.

.. image:: ../../img/gridtools/Create-a-Grid/create003.png


2. Select the Toggle Editing
   button from the QGIS Toolbar to activate the editor and then click the Add Polygon Feature button to create a polygon.

.. image:: ../../img/gridtools/Create-a-Grid/create004.png
 

3. Digitize the polygon in the map canvas and right click to close the polygon.
   Set the grid element size and click OK to complete the polygon.

.. image:: ../../img/gridtools/Create-a-Grid/create009.png

4. Save the layer and turn off the
   editor by clicking the Editor tool to toggle it off.

.. image:: ../../img/gridtools/Create-a-Grid/create005.png


5. From the Grid Tools widget,
   select Create Grid.

.. image:: ../../img/gridtools/Create-a-Grid/create006.png


6. If this is a new project, the grid system will be created automatically.
   If this is a current project, the user will be asked to overwrite the current grid system.
   Click Yes to continue or No to cancel.
   Once the grid system is generated, the Grid created! message will appear.
   Click OK to close.

.. image:: ../../img/gridtools/Create-a-Grid/create010.png


7. If the grid system is not as expected,
   edit the Computational Domain layer and repeat the Create Grid process.

.. note:: Each time the grid system is replaced,
          the elevation and roughness data are also reset and must be recalculated.

8. The grid system data is
   saved to the Grid Schematic Layer as shown below.

.. image:: ../../img/gridtools/Create-a-Grid/create007.png

Method 2: External Domain Polygon
---------------------------------------

1. This method will use a shapefile
   with 1 polygon that represents the model area.

2. Click the Create Grid
   button.

.. image:: ../../img/gridtools/Create-a-Grid/create006.png

2. Select the shapefile and an
   attribute for cell size and click OK.

.. image:: ../../img/gridtools/Create-a-Grid/create002.png

3. Optionally, select the elevation
   source to align the grid to a raster pixel.

4. The tool will add a polygon
   to the Computational Domain layer and then create the grid.

5. The optional raster alignment
   will align the grid to the pixels of a raster.
