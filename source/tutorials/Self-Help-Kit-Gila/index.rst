Self-Help Kit Gila
========================

**Running into Problems?**  Please email FLO-2D staff via the |Contact-Form| for support.

.. |Contact-Form| raw:: html

   <a href="https://flo-2d.com/contact/" target="_blank">Contact Form</a>

The Self-Help Kit focuses on fundamental aspects of initiating and executing a FLO-2D project,
these lessons establish a solid foundation for beginners.  These tutorials are Youtube videos only Separated into
Different lessons.

The full YouTube video Playlist is here:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/playlist?list=PLkT3KNZwX6zkkfrM5Pcdvt7WqZuHWYU4c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


    This guide outlines how to download and set up the Tailing Dam Modeling Workshop using the provided training files and demo engine.

Step 1: Download the Workshop Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Click the provided download link.
- You'll be taken to a ShareFile page to fill in your information.
- Click **Continue** to begin the download.

.. note::
   This training was recorded using version 0.10.115 of the plugin, but it can be adapted for newer versions.

Step 2: Install the Workshop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Once downloaded, **unblock** the file if prompted.
- Run the installer. It may require admin rights depending on your system configuration.
- The workshop files will install to:

  ``C:\Users\Public\Documents\FLO-2D Pro\Documentation and Example Projects\Tailing Dam Workshop``

- Consider adding this folder to your **Quick Access** panel in Windows Explorer.

Step 3: Understand the Folder Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each folder within the workshop directory represents a lesson, such as:
- **Computer Setup**: contains the plugin
- **Project Setup**: contains sample data
- **Mud Flow**: might require you to generate your own data

Each lesson folder includes the data necessary to follow the tutorials.

Step 4: Use the Demo Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This workshop includes a demo engine, so you don’t need to install the full FLO-2D Pro suite.

Files provided:
- FLO-2D Engine executable
- Required support DLLs

.. important::
   These files allow you to run simulations without needing a license or installer.

Step 5: Set Up QGIS to Use the Demo Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Open QGIS.
- In **FLO-2D Settings**, under *Engine Executable Path*, set it to:

  ``C:\Users\Public\Documents\FLO-2D Pro\Documentation and Example Projects\Tailing Dam Workshop\Demo Engine\flo2d_XXX.exe``

- Ensure your export paths align with your working folders.

Now you're ready to proceed to the first lesson: **Computer Setup**.


.. toctree::
   :maxdepth: 1
   :caption: Contents

   1-Setup
   2-Grid
   3-Hydrology
   4-Channels
   5-Storm Drain
   6-Buildings
   7-Realtime
   8-Hydraulic
   9-Mapping
   10-Troubleshooting

