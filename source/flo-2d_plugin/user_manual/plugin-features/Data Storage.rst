Data Storage
============

Database Format
---------------

.. |geopackage| raw:: html

    <a href="http://www.GeoPackage.org/spec/" target="_blank" rel="noopener">GeoPackage</a>

.. |sqlite| raw:: html

    <a href="http://www.sqlite.org/" target="_blank" rel="noopener">SQLite</a>

.. |sqlite_about| raw:: html

    <a href="https://www.sqlite.org/about.html" target="_blank" rel="noopener">Here</a>

The Plugin uses a |geopackage| for data storage.
It is a |sqlite| database with spatial extensions for storing vector and raster data.
The GeoPackage or \*.gpkg file is a binary file that stores data tables in SQLite format.
SQLite is a public domain data base engine that is used and supported worldwide.
More information about SQLite can be found at |sqlite_about|.
The GeoPackage encoding system is approved by an Open Geospatial Consortium, a standard that is deemed 
sustainable by the U.S. Library of Congress (Library of Congress, 2017).

The FLO-2D Plugin uses the GeoPackage to store the data in a series of tables.
The Plugin requires a single GeoPackage file for each project.
The project units and coordinate reference system are defined in the GeoPackage at the start of the project.

See the Technical Reference Manual for an outline of the GeoPackage data.  Find it here:
:ref:`Technical Reference Manual <tech_ref_manual>`


.. Warning:: Do not remove the default layers and tables from the GeoPackage.  It may break the structure of the
             project and the project may no longer load.

User Layers
-----------

Data is arranged as vector layers and tables in the Plugin.
The vector layers are organized as follows:

* Points

* Polylines

* Polygons

There is a layer for each FLO-2D model component that is digitized by the user and schematized into the “schematic” layers and tables.
These layers are used to define the schematized layers that are FLO-2D format.
The layers can be directly edited using the general QGIS editor tools and the FLO-2D Editor Widgets.
They can also be edited using the Attribute Table Editor and the Field Calculator.

.. image:: ../img/Data-Storage/data001.png

Schematic Layers
----------------

The Schematic Layers are organized such that the Plugin can generate the FLO-2D \*.DAT files from them.
These layers, created by the schematizing tools, should not be manipulated by the user.
The layers are vector layers with attribute fields that fill the FLO-2D data files.

.. image:: ../img/Data-Storage/data002.png

Hidden Layers
----------------

Hidden tables and layers can be accessed by using the checkbox in the FLO-2D Setting button.

.. image:: ../img/Data-Storage/data003a.png

The hidden layers are now visible in the Layers List.

.. image:: ../img/Data-Storage/data004a.png

QGIS Save
----------

The QGIS save button performs specific tasks when a FLO-2D Project is loaded.  These processes are outlined in
:ref:Save a FLO-2D Project <save_flo2d_project>.

.. image:: ../img/Buttons/savebutton.png
