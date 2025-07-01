Appendix C: FLO-2D HDF5 Data Structure
======================================

Use this reference as a structural map of the `input.hdf5` file. Variables shown in **red** correspond to entries in the Data Input 
Manual, while those in **green** are internal cross-reference or ID fields used by the HDF5 structure.

Boundary Conditions
-------------------

Inflow
~~~~~~
Defines the location and time series for inflow hydrographs.

*Corresponds to:* `INFLOW.DAT`

.. image:: ./img/hdf5/FLO060.png

Reservoirs
~~~~~~~~~~
Specifies the reservoir nodes, elevations and a manning's n value corrector.

*Corresponds to:* `INFLOW.DAT`

.. image:: ./img/hdf5/FLO060A.png

Outflow
~~~~~~~

**Floodplain Normal Depth**

*Corresponds to:* `OUTFLOW.DAT`

Defines rating curve or normal depth outflow control for floodplain cells.

.. image:: ./img/hdf5/FLO085.png

**Channel Normal Depth**

Normal depth outflow control for channels.

.. image:: ./img/hdf5/FLO086.png

**Floodplain Time Stage**

Time-series stage boundary for floodplain grid cells.


.. image:: ./img/hdf5/FLO087.png

**Floodplain and Channel Time Stage**

Combined time-stage outflow control affecting both domains.

.. image:: ./img/hdf5/FLO088.png

**Channel Time Stage**

Time-stage boundary applied to channel outflows.

.. image:: ./img/hdf5/FLO089.png

**Floodplain and Channel Time Stage and Free**

Free outflow combined with a time-stage control.

.. image:: ./img/hdf5/FLO090.png

**Channel Time Stage and Normal**

Combines stage-based control with a normal depth fallback.

.. image:: ./img/hdf5/FLO091.png

**Channel Depth-Discharge Power Regression**

Defines outflow using regression coefficients.


.. image:: ./img/hdf5/FLO092.png

**Channel Depth-Discharge Table**

Tabulated depth-discharge pairs for outflow control.

.. image:: ./img/hdf5/FLO093.png

Channels
--------

Global
~~~~~~

Channel control and bank data.

*Corresponds to:* `CHAN.DAT`, `CHANBANK.DAT`

.. image:: ./img/hdf5/FLO063.png

Channel Natural
~~~~~~~~~~~~~~~
Channel and cross section station elevation data.

*Corresponds to:* `CHAN.DAT`, `XSEC.DAT`

.. image:: ./img/hdf5/FLO065.png

Channel Trapezoidal
~~~~~~~~~~~~~~~~~~~
Defines trapezoidal cross sections using base width, depth, and side slope.

*Corresponds to:* `CHAN.DAT`

.. image:: ./img/hdf5/FLO083.png

Channel Rectangular
~~~~~~~~~~~~~~~~~~~
Defines simple rectangular cross sections using base width and depth.

*Corresponds to:* `CHAN.DAT`

.. image:: ./img/hdf5/FLO084.png

NoExchange / Confluence
~~~~~~~~~~~~~~~~~~~~~~~~
Reserved for special conditions like confluence or split flow.

*Corresponds to:* `CHAN.DAT`

[missing image]

Control Parameters
------------------

Contains global control data and switches and numerical tolerances.

*Corresponds to:* `CONT.DAT`, `TOLER.DAT`

.. image:: ./img/hdf5/FLO067.png

Grid
----

Defines spatial layout and surface properties.

*Corresponds to:* `TOPO.DAT`, `MANNINGS_N.DAT`, `CADPTS.DAT`, `FPLAIN.DAT`, `NEIGHBORS.DAT`

.. image:: ./img/hdf5/FLO068.png

Floodplain Cross Section
-------------------------

Specifies cross section grid elements that are reported to cross section output files.

*Corresponds to:* `FPXSEC.DAT`

.. image:: ./img/hdf5/FLO073.png

Gutter
------

Describes gutter system routing. [Add reference when applicable.]

*Corresponds to:* `GUTTER.DAT`

Hydraulic Structures
--------------------

[Awaiting description. Placeholder.]

*Corresponds to:* `HYSTRUC.DAT`

Control tables and name tables.

.. image:: ./img/hdf5/FLO106.png

Depth Discharge Tables and Culvert Equation Tables

.. image:: ./img/hdf5/FLO107.png

Rating curve and replacement curve tables.

.. image:: ./img/hdf5/FLO108.png

Bridge tables parameters and cross section data.

.. image:: ./img/hdf5/FLO111.png

.. image:: ./img/hdf5/FLO109.png

.. image:: ./img/hdf5/FLO110.png

Infiltration
------------

*Corresponds to:* `INFIL.DAT`

Method
~~~~~~
Defines the selected infiltration method: Green-Ampt, SCS, or Horton.

Green Ampt
~~~~~~~~~~

.. image:: ./img/hdf5/FLO076.png

.. _scs_hdf:

SCS Curve Number
~~~~~~~~~~~~~~~~
Defines curve number by grid or globally.

.. image:: ./img/hdf5/FLO077.png

.. _horton_hdf:

Horton
~~~~~~
Horton infiltration parameters spatially or globally defined.

.. image:: ./img/hdf5/FLO078.png

Levee
-----

*Corresponds to:* `LEVEE.DAT`

.. image:: ./img/hdf5/FLO071.png

Levee Failure Prescribed
~~~~~~~~~~~~~~~~~~~~~~~~
Time-based breach with user-defined data.

.. image:: ./img/hdf5/FLO096.png

Levee Failure Breach Erosion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dynamic breach using Fread BREACH method.

*Corresponds to:* `BREACH.DAT`

.. image:: ./img/hdf5/FLO097a.png

.. image:: ./img/hdf5/FLO097.png

Levee Failure Curve
~~~~~~~~~~~~~~~~~~~
User-defined breach progression using curve data.

Rainfall
--------


Uniform Rainfall
~~~~~~~~~~~~~~~~
Applies rainfall uniformly across all grid cells.

*Corresponds to:* `RAIN.DAT`

.. image:: ./img/hdf5/FLO079.png

Spatial Rainfall
~~~~~~~~~~~~~~~~
Applies rainfall using spatial rainfall depth distribution.

*Corresponds to:* `RAIN.DAT`

.. image:: ./img/hdf5/FLO080.png

Realtime Rainfall
~~~~~~~~~~~~~~~~~
Uses real-time precipitation from gridded time series.

*Corresponds to:* `RAIN.DAT`, `RAINCELL.DAT`

Note: IRAINDUM table is organized by grid columns x time rows.

.. image:: ./img/hdf5/FLO081.png

Storm Drain
----------------

The storm drain data for HDF5 can be cross referenced to the storm drain files in the Data Input Manual.   All other data is saved to the SWMM.INP and
SWMM.INI files.  The storm drain data is saved to the HDF5 file in the following tables:

*Corresponds to:* `SWMMFLO.DAT`, `SWMMOUTF.DAT`, `SWMMRT.DAT`, `SWMMFLODROPBOX.DAT`, `SDCLOGGING.DAT`


.. image:: ./img/hdf5/FLO101.png

SWMMFLO.DAT

.. image:: ./img/hdf5/FLO100.png

.. image:: ./img/hdf5/FLO102.png

.. image:: ./img/hdf5/FLO104.png

.. image:: ./img/hdf5/FLO103.png


Multiple Channel
----------------

*Corresponds to:* `MULT.DAT`, `SIMPLE_MULT.DAT`

.. image:: ./img/hdf5/FLO074.png

Reduction Factors
-----------------

Defines areal and watershed reduction factors.

*Corresponds to:* `ARF.DAT`

.. image:: ./img/hdf5/FLO075.png

QGIS
----

Data related to plugin-based preprocessing or export functions.

.. image:: ./img/hdf5/FLO082.png

Tailings
--------

Used for advanced mud/debris flow simulations.

**TAILINGS**  
*Corresponds to:* `TAILINGS.DAT`

**TAILINGS_CV**  
*Corresponds to:* `TAILINGS_CV.DAT`

**TAILINGS_STACK_DEPTH**  
*Corresponds to:* `TAILINGS_STACK_DEPTH.DAT`

.. image:: ./img/hdf5/FLO095.png

Spatially Variable
-------------------

The 2D attributes for FLO-2D are stored in the Spatially Variable tables. The table name can be cross referenced to the corresponding \*.DAT file in the Data Input Manual.

**FPFROUDE**  
*Corresponds to:* `FPFROUDE.DAT`

**LID_VOLUME**  
*Corresponds to:* `LID_VOLUME.DAT`

**SHALLOWN_SPATIAL**  
*Corresponds to:* `SHALLOWN_SPATIAL.DAT`

**STEEPSLOPEN**  
*Corresponds to:* `STEEP_SLOPEN.DAT`

**TOLSPATIAL**  
*Corresponds to:* `TOLSPATIAL.DAT`

.. image:: ./img/hdf5/FLO094.png

