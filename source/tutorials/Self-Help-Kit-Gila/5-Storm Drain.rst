Storm Drain
========================

This advanced lesson shows how to create a storm drain from Shapefiles.  Stay tuned for more lessons that will
show how to set up a storm drain from a swmm.inp.

.. Note:: It will be easier to view these videos on YouTube.

   Set the video playback speed to 2x to complete the lessons faster.

Storm drain checklist.

For those of you who love a challenge, it's good practice to do a "Speed Run" of the Self-Help
Kit.  Here is a checklist of tasks that might get skipped during storm drain model building.

- [ ] Adjust outfall location so all outfalls rest on a left bank node.
- [ ] Add a storage unit volume table and assign `Storage1` to all storage units.
- [ ] Ensure conduit length is a minimum of 30 ft, which is the cell size.
- [ ] Add Type 4 rating tables to the Type 4 inlets.
- [ ] Add a pump table and assign it to `P1`.
- [ ] Auto-assign nodes.
- [ ] Carefully inspect shapefile fields.
- [ ] Check storm drain control settings.
- [ ] Schematize the network.
- [ ] Perform a test run.

Data and Resources
--------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/YGHUA2fgIFA?si=hJIfJgNR7BOciJuL"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson provides an introduction to importing and understanding the storm drain system in FLO-2D using QGIS.

Step 1: Import Storm Drain Shapefiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Load storm drain shapefiles into your project.
- Sort files by type and select those labeled as **shapefiles**.
- Drag and drop into a **Storm Drain** group in your QGIS layer panel.

Step 2: Understanding FLO-2D Storm Drain Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- FLO-2D handles most drainage through the **surface model**:
  - Channels and detention basins are modeled at the surface.
  - Inlets and outfalls interface with the surface system.

.. note::
   You do **not** need subcatchments, rain gauges, or separate infiltration models like in SWMM.

- Storm drains receive water from:
  - Streets and inlets (inflow)
  - Outfalls discharge to channels or basins (outflow)

Step 3: Documentation and Learning Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- FLO-2D provides built-in documentation:

  **Storm Drain Editor Manual**
  - Located in the installation directory under ``FLO-2D > Manuals`` or via the **book icon** in the editor.
  - Key Chapters:
    - Chapter 2: Inlet data types
    - Chapter 3: Output file structure
    - Chapter 4: Setup guidelines
    - Chapter 5: Troubleshooting
    - Chapter 6: How to review your storm drain model

  **Advanced Tutorial**
  - Found on YouTube under the *New Self-Help Kit* playlist

  **EPA SWMM GUI**
  - Installed alongside FLO-2D
  - Use for pump setups, advanced SWMM elements, and additional documentation

  **OpenSWMM.org**
  - A knowledge base and community forum with examples, questions, and shared resources.

  **ChatGPT**
  - Use ChatGPT (3.5 or 4.0) to assist with modeling questions or examples
  - For example: "Build a SWMM example with a pump" will generate a valid ``.inp`` file

Step 4: Contact Support
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you get stuck:
- Contact FLO-2D support directly
- Email format: ``<firstname>@flowtwd.com``  
  (e.g., karen@flowtwd.com or contact@flowtwd.com)
- Use the **Contact Form** on the FLO-2D website for additional help

Wrap-up
-------
In this lesson, you’ve:
- Imported storm drain shapefiles
- Reviewed the role of inlets and outfalls
- Accessed documentation and training resources

Next lesson: Review and edit storm drain shape file attributes.


Node Overview - Inlet, Junction
----------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/KzIdcyYZKpQ?si=a3u6R2X0fQH_HiuQ"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


This lesson explains how to review and interpret inlet and junction shapefile data for storm drain modeling in FLO-2D.

Step 1: Storm Drain Feature Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Point features** (nodes): inlets, junctions, manholes, outfalls, storage units
- **Polyline features** (links): conduits, pumps, orifices

Inlet and junction nodes contain attributes that define how they interact with the grid and storm drain network.

Step 2: Documentation References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use the **Storm Drain Editor Manual** (Chapter 2) to understand inlet types:
  - Type 0: Junction (no interaction with surface)
  - Type 1: Curb opening
  - Type 2: Curb with gutter
  - Type 3: Grate
  - Type 4: Unique (e.g. headwall)
  - Type 5: Manhole

Step 3: Reviewing Node Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Open the shapefile table for inlets and junctions in QGIS.

- **Required attributes** (vary by type):
  - ``Name``: Must start with "I" for inlets
  - ``Type``: Integer (0 to 5)
  - ``Elevation``: Invert elevation
  - ``Max Depth``: From surface to invert
  - ``Length``, ``Width``, ``Perimeter``, ``Area``, ``Height``: As required per type
  - ``Weir Coefficient``
  - ``Feature Switch``: 0 (rim), 1 (invert), or 2 (special conditions)
  - Optional: ``Curb Height``, ``Clog Factor``, ``Clog Time``, ``Dropbox Area``

Step 4: Understanding Specific Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Type 0: Junction**
- No surface interaction
- Requires only invert elevation and max depth

**Type 1: Curb Opening**
- Requires: Length, Height, Weir Coefficient
- Does not include sag or width

**Type 2: Curb with Gutter**
- Requires: Length, Width (sag), Height, Weir Coefficient
- Optional: Curb Height, Dropbox Area

**Type 3: Grate**
- Requires: Perimeter, Area, Sag (optional), Weir Coefficient
- Often used in depressed road areas

**Type 4: Unique (Headwall)**
- Requires: Invert Elevation, Max Depth
- ``Feature Switch = 1`` sets grid elevation to invert
- Used for channel interfaces or direct inflow control

**Type 5: Manhole**
- Requires: Invert Elevation, Max Depth, Perimeter, Area, Surcharge Depth, Weir Coefficient
- Acts like a junction until surcharge pops the lid
- Allows bidirectional flow once popped

Step 5: Visualization Tips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Use **categorized symbology** to color nodes by inlet type
- Use **Zoom to Feature** and satellite imagery to verify node alignment
- Position nodes carefully relative to grid elements for accurate simulation

Step 6: Unit Notes
~~~~~~~~~~~~~~~~~~~~~~~~
- All dimensions in **feet**
- Clogging factor is a **percentage (0-1)**
- Clogging time is in **hours**

Wrap-up
-------
This lesson focused on how to interpret and verify inlet and junction attributes using shapefile data. Proper definition ensures realistic storm drain and surface flow interactions.

Node Overview - Outfall, Storage Unit
------------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/D-tWFxOMdXE?si=DjCLC3GfiyyMzqsu"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Link Overview - Conduit
-----------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ZReLFF5yfYQ?si=K1QSmsJcsPRt9Hr-"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Link Overview - Pump, Orifice, Weir
------------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/FQhkxsgntPY?si=CWEW6rvhRHw51-NA"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Create a Storm Drain from Shapefiles
------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/DNxhqBgOfuY?si=D67eo3YLWYpqs0x4"
   title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
   gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Summary and Review Results
---------------------------

Coming Soon

Storm Drain from SWMM.INP
---------------------------

Coming Soon