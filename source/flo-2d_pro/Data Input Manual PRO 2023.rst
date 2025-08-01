.. container::
   :name: page1-div

   |background image|
   O c t o b e r   2 0 2 3   -   B u i l d   2 3

.. container::
   :name: page2-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20231001.png

.. container::
   :name: page3-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20232002.png
   **PREFACE**

   **i**

   **FLO-2D INPUT DATA OVERVIEW**

   This manual describes the FLO-2D Pro Model data input param-

   eters and their format. The FLO-2D data base consists of a series of 

   ASCII files organized by model components.  A flood model starts 

   with routing a hydrograph over an unconfined floodplain surface.  

   This model can then be expanded with channel flow, levee or dam 

   breach or other components.  Flood simulation detail can be en-

   hanced by adding rainfall, infiltration, hydraulic structures, levees, 

   mudflows, sediment transport, rills and gullies, storm drains, build-

   ings and flow obstructions.  These components are initiated through 

   on-off switches found in the control data file (CONT.DAT).  If the 

   component options are “turned on”, then the appropriate data files 

   | must be created.
   | To conduct a basic FLO-2D flood simulation, eight data files must 

   be created.  These files can be generated using the FLO-2D Plugin 

   for QGIS.  The six required files for basic overland flow simulation 

   are:  

    · TOPO.DAT

    · MANNINGS_N.DAT

    · FPLAIN.DAT  

.. container::
   :name: page4-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20233003.png
   **ii**

   **P**

   **reface**

    · CADPTS.DAT  

    · CONT.DAT

    · TOLER.DAT

    · INFLOW.DAT

    · OUTFLOW.DAT

   There are two new data files in the Pro model to assist with GIS and 

   CADD program integration:  TOPO.DAT (coordinate data and el-

   evation) and MANNINGS_N.DAT (cell and roughness n-value).  

   These files can be used in lieu of the FPLAIN.DAT and CADPTS.

   DAT files.  The user is encouraged to start simple with a basic over-

   land flow simulation and build the flood detail into the model one 

   component at a time to observe the effects of each feature.  Pre-pro-

   cessor programs such as the QGIS/FLO-2D Plugin, Grid Developer 

   System (GDS), and PROFILES facilitate developing and graphically 

   | editing the data files.  
   | There are several ways to edit the FLO-2D data files.  Since the
     data 

   files are written in ASCII format, they can be edited in any ASCII 

   editor such as Microsoft NotePad®, TextPad®, UltraEdit®, and oth-

   ers.  The FLO-2D Plugin enables multiple selections of grid elements 

   to edit spatially variable data with mouse point and click
   commands.  

   The PROFILES program can be used to edit channel and cross section 

   | data.
   | There are two ways to run a FLO-2D simulation once the data files 

   are constructed.  1) The Pro model can be initiated from the FLO-2D 

   Plugin; or 2) a FLO-2D flood simulation can be started by copying 

   the FLOPRO.EXE file and its respective dlls into a project folder
   and 

   double-clicking on the executable.  When the model is running the 

   user has the option of graphically viewing the flood progression
   over 

   the grid system.  An inflow hydrograph and the rainfall temporally
   dis-

   tribution is also displayed.  Upon completion of the flood
   simulation, 

   there are post-processor programs (FLO-2D MapCrafter, MAPPER, 

   MAXPLOT, PROFILES, The QGIS Mesh tool, and HYDROG) that 

   will assist in reviewing the results. 

.. container::
   :name: page5-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20234004.png
   **iii**

   **D**

   **ata**

   ** I**

   **nPut**

   This Data Input Manual includes descriptions of the processor pro-

   grams, data variables and file format, and output files.  Each data
   file 

   description contains a list of variables, variable definitions and
   instruc-

   tional comments.  The instruction comments at the end of each file 

   description provide hints for data organization, range of data
   values 

   and data limitations.  For a discussion of the physical processes
   being 

   simulated please refer to the FLO-2D Reference Manual.

.. container::
   :name: page6-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20235005.png
   **iv**

   **t**

   **able**

   ** **

   **of**

   ** c**

   **ontents**

   **Contents**

   `FLO-2D INPUT DATA
   OVERVIEW ����������������������������������������������������������������������������������������������������������������������i <Data%20Input%20Manual%20PRO%202023-3.html>`__

   `Chapter 1  <Data%20Input%20Manual%20PRO%202023-11.html>`__

   `FLO-2D Installation and Getting
   Started  <Data%20Input%20Manual%20PRO%202023-11.html>`__

   `1 <Data%20Input%20Manual%20PRO%202023-11.html>`__

   `1�1 General ��������������������������������������������������������������������������������������������������������������������������������������������������������������1
   1�2  FLO-2D
   Installation ����������������������������������������������������������������������������������������������������������������������������������1
    <Data%20Input%20Manual%20PRO%202023-11.html>`__\ `1�3  Un-installing
   the FLO-2D
   Software ������������������������������������������������������������������������������������������������2
   1�4  Getting
   Started �������������������������������������������������������������������������������������������������������������������������������������������2
    <Data%20Input%20Manual%20PRO%202023-12.html>`__\ `1�5  Model
   Component
   Considerations ��������������������������������������������������������������������������������������������������7 <Data%20Input%20Manual%20PRO%202023-17.html>`__

   `Chapter 2  <Data%20Input%20Manual%20PRO%202023-19.html>`__

   `Creating and Editing with the
   GUI  <Data%20Input%20Manual%20PRO%202023-19.html>`__

   `9 <Data%20Input%20Manual%20PRO%202023-19.html>`__

   `2�1  FLO-2D
   Tutorials ����������������������������������������������������������������������������������������������������������������������������������������9
    <Data%20Input%20Manual%20PRO%202023-19.html>`__\ `2�2  FLO-2D
   Example Flood
   Simulations �����������������������������������������������������������������������������������������������13
    <Data%20Input%20Manual%20PRO%202023-23.html>`__\ `2�3  FLO-2D
   PowerPoint
   Presentations ������������������������������������������������������������������������������������������������14
   2�4  Other Help
   Documents �������������������������������������������������������������������������������������������������������������������������14
   2�5  Metric
   Option ���������������������������������������������������������������������������������������������������������������������������������������������14 <Data%20Input%20Manual%20PRO%202023-24.html>`__

   `Chapter 3  <Data%20Input%20Manual%20PRO%202023-27.html>`__

   `Pre-Processor
   Programs  <Data%20Input%20Manual%20PRO%202023-27.html>`__

   `17 <Data%20Input%20Manual%20PRO%202023-27.html>`__

   `3�1 Introduction �����������������������������������������������������������������������������������������������������������������������������������������������17
   3�2  QGIS FLO-2D
   Plugin ���������������������������������������������������������������������������������������������������������������������������������17
   3�3 GDS ���������������������������������������������������������������������������������������������������������������������������������������������������������������������17
    <Data%20Input%20Manual%20PRO%202023-27.html>`__\ `3�4 PROFILES ���������������������������������������������������������������������������������������������������������������������������������������������������������18 <Data%20Input%20Manual%20PRO%202023-28.html>`__

   `Chapter 4  <Data%20Input%20Manual%20PRO%202023-33.html>`__

   `Input Data File
   Description  <Data%20Input%20Manual%20PRO%202023-33.html>`__

   `23 <Data%20Input%20Manual%20PRO%202023-33.html>`__

   `4�1 General ������������������������������������������������������������������������������������������������������������������������������������������������������������23
    <Data%20Input%20Manual%20PRO%202023-33.html>`__\ `4�3  Data
   Files ��������������������������������������������������������������������������������������������������������������������������������������������������������24
    <Data%20Input%20Manual%20PRO%202023-34.html>`__\ `Data
   Files ���������������������������������������������������������������������������������������������������������������������������������������������������������������������25 <Data%20Input%20Manual%20PRO%202023-35.html>`__

   `CONT.DAT ..................................................................................................................................................27
    <Data%20Input%20Manual%20PRO%202023-37.html>`__\ `TOLER.DAT ...............................................................................................................................................37
    <Data%20Input%20Manual%20PRO%202023-47.html>`__\ `FPLAIN.DAT ..............................................................................................................................................41
    <Data%20Input%20Manual%20PRO%202023-51.html>`__\ `MANNINGS_N.DAT ................................................................................................................................44
    <Data%20Input%20Manual%20PRO%202023-54.html>`__\ `TOPO.DAT ..................................................................................................................................................46
    <Data%20Input%20Manual%20PRO%202023-56.html>`__\ `INFLOW.DAT .............................................................................................................................................48
    <Data%20Input%20Manual%20PRO%202023-58.html>`__\ `OUTFLOW.DAT ........................................................................................................................................53
    <Data%20Input%20Manual%20PRO%202023-63.html>`__\ `RAIN.DAT ...................................................................................................................................................58
    <Data%20Input%20Manual%20PRO%202023-68.html>`__\ `RAINCELL.DAT ........................................................................................................................................61 <Data%20Input%20Manual%20PRO%202023-71.html>`__

.. container::
   :name: page7-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20236006.png
   **v**

   **D**

   **ata**

   ** I**

   **nPut**

   `FLO2DRAINCELL.DAT .........................................................................................................................64
    <Data%20Input%20Manual%20PRO%202023-74.html>`__\ `RAINCELLRAW.DAT ...............................................................................................................................66
    <Data%20Input%20Manual%20PRO%202023-76.html>`__\ `INFIL.DAT ..................................................................................................................................................68
    <Data%20Input%20Manual%20PRO%202023-78.html>`__\ `EVAPOR.DAT ............................................................................................................................................77
    <Data%20Input%20Manual%20PRO%202023-87.html>`__\ `CHAN.DAT .................................................................................................................................................79
    <Data%20Input%20Manual%20PRO%202023-89.html>`__\ `CHANBANK.DAT ....................................................................................................................................89
    <Data%20Input%20Manual%20PRO%202023-99.html>`__\ `XSEC.DAT ...................................................................................................................................................91
    <Data%20Input%20Manual%20PRO%202023-101.html>`__\ `HYSTRUC.DAT ..........................................................................................................................................93
    <Data%20Input%20Manual%20PRO%202023-103.html>`__\ `SUBMERGE_FACTOR.DAT ............................................................................................................... 104
    <Data%20Input%20Manual%20PRO%202023-114.html>`__\ `STREET.DAT ........................................................................................................................................... 106
    <Data%20Input%20Manual%20PRO%202023-116.html>`__\ `ARF.DAT ................................................................................................................................................... 110
    <Data%20Input%20Manual%20PRO%202023-120.html>`__\ `MULT.DAT ............................................................................................................................................... 114
    <Data%20Input%20Manual%20PRO%202023-124.html>`__\ `SIMPLE_MULT.DAT ............................................................................................................................. 118
    <Data%20Input%20Manual%20PRO%202023-128.html>`__\ `SED.DAT ................................................................................................................................................... 121
    <Data%20Input%20Manual%20PRO%202023-131.html>`__\ `LEVEE.DAT ............................................................................................................................................ 130
    <Data%20Input%20Manual%20PRO%202023-140.html>`__\ `FPXSEC.DAT ........................................................................................................................................... 137
    <Data%20Input%20Manual%20PRO%202023-147.html>`__\ `BREACH.DAT ......................................................................................................................................... 140
    <Data%20Input%20Manual%20PRO%202023-150.html>`__\ `FPFROUDE.DAT ................................................................................................................................... 150
    <Data%20Input%20Manual%20PRO%202023-160.html>`__\ `SWMMFLO.DAT ..................................................................................................................................... 152
    <Data%20Input%20Manual%20PRO%202023-162.html>`__\ `SWMMFLORT.DAT ............................................................................................................................... 156
    <Data%20Input%20Manual%20PRO%202023-166.html>`__\ `SWMMOUTF.DAT ................................................................................................................................. 159
    <Data%20Input%20Manual%20PRO%202023-169.html>`__\ `SDCLOGGING.DAT ............................................................................................................................. 161
    <Data%20Input%20Manual%20PRO%202023-171.html>`__\ `SWMMFLODROPBOX.DAT ............................................................................................................... 163
    <Data%20Input%20Manual%20PRO%202023-173.html>`__\ `TOLSPATIAL.DAT................................................................................................................................. 165
    <Data%20Input%20Manual%20PRO%202023-175.html>`__\ `WSURF.DAT ............................................................................................................................................. 167
    <Data%20Input%20Manual%20PRO%202023-177.html>`__\ `WSTIME.DAT .......................................................................................................................................... 169
    <Data%20Input%20Manual%20PRO%202023-179.html>`__\ `TIMEDEPCELL.DAT ............................................................................................................................ 171
    <Data%20Input%20Manual%20PRO%202023-181.html>`__\ `SHALLOWN_SPATIAL.DAT .............................................................................................................. 173
    <Data%20Input%20Manual%20PRO%202023-183.html>`__\ `GUTTER.DAT ......................................................................................................................................... 176
    <Data%20Input%20Manual%20PRO%202023-186.html>`__\ `BUILDING_COLLAPSE.DAT ............................................................................................................ 180
    <Data%20Input%20Manual%20PRO%202023-190.html>`__\ `OUTRC.DAT ............................................................................................................................................ 182
    <Data%20Input%20Manual%20PRO%202023-192.html>`__\ `CHAN_INTERIOR_NODES.DAT .................................................................................................... 184
    <Data%20Input%20Manual%20PRO%202023-194.html>`__\ `BRIDGE_XSEC.DAT ............................................................................................................................ 186
    <Data%20Input%20Manual%20PRO%202023-196.html>`__\ `TAILINGS.DAT ...................................................................................................................................... 188 <Data%20Input%20Manual%20PRO%202023-198.html>`__

.. container::
   :name: page8-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20237007.png
   **vi**

   **t**

   **able**

   ** **

   **of**

   ** c**

   **ontents**

   `TAILINGS_CV.DAT .............................................................................................................................. 190
    <Data%20Input%20Manual%20PRO%202023-200.html>`__\ `TAILINGS_STACK_DEPTH.DAT .................................................................................................... 192
    <Data%20Input%20Manual%20PRO%202023-202.html>`__\ `LID_VOLUME.DAT .............................................................................................................................. 195 <Data%20Input%20Manual%20PRO%202023-205.html>`__

   `Chapter 5  <Data%20Input%20Manual%20PRO%202023-207.html>`__

   `Output Files and
   Options  <Data%20Input%20Manual%20PRO%202023-207.html>`__

   `198 <Data%20Input%20Manual%20PRO%202023-207.html>`__

   `5�1  Basic Guidelines for Using Output
   Files ��������������������������������������������������������������������������������� 198 <Data%20Input%20Manual%20PRO%202023-207.html>`__

   `Chapter 6  <Data%20Input%20Manual%20PRO%202023-251.html>`__

   `Post-Processor
   Programs  <Data%20Input%20Manual%20PRO%202023-251.html>`__

   `242 <Data%20Input%20Manual%20PRO%202023-251.html>`__

   `6�1 HYDROG  <Data%20Input%20Manual%20PRO%202023-251.html>`__

   ` ����������������������������������������������������������������������������������������������������������������������������������������������������� 242 <Data%20Input%20Manual%20PRO%202023-251.html>`__

   `6�3  FLO-2D
   MapCrafter ������������������������������������������������������������������������������������������������������������������������������ 247
    <Data%20Input%20Manual%20PRO%202023-256.html>`__\ `6�3  MAPPER
   Pro ����������������������������������������������������������������������������������������������������������������������������������������������� 249
   6�4   MAXPLOT
     �������������������������������������������������������������������������������������������������������������������������������������������������� 249
    <Data%20Input%20Manual%20PRO%202023-258.html>`__\ `6�5 PROFILES ������������������������������������������������������������������������������������������������������������������������������������������������������ 251 <Data%20Input%20Manual%20PRO%202023-260.html>`__

   `Chapter 7  <Data%20Input%20Manual%20PRO%202023-265.html>`__

   `Debugging and Trouble Shooting the Data
   Files  <Data%20Input%20Manual%20PRO%202023-265.html>`__

   `256 <Data%20Input%20Manual%20PRO%202023-265.html>`__

   `7�1  Troubleshooting
   Guidelines ���������������������������������������������������������������������������������������������������������� 256
    <Data%20Input%20Manual%20PRO%202023-265.html>`__\ `7�2  Trouble
   Shooting
   Technique  �������������������������������������������������������������������������������������������������������� 260
    <Data%20Input%20Manual%20PRO%202023-269.html>`__\ `7�3  List of
   Common Data
   Errors ����������������������������������������������������������������������������������������������������������� 261
    <Data%20Input%20Manual%20PRO%202023-270.html>`__\ `7�4  Runtime
   Errors ���������������������������������������������������������������������������������������������������������������������������������������� 262
    <Data%20Input%20Manual%20PRO%202023-271.html>`__\ `7�5  Debugging
   Errors ���������������������������������������������������������������������������������������������������������������������������������� 265
    <Data%20Input%20Manual%20PRO%202023-274.html>`__\ `7�6  Debug Output
   Tables ��������������������������������������������������������������������������������������������������������������������������� 270 <Data%20Input%20Manual%20PRO%202023-279.html>`__

   List of Tables

   `Table 1.1.  Grid System
   Size ..............................................................................................................4
    <Data%20Input%20Manual%20PRO%202023-14.html>`__\ `Table 2.1.
    English/Metric ............................................................................................................15
    <Data%20Input%20Manual%20PRO%202023-25.html>`__\ `Table 4.1.  List
   of \*.DAT Files and Unit
   Numbers ....................................................................25
    <Data%20Input%20Manual%20PRO%202023-35.html>`__\ `Table 4.2.  ARF
   Values Trigger
   Max ..........................................................................................113
    <Data%20Input%20Manual%20PRO%202023-123.html>`__\ `Table 4.3.  Cross
   Section Flow
   Direction ..............................................................................139 <Data%20Input%20Manual%20PRO%202023-149.html>`__

   `Table 5�1�  List of General \*�OUT Files and Unit
   Numbers ����������������������������������������������������������� 199
   Table 5�2�  List of 2-D Overland
   Output������������������������������������������������������������������������������������������������� 199
    <Data%20Input%20Manual%20PRO%202023-208.html>`__\ `Table 5�3�  List
   of 1-D Channel
   Output ��������������������������������������������������������������������������������������������������� 201
   Table 5�4�  List of Hydraulic Structures
   Output ���������������������������������������������������������������������������� 201
    <Data%20Input%20Manual%20PRO%202023-210.html>`__\ `Table 5�5�  List
   of Levee and Breach
   Output ���������������������������������������������������������������������������������������� 202
   Table 5�6�  List of Storm Drain
   Output ��������������������������������������������������������������������������������������������������� 202
   Table 5�7�  List of Multiple Channel
   Output �������������������������������������������������������������������������������������� 202 <Data%20Input%20Manual%20PRO%202023-211.html>`__

.. container::
   :name: page9-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20238008.png
   **vii**

   `D <Data%20Input%20Manual%20PRO%202023-212.html>`__

   `ata <Data%20Input%20Manual%20PRO%202023-212.html>`__

   ` I <Data%20Input%20Manual%20PRO%202023-212.html>`__

   `nPut <Data%20Input%20Manual%20PRO%202023-212.html>`__

   `Table 5�8�  List of Sediment Transport and Mudflow Output ������ 203
   Table 5�9�  List of Two Phase Flow
   Output  ���������������������������������������������� 203
    <Data%20Input%20Manual%20PRO%202023-212.html>`__\ `Table 5�10�  List
   of MODFLOW
   Output ������������������������������������������������������� 204
   Table 5�11�  List of \*�RHG Files and Unit
   Numbers �������������������������������� 204
    <Data%20Input%20Manual%20PRO%202023-213.html>`__\ `Table 5�12�  List
   of Batch Files and Unit Numbers �������������������������������� 205
   Table 5�13�  List of \*�TMP Files and Unit
   Numbers ��������������������������������� 205 <Data%20Input%20Manual%20PRO%202023-214.html>`__

   `Table 7.1   <Data%20Input%20Manual%20PRO%202023-265.html>`__

   `List of Misc Files and Unit
   Numbers �������������������������������������� 256 <Data%20Input%20Manual%20PRO%202023-265.html>`__

   `Table 7.2.  List of Common Data
   Errors ............................................ 262
    <Data%20Input%20Manual%20PRO%202023-271.html>`__\ `Table 7.3
     <Data%20Input%20Manual%20PRO%202023-273.html>`__

   `List of \*�CHK Files and Unit
   Numbers ����������������������������������� 264 <Data%20Input%20Manual%20PRO%202023-273.html>`__

   `Table 7.4.  Error Code
   Categories ..................................................... 270
    <Data%20Input%20Manual%20PRO%202023-279.html>`__\ `Table 7.5.  Basic
   Error
   Codes ............................................................... 273
    <Data%20Input%20Manual%20PRO%202023-282.html>`__\ `Table 7.6.
    Advanced Error
   Codes ....................................................... 282 <Data%20Input%20Manual%20PRO%202023-291.html>`__

.. container::
   :name: page10-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 20239009.png

.. container::
   :name: page11-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023100010.png
   **CHAPTER 1**

   **flo-2D I**

   **nstallatIon**

   ** **

   **anD**

   ** G**

   **ettInG**

   ** s**

   **tarteD**

   1

   **G**

   **ettin**

   **G**

   ** S**

   **tarted**

   **1.1 **

   **G**

   **eneral**

   Use this document to help create the FLO-2D input data and review the
   output 

   data.  It has chapters on getting started, resources, preprocessor
   programs, data 

   files, output files, post-processor programs and troubleshooting.
    Chapter 4 is 

   useful when learning to build data files.  It breaks down each data
   file into a set 

   | of variables and gives a definition and instructional comments for
     the data files.
   | FLO-2D is recommended for use with Windows 10 or higher with 64-Bit
     oper-

   ating systems, multiple processors and steady state hard drives.  To
   generate and 

   edit the data files, the QGIS/FLO-2D Plugin is used.  QGIS
   facilitates assigning 

   spatially variable data that can be interpolated from shape files,
   points and rasters.  

   PROFILES is used to edit channel geometry data.  Data files can also
   be edited 

   using an ASCII text editor such as UltraEdit© or NotePad++©.

   **1.2 **

   **flo-2D I**

   **nstallatIon**

   The FLO-2D Pro model has been compiled for 64 bit multi-core
   processor 

   computers. It cannot be run on a 32-bit computer. Recommended
   minimum 

   computer requirements are at least 4 GB RAM.  To install the FLO-2D
   on the 

   computer hard drive, unzip the installation file and double click the
   file FLO-2D-

   PRO-Setup.exe file.  Follow the installation instructions as they
   appear in the 

   dialog boxes on the screen.  The default directory is C:\\PROGRAM
   FILES(x86)\\

   FLO-2D PRO.  The FLO-2D model, and the processor programs are loaded
   into 

   the FLO-2D Pro folder.  The FLO-2D resource files are saved to the
   FLO-2D 

   Documentation folder under C:\\Users\\Public\\Public
   Documents\\FLO-2D PRO 

.. container::
   :name: page12-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023110011.png
   2

   **c**

   **haPter**

   ** 1**

   **G**

   **ettInG**

   ** s**

   **tarteD**

   Documentation.  These files include helpful resources such as user
   manuals, example 

   projects, lessons and PowerPoint presentations and instructional
   handouts. 

   **1.3 **

   **u**

   **n**

   **-**

   **InstallInG**

   ** **

   **the**

   ** flo-2D s**

   **oftware**

   Remove the FLO-2D program and all of its attendant software from the
   computer 

   with the Windows system Add Remove Programs tool.  When removing the model, 

   if the option appears to keep shared DLL/OCX files, do not remove
   them from the 

   computer. To completely remove the FLO-2D files, delete the FLO-2D
   Pro Folder 

   from the Program Files (x86).  

   **1.4 **

   **G**

   **ettInG**

   ** s**

   **tarteD**

   **Updates  **

   When starting a new FLO-2D project, first visit the Sharefile FTP
   and download 

   any executable updates. New features are frequently added to the
   model.  Do not 

   hesitate to notify FLO-2D Staff of any apparent programming bugs or problems 

   that are encountered.  These will be addressed as soon as possible.
    Program revisions 

   are listed in the FLO-2D Pro Model Revisions document.
   C:\\Users\\Public\\Docu-

   ments\\FLO-2D PRO Documentation\\flo_help\\Handouts

   **Tutorials and Lessons**

   Tutorials and training videos are available for the FLO-2D Plugin.  The Plugin is the 

   recommended data editor.

   C:\\users\\public\\public documents\\flo-2d pro documentation

   https://documentation.flo-2d.com

   **Seeking Assistance – Technical Support**

   Send technical support questions by e-mail to contact@flo-2d.com.  If
   there is a 

   specific problem that needs to be resolved, zip the data files (only
   the \*.DAT files, 

   no output files \*.OUT) and attach them to the e-mail along with a
   brief description 

   of the problem and the project.  Before sending the files, try to
   reduce the problem 

   to its simplest form by turning off all components that are not
   contributing to the 

   problem.  For example, if the problem involves channel
   volume conservation, turn 

   off the streets, buildings and levees and run the simulation again to
   determine if the 

   problem still persists.  Try to identify when the problem is first
   observed during the 

   simulation (review SUMMARY.OUT) so that it is not necessary to run
   the entire 

   simulation.

   Questions regarding a project application are considered to be
   technical consult-

   ing and outside the scope of data input
   technical support.  If assistance is needed 

   Hint: 

   When sending data files 

   for tech support, zip 

   together only \*.DAT 

   files and send them to 

   contact@flo-2.d.com

.. container::
   :name: page13-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023120012.png
   3

   **D**

   **ata**

   ** I**

   **nPut**

   **G**

   **ettin**

   **G**

   ** S**

   **tarted**

   on a project, reasonable consulting fees can be discussed to provide
   guidance and 

   oversight.  

   **Hydrology, Base Mapping and DTM Points**

   *DTM data*

   To start a FLO-2D model, define the project area and compile
   available 

   mapping, imagery and digital terrain model (DTM) data which might 

   consist of LiDAR data, point shape files, rasters, contour maps or
   digital 

   elevation model DEM data.  The imagery and DTM points must have the 

   same coordinate system.  The most common formats for digital imagery
   are 

   \*.tif, \*.sid and \*.jpg  files and the images must have
   corresponding world 

   files (e.g. \*.tfw, \*.sdw and \*.jgw).  If photogrametric or LiDAR
   data are not 

   available, DEM data can be used.  Elevation data formats that are
   accepted 

   by the QGIS/FLO-2D Plugin and GDS are ASCII Grid, ASCII xyz data 

   sets and ArcGIS elevation shapefiles and Elevation Raster GeoTiff
   files.  

   *Hydrologic data*

   Hydrologic data for a flood simulation can include both rainfall and
   dis-

   charge hydrographs.  The rainfall runoff from a watershed model can
   be 

   the desired product or the watershed model can be used to generate
   inflow 

   flood hydrographs for downstream flood routing.  In either case the
   hydro-

   logic data should be carefully reviewed because the area of
   inundation is 

   determined by the flood and rainfall volume. 

   *Floodplain and channel detail*

   If river channels, bridges, culverts, buildings and streets are to be
   simulated, 

   the user must be able to locate these features with respect to
   individual grid 

   elements.  Aerial imagery and shape files are used for this purpose.
    Ad-

   ditional data may be required for these components including bridge and 

   culvert rating curves or tables, streets width and curb height, and
   river cross 

   section surveys.

   **Estimate the project area**

   To create a computationally efficient model, it is best to minimize
   the grid system 

   around the project area.  The project computational domain (or grid
   system) can be 

   outlined using the aerial photography.  The grid system boundary should be located 

   so that the project area it is not affected by either inflow or
   outflow conditions. The 

   inflow and outflow nodes should be considered as non-essential nodes
   (sources and 

   | sinks) and these should be located away from the project area.  
   | If the project area is relatively small compared to the entire
     hydrologic basin that 

   may  need to be modeled, more than one FLO-2D simulation could be
   considered.  

   A coarse grid system can be established for watershed or river system and a more 

   Hint: 

   Use any ASCII editor 

   such as NotePad™ to edit 

   the data files.   

   Hint: 

   An alternate method to 

   run the model is to copy 

   the FLO.EXE file into the 

   project folder and double 

   click on it from a browser. 

.. container::
   :name: page14-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023130013.png
   4

   **c**

   **haPter**

   ** 1**

   **G**

   **ettInG**

   ** s**

   **tarteD**

   detailed grid system created for the local project area where flood
   detail may be im-

   portant.  The outflow from the course grid system will constitute the
   inflow to the 

   detailed grid system.  

   **Selecting the grid element size**

   See the FLO-2D Reference Manual for more instructions.  Once the
   overall project 

   area has been identified, estimate the grid system size (as a rough
   rectangle) and 

   determine the approximate number of grid elements that would be
   required for dif-

   ferent size square grid elements such as 50 ft, 100 ft, 200 ft, etc.
    The grid element 

   | size will control how fast the FLO-2D flood simulation will run.  
        
   | To help with the grid element size selection, the following criteria are suggested 

   based on a rough estimate of peak discharge.  The peak discharge Q

   peak

    divided by 

   the surface area of the grid element A

   surf

    should be in the range:

   Q

   peak

   /A

   surf 

   < 10.0 cfs/ft

   2

    

   or in metric:  

   Q

   peak

   /A

   surf

    < 0.3 cms/m

   2

    

   The closer Q

   peak

   /A

   surf

    is to 3.0 cfs/ft

   2

    (0.1 cms/m

   2

   ),  the faster the model will run.  If 

   the Q

   peak

   /A

   surf

    is much greater than 10.0 cfs/ft

   2

    or 0.3 cms/m

   2

   , the model will run 

   more slowly.  After the grid element size has been selected, proceed
   with establishing 

   the grid system using the QGIS/FLO-2D Plugin.  There are QGIS
   workshop lessons 

   to assist in getting started on a new project. 

   Table 1.1.  Grid System Size

   Number of 

   Grid Elements

   Model Simulation Speed

   < 50,000 

   Fast (minutes)

   50,000 – 250,000

   Moderate (<12 hours)

   250,000 – 1,000,000

   Slow (> 12 hours)

   > 1,000,000

   Very Slow (> 1 day)

.. container::
   :name: page15-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023140014.png
   5

   **D**

   **ata**

   ** I**

   **nPut**

   **G**

   **ettin**

   **G**

   ** S**

   **tarted**

   **Start simple, then add detail**

   The first flood simulation for any project will be a simple overland
   flow model upon 

   | which a more detailed flood simulation will be built.  
   | A suggested order of component construction is as follows:  

    ·

    Rainfall/Infiltration

    ·

    Channels

    ·

    Levees

    ·

    Streets 

    ·

    Buildings

    ·

    Hydraulic Structures (culverts, weirs and bridges)

    ·

    Storm Drains

    ·

    Multiple Channel (rills and gullies)

    ·

    Mud and debris flows/sediment transport 

   As new components are added to a model and tested, other components
   switches 

   | can be turned off in the CONT.DAT file. 
   | FLO-2D routes flows in eight directions as shown in the sidebar figure.  The four 

   compass directions are numbered 1 to 4 and the four diagonal
   directions are num-

   bered 5 to 8.  Some components such as levees are placed on
   boundaries of the grid 

   element.  The grid element boundaries constitute an octagon for
   components associ-

   ated with the boundary.

   **Saving data**

   When creating or editing the data files, it is suggested that the
   data files saved 

   frequently and that one folder for testing a project and another one
   for editing a 

   project.  It is suggested that the data files be saved after
   finishing each component.

   **Develop the Project Files**

   *Create a Project Folder*

   Start by creating a subdirectory for the project data files and
   import the 

   DTM data base files, map images and aerial photos. 

   *Build the Project Files*

   Use the QGIS/FLO-2D Plugin to graphically create and edit the grid
   sys-

   tem   Follow the QGIS Lesson 1 “Getting Started” lesson.   

   Hint: 

   Basic Data Files:

    

   ·

   FPLAIN.DAT

    

   ·

   CADPTS.DAT

    

   ·

   CONT.DAT

    

   ·

   TOLER.DAT

    

   ·

   TOPO.DAT

    

   ·

   MANNINGS_N.DAT

   Optional

    

   ·

   INFLOW.DAT 

    

   ·

   OUTFLOW.DAT

.. container::
   :name: page16-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023150015.png
   6

   **c**

   **haPter**

   ** 1**

   **G**

   **ettInG**

   ** s**

   **tarteD**

   *Run the FLO-2D model  *

   The required data files for a basic overland flood model are:

    ·

   FPLAIN.DAT

    ·

   CADPTS.DAT

    ·

   CONT.DAT

    ·

   TOLER.DAT

    ·

   INFLOW.DAT

    ·

   OUTFLOW.DAT

    ·

   TOPO.DAT

    ·

   MANNINGS_N.DAT

   The INFLOW.DAT and OUTFLOW.DAT files are optional but are typi-

   | cally necessary for most applications.  Run a FLO-2D simulation by:
      
   | i) QGIS - click on ‘

   Run FLO-2D’  

   command in the File menu.

   ii) Copy the ‘

   FLOPRO.EXE

   ’  file in the project folder and double click it.

   **Some General Guidelines**

   *Data Input*

   When the data format appears confusing, review the data files
   provided in 

   the Example Projects subdirectory of the FLO-2D  folder using an ASCII 

   editor such as NotePad++©.  

   *File Management*

   The output files are always generated with the same name and will be over-

   written  in subsequent model runs.  To save any output files that
   could 

   be overwritten, rename the file or create a new project folder, copy
   all the 

   \*.DAT files into it and then run the new flood simulation in that
   folder.

   *Graphics Mode*

   To view the floodwave progression during the simulation, run the
   simula-

   tion in graphics mode.  This switch is set in the QGIS/FLO-2D Plugin
   by 

   clicking the Control Variables button.  Then check the Graphics
   Display 

   mode and the Run button.

   Things to check when creating the data files:

   *Grid System*

   The grid system should begin with grid element #1 and have no
   missing 

   grid element numbers. There should be no dangling grid elements con-

   nected only by a diagonal. 

   Hint: 

   Test initial model runs with 

   a simple steady state inflow 

   hydrograph.

.. container::
   :name: page17-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023160016.png
   7

   **D**

   **ata**

   ** I**

   **nPut**

   **G**

   **ettin**

   **G**

   ** S**

   **tarted**

   *Inflow/Outflow Nodes*

   Inflow and outflow nodes should not have other components assigned
   to 

   them such as hydraulic structures, streets, ARF’s, etc. Outflow nodes
   should 

   not be doubled up.   Use a single line of outflow nodes.  

   **1.5 **

   **M**

   **oDel**

   ** c**

   **oMPonent**

   ** c**

   **onsIDeratIons**

   **Channel Modeling **

   The 1-D channel component can simulate flow in channels defined by
   various ge-

   ometries.  The flow shares between the channel banks and the
   floodplain.  Channels 

   are defined in FLO-2D whenever 1-D flow is more accurate than
   overland flow.  

   They can reduce flooding and help the water move downstream mare
   quickly than 

   flow on the floodplain.  An extensive Channel Guidelines document is
   available in 

   | the Manuals Folder.  C:\\users\\Public\\Public Documents\\FLO-2D
     Pro Documenta-
   | tion\\flo_help\\Manuals.

   **Street Flow **

   Streets may convey or store only a small portion of the total flood
   volume, but may 

   be important for distributing the flow to remote areas of the grid
   system.  Street flow 

   is simulated as a shallow rectangular channel with curbs.  Street
   width and n-values 

   are spatially variable.  Streets are important to flood distribution
   in urban areas.

   **Levees, Dams and Breach**

   Levees and levee failure can be an important detail for floodplain
   projects.  Levees 

   are assigned to grid element boundaries with a crest elevations.
   Levee failure can in-

   clude piping, overtopping and collapse. There is a levee and dam
   erosion component 

   in FLO-2D.  An extensive Levee, Dam, and Wall Breach document
   is available in 

   the Manuals folder.  C:\\Users\\Public\\Documents\\FLO-2D PRO
   Documentation\\

   flo_help\\Manuals\\Levee Dam and Wall Breach Guidelines.pdf

   **Rainfall and Infiltration on Alluvial Fans**

   Alluvial fan surfaces can be as large as the upstream watershed.  Fan
   rainfall can 

   contribute a volume of water on the same order of magnitude as the
   inflow flood 

   hydrograph at the fan apex.  Infiltration losses can also
   significantly effect flood-

   wave attenuation.  Infiltration losses can be calibrated by adjusting
   the hydraulic 

   conductivity.  Spatial variable hydraulic conductivity can be
   assigned in the QGIS/

   FLO-2D Plugin.

   Hint: 

   The channel bank on each 

   side of the rive can have 

   a unique elevation.  If 

   the two bank elevations 

   are different, the model 

   automatically assigns the 

   channel into two elements 

   even if the channel  would 

   fit into one grid element.

.. container::
   :name: page18-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023170017.png
   8

   **c**

   **haPter**

   ** 1**

   **G**

   **ettInG**

   ** s**

   **tarteD**

   **Sediment Bulking of Flood Hydrographs**

   An alluvial fan will have geomorphic features that identify the
   watershed potential 

   for generating mudflows.  For mudflow simulation, sediment
   concentration can be 

   assigned in the INFLOW.DAT file.  For desert alluvial fans with a
   sand bed, sedi-

   ment concentrations in flood events can reach 15% by volume.  For
   concentrations 

   less than 20% by volume, the flow will behave like a water flood.
    The primary effect 

   of increasing the sediment concentration, in this case, is to bulk
   the flow volume.  

   | Simulating Mudflow Guidelines is avaliable in the Handouts folder. 
   | C:\\Users\\Public\\Documents\\FLO-2D PRO
     Documentation\\flo_help\\Handouts\\
   | Simulating Mudflow Guidelines.pdf.

.. container::
   :name: page19-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023180018.png
   **CHAPTER 2**

   **flo-2D h**

   **elP**

   ** r**

   **esources**

   9

   **R**

   **esou**

   **R**

   **ces**

   **2.1 **

   **flo-2D t**

   **utorIals**

   **Tutorials**

    

   There are several workshop lessons located in the FLO-2D
   Documentation subdi-

   rectory. 

   **QGIS/FLO-2D Plugin Lessons**

   **Access lessons here: https://documentation.flo-2d.com/**

   *QGIS Lesson 1 – Getting Started*

   Part 1 of this lesson is setting up the
   grid and assinging elevation, roughness 

   | and saving the project.
   | Part 2 of this lesson shows the user how to build recovery and
     backup files.
   | Part 3 of this lesson shows the user how to add inflow nodes, assign rainfall 

   and add infiltration.

   *QGIS Lesson 2 – Channels, Culverts *

   This lesson outlines the process of setting up channels, hydraulic
   structures 

   and in QGIS using the FLO-2D Plugin.

   *QGIS Lesson 3 – Storm Drain Urban*

   This lesson outlines the process of converting a storm drain network
   from 

   shapefile into a FLO-2D Storm Drain system in QGIS using the FLO-2D 

.. container::
   :name: page20-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023190019.png
   10

   **c**

   **haPter**

   ** 2**

   Plugin.

   *QGIS Lesson 4 – Buildings and Walls*

   This lesson shows the user how to set up buildings and walls using
   QGIS 

   and the FLO-2D Plugin.

   *QGIS Lesson 5 – Realtime Rainfall*

   This lesson outlines the process of generating realtime rainfall data for each 

   cell in QGIS using the FLO-2D Plugin.

   *QGIS Lesson 6 – Hydraulic Structures*

   This lesson outlines the process to create culverts using rating
   tables in 

   QGIS with the FLO-2D Plugin.

   **QGIS Advanced Training**

   *Advanced Training Module 1 – Project Recovery and Debug*

   This lesson outlines the process create a recovery file and use the
   Debug 

   tools in QGIS with the FLO-2D Plugin.

   *Advanced Training Module 2 – Advanced Hydraulic Structures*

   Part 1.  This lesson outlines the process create generalized culvert
   equations 

   | in QGIS with the FLO-2D Plugin.  It expands on QGIS Lesson 6.
   | Part 2.  This lesson outlines the process to create a bridge using
     QGIS with 

   the FLO-2D Plugin.

   *Advanced Training Module 3 – Prescribed Dam Breach*

   This advanced training module explores the watershed that connects to
   a 

   flood and debris basin.  It shows how to define a reservoir node,
   create the 

   Levee component to represent the detintion dam, and define the breach.  It 

   also explains how to change the elevation around the dam so that the
   breach 

   can proceed.  The lesson shows how to create a riser inlet for low
   flow dis-

   charge.  It also has extensive information on potential issues that
   stem from 

   breach modeling. 

   *Advanced Training Module 5 – Watershed Mudflow Modeling*

   | Part 1.  This lesson shows how to set up a watershed rainfall
     model.
   | Part 2.  This part of the lesson shows how to convert the watershed
     model 

   into a mudflow model and run the mudflow out of a canyon, over an al-

   luvial fall and into an urban area.

   *Advanced Training Module 6 – Erosion Dam Breach*

   In this tutorial, an erosion dam breach with failure is created.  The
   reservoir 

   is filled to the breach elevaiton with a reservoir node.  The
   bathymetric 

.. container::
   :name: page21-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023200020.png
   11

   **D**

   **ata**

   ** I**

   **nPut**

   **R**

   **esou**

   **R**

   **ces**

   elevations is also known.

   *Advanced Training Module 7 – Tailings Dam Tool*

   In this tutorial, use QGIS and the tailings dam tool to create a
   tailings dam 

   failure.

   *Advanced Training Module 8 – Advanced Storm Drain Modeling*

   This lesson will outline how to construct a storm drain network that
   is ready 

   for FLO-2D Plugin to process.  Add data to a storm drain network.

   *Advanced Training Module 9 – Advanced Storm Drain Modeling*

   This lesson will outline how to construct a storm drain network
   that is 

   ready for FLO-2D Plugin to process.  Use QGIS to process a storm
   drain 

   network.

   **GDS Lessons - Available with the GDS-Mapper Installation**

   *Lesson 1 – GDS Getting Started*

   This lesson demonstrates how to create a FLO-2D grid system from a
   digi-

   tal terrain model (DTM points) using the Grid Developer System.  

   *Lesson 2 – GDS Spatially Variable Attributes*

   This lesson describes how to graphically edit the FLO-2D component
   at-

   tributes with the GDS.  Part 1 covers general floodplain attributes
   such as 

   n-values and elevation.  Part 2 covers urban features such as
   streets, levees, 

   ARF and WRF values and infiltration. The tutorial uses a small
   project with 

   an aerial photo to illustrate editing the component data files.

   *Lesson 3 – Basic Channel *

   This lesson provides instruction on creating the CHAN.DAT file from 

   scratch.  It facilitates selection of the grid elements for a channel
   and assign-

   ment of channel parameters using aerial photo images as background.

   *Lesson 4 – HEC-RAS Conversion*

   In this lesson, a HEC-RAS cross section data file is automatically converted 

   to a FLO-2D XSEC.DAT cross section file.

   *Lesson 5 – Profiles*

   This lesson explains how to interpolate channel slope and geometry
   using 

   the PROFILES program.  It will simplify getting the CHAN.DAT and 

   XSEC.DAT files prepared for the model simulation.  

   *Lesson 6 – MAPPER Pro*

   This lesson describes how to view FLO-2D data results in MAPPERPro
   and 

   how to manipulate the mapping layers.  It also covers creating
   exclusion 

.. container::
   :name: page22-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023210021.png
   12

   **c**

   **haPter**

   ** 2**

   polygons, hazard maps, damage assessment and layer editing.  

   *Lesson 7 – Rain/Infiltration *

   This lesson shows how to input global and spatially variable
   Green-Ampt 

   and SCS curve number infiltration parameters and how to set up and
   run a 

   simple rain fall simulation using total rainfall and a percent
   distribution.

   *Lesson 8 – Natural Channel using HEC-RAS Data *

   In this lesson a HEC-RAS channel and cross section data is overlaid
   onto a 

   FLO-2D grid system.  The steps required to create a FLO-2D natural
   chan-

   nel data base from HEC-RAS data are followed.

   *Lesson 9 – Hydraulic Structures *

   This lesson outlines the process of creating several hydraulic
   structures using 

   the GDS.

   *Lesson 10 – Levees, Walls and Berms *

   This is an advanced workshop lesson which shows how to create lateral
   ob-

   structions such as levees and walls using the levee tool in the GDS.

   *Lesson 11 – Streets and Buildings *

   For this lesson streets and buildings are created in an urban
   environment.  It 

   uses the polyline street tool and a buildings shapefile.

   *Lesson 12 – Dam Breach Modeling*

   The procedure for setting up a dam breach erosion model is presented
   in 

   this lesson.

   *Lesson 13 – Multi-Domain Interface (Outflow to Inflow) *

   This lesson prepares the outflow discharge hydrograph from one grid
   system 

   as the inflow hydrograph to another grid system and describes how to
   set up 

   the outflow nodes that will automatically capture the upstream grid
   system 

   hydrograph.   The two models must overlap at the boundary.

   *Lesson 14 – Advanced Natural Channel*

   This lesson outlines the complete process for setting up a natural
   chan-

   nel.  It is a comprehensive channel development guide.  This lesson
   brings 

   together several ideas from Lessons 3, 4, 5 and 8.  It also gives the
   user an 

   guidelines on finalize the channel and prep it for calibration.

   *Lesson 15 – Prescribed Levee Breach*

   This lesson outlines the process of setting up and testing simple levee pre-

   scribed breach criteria and performing test runs.

   *Lesson 16 – Simple Storm Drain*

   Hint: 

   Review the Example 

   Project data files that are 

   similar in concept your 

   project.

.. container::
   :name: page23-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023220022.png
   13

   **D**

   **ata**

   ** I**

   **nPut**

   **R**

   **esou**

   **R**

   **ces**

   This lesson outlines the process of setting up and testing simple
   storm drain 

   using GDS and EPA SWMM 5.0.

   **2.2 **

   **flo-2D e**

   **xaMPle**

   ** f**

   **looD**

   ** s**

   **IMulatIons**

   A number of example projects are provided in
   the FLO-2D Documentation/Ex-

   ample Projects subdirectory.  To run these projects, either load them
   in the GDS 

   or run them the project folder (first make sure that the FLOPRO.
   EXE file is in the 

   project subdirectory and double click on the FLOPro.exe name).  Most of the ex-

   ample simulations are setup for the graphics mode and will take only
   a few minutes 

   to run.   

   *Working with Geo-referenced Images – Goat Camp Creek, Gila County,
   Ari-*

   *zona (Goat subdirectory)*

   This project provides an opportunity to work with the GDS editor
   compo-

   nents and capabilities.  The aerial photos can be imported and used
   to edit 

   the various model components such as channels, streets, ARF’s and
   WRF’s, 

   and levees.  This flood simulation includes channel overbank flow
   from a 

   small river through an urban area. 

   *Large River Flooding – Rio Grande, New Mexico (Rio Grande
   subdirectory)*

   Over 173 miles of the Middle Rio Grande is simulated using surveyed 

   channel cross section data.    The river floodplain is confined by
   levees 

   along most of its length.  Use this flood simulation to review the
   data input 

   in the XSEC. DAT and CHAN.DAT files and river-floodplain discharge 

   exchange.  

   *Urban Watershed Flooding  – Waikiki Beach, Oahu, Hawaii (Alawai
   subdi-*

   *rectory)*

   This urban flooding example includes street flow and numerous
   buildings. 

   Alawai Canal runs through the center of the project area and is open
   to the 

   ocean.  Excess rainfall runs off steep watersheds and enters channels
   that 

   join the canal system in Waikiki beach.  The Alawai Canal is nearly
   flat and 

   is filled with water from the ocean at the start of the simulation.  

   *Urban Fan and Mudflow Simulation - Barnard Creek, Utah (BARN
   subdirec-*

   *tory)*

   An example mudflow simulation is provided for an urbanized alluvial
   fan 

   (Barnard Creek) near Centerville, Utah.  This model simulates a
   mudflow 

   debouching from a small watershed ravine onto a very steep alluvial
   fan 

   with numerous streets and buildings.  The mudflow enters the grid
   sys-

   tem at a debris basin, flows down a steep street and spreads out into the 

   Hint: 

   Copy the following 

   Processor Programs into 

   a project folder.  Double 

   click the executable name 

   to run the program:

    

   ·

   FLO.EXE

    

   ·

   PROFILES.EXE

    

   ·

   MAXPLOT.EXE

    

   ·

   HYDROG.EXE

.. container::
   :name: page24-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023230023.png
   14

   **c**

   **haPter**

   ** 2**

   residential area.  The mudflow is viewed overflowing the street,
   entering 

   side streets and developed lots and becoming more fluid as the
   floodwave 

   progresses downslope. Buildings have been simulated to account for
   the loss 

   of storage and flow redirection. The mudflow simulation includes
   variable 

   sediment concentration and the computation of viscosity and yield
   stresses.  

   This flood simulation is a good example to review for mudflow,
   buildings 

   and streets.

   *Ocean Storm Surge/Tsunami Model in an Urban Area – Waikiki Beach, *

   *Oahu, Hawaii (Alawai-Tsunami subdirectory)*

   By assigning stage-time relationships to the outflow elements along
   the Wai-

   kiki coast line, the Alawai watershed model is converted to an ocean
   storm 

   surge or tsunami model.  A high water surface elevation is specified
   for the 

   coastal elements for a short duration.  This results in a rapid
   progression of 

   the ocean storm surge over the urban area.  The ocean surge enters
   streets 

   and the Alawai Canal in the center of the city.  The model demonstrates the 

   application of the FLO-2D model to simulate the overland progression
   of 

   hurricane storm surges or tsunami waves in urban areas.  

   *Urban Shallow Flooding - Urban Project Example*

   Small isolated portion of a large urban study.  This project has
   examples of 

   trapezoidal channels, culvert, walls, buildings, urban n-values and a
   simple 

   storm drain system.  

   *Sediment Transport - Sediment Transport Channel Example*

   Fully functional example of sediment transport routing in a 1-D
   channel.  

   **2.3 **

   **flo-2D P**

   **ower**

   **P**

   **oInt**

   ** P**

   **resentatIons**

   These presentations discuss most of the FLO-2D components.  The files
   can be 

   found in FLO-2D Pro Documentation\\flo_help\\PowerPoint
   Presentations.

   **2.4 **

   **o**

   **ther**

   ** h**

   **elP**

   ** D**

   **ocuMents**

   Several documents in the FLO-2D Handout folder provide advanced model
   guid-

   ance and discussion of specific components and model techniques.
    They can be 

   found in FLO-2D Pro Documentation\\flo_help\\Handouts.

   **2.5 **

   **M**

   **etrIc**

   ** o**

   **PtIon**

   The user can choose either the English or Metric system of units (for
   the Metric 

   system set METRIC = 1 in the CONT.DAT file).  When using the Metric
   system, 

.. container::
   :name: page25-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023240024.png
   15

   **D**

   **ata**

   ** I**

   **nPut**

   **R**

   **esou**

   **R**

   **ces**

   substitute the appropriate metric unit for the English unit in the
   data files. The fol-

   lowing basic units are used in the model:

   Manning’s n-Value is considered an Imperial number and it is not
   necessary to con-

   vert it for Metric or English units.  The conversion is part of the
   calculation.

   Table 2.1.  English/Metric

   Variable

   English

   Metric

   discharge

   cfs

   m

   3

   /s (cms)

   depth

   ft

   m

   hydraulic conductivity

   inches/hr

   mm/hr

   rainfall and abstraction

   inches

   mm

   soil suction

   inches

   mm

   velocity

   fps

   mps

   volume

   acre-ft

   m

   3

    (cm)

   viscosity

   dynes-s/cm

   2

   dynes-s/cm

   2

   yield stress

   dynes/cm

   2

   dynes/cm

   2

.. container::
   :name: page26-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023250025.png
   [16]

   This page is intentionally Blank.

.. container::
   :name: page27-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023260026.png
   **CHAPTER 3**

   **P**

   **re**

   **-P**

   **rocessor**

   ** P**

   **roGraMs**

   17

   **P**

   **re**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   **3.1 **

   **I**

   **ntroDuctIon**

   There are two pre-processor programs to help to create or edit the FLO-2D data 

   files:  QGIS Plugin, and PROFILES.  Tutorials and workshop lessons
   for some of 

   the programs’ functions are available in the FLO-2D/flo_help
   subdirectory. A dis-

   cussion of the commands in the PROFILES program is included in this
   manual.    

   **3.2 **

   **QGIs flo-2D P**

   **luGIn**

   The FLO-2D Plugin for
   Quantum Geographical Interface System (QGIS) is a 

   program developed to generate FLO-2D data files using QGIS.  This
   program has 

   separate documentation available in the FLO-2D Documentation
   subdirectory.  

   Tutorials and sample projects are available at
   https://documentation.flo-2d.com.

   **3.3 **

   **GDs**

   The grid developer system (GDS) is a GIS program used to create and
   edit the 

   FLO-2D grid system and its attributes.  As of October 2023, the GDS
   and Map-

   per are now distributed separately from FLO-2D.  These tools are
   aging and their 

   Visual Basic code has an unknown life limit via Microsoft.  If a user
   requires these 

   tools, they can be downloaded via the FLO-2D Shafefile account.  The
   GDS has 

   a separate reference manual.  In addition, there are a number of GDS
   tutorials 

   and workshop lessons that are available in the FLO-2D
   Documentation\\flo_help 

   subdirectory.  

.. container::
   :name: page28-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023270027.png
   **18**

   **c**

   **haPter**

   ** 3**

   **P**

   **re**

   **-P**

   **rocessors**

   **3.4 **

   **ProfIles**

   The PROFILES processor program displays the channel slope and permits
   interac-

   tive adjustment of the channel bed elevation, channel depth, channel
   n-values and 

   channel geometry.  It will display the channel cross section geometry
   and interpo-

   late the slope and cross section geometry between surveyed cross
   sections.  PRO-

   FILES can also be used to view output water surface profiles (see the
   Post-Processor 

   Programs Section).  To run PROFILES, access the program from the GDS
   File 

   | menu or copy the PROFILES.EXE to the project folder and double
     click it.
   | Before using the PROFILES program, the basic FLO-2D files plus the
     CHAN.

   DAT file have to be created.  The XSEC.DAT will also have to be
   created if sur-

   veyed cross section data will be used.  The general procedure for
   using the PRO-

   FILES program is as follows:

   | 1.  Create the six basic FLO-2D data files.
   | 2.  Develop the XSEC.DAT file for surveyed cross section data if
     necessary.  
   | 3.  Complete the channel data file (CHAN.DAT) based on rectangular,
     trap-

   ezoidal or surveyed (natural) cross sections.

   4.  For surveyed cross sections, identify the channel element cross
   section 

   number XSECNUM in the CHAN.DAT file to represent the cross sec-

   tion.  All other XSECNUM’s will be assigned a zero ‘0’ value.

   | 5.  Run the PROFILES program from the GDS or Explorer.  
   | 6.  The model bed slope can be compared with surveyed bed
     elevations by 

   developing the WSURF.DAT file.

   7.  Save data in PROFILES using the Save menu.  This option is
   activated 

   after an edit has been made.  The save option allows for two
   datasets.  The 

   data can be overwritten or saved as new.  The data is not written to
   file until 

   PROFILES is closed.

   Initially the PROFILES program will display a blank screen with a
   Main Menu 

   showing options to ‘View Segment Bed Slope’ or ‘Interpolate Segment
   Slope/

   Shape’.  

   Hint: 

   To quickly access the 

   PROFILES program, 

   copy the executable 

   PROFILES.EXE into 

   the project folder and 

   double click on it.

   Hint: 

   When assigning cross 

   section numbers to the 

   CHAN.DAT file, make 

   sure all channel elements 

   that are not associated 

   with a surveyed cross sec-

   tion have XSECNUM 

   values of 0.

.. container::
   :name: page29-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023280028.png
   **19**

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **re**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   **Interpolating a New Channel with Surveyed Cross Sections**

   To interpolate the cross sections and slope and assign a cross
   section to every channel 

   element in PROFILES, use the ‘Interpolate Segment Slope/Shape’ menu
   option as 

   follows:

   1.  Select a channel segment from the list provided in the
   dialog box shown in 

   the sidebar.  If there is only one channel segment, the interpolation
   will be 

   completed directly. Note that before interpolation, the channel slope
   profile 

   may look like a stair case because only the surveyed cross sections
   define the 

   channel profile at this point.  Following interpolation the slope
   profile will 

   be more representative of the actual river profile.

   2.  PROFILES will automatically locate the surveyed cross section
   data and 

   interpolate the cross section geometry and elevation (thalweg slope)
   for all 

   those channel elements between the surveyed cross sections within the
   seg-

   ment.  The following dialog box will appear indicating that the original 

   cross sections have been renamed with a prefix ‘X-’ before each cross
   section 

   name.

   3.  Click ‘OK’ in the dialog box to view the interpolated bedslope. 

   4.  Click on the ‘View Local Reach’ button on the menu bar.  Click
   anywhere 

   along the bedslope profile to zoom in on a local reach of 10 channel
   ele-

   ments.

.. container::
   :name: page30-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023290029.png
   **20**

   **c**

   **haPter**

   ** 3**

   **P**

   **re**

   **-P**

   **rocessors**

   5.  Click on ‘View/Edit Cross Section Data’ to view the following
   dialog box 

   displaying the channel element characteristics: 

   Note: 

   Refer to the Workshop 

   Lesson PROFILES tuto-

   rial for a more detailed 

   example of this procedure.

.. container::
   :name: page31-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023300030.png
   **21**

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **re**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   6.  Click on the  ‘Xsec’ button in the dialog box to view the cross
   section data 

   and image. 

   7.  View additional cross sections by clicking on the “Up” and “Down”
   but-

   tons in the dialog box.  The computed cross section geometry and all
   the 

   cross section station and elevation data can be reviewed and edited.
    Edit 

   the channel and cross section data by adding or deleting stations and
   eleva-

   tions, revising the Manning’s n-value, or raising or lowering
   the entire cross 

   section.

   8.  Interpolate bedslope and or channel geometry.  Identify the
   Upstream and 

   Downstream channel elements in the group boxes labeled ‘Slope and
   Xsec-

   tion Interpolation’.  Use ‘Up’ and ‘Down’ buttons to locate one of
   the 

   surveyed cross sections and then type in the other either upstream or
   down-

   stream channel elements.  There may be several channel elements
   between 

   two cross sections selected for interpolation.  Click on either the
   ‘Slope 

   Only’ or ‘Shape/Slope’ buttons to interpolate either the channel bed slope 

   or slope and the cross section shape.  The cross section geometry is
   linearly 

   interpolated according to top width and distance and is adjusted for
   the 

   weighted flow area.  One cross section is overlaid on the other cross
   section, 

   stretched or contracted and the elevations averaged.    

   9.  Save the results frequently by clicking on ‘Save’ on the menu
   bar.  The saved 

   data will not be written to file until the program is closed.  

   10.  NOTE:   Perform the initial channel interpolation of the cross
   sections 

   automatically in the GDS or QGIS.

   Hint: 

   When interpolating be-

   tween two cross sections, 

   they must be entered in 

   order from upstream to 

   downstream..

.. container::
   :name: page32-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023310031.png
   [22]

   This page is intentionally Blank.

.. container::
   :name: page33-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023320032.png
   **CHAPTER 4**

   **I**

   **nPut**

   ** D**

   **ata**

   ** f**

   **Ile**

   ** D**

   **escrIPtIon**

   23

   **D**

   **ata**

   ** F**

   **iles**

   **4.1 **

   **G**

   **eneral**

   The FLO-2D data file variables and format are described in this
   chapter.  These 

   files are accessed directly by the model.  For each data file a list
   of the variables, a 

   portion of an example data file, and an alphabetical description of
   the variables are 

   presented.  Some instructional comments follow the variable
   descriptions for clari-

   | fication.  QGIS or any ASCII text editor can be used to create or
     edit the data files.  
   | All of the data entries, integers (i) or real numbers (r) are in free format space de-

   limited. The ID characters (letters)
   are case sensitive.  The variables are listed line by 

   line and each line may contain several variables that are highlighted
   by bold text and 

   capital letters.  Array variables are indexed as shown in the
   following example from 

   the INFLOW.DAT file, Line 3:

   Line 3

   **  HYDCHAR = ‘H’, HP(I,J,1), HP(I,J,2), HP(I,J,3)**

   *I = 1, J = 1, Number of inflow hydrograph pairs*

   where: 

   I and J (array indices) represent element number and hydrograph pair;

   **H(I,J,1)**

    = time (hrs) start of the discretized interval of inflow hydrograph;

   **H(I,J,2)**

    = discharge (cfs);

   **H(I,J,3)**

    = mudflow sediment concentration by volume inflow hydrograph.

   **HDYCHAR**

    is a line identifier character ‘H’. 

   The variables in Line 3 on the INFLOW.DAT file represent one line of
   a discretized 

   inflow hydrograph that is repeated for each of the hydrograph pairs
   for each inflow 

   grid element.  The Line 3 data for the first four time steps is as
   follows: 

.. container::
   :name: page34-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023330033.png
   24

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   INFLOW.DAT Variable Example

    

   **HP(J,1)    HP(J,2)          HP(J,3)**

   | Time       Discharge       Sediment Conc.
   |   (hrs)         (cfs)             % by Volume
   |    0.0            0.0                   0.00
   |    0.1          10.0                   0.00
   |    0.2          25.0                   0.20
   |    0.3          50.0                   0.25

   Backup files of the data files (\*.BAC) can be created when program
   reads the data.  

   The backup option is invoked by a switch (IBACKUP) in the CONT.DAT
   file. 

   **4.2 **

   **l**

   **Ist**

   ** **

   **of**

   ** P**

   **roGraM**

   ** f**

   **Ile**

   ** u**

   **nIts**

   The following table lists the data and output file (‘Unit’) numbers
   that are assigned 

   by the FLO-2D model at runtime.  These unit numbers may be reported
   in error 

   messages and referring to these numbers may help to locate input data
   errors.

   **4.3 **

   **D**

   **ata**

   ** f**

   **Iles**

   Four data files are required for every flood simulation:  CONT.DAT,
   TOLER.

   DAT, FPLAIN.DAT, CADPTS.DAT. The INFLOW.DAT and OUTFLOW.

   DAT files are optional, but typically are necessary for a FLO-2D
   flood simulation.  

   The CADPTS.DAT is not listed.  Although, it is required for every flood simulation, 

   this file is automatically created by the FLO-2D Plugin and QGIS and
   does not 

   require editing.   The TOPO.DAT and MANNINGS_N.DAT files are generated 

   by the Plugin QGIS and the FLO-2D Pro model at runtime.  The TOPO.DAT and 

   MANNINGS_N.DAT files replace the FPLAIN.DAT and CADPTS.DAT file (are 

   obsolete and not necessary but can still be used).

.. container::
   :name: page35-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023340034.png
   25

   **D**

   **ata**

   ** I**

   **nPut**

   TABLE 4.1.  LIST OF \*.DAT FILES AND UNIT NUMBERS

   **File
   No.**

   **File Name**

   **File
   No.**

   **File Name**

   9

   TOLER.DAT

   250

   BREACH.DAT

   10

   CADPTS.DAT

   287

   BUILDING_COLLAPSE.DAT

   30

   CONT.DAT

   300

   BATCHCYCLE.DAT

   31

   FPLAIN.DAT

   311

   MANNINGS_N.DAT

   32

   RAIN.DAT

   312

   CURBHEIGHT.DAT

   33

   INFIL.DAT

   381

   SIMPLE_MULT.DAT

   34

   INFLOW.DAT

   391

   SCOURDEP_SPATIAL.DAT

   36

   CHAN.DAT

   673

   SUBMERGE_FACTOR.DAT

   37

   ARF.DAT

   850

   BRIDGE_XSEC.DAT

   38

   MULT.DAT

   908

   BRIDGE_COEFF_DATA.DAT

   39

   SED.DAT

   1119

   CHAN_INTERIOR_NODES.

   DAT

   50

   OUTFLOW.DAT

   1556

   SWMMFLODROPBOX.DAT

   52

   STREET.DAT

   1557

   SWMMFLO.DAT

   57

   LEVEE.DAT

   1558

   SWMM.RAIN

   68

   HYSTRUC.DAT

   1559

   SWMMFLORT.DAT

   85

   XSEC.DAT

   1562

   SWMMOUTF.DAT

   89

   RAINCELL.DAT

   1568

   SDCLOGGING.DAT

   95

   EVAPOR.DAT

   1575

   SWMM.INP

   **D**

   **ata**

   ** f**

   **Iles**

.. container::
   :name: page36-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023350035.png
   26

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   TABLE 4.1.  LIST OF \*.DAT FILES AND UNIT NUMBERS

   97

   TOPO.DAT

   1600

   TOLSPATIAL.DAT

   98

   OUTRC.DAT

   1608

   SHALLOWN_SPATIAL.DAT

   119

   CHANBANK.DAT

   1609

   GUTTER.DAT

   120

   FPXSEC.DAT

   1651

   QGISDEBUG.DAT

   125

   FPFROUDE.DAT

   1709

   NEIGHBORS.DAT

   162 - 

   170

   CADPTS_DS1-9.DAT

   2200

   TAILINGS.DAT

   171 - 

   179

   INFLOW1-9_DS.DAT

   2201

   TAILINGS_CV.DAT

   180

   WSTIME.DAT

   2401

   LID_VOLUME.DAT

   211

   TIMDEPCELL.DAT

   2903

   TAILINGS_STACK_DEPTH.

   DAT

   230 FLO2DRAINCELL.DAT

   231

   RAINCELLRAW.DAT

.. container::
   :name: page37-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023360036.png
   27

   **D**

   **ata**

   ** I**

   **nPut**

   CONT.DAT File Variables

   24.0  0.10  2  0  0 

   Line 1: 

   **SIMULT  TOUT  LGPLOT  METRIC  IBACKUP**

   1  1  0  0  0 

   Line 2: 

   **ICHANNEL  MSTREET  LEVEE  IWRFS  IMULTC**

   0  1  0  0  0   0   0 

   Line 3: 

   **IRAIN  INFIL  IEVAP  MUD  ISED  IMODFLOW**

   **  **

   ** **

   **SWMM**

   0  0  0 

   Line 4: 

   **IHYDRSTRUCT  IFLOODWAY  IDEBRV**

   0.000 0.0 0.0 0.30 0.70 0.150  

   Line 5: 

   **AMANN  DEPTHDUR  XCONC  XARF  FROUDL**

    

   ** **

   ** **

   **SHALLOWN  ENCROACH**

   2  3.0   

   Line 6: 

   **NOPRTFP  DEPRESSDEPTH**

   2   

   Line 7: 

   **NOPRTC**

   0  0.0 

   Line 8: 

   **ITIMTEP  TIMTEP   STARTTIMTEP   ENDTIMTEP**

   0.1 

   Line 9: 

   **GRAPTIM**

   Notes:

   Line 5:  If IFLOODWAY = 0 omit ENCROACH

   Line 7:  If ICHANNEL = 0 omit Line 7

   Line 8:  If ITIMTEP = 5 TIMEDEPCELL.DAT is required

   Line 8:  If ITIMTEP = 11, 21, 31, 41, or 51 add STARTTIMTEP and
   ENDTIMTEP

   Line 9:  If LPLOT = 0 omit Line 9

   CONT.DAT File Example

   24.0  0.10  2  0  0

   1  1  0  0  0 

   0  1  0  0  0  0  0

   0   0   0

   0.000  0.0  0.0  0.30  0.70  0.150 

   2 3.0 

   2

   0  0.0

   0.1

   FILE:  CONT.DAT  

   SYSTEM CONTROL DATA

.. container::
   :name: page38-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023370037.png
   28

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   CONT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT RANGE

   DESCRIPTION

   AMANN

   **r**

   **0**

   **  -1 to 1**

   **-99 > 1.0**

   Increments the floodplain Manning’s n roughness coefficient 

   at runtime.  

   | If AMANN is 0, n = n
   | If the ABS(AMANN) < 1, n = n + AMANN (positive or 

   | negative)  
   | If the AMANN >  1, n = n \* AMANN (positive)
   | If the AMANN < -1,  n =  n \* (1 + AMANN)  where 

   | AMANN is negative
   | After AMANN is applied, the shallow n is applied
   | If AMANN is -99  no depth integrate n-value adjustment 

   and no adjustment for exceeding Courant number.

   DEPRESSDEPTH

   **r**

   **-110.0 to **

   **10.0**

   The DEPRESSDEPTH variable has two functions:

   1.  DEPRESSDEPTH identifies depressed grid elements that 

   are lower than all contiguous nodes.  A value of DEPRESS-

   DEPTH  = 3.0 ft is suggested.  Depressed elements may be 

   real, but in most cases isolated depressed elements are a result 

   of poor topographic data. 

   2.  Identifies low levee crst elevations.  A typical value of 

   DEPRESSDEPTH  3.0 (default value if zero).  

    (see comments 11 and 12).

   DEPTHDUR

   **r**

   **0.01 - 100**

   **0.003 - 30**

   Flow depth (ft or m) for a depth-duration analysis.  When a 

   flow depth greater than DEPTHDUR is computed, the time 

   duration of inundation for that grid element is tracked and 

   reported in the DEPTHDUR.OUT file (see comment 8). 

   ENCROACH

   **r**

   **0 - 10**

   **0 - 3**

   The floodway encroachment increase in flow depth (ft or m). 

   The IFLOODWAY switch must be set to 1 and a previous 

   FLO-2D simulation must be completed for the project to 

   generate the maximum water surface elevations. 

.. container::
   :name: page39-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023380038.png
   29

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   CONT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT RANGE

   DESCRIPTION

   ENDTIMTEP

   **r**

   The end time for the delayed time series output data (hours).  

   Should be greater than STARTTIMTEP and up to SIMUL.  

   To shorten the timeseries output, set the value to a lower 

   time limit than SIMUL.

   FROUDL

   **r**

   **0 - 5**

   Limiting Froude number for overland flow.  When 

   FROUDL is exceeded, the floodplain n-value is increased 

   by 0.001 for that grid element for the next timestep (see 

   comment 3).  The increased n-values are reported in the 

   ROUGH.OUT and FPLAIN.RGH files (see comments 3 

   and 4).

   GRAPTIM

   **r**

   **0.01 - 10.**

   Time interval in hours that the graphics display is updated 

   (e.g. set GRAPTIM = 0.02 for a frequent update).  GRAPH-

   TIM is required when LGPLOT = 2.  This variable will not 

   affect the file output data time interval (TOUT).  The graph-

   ics mode is limited to a 48-day inflow hydrograph.

   IBACKUP

   **s**

   **0 = off**

   **1 = on**

   **2**

   IBACKUP = 1 creates a backup file of all the data files with 

   a \*.BAC extension for data error troubleshooting.  It also 

   enables the model to be resumed following termination from 

   the last output interval. IBACKUP = 2 enables elevation 

   changes for outflow nodes made at runtime to be perma-

   nently written to the FPLAIN.RGH file (see comment 10).

   ICHANNEL

   **s**

   **0 = off**

   **1 = on**

   If ICHANNEL = 1, the channel component will be used 

   and the CHAN.DAT must be created (comments 1 and 6).

   IDEBRV

   **s**

   **0 = off**

   **1 = on**

   Set IDEBRV = 1 if a debris basin volume should be filled 

   before routing the flow hydrograph.

   IEVAP

   **s**

   **0 = off**

   **1 = on**

   Set IEVAP = 1 if simulating free water surface evaporation 

   from overland or channel flow.

   IFLOODWAY

   **s**

   **0 = off**

   **1 = on**

   If FLOODWAY =1, a floodway analysis will be performed 

   in the subsequent FLO-2D simulation.  An initial FLO-2D 

   flood simulation must be completed prior to a floodway 

   simulation (see comment 5).

.. container::
   :name: page40-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023390039.png
   30

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   IHYDRSTRUCT

   **s**

   **0 = off**

   **1 = on**

   Set IHYDRSTRUCT = 1 to simulate hydraulic structures 

   either on the floodplain or in the channel. The HYSTRUC.

   DAT file must be created.

   IMULTC

   **s**

   **0 = off**

   **1 = on**

   Set IMULTC = 1 to simulate multiple channel (rill and gully 

   flow) rather than overland sheet flow between multiple chan-

   nel elements.  The MULT.DAT file must be created.

   IMODFLOW

   **s**

   **0 = off**

   **1 = on**

   Set IMODFLOW = 1 to simulate surface-groundwater 

   exchange.  This switch initiated the linked MODFLOW 

   groundwater model a during the FLO-2D simulation.

   INFIL

   **s**

   **0 = off**

   **1 = on**

   INFIL = 1 initiates an infiltration subroutine using the 

   Green-Ampt infiltration model for either channel or over-

   land infiltration.  The INFIL.DAT file must be created.

   IRAIN

   **s**

   **0 = off**

   **1 = on**

   Set IRAIN = 1 to simulate rain on the grid system.  The 

   RAIN.DAT file must be created (see comment 1).

   ISED

   **s**

   **0 = off**

   **1 = on**

   If ISED = 1, the sediment transport routine will be used.  

   The SED.DAT file must be created.

   ITIMTEP

   **s**

   **0 = off**

   **1, 2, 3, 4, 5, **

   **and 6 = on**

   **11, 21, 31, **

   **41, 51 = **

   **on for an **

   **interval**

   0 = No time series output is written.

   1 = TIMDEP.OUT and TIMDEP_NC4.out are written.

   2 = TIMDEP.HDF5 files is written.

   3 = TIMDEPNC.HDF5 file is written.

   4 = All time series output is written.

   5 = Extract a time series for specific cells. Requires TIMDEPCELL.DAT

   11 = TIMDEP.OUT and TIMDEP_NC4.OUT are written for the time 

   interval.

   21 = TIMDEP.HDF5 files is written for the time interval.

   31 = TIMDEPNC.HDF5 file is written for the time interval.

   41 = All time series output is written for the time interval.

   51 = Extract a time series during the time interval for specific
   cells. Requires 

   TIMDEPCELL.DAT

   IWRFS

   **s**

   **0 = off**

   **1 = on**

   IWRFS = 1 specifies that area and width reduction factors 

   (ARFs and WRFs) will be assigned in the ARF.DAT file.

   LEVEE

   **s**

   **0 = off**

   **1 = on**

   Set LEVEE = 1 to simulate levees.  The LEVEE.DAT file 

   must be created.

   Variable Descriptions for the 

   CONT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page41-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023400040.png
   31

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   LGPLOT

   **s**

   **0 = text**

   **1 = batch**

   **2 = graphic**

   LGPLOT = 0 will display screen text scrolling the simulation 

   | time, minimum timestep and volume conservation. 
   | LGPLOT = 1 will display nothing.  Use this switch position 

   | with batch runs.
   | LGPLOT = 2 displays the graphical floodwave progression 

   over the grid system (flow depth) and inflow hydrograph.

   METRIC

   **s**

   **0 = English**

   **1 = Metric**

   METRIC = 0 for English units and METRIC = 1 for the 

   metric system of units.

   MSTREET

   **s**

   **0 = off**

   **1 = on**

   MSTREET = 1 to initiate the street flow component.  The 

   STREET.DAT file must be created (see comment 2).

   MUD

   **s**

   **0 = off**

   **1 = on**

   Set MUD = 0 for clear water and MUD = 1 for hyper-

   concentrated sediment flow.  If MUD = 1 the sediment 

   load (volume or concentration by volume) for either the 

   floodplain hydrograph HP(I,J,3) or the channel hydrograph 

   H(I,J,3) must be assigned to each inflow hydrograph pair 

   (comments 1 and 3).  The SED.DAT file must be created.

   NOPRTC

   **s**

   **0, 1 or 2**

   | If NOPRTC = 0, the BASE.OUT channel data is reported.  
   | If NOPRTC = 1, the BASE.OUT channel outflow data is 

   | not reported.
   | If NOPRTC = 2, the BASE.OUT file is not reported.

   NOPRTFP

   **s**

   **0, 1, 2 or 3**

   If NOPRTFP = 0, the BASE.OUT floodplain flow data is 

   | reported. 
   | If NOPRTFP = 1, the BASE.OUT floodplain outflow data 

   | is not reported. 
   | If NOPRTFP = 2, BASE.OUT is not written.  This reduces 

   | the time for writing model output.
   | If NOPRTFP = 3, only floodplain outflow data is reported 

   to the BASE.OUT file.

   SHALLOWN

   **r**

   **0 = off**

   **0.1 - 0.99**

   Flow roughness n-value for shallow overland flow (flow 

   depth < 0.2 ft or 0.06 m) (see comment 9).

   Variable Descriptions for the 

   CONT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page42-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023410041.png
   32

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   SIMUL

   **r**

   **0.01 - **

   Simulation time (hours).

   STARTIMTEP

   **r**

   **0 to  **

   **ENDTIM-**

   **TEP **

   Start time for the time series output data (hours).  Set this 

   value to any time 0 to ENDTIMTEP.  It should represent 

   the delayed start of time dependant data.

   SWMM

   **s**

   **0 = off**

   **1 = on**

   SWMM = 1 initiates the FLO-2D storm drain model.

   TIMTEP

   **r**

   **0 - 100**

   Output interval (hrs) that the flow depth, resolved velocity, 

   x-velocity, y-velocity and water surface elevation datasets are 

   reported to the TIMDEP.OUT file for a post-simulation 

   flood animation.  TIMTEP should be a multiple of TOUT.  

   The switch ITIMTEP is required.

   TOUT

   **r**

   **0.01 - 24.**

   Output interval (hrs) that hydraulic data is reported to the 

   various output files \*.OUT.

   XARF

   **r**

   **0. - 1.**

   Global area reduction factor applied to all grid elements.  

   This factor reduces the grid element surface area available for 

   flood volume storage.  XARF can be used to account irregu-

   lar surface topography, dense vegetation or other features.   

   Range:  0 < XARF < 1.  A typical value for XARF of 0.10 

   indicates that 10% of each grid element surface is not avail-

   able for flood storage.  The XARF value is overridden by the 

   ARF variable specified for the individual grid elements in the 

   ARF.DAT file.  Assign XARF = 0. to flood the entire surface 

   area of the grid elements.

   XCONC

   **r**

   **0 - 0.60**

   Volumetric concentration to bulk the inflow discharge hy-

   drograph (channel or floodplain).  For example, set XCONC 

   = 0.20 for a concentration of 20% by volume.  This will 

   account for sediment bulking without initiating the hyper-

   concentrated sediment transport routine.  If simulating clear 

   water flooding, set XCONC = 0.  If MUD = 2, XCONC is 

   the global mudflow or tailings sediment concentration by 

   volume. 

   Variable Descriptions for the 

   CONT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page43-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023420042.png
   33

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments 

   CONT.DAT File

   These instructions will aid in assigning of the CONT.DAT file
   parameters:

   1.  If any of the switches MUD, ISED, IRAIN, IMULT, INFIL, MSTREET, 

   LEVEE, ICHANNEL, IWRFS, IMODFLOW, SWMM or IHYDRSTRUCT 

   are set to 0 “off”, then the corresponding data file can be omitted.
    For example, 

   set MSTREET = 0 and the STREET.DAT file can be omitted.  

   2.  Streets, groundwater, mudflow, levees, and rill and gully flow
   can be simulated 

   with or without a channel.  

   3.  Supercritical flow is uncommon on alluvial surfaces and may be
   inhibited by 

   sediment entrainment.  There are three possible approaches to a high
   Froude 

   number flow analysis:

   | a.  Allow supercritical flow and do not limit the Froude number.
   | b.  Increase the grid element roughness by assigning AMANN or
     setting higher 

   individual grid element n-values to reduce the Froude number (assign
   spa-

   tially variable n-values).

   c.  Set the Limiting Froude number or the floodplain (e.g. set FROUDL
   = 

   0.99 or 1.11). When FROUDL is exceeded the grid element roughness 

   value will be increased by 0.001 for the next timestep.  After a
   flood simula-

   tion, review ROUGH.OUT to determine where FROUDL was exceeded 

   and the maximum n-values for that cell were computed.  Consider
   revis-

   ing the n-values in the MANNINGS_N.DAT file to match those in the 

   ROUGH.OUT file.  This will ensure that FROUDL is not exceeded. Re-

   name the MANNINGS_N.RGH file to MANNINGS_N.DAT.

   d.  Spatially variable limiting Froude numbers can also be assigned
   to indi-

   vidual grid elements in FPFROUDE.DAT.

   e.  The shallow n-value is off when SHALLOWN = 0. or when AMANN = 

   -99.   The limiting Froude number is off if you set FROUDL = 0. for
   the 

   floodplain.  AMANN= -99 turns off the depth variable n-value, but not
   the 

   limiting Froude number n-value adjustments.

   4.  The floodwave travel time should be reviewed to determine if it
   is appropriate.  

   The travel time can also be used to calibrate the n-values.
    Adjusting n-values 

   with FROUDL will slow the arrival of the frontal wave.  During the
   hydro-

   graph recessional limb when the Froude number is less than 0.5 and
   the flow is 

   shallow, the n-value decreases by 0.0005 until the original n-value
   is reached

   5.  IFLOODWAY initiates the floodway routine.  Flow will not be
   exchanged 

   between floodplain grid elements unless the maximum water surface
   plus the 

.. container::
   :name: page44-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023430043.png
   34

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   encroachment depth (ENCROACH) from a previous FLO-2D simulation is 

   exceeded.    An initial FLO-2D simulation is required to establish
   the maxi-

   mum water surface elevations.  See the Floodway discussion in the
   Reference 

   Manual component section.

   6.  If channel flow is simulated (ICHANNEL = 1), then the
   NOPRTC variable 

   must be set in CONT.DAT.  In addition, channel outflow control can be
   as-

   signed in OUTFLOW.DAT.

   7.  ITIMTEP will enable a simple animation (time and space output) of
   the over-

   land flow to be displayed in Mapper, MAXPLOT or other map
   software.  The 

   animation will be based on a time interval TIMTEP specified by the
   user.  

   8.  The depth duration analysis is used to determine how long a
   floodplain grid 

   element is inundated at a flow depth greater than the DEPTHDUR
   variable.  

   If DEPTHDUR = 1 ft, the output file DEPTHDUR.OUT has the total du-

   ration in hours that the depth exceeded 1 ft.  The results can be reviewed in 

   MAXPLOT.  If the depth duration analysis is activated, then a second
   output 

   file DEPTHDURATION2.OUT is generated for the cumulative time dura-

   tion above 2 ft (0.61 m).  

   9.  To improve the timing of the floodwave progression through the
   grid system, a 

   depth variable roughness can be assigned.  The basic equation for the
   grid ele-

   ment roughness n

   d

    as function of flow depth is:

   n

   d

    = n

   b

    \*1.5 \* e 

   -(0.4 depth/dmax)

   where:

   n

   b

    =  bankfull discharge roughness 

   depth = flow depth

   dmax = flow depth for drowning the roughness elements and vegetation 

   (hardwired 3 ft or 1 m)

   This equation prescribes that the variable depth floodplain roughness
   is equal 

   to the assigned flow roughness for complete submergence of all
   roughness ele-

   ments (assumed to be 3 ft or 1 m).  This equation is applied by the
   model as a 

   default and the user can turn ‘off’ the depth roughness adjustment
   coefficient 

   for all grid elements by assigning AMANN = -99.  This roughness
   adjustment 

   will slow the progression of the floodwave.  It is valid for flow
   depths ranging 

   from 0.5 ft (0.15 m) to 3 ft (1 m).   For example, at 1 ft (0.3 m),
   the computed 

   roughness will be about 1.31 times the assigned roughness for a flow depth 

   of 3 ft. Assigning a ROUGHADJ value may reduce unexpected high
   Froude 

   numbers.  

.. container::
   :name: page45-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023440044.png
   35

   **D**

   **ata**

   ** I**

   **nPut**

   The following rules apply:

   0.0 < flow depth < 0.2 ft (0.06 m) 

   n = SHALLOWN value

   | 0.2 ft (0.06 m) < flow depth < 0.5 ft (0.15 m)  n = SHALLOWN/2.
   | 0.5 ft (0.15 m) < flow depth < 3 ft (1 m) 

   n = n

   b

    \*1.5 \* e

   -(0.4 depth/dmax)

   3 ft (1 m) < flow depth 

   n = n-value in  

    MANNINGS_N.DAT

   10.  The IBACKUP = 1 switch is used to create a backup file with an
   \*.BAC exten-

   sion.  The\*.BAC files can be reviewed to see if the model is
   correctly reading 

   the data.  This is a data file format troubleshooting tool.  These
   files can be 

   renamed to \*.DAT and the model can be run with them. IBACKUP = 1
   will 

   also generate a series of binary files that represent the model
   results at the last 

   output interval. The binary files are overwritten at the end of each
   output inter-

   val so if the model is terminated prior to the end of the run for any
   reason, the 

   simulation can be restarted from the last interval. Setting the
   switch to 1 can 

   significantly lengthen the model run time.  Setting IBACKUP = 2 will
   write all 

   elevation changes associated with the outflow nodes and channel
   top-of-bank 

   | revisions to the FPLAIN.RGH file which can be renamed to the
     FPLAIN.DAT 
   | file to run the model. 

   11.  The DEPRESSDEPTH parameter can be
   used to either identify depressed ele-

   ments or low levee crest elevations.  Set SIMUL = 0.01 hrs for
   separate val-

   ues for each filter.   Set DEPRESSDEPTH = 3.0 ft to  review the
   depressed 

   elements in the DEPRESSED_ELEMENTS.OUT ﬁle, rename the file and 

   reassign DEPRESSDEPTH to 1.0 ft or so and rerun the model to
   generate 

   LOW_LEVEE\_ CREST_ELEVATIONS.OUT ﬁle.

   12.  If a grid element is lower than every neighboring  cell, to the
   depth of DE-

   PRESSDEPTH, the grid element is considered to be a topographical
   depres-

   sion and a probable error.   The grid element is listed in
   DEPRESSED_ELE-

   MENTS.OUT file.

   13.  DEPRESSDEPTH is also used to identify levees that have a low
   crest elevation.   

   A levee  or wall that is only 0.1 ft above the ground is
    superfluous.  The low 

   levee warning message and action has three options:

   a.  DEPRESSDEPTH = 0.0 to 10.0 ft; Identifies the wall with a crest 

   elevation lower than DEPRESSDEPTH in LOW_LEVEE_CREST\_

   ELEVATIONS.OUT file.

   b.  DEPRESSDEPTH = -1.0 to - 10.0 ft; Assesses the side of the wall 

   where the crest elevation is assigned to
   determine if the levee height is 

   lower than the DEPRESSDEPTH value.

.. container::
   :name: page46-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023450045.png
   36

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   c.  DEPRESSDEPTH = -101.0 to -110.0 ft; Assesses both sides of the 

   wall to determine if the height is lower than DEPRESSDEPTH (1 ft 

   to 10 ft).

   d. 

   If  DEPRESSDEPTH  is  negative,  LEVEE.BAC  file  is  written  as  a 

   backup file omitting the low levees that can be renamed as LEVEE.

   DAT.

.. container::
   :name: page47-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023460046.png
   37

   **D**

   **ata**

   ** I**

   **nPut**

   TOLER.DAT File Variables

   0.1  0.00   

   Line 1: 

   **TOLGLOBAL   DEPTOL**

   C  0.6   0.6   0.6

   ** **

   **Line 2:   COURCHAR = ‘C’   COURANTFP   COURANTC **

   **  **

   ** **

   **COURANTST**

   T   0.1

   ** **

   **Line 3:  COURCHAR = “T”   TIME_ACCEL**

   TOLER.DAT File Example

   0.1  0.00

   C   0.6   0.6   0.6

   T   0.1

   FILE:  TOLER.DAT

   NUMERICAL STABILITY CONTROL DATA

.. container::
   :name: page48-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023470047.png
   38

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   TOLER.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   COURANTC

   **r**

   0.2 - 0.9

   Courant number for channels.  Courant-Friedrich-Lewy 

   numerical stability parameter that relates the floodwave 

   movement in channels to the discretized model in space and 

   time (see comments 3 thru 5).

   COURANTFP

   **r**

   0.2 - 0.9

   Courant number for floodplain.  Courant number for 

   floodplain.  Numerical stability parameter that relates the 

   floodwave movement for overland flow to the discretized 

   model in space and time (see comments 3 thru 5).

   COURANTST

   **r**

   0.2 - 0.9

   Courant number for streets.  Courant number for floodplain.  

   Numerical stability parameter that relates the floodwave 

   movement  in streets to the discretized model in space and 

   time. (see comments 3 thru 5).

   COURCHAR

   **c**

   C, T

   Character ‘C’ that identifies Line 2 with the Courant stabil-

   ity parameter.  This variable is case sensitive.  It must be 

   upper case.

   DEPTOL

   **r**

    

   0.1 - 0.5

   Tolerance value for the percent change in the flow depth for 

   a given timestep.  When a given element DEPTOL is ex-

   ceeded, the timestep will be reduced.  If DEPTOL = 0, then 

   the timestep is governed by the Courant numerical stability 

   criteria.  It is recommended that DEPTOL only be used for 

   specific ponded flow conditions where the Courant number 

   is ineffective (see comment 2).

   TIME_ACCEL

   **r**

   0.1 to 2

   Coefficient to increase the rate of incremental timestep 

   change.  Default value = 0.1  A value of 0.1 may result in a a 

   more stable simulation time.   A value of 0.2 or higher may 

   result in a faster simulation.

   TOLGLOBAL

   **r**

   0.004 - 0.5

   typ

   0.0012 - 

   0.03

   Surface detention.  TOLGLOBAL is a minimum value of 

   the flow depth for flood routing.  A typical value river flood-

   ing is 0.10 ft (see comment 1).  Use a small value for rainfall 

   runoff (0.004 ft to 0.10 ft; 0.0012 m to 0.030m).  

.. container::
   :name: page49-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023480048.png
   39

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   TOLER.DAT File

   1.  The TOLGLOBAL value prescribes the flow depth for a floodplain or channel 

   grid element below which no flood routing will be performed.
    TOLGLOBAL 

   is analogous to a depression storage rainfall abstraction.  The
   TOLGLOBAL 

   value for streets is hardwired (0.03 ft or 0.01 m).   TOLSPATIAL is
   another 

   variable that can be assigned to any cell.  The TOLSPATIAL variable
   will re-

   place TOLGLOBAL if assigned.  See TOLSPATIAL tab for futher instruc-

   tions.

   2.  DEPTOL controls the percent change in grid element or channel
   flow depth 

   for a given timestep.  It is
   a generic control that eliminates further analysis of 

   the numerical stability criteria. DEPTOL affects the computer runtime
   and 

   flow depth resolution.  The Courant is the primary numerical
   stability control.  

   For some models with ponded flow, the water surface and velocities
   for low 

   n-value may exhibit numerical instability.  Using or decreasing DEPTOL will 

   reduce the timestep and, improve the numerical stability and result
   in longer 

   computational times.  Setting DEPTOL = 0 dictates that only the Courant 

   criteria will be applied for numerical stability.  

   3.  To identify numerical instability, review the CHANMAX.OUT file
   and the 

   HYDROG program hydrograph plots for hydrograph spikes.  Review MAX-

   PLOT or Mapper or the VELTIMEFP.OUT file to determine if floodplain 

   velocities are too high. 

   4.  If the model is unstable, reduce the appropriate Courant number
   by 0.1 in suc-

   cessive runs until the Courant number reaches 0.2.

   5.  Using the Courant criteria, the timestep Δt is limited by:

    

   Δt = C Δx / (

   β

   V 

   + 

   c) 

       

   where:

   C is the Courant number (C ≤ 1.0)

   Δx is the square grid element width

   V is the computed average cross section velocity

   β

    is a coefficient (e.g. 5/3 for a wide channel) but is seldom used

   c is the computed wave celerity

   The Courant coefficient C may vary from 0.2
   to 0.9 depending on the size of 

   the grid element and floodwave velocity.  If C is set to 1.0,
   artificial or numerical 

   diffusivity is assumed to be zero. A typical value of the Courant
   number is 0.6 to 

   0.7.   Start with the default value of 0.6. 

.. container::
   :name: page50-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023490049.png
   40

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Use the following approach to improve numerical stability:

    ·

   Initially run the model with the Courant numbers = 0.6.   If the
   model 

   is unstable, reduce the appropriate Courant number by 0.1 increments
   in 

   successive runs until the Courant number reaches 0.2.  

    ·

   Run the model with an appropriate limiting Froude number (e.g. 

   FROUDL in CONT>DAT = 0.9 subcritical flow on an alluvial surface).  

   This will calibrate the model n-values for reasonable Froude numbers.

    ·

   Review the maximum velocities in VELTIMEC.OUT, VELTIMEFP.

   OUT and VELTIMEST.OUT (or in MAXPLOT or Mapper) and the 

   maximum Froude numbers in SUPER.OUT to determine the location of 

   any inappropriate high velocities related to numerical surging and
   increase 

   the n-values in the vicinity of the grid elements with high
   velocities.

    ·

   Review the n-values in ROUGH.OUT and MANNINGS_N.DAT.  Make 

   n-value adjustments in MANNINGS_N.DAT based on exceedingly high 

   n-values in ROUGH.OUT then replace MANNINGS_NDAT with 

   MANNINGS.RGH.

    ·

   Run the simulation and repeat steps 3 and 4 making adjustments to 

   MANNINGS_N.DAT until ROUGH.OUT is essentially empty. A few 

   incremental n-value changes will not affect the simulation.  Make
   adjust-

   ments to FROUDL to decrease the number of n-value adjustments.

   6.  Increase the model speed:

    ·

   Increase the Courant numbers in 0.1 increments until C = 0.9.

    ·

   Increase the TIME_ACCEL parameter in TOLER.DAT in 0.1 increments 

   to increase the computational timesteps increments.

    ·

   Review the model numerical stability with the maximum velocity and 

   Froude number output files.  Decrease the TIME_ACCEL parameter if 

   unreasonable increases in the maximum velocity and Froude number are 

   reported.

    ·

   Review the computational runtime in the SUMMARY.OUT file and bal-

   ance the increased Courant numbers and TIME_ACCEL parameter to 

   achieve the best runtime.  This may require only an increase
   in TIME_AC-

   CEL.

.. container::
   :name: page51-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023500050.png
   41

   **D**

   **ata**

   ** I**

   **nPut**

   FPLAIN.DAT File Variables

   1 0 2 10 0 

   0.060  4005.23  Line 

   1: 

   **DUM   FP(I, J)   FP(I, 5)   FP(I, 6)**

   2 0 3 11 1 

   0.065  4008.65  Line 

   1: 

   **DUM   FP(I, J)   FP(I, 5)   FP(I, 6)**

   3 0 4 12 2 

   0.065  4002.23  Line 

   1: 

   **DUM   FP(I, J)   FP(I, 5)   FP(I, 6)**

   ...

   ...

   ...

   18 

   9 0 27 17  0.065  4010.78  Line 

   1: 

   **DUM   FP(I, J)   FP(I, 5)   FP(I, 6)**

   Note:  FPLAIN.DAT is a list of the grid element and its bordering
   grid elements.  Zeros indicate 

   boundary elements.

   FPLAIN.DAT File Example

   1 0 2 10 0 

   0.060  4005.23

   2 0 3 11 1 

   0.065  4008.65

   3 0 4 12 2 

   0.065  4002.23

   4 0 5 13 3 

   0.065  4003.15

   ...

   33 24 34 0  32 

   0.065  4000.22

   34 25 35 0  33 

   0.065  4000.56

   35 26 36 0  34 

   0.065  4001.00

   36 

   27 0 0 35  0.065  4001.45

   ...

   **1**

   **2**

   **3**

   **4**

   **5**

   **6**

   **7**

   **8**

   **9**

   **10 11 12 13 14 15 16 17 18**

   **19 20 21 22 23 24 25 26 27**

   **28 29 30 31 32 33 34 35 36**

   **Example Grid**

   Line 1:  

   1 = grid element, 

   0 = cell to the north, 

   2 = cell to the east, 

   10 = cell to the south, 

   0 = cell to the west    

   0.060 = n-value for the cell 

   4005.23 = cell elevation

   FILE:  FPLAIN.DAT

   FLOODPLAIN GRID ELEMENT DATA

.. container::
   :name: page52-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023510051.png
   42

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   DUM

   **i**

   **1 - NNOD**

   Grid element number (I) of the floodplain grid system.  This 

   is a dummy variable that is not used by the model.  It is only 

   used for the convenience of viewing the input data file.

   FP(I,J)

   **i**

   **1 - NNOD**

   Floodplain element contiguous to grid element I (where I = 

   1, NNOD) and located in the J-direction (where J = 1,4).  

   The J-direction corresponds to one of the four compass 

   directions (see comments 1 thru 5).

   FP(I,5)

   **r**

   **0.010 - 0.4**

   Manning’s n roughness coefficient assigned to grid element I 

   (see comment 6).

   FP(I,6)

   **r**

   Ground surface elevation for grid element I (ft or m).

   **IMPORTANT NOTE: **

     If a grid size, shape, elevation or roughness is adjusted with the
   FLO-2D Plugin, 

   the exported data will not overwrite FPLAIN.DAT, CADPTS.DAT, or
   NEIGHBORS.DAT.  Those files 

   should be deleted prior to running the engine. 

   FLOPRO.EXE reads the grid, elevation, and Manning’s n data as
   follows:

   The model verifies the following files:

    ·

   If FPLAIN.DAT, CADPTS.DAT, and, NEIGHBORS.DAT, exist, the engine will
   use them and 

   ingore TOPO.DAT AND MANNINGS_N.DAT.

    ·

   If TOPO exists, the model reads it to count the number of grid
   elements and grid element size.  

    ·

   If NEIGHBORS.DAT exists, the model reads this file to define the
   neighbors.  If it does not 

   exist, FLOPRO uses TOPO.DAT to define the neighbors and creates
   NEIGHBORS.DAT.  The 

   model starts faster when the file is present.

    ·

   If MANNINGS_N.DAT exists, the model reads it to define the floodplain
   roughness.  If the file 

   does not exist but all others do, the model will generate a fatal
   error message and stop.

    ·

   If CADPTS.DAT and FPLAIN.DAT do not exist, the model will generate
   them.

    ·

   If TOPO.DAT and MANNINGS_N.DAT do not exist, the model will use
   FPLAIN.DAT and 

   CADPTS.DAT to create them. 

   Variable Descriptions for the 

   FPLAIN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page53-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023520052.png
   43

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   FPLAIN.DAT File 

   1.  There should be no elements in the grid system that do not have
   at least one 

   neighbor element sharing one side.  In other words, no element should
   be con-

   nected only by a single diagonal corner.  

   | 2.  The elements should be numbered consecutively starting with 1. 
   | 3.  If a grid element (I) is a boundary element, then the
     neighboring grid element 

   FP(I,J) where J = 1, 2, 3, or 4, is set equal to 0.

   4.  Any additional grid elements in the FPLAIN.DAT file must have correspond-

   ing grid elements in the CADPTS.DAT file. 

   5.  The roughness assigned to the floodplain grid element should
   represent the 

   flow resistance associated with a flow depth of 3 ft
   (1 m) or greater.  The model 

   automatically computes a depth variable roughness for depths less
   than 3 ft ap-

   proximately as follows:

   n

   d

    = n

   b

    \*1.5 \* e-

   (0.4 depth/dmax)

   where:

   n

   b

    =  bankfull discharge roughness 

   depth = flow depth

   dmax = flow depth for drowning the roughness elements and vegetation
      

   (hardwired 3 ft or 1 m)

   To turn off the depth variable roughness set AMANN = -99.  See the
   Com-

   ment 9 in the CONT.DAT file.  

.. container::
   :name: page54-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023530053.png
   44

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   MANNINGS_N.DAT File Variables

   1  0.04  

    

    

    

    

   Line 1: 

   **DUM   FP(I, J)**

   2 

   0.04 

      

    

    

   Line 

   1: 

   **DUM   FP(I, J)**

   3 

   0.04 

      

    

    

   Line 

   1: 

   **DUM   FP(I, J)**

   ...

   ...

   ...

   18   0.04   

    

    

    

   Line 1: 

   **DUM   FP(I, J)**

   Note:  MANNINGS_N.DAT is a list of the grid elements and their
   n-values.  This file is automatically 

   generated by the GDS or QGIS and FLO-2D model at runtime.  The
   n-values are the same as those 

   listed in FPLAIN.DAT when it is created or edited.  Use this file for
   GIS or CADD applications.  Com-

   bined with TOPO.DAT, it can replace the FPLAIN.DAT and CADPTS.DAT
   files.

   MANNINGS_N.DAT File Example

   1 0.040 

   2 0.040

   3 0.040

   4 0.040

   ...

   33 0.040

   34 0.040

   35 0.040

   36 0.040

   ...

   FILE:  MANNINGS_N.DAT

   FLOODPLAIN GRID ELEMENT NVALUE DATA

.. container::
   :name: page55-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023540054.png
   45

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   DUM

   **i**

   **1 - NNOD**

   Grid element number (I) of the floodplain grid system.  This 

   is a dummy variable that is not used by the model.  It is only 

   used for the convenience of viewing the input data file.

   FPNVALUE

   **r**

   **0.010 - 0.4**

   Manning’s n roughness coefficient assigned to grid element I 

   (see comment 1).

   Variable Descriptions for the 

   MANNINGS_N.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   MANNINGS_N.DAT File 

   This file is prepared and edited by the GDS or QGIS pre-program for
   spatially vari-

   able n-values. 

   | 1.  The elements should be numbered consecutively starting with 1. 
   | 2.  The roughness assigned to the floodplain grid element should
     represent the 

   flow resistance associated with a flow depth of 3 ft (1 m) or
   greater.  

   | 3.  This file is a substitute for the n-values listed in the
     FPLAIN.DAT. 
   | 4.  MANNING_N.DAT, MANNING_N.BAC, MANNING_N.RGH:   This 

   series of files is automatically generated by the FLOPro model and
   has the 

   format of grid element number and Manning’s n-value in two columns.
    When 

   combined with TOPO.DAT, MANNINGS_N.DAT can be used as a substi-

   tute for FPLAIN.DAT.  FPLAIN.DAT can be deleted or not used if these
   two 

   files are present in the project folder.  The model will recognize
   that either the 

   TOPO.DAT and MANNINGS_N.DAT files or the FPLAIN.DAT is present 

   and will automatically generate the missing file(s).  These files can be used to 

   assigned or edit the n-values.  TOPO.DAT and MANNINGS_N.DAT are in 

   a format that is more GIS compatible and FPLAIN.DAT is therefore
   obsolete. 

   MANNINGS_N.RGH is used with the limiting Froude number component 

   to report adjusted n-values during a simulation in place of
   FPLAIN.RGH.

.. container::
   :name: page56-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023550055.png
   46

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   TOPO.DAT File Variables

   551397.50  44608.95   6.00 

    

   **Line 1: **

   **XCOORD(I), YCOORD(I)   FP(I, J)**

   Note:  TOPO.DAT is a list of the grid element x- and y-coordinates
   and their elevations.  The eleva-

   tions are interpolated from topographical data by the GDS or QGIS.
    This files contains the same data 

   as the FPLAIN.DAT and CADPTS.DAT files except for the neighbor grid
   elements and n-value.  It is 

   automatically generated and edited by the GDS or QGIS when the
   FPLAIN.DAT is written.  Use this 

   file together with Mannings_N.DAT for GIS and CADD applications.

   TOPO.DAT File Example

   551397.50  44608.95   6.00

   551397.50  44708.95   6.05

   551397.50  44808.95   6.06

   551397.50  44908.95   6.06

   551397.50  45008.95   6.11

   551397.50  45108.95   6.09

   551397.50  45208.95   6.12

   551397.50  45308.95   6.14

   ...

   ...

   FILE:  TOPO.DAT

   TOPOGRAPHICAL ELEVATION DATA

.. container::
   :name: page57-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023560056.png
   47

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   TOPO.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT RANGE

   DESCRIPTION

   XCOORD(I)

   **r**

   X coordinate of grid element node at center.

   YCOORD(I)

   **r**

   Y coordinate of grid element node at center.

   ELEV(I)

   **r**

   Elevation of grid element.

   Instructional Comments for the 

   TOPO.DAT File

   1.  The TOPO.DAT data as that contained in FPLAIN.DAT and CADPTS.DAT 

   and is in a format that enables GIS and CADD applications to use it
   directly.  

   TOPO.DAT has the format of x- and y-coordinate, and elevation (x,y,z
   file) of 

   the center of the node in a GIS or CADD compatible format.  

   2.  The TOPO.DAT and MANNINGS_N.DAT files replace FPLAIN.DAT and 

   CADPTS.DAT files.  If these files are generated by GIS and CADD
   programs, 

   the FLO-2D model can run without the FPLAIN.DAT and CADPTS.DAT if 

   the data is space delimited.  If the TOPO.DAT file is missing at
   runtime, the 

   model automatically generates it.  Conversely if FPLAIN.DAT is
   missing at 

   runtime, the model automatically generates this file.  FPLAIN. DAT
   is obsolete 

   and is no longer required to run the model

.. container::
   :name: page58-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023570057.png
   48

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   INFLOW.DAT File Variables

   0   4335 

   Line 1: 

   **IHOURDAILY   IDEPLT**

   C    0   4335 

   Line 2: 

   **IFC(I) = ‘F’ or ‘C’   INOUTFC(I)   KHIN(I)**

   ** **

   *I = Number of inflow nodes.*

   H      0      0 

   Line 3: 

   **HYDCHAR = ‘H’   HP(J,1)   HP(J,2)   HP(J,3)   J=1**

   H      1       50.00 

   Line 3: 

   **HYDCHAR = ‘H’   HP(J,1)   HP(J,2)   HP(J,3)   J=2**

   H     24   1553.0 

   Line 3: 

   **HYDCHAR = ‘H’   HP(J,1)   HP(J,2)   HP(J,3)   J=3**

   R   5232   3320   0.250 

   Line 4: 

   **RESCHAR = ‘R’  IRESGRID(II)   RESERVOIREL(II)  **

   **  **

   ** **

   **RESERVOIRN(II)**

   R   6528   3295  3292   0.250  Line 4: 

   **RESCHAR = ‘R’  IRESGRID(II)   RESERVOIREL(II)**

   **  **

   ** **

   **T**

   **AILINGSELEV(II)   **

   **RESERVOIRN(II)**

   *   *

   * *

   *II = Number of data pairs.*

   ....

   Notes:

   If only rainfall is being simulated omit this file

   Line 2, 3:  Repeat these lines for each inflow grid element.

   Line 3:  If MUD = 0, HP(I,J,3) is omitted.

   Line 4:  Tailings elevation is optional is optional the n value is
   required.

   INFLOW.DAT File Example

      0   4335

      C           0    4335

      H           0      0

      H           1     55.30

      H           2     155.30

      H           3     253.78

      H           4     537.8

      H           5     522.7

      H           6     507.5

      H           7     492.4

      R      5232   1734.02  0.250

            ....

   FILE:  INFLOW.DAT 

   INFLOW HYDROGRAPH DATA

.. container::
   :name: page59-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023580058.png
   49

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   INFLOW.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT RANGE

   DESCRIPTION

   HP(I,J,1)

   **r**

   **0.0 - **

   ** **

   Time corresponding to the start of the floodplain inflow 

   hydrograph interval (hours or days).  The first hydrograph 

   time-discharge set should be 0.0 and 0.0.

   HP(I,J,2)

   **r**

   **0.0 - **

   Floodplain discharge (cfs or cms) corresponding to the time 

   interval which starts at HP(I,J,1).

   HP(I,J,3)

   **r**

   **0 - 1**

   Sediment concentration by volume or sediment volume for 

   a mudflow simulation (see comment 2). 

   HYDCHAR

   **c**

   **H**

   Character ‘H’ that identifies Line 3 inflow hydrograph time 

   and discharge pairs.  Each line of the hydrograph begins 

   with ‘H’. Variable is case sensitive.  It must be upper case.

   IDEPLT

   **i**

   **1 - NNOD**

   Inflow grid element number whose hydrograph is to be 

   graphically displayed at runtime.  Only one inflow grid 

   element hydrograph can be plotted on the screen.  If no 

   graphic display is desired (LGPLOT = 0) set IDEPLT = 0 

   (see comment 3).

   IFC(I)

   **c**

   **F or C**

   Character ‘F’ or ‘C’ to identify the inflow hydrograph grid 

   element as a floodplain ‘F’ or a channel ‘C (see comment 

   1).

   Variable is Case Sensitive.  It must be upper case.

   INOUTFC(I)

   **s**

   **0, 1, 2, or 3**

   Floodplain

   INOUTFC = 0      Inflow

   INOUTFC = 1      Diversion

   INOUTFC = 2      Source from groundwater

   INOUTFC = 3      Sink to groundwater

   Channel

   INOUTFC = 0      Inflow

   INOUTFC = 1      Diversion

   INOUTFC = 2      MODFLOW Source

   INOUTFC = 3      MODFLOW Sink

   (see Comment 7, 8 and 9)

.. container::
   :name: page60-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023590059.png
   50

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   IHOURDAILY

   **s**

   **0 = hourly**

   **1 = daily**

   IHOURDAILY = 0 for inflow hydrograph hourly intervals 

   HP (I,J,1).  IHOURDAILY = 1 for daily (24hr) intervals of 

   HP (I,J,1).

   KHIN(I) 

   **i**

   **1 - NNOD**

   Array of grid elements with a inflow hydrograph (inflow 

   nodes).

   RESCHAR

   **c**

   **R**

   Character ‘R’ that identifies Line 4 for reservoir or ponded 

   area water surface assignment.

   Variable is Case Sensitive.  It must be upper case.

   IRESGRID

   **i**

   **1 - NNOD**

   Grid element located somewhere inside the reservoir or 

   ponded water area.  Only one grid element has to be as-

   signed a water surface elevation (see comment 5).  

   RESERVOIREL

   **r**

   **0 - **

   **0 - (- **

   **)**

   Water surface elevation (ft or m) of the reservoir or ponded 

   water area.

   Negative water surface elevation assigns the reservoir bed elevations
   below 

   the breach foundation elevation as dead pool ground and reduces the 

   reservoir starting flow depth for those dead pool elements.

   RESERVOIRN

   **r**

   **0.1 - 0.4**

   Optional reservoir n-value for all reservoir elements as-

   signed a starting water surface elevation. If RESERVOIRN 

   is not assigned, the model will use the floodplain element 

   n- value. The n-value should be high enough to reduce 

   reservoir velocities to less than 2.0 fps (0.67 mps).  A value 

   of 0.25 is suggested (see Comment 6).   

   TAILINGSELEV(II)

   **r**

   **0 - **

   Tailings dam material surface elevation (ft or m).

   Variable Descriptions for the 

   INFLOW.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page61-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023600060.png
   51

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   INFLOW.DAT File

   1.  Either the channel or the floodplain grid elements can be used to
   input the 

   inflow hydrograph to grid system.

   2.  The user has a choice to input either the
   sediment concentration by volume 

   associated with the inflow water discharge or a sediment volume for
   the time 

   interval HP(I,J,1).  The mudflow volume (ft

   3

    or m

   3

   ) can represent erosion, 

   hillslope failure, or any other type of mass sediment loading.  When
   HP(I,J,3) 

   is less than 1.0, HP (I,J,3) corresponds to the sediment
   concentration by vol-

   ume for floodplain discharge HP(I,J,2) for the time interval which starts at 

   HP(I,J,1).  If HP(I,J,3) is greater than 1.0, then HP(I,J,3)
   represents a sediment 

   inflow volume.  If a mudflow scenario is being used each hydrograph
   should 

   have concentration data.  If one hydrograph does not
   have mudflow, give it the 

   minimum amount of 0.10 concentration.

   | 3.  IDEPLT must be an inflow grid element KHIN(I) listed in Line 2.
   | 4.  If the channel inflow hydrograph is to be plotted at runtime on
     the screen.  Set 

   LGPLOT = 2 in the CONT.DAT file.  

   5.  To create a filled reservoir, pond, or
   tailings dam, simply assign the desired 

   water or tailings surface elevation to one grid element (IRESGRID)
   within the 

   reservoir or ponded area.  At model runtime, the model will
   automatically as-

   sign the same water surface to all the grid elements in an expanding
   circle of ele-

   ments around IRESGRID that have a ground elevation less than the prescribed 

   water surface elevation RES-ERVOIREL and.or the tailings surface
   elevation 

   TAILINGSELEV(II).

   6.  Flooding routing a deep reservoir pool is essentially
   frictionless flow and should 

   not be simulated using
   a friction slope given by Manning’s equation.  Friction-

   less flow cannot be predicted with the full dynamic equation without
   a friction 

   slope term.  In order to apply the revised Manning’s equation for
   ponded flow, 

   it is recommended that a high n-value be used on the order of 0.1 to
   0.4.  This 

   will result in reservoir velocities of approximately 1 fps (0.3 mps)
   which will be 

   representing for filling or draining the reservoir when the water
   surface slope is 

   almost flat.  RESERVOIRN is a required variable in Build 22 and on.

   7.  INOUTFC can be set up for a floodplain or channel invlow,
   diversion, sink, 

   source, or MODFLOW conditions.

   a.  INOUTFC = 0; Floodplain inflow hydrograph, a cell can be either
   source 

   or sink at a given time, for this condition. The grid cell can become
   a source 

.. container::
   :name: page62-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023610061.png
   52

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   at one time-step and a sink at another time-step during a simulation.
    Sink 

   (negative) and sources (positive) at a given time. 

   b.  INOUTFC = 1; Floodplain diversion will be removed from the
   cell but not 

   added to groundwater.

   c.  INOUTFC = 2; Floodplain node, the source of this discharge comes
   from 

   groundwater.  The following source flow condition at a given time
   step will 

   be added to the surface grid.

   d.  INOUTFC = 3; Floodplain, this sink flow condition is subtracted
   from the 

   surface grid. If the cell is dry, no outflow will be subtracted from
   the cell. 

   If the discharge at the grid cell is less than the sink outflow
   condition, then 

   only the available flow in the cell is subtracted from the surface.

   e.  INOUTFC = 0; Channel inflow hydrograph a cell can either be a
   source 

   or a sink for this condition. The channel cross section can become a
   source 

   at one time-step and a sink at another time-step during a simulation.
    Sink 

   (negative) and sources (positive) at a given time. 

   f. 

   INOUTFC = 1; Channel, the diversion will act as a sink but not
   added to 

   ground water.

   g.  INOUTFC = 2; MODFLOW Source (See Comment 8). Channel node, 

   the source of this discharge comes from groundwater. The source flow
   will 

   be added to the cross-section flow.  

   h.  INOUTFC = 3; MODFLOW Sink (See Comment 8). Channel, the sink 

   of this discharge condition to groundwater from the channel cross
   section. 

   8.  A floodplain cell can be either source or sink at a given
   time-step. It may be 

   source at one time-step and sink at another time-step during a
   simulation.  

   They cannot be channel bank elements or interior channel elements.  Q
   (+) for 

   source to surface water. Q (-) to sinks for surface water.

   9.  Source and sink discharges from/to groundwater for an uncoupled
   simulation. 

   A source and sink discharge cannot be assigned to the same channel
   element.  

   The channel element is either a source or a sink, but it cannot be
   both.  That 

   means that if you have a switch occur in a reach from source to sink,
   you will 

   need to select those channel elements that you want to be sources and
   those you 

   want to be sinks. You can just assign a group of channel elements as
   a source 

   and another group as a sink in the reach and assign different times.

   10.  To create a tailing dam storage area with uniform tailings surface, the tailings 

   elevation or depth should be assigned to the grid element (IRESGRID).
    At 

   model runtime, the model will automatically assign the same tailings
   surface or 

   tailings depth to all the grid elements that are inside the tailings
   dam storage 

   area.

.. container::
   :name: page63-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023620062.png
   53

   **D**

   **ata**

   ** I**

   **nPut**

   OUTFLOW.DAT File Variables

   K      374 

   Line 1: 

   **OUTCHAR = ‘K’   KOUT**

   H    10.0    2.6    0.35 

   Line 2: 

   **OUTCHAR = ‘H’   HOUT(J,1)  HOUT(J,2)   HOUT(J,3)**

   ** **

   K     1007                     

   Line 1: 

   **OUTCHAR = ‘K’   KOUT**

   T      0.0         0.00 

   Line 3: 

   **OUTCHAR = ‘T’   CHDEPTH(J)   CQTABLE(J)  J=1**

   T      3.0       50.35 

   Line 3: 

   **OUTCHAR = ‘T’   CHDEPTH(J)   CQTABLE(J)  J=2**

   T      5.0     157.67 

   Line 3: 

   **OUTCHAR = ‘T’   CHDEPTH(J)   CQTABLE(J)  J=3**

   K      567                     

   Line 1: 

   **OUTCHAR = ‘K’   KOUT**

   N           567    1 

   Line 4: 

   **OUTCHAR = ‘N’   NOSTA  NOSTACFP**

   S         0.00    0.00 

   Line 5: 

   **OUTCHAR = ‘S’   STA_TIME(J)   STA_STAGE(J)  J=1**

   S         0.50    10.00 

   Line 5: 

   **OUTCHAR = ‘S’   STA_TIME(J)   STA_STAGE(J)  J=2**

   **  **

    O     273 

    

          Line 6    

   **OUTCHAR = ‘O’   NODDC(J)    J=1**

   O1   373 

   Line 6: 

   **OUTCHAR = ‘O1’   NODDC(J)   J=2**

   O2   374 

   Line 6: 

   **OUTCHAR = ‘O2’   NODDC(J)   J=3**

   O3   567 

   Line 6: 

   **OUTCHAR = ‘O3’   NODDC(J)   J=4**

   **  **

   ** **

   *J = number of parameters *

   Notes:

   Line 1, 2 and 3:  If ICHANNEL = 0 in CONT.DAT omit these lines.

   Line 1:  Repeat for each channel outflow element.

   Line 2:  Omit line if no stage-discharge control relationship is
   required for the channel outflow.

   Line 3:  Omit line if no stage-discharge control is required for the
   channel outflow.  If Lines 2 and 3 

    

     are omitted, the channel outflow will be discharge from the grid
   system as normal flow.

   Line 4 and 5:  Repeat lines for each element with a time-stage
   relationship.

   Line 6:  Repeat for each floodplain outflow grid element and each
   outflow node that will generate a 

    

     hydrograph to a downstream grid system.

   FILE:  OUTFLOW.DAT

   OUTFLOW HYDROGRAPH DATA

.. container::
   :name: page64-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023630063.png
   54

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   OUTFLOW.DAT File Example

   K      374

   H    10.0    2.6    0.35

   K     1007

   T      0.0         0.00

   T      3.0       50.35

   T      5.0     157.67

   T    10.0     366.58

   K      567

   N           567    1

   S         0.00    0.00

   S         0.50    10.00

   S         1.00    20.00

   S         1.50    10.00

   S         2.00      0.00

   O     273

   O     373

   O     374

   O     564

   O     565

   O     566

   O     566

   O     567

   O     568

   O1    1005

   O1    1006

   O1    1007.....

   FILE:  OUTFLOW.DAT

   OUTFLOW HYDROGRAPH DATA

.. container::
   :name: page65-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023640064.png
   55

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   OUTFLOW.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CHDEPTH(J)

   **r**

   **0.0 - **

   Array of channel maximum depths above the thalweg (not 

   water surface elevation) for the outflow rating table.

   CQTABLE(J)

   **r**

   **0.0 - **

   Array of discharges for the channel outflow rating table.

   HOUT(J,1)

   **r**

   **0.01 - **

   Array of channel maximum depths for which a channel 

   outflow stage-discharge relationship is valid.

   HOUT(J,2)

   **r**

   **0.0 - **

   Array of coefficients for the channel element outflow stage-

   discharge relationship (see comment 3).

   HOUT(J,3)

   **r**

   **0.0 - **

   Array of exponents for the channel element (I) outflow stage-

   discharge relationships

   KOUT

   **i**

   **1 - NNOD**

   Array of channel outflow elements.  These elements discharge 

   flow out of the grid system from the channel (see comments 

   1 and 2).

   NODDC

   **i**

   **1 - NDC**

   Array of floodplain outflow grid elements.  These elements 

   discharge flow out of the grid system from the floodplain (see 

   comments 1 and 2).

   NOSTA

   **i**

   **1 - NNOD**

   Array of grid elements with stage-time relationships.  If 

   NOSTA is a inflow element, assign NOSTA as a negative 

   value to compute inflow volume (see comments 4, 5 and 6).

   NOSTACFP

   **s**

   **0 = flood-**

   **plain**

   **1 = channel**

   Channel or floodplain identifier.  If NOSTACFP = 0, the 

   following stage-time relationship is for a floodplain element.  

   If NOSTACFP = 1, the stage-time relationship is for a chan-

   nel element.

   OUTCHAR

   **c**

   **K, H, T, N, **

   **S, O**

   **O1 - O9**

   Character line identifier that initializes each line in the data 

   file (see Comment 7). Variable is case sensitive.  It must be 

   upper case.

   STA_TIME(J)

   **r**

   **0.0 - **

   **500 pairs**

   Array of time intervals (hrs) for the grid element stage-time 

   relationship.

   STA_STAGE(J)

   **r**

   **0.0 - **

   **500 pairs**

   Array of water surface elevations (ft or m) for the stage-time  

   relationship.

.. container::
   :name: page66-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023650065.png
   56

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   OUTFLOW.DAT File

   1.  Either the channel or the floodplain outflow elements can be used
   to discharge 

   the flow off the grid system.  The outflow node is an artificial grid
   element 

   whose sole purpose is to discharge flow off the grid system. The
   outflow nodes 

   should not contain hydraulic structures, streets or other attributes.
   The flood-

   plain elevation of the outflow node is automatically set to an
   elevation lower 

   (0.25 ft or 0.1 m) than the lowest upstream grid element unless it is
   already 

   lower than all the upstream grid elements.

   2.  Omitting Lines 2 and 3 will cause all the inflow to the outflow
   elements to dis-

   charge from the grid system at normal flow conditions.  This outflow
   is equal to 

   the sum of the inflow from the contiguous elements that are not
   outflow nodes 

   and enables an approximation of normal flow depth in the outflow
   elements.  

   This is a simple method to ensure that backwater related to
   artificial boundary 

   conditions does not occur in the upstream elements.  

   3.  Channel boundary outflow condition may be established by
   specifying a stage-

   discharge relationship given by Q = a h

   b

    where the coefficient (a) and exponent 

   (b) are required input and h is the flow depth.  The coefficient (a)
   and exponent 

   (b) can be used to established critical flow at the outflow grids.

   4.  A discretized time-stage relationship can be employed to specify
   a water surface 

   elevation for at various channel or floodplain locations in the grid
   system.  This 

   is a simple method by which to simulate storm surge flooding on the coastal 

   floodplain.  Floodplain or
   channel elements can be specified with increasing 

   tides or storm surge water surface elevations.   

   5.  If coastal flooding (storm surges or tsunamis) is being simulated
   with a time-

   stage hydraulic control, assign the time-stage control to the outflow
   nodes.  

   When the time-stage water surface elevation in OUTFLOW.DAT is higher 

   than the model predicted stage, inflow to the grid system will occur
   with as-

   signed time-stage elevation to the outflow node. If the model
   predicted water 

   surface is higher than the assigned time-stage elevation, the grid
   element will 

   function as an outflow node discharging flow off the grid system.  It is permis-

   sible to assign NOSTA time-stage control to grid elements that are
   not outflow 

   nodes.

   6.  If a water surface elevation is specified for a NOSTA element,
   determine if it is 

   an inflow element in the INFLOW.DAT file.  If NOSTA is an inflow
   element, 

   set NOSTA as negative value to compute the inflow volume at this
   element 

   which corresponds to the constant water surface elevation.

.. container::
   :name: page67-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023660066.png
   57

   **D**

   **ata**

   ** I**

   **nPut**

   7.  If the OUTCHAR is O1-O9, these outflow grid elements will
   generate hy-

   drographs that can be used as inflow hydrographs to a separate
   downstream 

   FLO-2D model with a different grid system (even if the downstream
   system 

   has a different element size).  The inflow hydrograph will be in the
   format of the 

   INFLOW.DAT file.  This enables a row or column of outflow grid
   elements to 

   be defined as inflow elements to the downstream grid system.  Up to
   nine sepa-

   rate additional grid systems can be used.  If only one downstream
   grid system 

   will have the inflow hydrographs, set OUTCHAR = O1 for
   those boundary 

   outflow nodes.  The CADPTS.DAT file for the downstream grid system
   must 

   be included in the project folder as CADPTSDS1.

.. container::
   :name: page68-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023670067.png
   58

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  RAIN.DAT

   RAINFALL DATA

   RAIN.DAT File Variables

    

    0     0 

   Line 1: 

   **IRAINREAL, IRAINBUILDING**

     

    3.100     0.000     1     1 

   Line 2: 

   **RTT   RAINABS   RAINARF   MOVINGSTORM**

    R   0.000        0.000 

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(I)   R_DISTR(I)  I=1**

    R   0.083        0.050 

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(I)   R_DISTR(I)  I=2**

    R   0.167        0.110 

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(I)   R_DISTR(I)  I=3**

    R   0.250        0.300 

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(I)   R_DISTR(I)  I=4**

    R   0.330        0.450 

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(I)   R_DISTR(I)  I=5**

    R....

    2.0   5 

   Line 4: 

   **RAINSPEED   IRAINDIR**

   **  **

   2558   0.5 

   Line 5 

   **IRGRID(I)   RAINARF(I)**

   ** **

   *I = number of rainfall depth-area reduction values*

   ** **

   Notes:

   Line 4:  If MOVINGSTORM = 0, omit this line.

   Line 5:  If IRAINARF = 0, omit this line

   RAIN.DAT File Example

    0    0

    3.100     0.000     1     1

    R   0.000        0.000

    R   0.083        0.050

    R   0.167        0.110

    R   0.250        0.300

    R   0.330        0.450

    R....

    2.0   5

      2558   0.50

     

    

.. container::
   :name: page69-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023680068.png
   59

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   RAIN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IRAINARF

   **s**

   **0 = off**

   **1 = on**

   IRAINARF = 1 indicates that individual grid element depth-

   area reduction values will be assigned.

   IRAINBUILDING

   **s**

   **0 = off**

   **1 = on**

   IRAINBUILDING = 1 indicates that rainfall on an ARF = 1 

   grid element will be contributed to the surface water runoff 

   for that element (see comment 3).

   IRAINDIR

   **i**

   **1 thru 8**

   Direction of the moving storm.  Directions are as follows:

   1 = N  5 = NE

   2 = E  6 = SE

   3 = S 

   7 = SW

   4 = W  8 = NW

   IRAINREAL

   **s**

   **0 = off**

   **1 = on**

   IRAINREAL = 1 indicates that real-time rainfall (e.g. 

   NEXRAD) will be simulated.  The RAINCELL.DAT file 

   containing the spatial and temporal rainfall data must be 

   prepared by the GDS.

   IRGRID

   **i**

   **1 - NNOD**

   Grid element with a spatially defined rainfall depth area 

   reduction value.  This data is automatically generated in the 

   GDS.

   MOVINGSTORM

   **s**

   **0 = off**

   **1 = on**

   MOVINGSTORM = 1 indicates that a moving storm will 

   be simulated. 

   RAINABS

   **r**

   **0 - 1**

   Rainfall interception and abstraction (inches or mm) if infil-

   tration is not being modeled (see comment 2).

   RAINARF

   **r**

   **0 - 1**

   Rainfall depth area reduction to create spatially variable 

   rainfall.  This data is automatically generated in the GDS 

   processor program (see comment 4).

   RAINCHAR

   **c**

   **R**

   Character ‘R’ that identifies Line 3.  Variable is case sensitive 

   and it must be upper case.

   RAINSPEED

   **r**

   **0 - 100**

   **0 - 50**

   Storm speed (mph or kph)

   RTT

   **r**

   **0.0 - **

   Total storm rainfall (inches or mm).

   R_TIME(I)

   **0.0 - **

   Time (hrs) corresponding to the start of the specified rainfall 

   interval.

   R_DISTR(I)

   **r**

   **0 - 1**

   Rainfall distribution as a cumulative percentage of the total 

   storm which initiates at the time interval R_TIME(I) (see 

   comment 1).

.. container::
   :name: page70-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023690069.png
   60

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

    

   Instructional Comments for the 

   RAIN.DAT File

   1.  The rainfall distribution has to be correlated to the flood
   simulation time.  The 

   rainfall may occur for only a portion of the total flood simulation
   and may 

   start after the flood simulation begins.  For most rain storms, the
   start of the 

   simulation correlates with the start of the rainfall.  In those cases
   where the 

   rainfall and the simulation time are not correlated, it may be necessary to use 

   0.0 cumulative rainfall at the beginning of the flood simulation for a period of 

   time. Similarly the final cumulative rainfall at the end of the
   simulation could 

   be set equal to 1.0.   

   2.  If infiltration is being simulated, set the RAINABS = 0 and
   assign the rainfall 

   abstraction in the INFIL.DAT file.  

   3.  When rainfall occurs on a grid element with a complete storage
   loss assigned 

   (ARF = 1 value), the model removes that rainfall volume from the
   surface water 

   in that cell.  It assumes that the rainfall on buildings enters the
   storm drain 

   system and is eliminated as runoff.  Setting IRAINBUILDING = 1
   enables 

   the model to add the building rainfall to the surface water of the
   grid element 

   with an ARF value.  It assumes that the buildings have a gutter
   system that 

   discharges the water to the ground.

   4.  RAINARF values are used for design storm data.  The variable is a
   percentage 

   of the total depth for the cell or the total depth for the cell when
   using a design 

   storm event in the RAIN.DAT file.  For example, set the variable to
   zero, no 

   rain will fall on the cell.  Set it to 0.5, half of the assigned
   rainfall on that ele-

   ment will be computed for that interval and set the RAINARF value to
   1 and 

   all of the rain will fall on the cell.  The realtime rainfall
   (spatially and temporally 

   variable) is also reduced by the RAINARF value over each rainfall
   interval.  

.. container::
   :name: page71-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023700070.png
   61

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  RAINCELL.DAT

   RAINCELL.DAT File Variables

    

    15   96  1/1/2000     12:00:00 AM   1/2/2000     12:00:00 AM

    

   Line 1: 

   **RAININTIME   IRINTERS   TIMESTAMP**

    

    1   0.0    

   Line 2: 

   **IRAINDUM (I)   RRGRID(I,K)**

    

   RAINCELL.DAT File Example

      

    1             73           4/17/2013     12:00:00 AM   4/20/2013    
   2:00:00 AM 

    1            0.0

    2            0.0

    3            0.0

    4            0.0

    5            0.0

.. container::
   :name: page72-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023710071.png
   62

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   RAINCELL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IRAINDUM(I)

   **r**

   **i - NNOD**

   Repeated set of grid elements for each interval.  

   IRINTERS

   **r**

   **0.0 - **

   Number of intervals in the dataset.  There will be a complete 

   set of cell values and rain data repeated for each interval.

   RAININTIME

   **r**

   **0.0 - **

   Time interval in minutes of the realtime rainfall data.  This 

   is a single variable in line 1.  The time interval starts at zero 

   when the simulation starts.  

   RRGRID(I,K)

   **i**

   **0.0 - **

   Cumulative rainfall in inches or mm over the time interval.

   TIMESTAMP

   **c**

   **Alpha **

   **Numeric**

   Timestamp indicates the start and end time of the storm. 

   (see comment 3)

.. container::
   :name: page73-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023720072.png
   63

   **D**

   **ata**

   ** I**

   **nPut**

    

   Instructional Comments for the 

   RAINCELL.DAT File

   1.  Real-time rainfall, specifically NEXRAD rainfall data, is
   rainfall information 

   that varies both in space and time and is applied to individual cells
   within a 

   grid system. The rainfall data is usually recorded at
   fifteen-minute intervals over 

   a specific duration. All the relevant data for this rainfall, forming
   a comprehen-

   sive dataset, is stored within the RAINCELL.DAT file.

   2.  Rainfall data obtained from radar systems is typically collected
   on relatively 

   large grids, such as 400 m by 400 m, 1 km by 1 km, or even larger,
   like 2 km 

   by 2 km grid resolutions. To determine the rainfall amount at each
   FLO-2D 

   grid cell for a specific time interval and rainfall period, the
   NEXRAD grid cells 

   are overlaid with the FLO-2D grid cells. The comprehensive dataset
   resulting 

   from this process is stored in the RAINCELL.DAT data file. This file
   can be 

   generated using the FLO-2D QGIS plugin.

   3.    A small sample of the catalog data is shown below.   

   7/13/2008 10:00 7/13/2008 15:00 1 5

   C:\\Projects\\NexRAD\\Min1.asc

   C:\\Projects\\NexRAD\\Min2.asc

   C:\\Projects\\NexRAD\\Min3.asc

   C:\\Projects\\NexRAD\\Min4.asc

   C:\\Projects\\NexRAD\\Min5.asc

   4.  The timestamp is not used by the FLO-2D Plugin or
   FLOPRO.EXE engine.  

   It is a reference variable.  It can be used to synchronize the
   raincell storm data 

   to inflow hydrographs.

   5.  RAINCELL data is also stored as RAINCELL.HDF5. Realtime rainfall 

   (NEXRAD rainfall data) is spatially and temporally variable rainfall
   data that is 

   applied to each cell of the grid system. A complete dataset is stored
   in the data 

   file RAINCELL.HDF5 using a Hierarchical binary Data Format. The HDF5 

   data is primarily stored using two types of objects: datasets and
   groups.

.. container::
   :name: page74-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023730073.png
   64

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  FLO2DRAINCELL.DAT

   FLO2DRAINCELL.DAT File Variables

    

     1   10055330    

   Line 1: 

   **IRAINDUM (I)   NXRDGD(I)**

    

   FLO2DRAINCELL.DAT File Example

      

    1 10055330

    2 10055330

    3 10055330

    .

    .

    .

    NNOD   10054387

.. container::
   :name: page75-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023740074.png
   65

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   FLO2DRAINCELL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   **IRAINDUM (I)**

   **i**

   **i - NNOD**

   FLO-2D grid element number of the floodplain grid system.

   **NXRDGD (I)**

   **i**

   **i - NNOD**

   NEXRAD grid element intersecting IRAINDUM. (see com-

   ment 1)

    

   Instructional Comments for the 

   FLO2DRAINCELL.DAT File

   1.  This data file stores the intersected
   real time rainfall grid (NEXRAD Grid) for 

   each FLO-2D grid cell.  The real time rainfall data (NEXRAD) are
   typically 

   collected on large grids like 1 km by 1 km or even larger. FLO-2D
   cells are in 

   the order of 10 ft (3 m) to 100 ft (30 m). The  FLO2DRainCell.dat has
   two 

   columns, the first column is the FLO-2D grid element number and the
   second 

   column is the real time rainfall grid that intersects the FLO-2D grid
   cell.  The 

   FLO2DRainCell.dat and RainCellRaw.dat files serve as an alternative
   to the 

   RAINCELL.DAT or RAINCELL.HDF5 files, providing a second option to 

   assign real-time rainfall data into the simulation. 

.. container::
   :name: page76-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023750075.png
   66

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  RAINCELLRAW.DAT

   RAINCELLRAW.DAT File Variables

    

     15min   96 intervals    

   Line 1: 

   **RAININTIME   IRINTERS**

     N   10055330    

   Line 2: 

   **RAINCHAR = ‘N' NXRGD(I)**

     R   0   0    

   Line 3: 

   **RAINCHAR = ‘R’   R_TIME(K)   RRGRID(I,K) K=1**

    

   RAINCELLRAW.DAT File Example

      

     15min  96 intervals

    N 10055330

    R 0 0

    R 0.25 0

    R 0.5 0

    R 0.75 0

    R 1 0.01

    R 1.25 0.01

    R 1.5 0.01

    R 1.75 0.01

    R 2 0.01

    ...

.. container::
   :name: page77-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023760076.png
   67

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   RAINCELLRAW.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   **IRINTERS**

   **i**

   **1 - n **

   **intervals**

   Number of intervals in the dataset. There will be a complete 

   set of cell values and rain data  repeated for each interval.

   **NXRDGD(I)**

   **i**

   **i - NNOD**

   NEXRAD grid element.

   **RAINCHAR**

   **c**

   **N, R**

   Character ‘N’  or ‘R’  that identifies Line 2 and Line 3 to the 

   Number of rainfall lines. Variable is case sensitive and it must 

   be upper case.

   **RAININTIME**

   **r**

   **0.0 - **

   Time interval in minutes of the realtime rainfall data. This 

   is a single variable in line 1. The time interval starts at zero 

   when the simulation starts.

   **R_TIME**

   **r**

   **0.0 - **

   Time (hrs) corresponding to the start of the specified rainfall 

   interval.

   **RRGRID(I,K)**

   **r**

   **0.0 - **

   Cumulative rainfall in inches or mm over the time interval.

    

   Instructional Comments for the 

   RAINCELLRAW.DAT File

   1.  This data file stores cumulative rainfall depth for each
   real-time rainfall grid 

   and at each time interval. For each NEXRAD grid a rainfall table of
   time and 

   depth is required.

.. container::
   :name: page78-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023770077.png
   68

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  INFIL.DAT 

   INFILTRATION DATA

   INFIL.DAT File Variables

   3 

   Line 1: 

   **INFMETHOD**

   0   0.7   1   0.4  10.0  1 

   Line 2: 

   **ABSTR   SATI   SATF   POROS  SOILD  INFCHAN**

   0.1   4.3   0 

   Line 3: 

   **HYDCALL   SOILALL   HYDCADJ**

   0.03 

   Line 4: 

   **HYDCXX   \*See Notes**

   R   0.03 

   Line 4a: 

   **INFILCHAR = ‘R’ **

     

   **HYDCX(IC)   \*See Notes**

   R   0.03   0.3   10.0 

   Line 4b: 

   **INFILCHAR = ‘R’**

      

   **HYDCX(IC)   HYDCXFINAL(IC)  **

   ** **

   ** SOIL_DEPTHCX(IC)**

   ** **

   ** **

   ** **

   ** **

   **       **

   *IC= number of channel segments or reaches*

   99   0 

   Line 5: 

   **SCSNALL   ABSTR1**

   F  1730  0.01  4.3  0.3  0.0  0.0  10.0 

    

   Line 6: 

   **INFILCHAR = ‘F’  INFGRID(IF)  HYDC(IF) **

   ** **

   ** **

   **SOILS(IF)   DTHETA(IF)  ABSTRINF(IF) **

   ** **

   ** **

   **RTIMPF(IF)   SOIL_DEPTH(IF) **

   **  **

   *IF =  1 - number of infiltration data sets*

   S  320   82.00 

   Line 7: 

   **INFILCHAR = ‘S’  INFGRID(IF)  SCSCN(IF)  **

   C  2   0.04 

   Line 8: 

   **INFILCHAR = ‘C’  INFCH(N)   HYDCONCH(N) **

   I  5.0   1.0   0.0007 

   Line 9: 

   **INFILCHAR = ‘I’  FHORTONI   FHORTONF   **

   ** **

   ** DECAYA**

   H  3450   3.0   0.5   0.00018  Line 10: 

   **INFILCHAR = ‘H’  INFGRID(IF)**

     

   **FHORTI(INFGRID(IF))   FHORTF(INFGRID(IF)) **

   ** **

   ** DECA(INFGRID(IF))**

   **  **

   *IF =  1 - number of Horton infiltration elements*

   Notes:

   If INFIL = 0 in the CONT.DAT file, omit this file.

   If INFMETHOD = 1 (Green-Ampt) add Line 2 thru 4, skip Line 5.  Line 6
   is optional.

   If INFMETHOD = 2 (SCS Curve)  add Line 5, skip Lines 2 thru 4.  Line
   7 is optional.

   If INFMETHOD = 3 (Both Green-Ampt and SCS)  add Lines 2 thru 5. Line
   6 and 7 are optional.

   If INFMETHOD = 4 (Horton), add lines 9 and 10.

   \*If INFCHAN = 1 add Line 4.  Line 8 is optional.

   If SOILD = 0. Use Line 4 or 4a

   If SOILD > 0. use Line 4b

   Line 4a or 4b, use one line per reach.

.. container::
   :name: page79-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023780078.png
   69

   **D**

   **ata**

   ** I**

   **nPut**

   INFIL.DAT File Example

   3 

   0   0.7   1   0.4   10.0  1

   0.0   4.3

   R   0.03   0.2   5.0

   R   0.12   0.3   10.0

   99   0

   F   1730   1.01   4.3   0.3   0.0   0.0    8.5

   F   1730   1.01   4.3   0.3   0.0   0.0  10.0

   F   1730   1.01   4.3   0.3   0.0   0.0    9.2

   F...

   S   320   82.00

   S   321   82.00

   S   322   82.50

   S...

   C   2   0.04

   C  10  0.04

   C... 

   FILE:  INFIL.DAT

   INFILTRATION DATA

.. container::
   :name: page80-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023790079.png
   70

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ABSTR

   **r**

   **0 - 1**

   **0 - 25**

   Green Ampt global floodplain rainfall abstraction or inter-

   ception (inches or mm) (see comments 1 and 7).

   ABSTRINF(N)

   **r**

   **0 - 1**

   **0 - 25**

   Grid element rainfall abstraction (inches or mm).

   ABSTR1

   **r**

   **0 - 1**

   **0 - 25**

   SCS global floodplain rainfall abstraction or interception 

   (inches or mm).  Assign ABSTRSCS = 0 for automatic com-

   putation of the initial abstraction (see comments 7 and 10).

   DECA

   (INFGRID(IF))

   **r**

   **0.0007 - **

   **0.0018**

   Horton’s equation spatially variable decay coefficient (1/

   second; no metric) (see comment 14).

   DECAYA

   **r**

   **0.0007 - **

   **0.0018**

   Horton’s equation decay coefficient (1/second; no metric) 

   (see comment 14).

   DTHETA(N)

   **r**

   **0.0 - 1**

   **0.0 - 0.5**

   The grid element soil moisture deficit (SATF-SATI) is ex-

   pressed as a decimal with a range from 0.0 to 1.0.  It can also 

   represent the grid element volumetric soil moisture deficit 

   that is defined as the soil moisture deficit multiplied by the 

   porosity (SATF-SATI)*POROS with a range from 0.3 to 0.5 

   (see comment 11).  Set POROS = 0 for the volumetric soil 

   moisture deficiency.

   DTHETAC(I)

   **r**

   **0.0 - 1**

   **0.0 - 0.5**

   The channel segment or reach soil moisture deficit (SATF-

   SATI) is expressed as a decimal with a range from 0.0 to 

   1.0. It can also represent the channel reach volumetric soil 

   moisture deficit that is defined as the soil moisture deficit 

   multiplied by the porosity (SATF-SATI)*POROS with a 

   range from 0.3 to 0.5 (see comment 11). Set POROS = 0 for 

   the volumetric soil moisture deficiency.

   FHORTF

   (INFGRID(IF))

   **r**

   **0.5 - 1.0**

   Horton’s equation spatially variable floodplain final infiltra-

   tion rate (inches/hr; no metric).

   FHORTI

   (INFGRID(IF))

   **r**

   **3.0 - 5.0**

   Horton’s equation spatially variable floodplain initial infiltra-

   tion rate (inches/hr, no metric).

   FHORTONF

   **r**

   **0.5 - 1.0**

   Global Horton’s equation final infiltration rate (inches/hr; no 

   metric)

   Variable Descriptions for the 

   INFIL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page81-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023800080.png
   71

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   INFIL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   FHORTONI

   **r**

   **3.0 - 5.0**

   Global Horton’s equation initial infiltration rate (inches/hr; 

   no metric) (see comment 14).

   HYDC(N)

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Grid element average hydraulic conductivity of an (inches/hr 

   or mm/hr) (see comments 2, 4 and 5).

   HYDCALL

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Average global floodplain hydraulic conductivity (inches/hr 

   or mm/hr).

   HYDCADJ

   **r**

   **0.01 - 1**

   **1 - 100**

   **-2.0 - (-1.0)**

   Hydraulic conductivity adjustment variable for spatially vari-

   able hydraulic conductivity:

   0.01 – 1;     HYDCON = HYDCON + HYDCADJ

   1 – 100;      HYDCON = HYDCON \* HYDCADJ

   -2 TO -1;    HYDCON = HYDCON \* 2.HYDCADJ

   HYDCHN

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Average global hydraulic conductivity for the entire channel 

   (inches/hr or mm/hr) (see comment 8).

   HYDCHN(I)

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Channel reach hydraulic conductivity channel (inches/hr or 

   mm/hr) (see comment 8).

   HYDCONCH(N)

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Hydraulic conductivity for a channel element (inches/hr or 

   mm/hr).

    HYDCX(IC)

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Initial hydraulic conductivity for a channel segment (inches/

   hr or mm/hr) (see comment 15).

   HYDCXFINAL(IC)

   **r**

   **0.01 - 10**

   **0.25 - 250**

   Final hydraulic conductivity for a channel segment (inches/

   hr or mm/hr).

   INFCH(N)

   **i**

   **1 - NNOD**

   Array of channel elements with a unique hydraulic conduc-

   tivity

   INFCHAN

   **s**

   **0 = off**

   **1 = on**

   Set switch to 1 to simulate channel infiltration (comment 6).

   INFGRID(IF)

   **i**

   **1 - NNOD**

   Array of floodplain grid elements with individual infiltration 

   parameters (see comment 3).

.. container::
   :name: page82-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023810081.png
   72

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   INFIL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   INFILCHAR(N)

   **c**

   **F, S, C, R, **

   **I, H**

   ‘F’ = spatially variable floodplain Green-Ampt data (Line 6),

   ‘S’ = floodplain spatially variable SCS curve number (Line 

   7);

   ‘C’ = channel spatially variable channel infiltration (Line 8);

   ‘R’ = channel reach infiltration data (Line 4 and 4a);

   ‘I’ = Horton global parameters (Line 9);

   ‘H’ = Horton spatially variable floodplain data (Line 10).

   Variable is case sensitive and it must be upper case.

   INFMETHOD

   **s**

   **1, 2, 3 or 4**

   1:  Green-Ampt method;

   2:  SCS curve number method;

   3:  Combined Green-Ampt and CN methods;

   4:  Horton method.

   POROS

   **r**

   **0.3 - 0.5**

   Global floodplain soil porosity.  If using the volumetric soil 

   moisture deficiency for DTHETA, set POROS = 0.

   RTIMPF(N)

   **r**

   **0.0 - 1**

   Percent impervious floodplain area on a grid element.

   SATF

   **r**

   **0.5 - 1**

   Global final saturation of the soil (decimal percentage) for 

   computing infiltration.  

   SATI

   **r**

   **0.0 - 0.95**

   Global initial saturation of the soil (decimal percentage).  

   SCSNALL

   **r**

   **1 - 99**

   Global floodplain SCS curve number for infiltration (see 

   comment 9).  The variable can range from 1 to 99 but use 

   engineering judgment.  Values lower than  67 will result in 

   an excessive loss and variables higher than 99 will be reset to 

   99.

   SCSCN(N)

   **r**

   **1 - 99**

   SCS curve numbers for spatially variable infiltration of the 

   floodplain grid elements.  The variable can range from 1 to 

   99 but use engineering judgment.  Values lower than  67 will 

   result in an excessive loss and variables higher than 99 will be 

   reset to 99.

   SOIL_DEPTH(N)

   **r**

   **0.0 - 100.**

   Spatially variable Green-Ampt infiltration soil limiting depth 

   storage (ft or m).  Maximum soil depth for infiltration on a 

   grid element (see comment 12).

.. container::
   :name: page83-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023820082.png
   73

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   SOIL_DEPTHCX(IC)

   **r**

   **0.0 - 100.**

   Maximum soil depth for the initial channel infiltration. 

   When SOIL_DEPTHCX is exceeded, the exponential decay 

   from the initial hydraulic conductivity to the final hydraulic 

   conductivity begins (see comment 12).

   SOILD

   **r**

   **0.0 - 100.**

   Global Green-Ampt infiltration soil limiting depth storage 

   (ft or m).  Maximum soil depth for infiltration.  Set SOILD 

   = 0 to have unlimited infiltration and do not assign spatially 

   variable SOIL_DEPTH(N).

   SOILS(N)

   **r**

   **1 - 20**

   **25 - 500**

   Capillary suction head for floodplain grid elements (inches 

   or mm).

   SOILALL

   **r**

   **1 - 20**

   **25 - 500**

   Average global floodplain capillary suction head (inches or 

   mm).

   Variable Descriptions for the 

   INFIL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page84-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023830083.png
   74

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   INFIL.DAT File

   1.  The Green-Ampt infiltration parameters including hydraulic
   conductivity 

   HYDC, initial abstraction ABSTR, initial saturation SATI, and soil
   capillary 

   suction head SOILS, can be estimated from the tables in the FLO-2D
   Refer-

   ence Manual (Tables 3-6).  Generally, the final SATF can be set at
   100% and 

   the porosity can be assumed to be 0.4.

   2.  No infiltration is simulated if the sediment concentration by
   volume is greater 

   than 10%.  This precludes simulating infiltration during mudflows.

   3.  Floodplain grid elements with unique Green-Ampt infiltration
   parameters are 

   specified in Line 6 which supersede then global values in Line 2.

   4.  No infiltration is computed for the portion of the grid element
   removed from 

   the potential flow surface with an Area Reduction Factor (ARF).  No
   infiltra-

   tion is computed for grid elements that are completely removed from
   the po-

   tential flow surface (ARF = 1.0).  Rainfall runoff, however, is
   assumed to occur  

   for an ARF = 1 grid element if IRAINBUILDING = 1 in the RAIN.DAT
   file.  

   Increased runoff resulting from proposed development can be predicted
   by us-

   ing the ARF values to limit infiltration on a grid element. 

   5.  No infiltration is computed for street areas of a grid element.
    The street area is 

   subtracted from the overland portion of the grid system.  

   6.  Channel infiltration is computed only if INFCHAN =
   1. Generally channel 

   infiltration is negligible for channels with perennial flow. The
   simulation of 

   channel infiltration may be important for small flood events in
   ephemeral al-

   luvial fan channels with porous bed material. 

   7.  Precipitation abstraction is an initial loss of rainfall that
   precedes infiltration 

   and excess rainfall runoff.  Vegetation interception is a component
   of the initial 

   loss.  Abstraction values will generally range from 0.01 to 0.5
   inches.  In addi-

   tion, FLO-2D does not initiate any flood routing until the depression
   storage 

   TOL is filled.  The TOL value is specified in TOLER.DAT file.
    Abstraction 

   is often assumed to include depression storage, but in FLO-2D a TOL
   value 

   of ranging from 0.004 to 0.1 ft (0.001 to 0.03 m) represents the
   depression 

   storage.

   8.  Use HYDCX(IC) and all other parameters on Line 4 to specify
   channel infiltra-

   tion data by reach.  Use line 8 HYDCON parameter to specify spatially
   vari-

   able hydraulic conductivity in the channel grid elements that will
   supersede the 

   HYDCX(IC) value in Line 4.  It is not necessary to specify individual
   channel 

.. container::
   :name: page85-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023840084.png
   75

   **D**

   **ata**

   ** I**

   **nPut**

   element soil suction, initial or final saturation values when
   assigning channel 

   infiltration. If SOILD is = 0, use Line 4, where IC is the number of
   channel 

   segments or reaches each entered on a new line.  If SOILD is greater
   than 0, use 

   line 4a where IC is the number of segments or reaches.

   9.  If SCS curve number method (INFMETHOD = 2) is used, it is assumed that 

   the channel infiltration is negligible.  Simulate channel
   infiltration with the 

   Green-Ampt method.  

   10.  With the SCS curve number method (INFMETHOD = 2), assign the AB-

   STRSCS variable in Line 5 to the abstraction (inches or mm).  If
   ABSTRSCS = 

   0.0, the abstraction value is automatically computed using the SCS
   method.

   11.  The infiltration parameters can be estimated from the tables in
   the Reference 

   Manual.  The user must distinguish whether soil moisture deficit
   parameter 

   DTHETA will represent the volumetric soil moisture deficit (soil
   moisture def-

   icit times the porosity) as prescribed from a drainage manual or if
   DTHETA 

   will be defined as just the soil moisture deficit (SATF-SATI).  If
   the volumetric 

   soil moisture deficit (SATF-SATI)*POROS is being applied, set POROS =
   0.0 

   in Line 1 and assign a DTHETA value in the range from 0.0 to 0.5.  If
   the only 

   soil moisture deficit is being used, then assign a typical porosity
   (POROS) in 

   the range: 0.35 to 0.45.

   12.  The Green-Ampt infiltration will cease when the wetting front
   reaches the lim-

   iting soil depth either SOILD, SOIL_DEPTH or SOIL_DEPTHCX for the 

   channel.  

   13.  It is not necessary to specify the soil suction, initial or
   final saturation values 

   when simulating channel infiltration. These values are assumed not to
   be im-

   portant to the channel bed seepage or bank infiltration.   

   14.  Horton’s infiltration model is defined by the equation: 

   f = f

   n

    + (f

   i

    - f

   n

   ) e

   -at

    Where:

   | f = infiltration rate at simulation time t from start of the
     rainfall
   | f

   i 

   = initial infiltration rate (in/hr)

   f

   n

    = final infiltration rate (in/hr)

   | a = decay coefficient (1/sec)
   | t = time from start of rainfall (sec)

    

   There are no metric equivalent values.  This method is based on the
   NRCS 

   hydrologic groups in English Units.

.. container::
   :name: page86-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023850085.png
   76

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   15.  As the channel infiltration storage fills, the infiltration rate
   declines but does 

   not cease.  The decay of the hydraulic conductivity H

   c

    from the initially as-

   signed hydraulic conductivity H

   i  

   to a final saturated hydraulic conductivity H

   f  

   is based on the following equation:

   H

   c

    = H

   f

    

   + (H

   i

    - H

   f

   ) e

   -at

    

   where:  

   a = decay coefficient hardwired to 0.00002, selected to have the
   decay from 

   the initial to the final hydraulic conductivity over a 72 hr period
   with 

   the decay to half the original hydraulic conductivity in 12 hours.

   t = time (seconds) from when the wetting front reaches the limiting
   soil 

   depth

.. container::
   :name: page87-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023860086.png
   77

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  EVAPOR.DAT 

   EVAPORATION DATA

   EVAPOR.DAT File Variables 

   5   1   0.00 

   Line 1: 

   **IEVAPMONTH   IDAY   CLOCKTIME**

   january   2 

   Line 2: 

   **EMONTH(I)   EVAP(I)   **

   *I = 1 - 12*

   0.0071 

   Line 3: 

   **EVAPER(I, J) **

   *I = 1, 12 Months, J = 1,24 Hours*

   0.0086 

   Line 3: 

   **EVAPER(I, J) **

   *I = 1, 12 Months, J = 1,24 Hours*

   0.0051 

   Line 3: 

   **EVAPER(I, J) **

   *I = 1, 12 Months, J = 1,24 Hours*

   **...**

   Notes:

   If IEVAP = 0 in the CONT.DAT file, omit this file.

   Line 3:  Repeat 24 times for every Line 2.

   An example of the EVAPOR.DAT file is available in the FLO-2D Example
   Project subdirectory based 

   on available data for the Rio Grande project.

   EVAPOR.DAT File Example

    5   1   0.00

     january  2.00

       0.0071

       0.0086

       0.0051

       0.0065

       0.0038

       0.0040

       0.0055

       0.0090

       0.0285

       0.0556

       0.0799

       0.0975

       0.1154

       ...

.. container::
   :name: page88-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023870087.png
   78

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CLOCKTIME

   **r**

   **0.0 - 24.0**

   Starting clock time (hrs) of the simulation time during the 

   day.

   EMONTH(I)

   **c**

   **Jan - Dec**

   Name of month for user identification purposes only.

   EVAP(I)

   **r**

   **0 - 100**

   **0 - 2500**

   Monthly evaporation rate (in/month or mm/month).

   EVAPER(I,J)

   **r**

   **0.0 - 1.0**

   Hourly percentage of the daily total evaporation for each 

   month.  There will be 24 values that will total 1.00 for each of 

   the twelve months. 

   IEVAPMONTH

   **i**

   **1 - 12**

   Starting month of simulation.

   IDAY

   **i**

   **1 - 7**

   Starting day of the week.

   Variable Descriptions for the 

   EVAPOR.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page89-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023880088.png
   79

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  CHAN.DAT

   CHANNEL DATA

   CHAN.DAT File Variables

     Line 1:   

   **DEPINITIAL(K)    FROUDC(K)    ROUGHADJ   ISEDN(K)    **

   0.00   0.50   0.20   0

     Line 2a:  

   **SHAPE **

   *‘R’ = Rectangular*

   **    ICHANGRID(I)   BANKELL(I)  **

   **   **

   **BANKELR(I)   FCN(I)   FCW(I)   FCD(I)   XLEN(I)**

   R   50     4765.52   4765.00   0.031   22.54   6.32   100.00 

     Line 2b:  

   **SHAPE **

   *‘V’ = Variable Area *

   **  ICHANGRID(I)   BANKELL(I)  **

   **   **

   **BANKELR(I)    FCN(I)   FCD(I)   XLEN(I)   A1(I)   A2(I)   B1(I)  
   B2(I)   **

   **   **

   **C1(I)  C2(I)   EXCDEP(I)   A11(I)   A22(I)   B11(I)   B22(I)  
   C11(I)   C22(I)**

   V   50     4765.52   4765.00   0.031   6.32   505.00  36.77  1.63
    63.37  0.491  63.261  0.49  0.00

     Line 2c: 

   **SHAPE **

   *‘T’ = Trapezoidal*

   **   ICHANGRID(I)   BANKELL(I)**

   ** **

   ** **

   **BANKELR(I)   FCN(I)    FCW(I)   FCD(I)   XLEN(I)   ZL(I)   ZR(I)**

   T   50     4765.52   4765.00   0.031   22.54   6.32   100.00  2.40
    1.50

     Line 2d:  

   **SHAPE  **

   *‘N’ = Natural*

   **   ICHANGRID(I)   FCN(I)   XLEN(I)  NXECNUM(I)**

   N   50   1    0.031   100.00   1

   50  4763.00 

   Line 3a: 

   **ISTART  WSELSTART**

   77  4761.00 

   Line 3b: 

   **IEND   WSELEND**

   C  501  498 

   Line 4:  C

   **HANCHAR = ‘C’  ICONFLO1(J)  ICONFLO2(J) **

   E  5112

   ** **

   Line 5: 

   **CHANCHAR = 'E'   ICHANGRID(N)**

   B  12.3

   ** **

   Line 6: 

   **CHANCHAR = 'B'   IBASEFLOW(K)**

   **  **

   *I = number of channel nodes.*

   * *

   * *

   *J = number of channel confluences*

   * *

   * *

   *K = number of channel segments*

   * *

   *  *

   *N = number of nofloc and noexchange data sets*

   Notes:

   If ICHANNEL = 0 in the CONT.DAT file, omit this file.

   Line 1:  This line is repeated at the start of each channel segment.
    If ISED = 0 in the CONT.DAT file 

   omit ISEDN(K).

   Line 2:  This line is repeated for each channel grid element.  Use
   2a, 2b, 2c, or 2d for this line.

   Line 3:  If not simulating an initial water surface elevation in the
   channel, omit this line.  Repeat 3a and 

   3b for each channel segment.

.. container::
   :name: page90-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023890089.png
   80

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   CHAN.DAT File Example

       0.00   0.60   0.40

    R  3170  4433.00 4433.00 0.032 40.00  9.30 520.00 

    R  3118  4431.00 4431.00 0.032 20.00  9.50 510.00 

    R  3066  4430.30 4430.30 0.032 35.00 11.00 500.00 

    R  3013  4430.00 4430.00 0.032 35.00 12.70 500.00 

    R  ...

      0.00   0.70   0.20

    V  4560 4675.19 4675.19 0.060 10.59 550.00 36.774  1.630 63.369
   0.491 63.261  0.486  0.00

    V  4385 4673.10 4673.10 0.050 11.00 620.00 30.774  1.630 63.369
   0.491 63.261  0.486  0.00

    V  4212 4672.86 4672.86 0.040 13.56 560.00 24.439  1.905 53.016
   0.749 42.886  0.745  0.00

    V  4213 4672.46 4672.46 0.040 16.16 550.00 22.200  1.807 31.248
   0.696 31.235  0.688  0.00

    V  ...

      0.00   0.60   0.40

    T  7170  4423.00 4423.00 0.032 40.00  9.30 520.00 1.60 1.90

    T  7118  4421.00 4421.00 0.032 20.00  9.50 510.00 2.60 2.70

    T  7066  4420.30 4420.30 0.032 35.00 11.00 500.00 1.60 1.20

    T  7013  4420.00 4420.00 0.032 35.00 12.70 500.00 1.60 1.20

    T  ...

     -1.00   0.60   0.20   5               

    N  7432 0.060  450.00    1       

    N  7389 0.059  450.00    2       

    N  7344 0.050  590.00    3       

    N  7298 0.060  590.00    4       

    N  7299 0.060  590.00    5       

    N  ...     

   7432  4432.00

   7160  4427.00

    C  3669  3825

    C  6296  6377

    C  ...

   FILE:  CHAN.DAT

   CHANNEL DATA

   CHAN.DAT File Variables cont

   Notes:

   Line 3, 4 and 5:  Multiple lines are grouped together.

   Line 6: If a baseflow is used to report a
   time TIME_TO_ABOVE_BASEFLOW.OUT.  Place Line 6 

   after each segment.

.. container::
   :name: page91-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023900090.png
   81

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   A1(I)

   **r**

   **0.0 - **

   Coefficient for the variable area regression relationships (see 

   comment 5).

   A2(I)

   **r**

   **0.0 - **

   Exponent for the variable area regression relationships (see 

   comment 5).

   A11(I)

   **r**

   **0.0 - **

   Coefficient for the variable area regression relationships for 

   flow depth above EXCDEP(I) (see comment 5).

   A22(I)

   **r**

   **0.0 - **

   Exponent for the variable area regression relationships for 

   flow depth above EXCDEP(I) (see comment 5).

   B1(I)

   **r**

   **0.0 - **

   Coefficient for the variable wetted perimeter relationships 

   (see comment 5).

   B2(I)

   **r**

   **0.0 - **

   Exponent for the variable wetted perimeter relationships (see 

   comment 5).

   B11(I)

   **r**

   **0.0 - **

   Coefficient for the variable wetted perimeter relationships for 

   flow above EXCDEP(I) (see comment 5).

   B22(I)

   **r**

   **0.0 - **

   Exponent for the variable wetted perimeter relationships for 

   flow above EXCDEP(I) (see comment 5).

   BANKELR(I)

   **r**

   **0.01 - **

   Right bank elevation looking downstream  (see comment 

   12).  

   BANKELL(I)

   **r**

   **0.01 - **

   Left bank elevation looking downstream (see comment 12).  

   C1(I)

   **r**

   **0.0 - **

   Coefficient for the variable top width relationships (see com-

   ment 5).

   C2(I)

   **r**

   **0.0 - **

   Exponent for the variable top width relationships (see com-

   ment 5).

   C11(I)

   **r**

   **0.0 - **

   Coefficient for the variable top width relationships for flow 

   depth above EXCDEP(I) (see comment 5).

   C22(I)

   **r**

   **0.0 - **

   Exponent for the variable top width relationships for flow 

   depth above EXCDEP(I) (see comment 5).

   CHANCHAR

   **c**

   **C, E, B**

   Character line identifier for ICONFLO ‘C’   and NOEX-

   CHANGE ‘E’ channel elements. 'B' is for baseflow after a 

   segment.  Variable is case sensitive and it must be upper case.

   ICONFLO1(J)

   **i**

   **1 - NNOD**

   Tributary channel element at confluence (see comment 8).

   Variable Descriptions for the 

   CHAN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page92-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023910091.png
   82

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ICONFLO2(J)

   **i**

   **1 - NNOD**

   Main channel element at the confluence.

   DEPINITIAL(K)

   **r**

   **0.0 - **

   ** or **

   **-1**

   DEPINITIAL(K) = 0 for no initial channel flow depth in the 

   | channel segment (default).
   | DEPINITIAL(K) =  Initial flow depth for the all channel 

   | elements in the  channel segment (optional).  
   | DEPINITIAL(K) = -1 to assign an initial water surface eleva-

   tion to a channel reach. Include Line 3 (see comment 2). 

   EXCDEP(I)

   **r**

   **0.0 - **

   Channel depth above which a second variable area relation-

   ship will apply (see comment 4).  If only one channel geom-

   etry relationship is used, set EXCDEP(I) = 0.

   FCN(I) 

   **r**

   **0.01 - 0.15**

   Average Manning’s n roughness coefficient the channel in 

   the grid element ICHANGRID (see comments 6 and 19).

   FCD(I)

   **r**

   **.01 - 1000**

   Channel thalweg depth (ft or m).  The thalweg depth is the 

   deepest part of the channel measured from the lowest top of 

   bank (see comment 1).

   FCW(I)

   **r**

   **0.1 - **

   | Set FCW(I) = channel width for rectangular channel.
   | Set FCW(I) = width of channel base for trapezoidal channel.  

   FROUDC(K)

   **r**

   **0.0 - 5**

   Maximum channel Froude number if the Froude number 

   exceeds FROUDC, the Manning’s n roughness value is 

   increased by 0.001. Set FROUDC = 0 for no adjustments 

   of the n-value in a given channel segment. The increased n-

   values are reported in the ROUGH.OUT and CHAN.RGH 

   files (see comment 7).

   IBASEFLOW(K)

   **i**

   **0.0 - **

   Baseflow of a channel to establish a flow condition for floodwave 

   arrival time.  Place this line after each segment if more than one 

   segment is used.

   ICHANGRID(I)

   **i**

   **1 - NNOD**

   Channel grid element number.

   IEND

   **i**

   **1 - NNOD**

   Last channel element for which a starting water surface eleva-

   tion is specified.

   Variable Descriptions for the 

   CHAN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page93-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023920092.png
   83

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ISEDN(K)

   **i**

   **0 - 10**

   Sediment transport equation or data group for routing by 

   size fractions for the channel segment.  Set ISED = 1 in the 

   CONT.DAT file to use this option.  Choose one of the two 

   | following options for each channel segment:  
   | For sediment routing without size fractions:  Set ISEDN(K) 

   = 1 - 11 (one of eleven sediment transport equations).  

   or 

   For sediment routing with size fractions:  Set ISEDN(K) = 

   sediment data group (Line 3 in SED.DAT which includes a 

   sediment transport equation).

   ISTART

   **i**

   **1 - NNOD**

   First channel element for which a starting water surface eleva-

   tion is specified.  

   NXSECNUM(I)

   **i**

   **1 **

   **to  **

   **NNODC**

   Surveyed cross section number assigned in the XSEC.DAT file that
   will 

   represent the specific channel element.  This variable is used only
   for the 

   cross section data option (see comments 14 and 18). Set NXSECNUM = 

   0, if there is no cross section data for the channel element (I).
    The cross 

   section data is interpolated and assigned in the PROFILES program. 

   ROUGHADJ

   **r**

   **0.00 - 1.2**

   A coefficient used in the depth adjustment of the Manning’s n-value
   and the 

   shallown value for channel segments (see comment 17).

   SHAPE

   **c**

   **R, V, T or **

   **N**

   | Character line identifier (see comments 4 and 16); 
   | SHAPE = ‘R’, rectangular channel geometry (width and depth data). 

   SHAPE = ‘V’, variable area channel geometry (power relationships).

   SHAPE = ‘T’, trapezoidal channel (bottom width, depth and slopes
   data).

   | SHAPE = ‘N’, channel cross sections (cross section survey data). 
   | Variable is case sensitive and it must be upper case.

   WSELEND

   **r**

   **0 - 30,000**

   **0 - 9,000**

   Ending water surface elevation for the channel element IEND (ft or
   m).

   WSELSTART

   **r**

   **0 - 30,000**

   **0 - 9,000**

   Starting water surface elevation for the channel element ISTART (ft
   or m).

   Variable Descriptions for the 

   CHAN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page94-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023930093.png
   84

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   CHAN.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   XLEN(I)

   **r**

   **0.01 - **

   Channel length contained within the grid element ICHANGRID (ft).  If 

   more than one channel exists in a given grid element, assign XLEN(I)
   equal 

   to the average representative flow length in one direction (see
   comments 9, 

   10, 13 and 15).

   ZL(I)

   **r**

   **0.01 - 100**

   ZL(I) is the left side slope of  the trapezoidal channel.

   ZR(I)

   **r**

   **0.01 - 100**

   ZR(I) is the right side slope of the trapezoidal channel.

.. container::
   :name: page95-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023940094.png
   85

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   CHAN.DAT File

   1.  The channel bottom elevation is calculated by the model based on
   the input 

   channel depth and the floodplain or bank elevation.

   2.  When DEPINITIAL > 0, an initial depth is specified for all the
   elements in that 

   channel segment.  Setting DEPINITIAL = -1 will assign starting and
   ending 

   water surface elevations (WSELSTART and WSELEND, Line 3) for a
   channel 

   segment beginning with channel element ISTART and ending with
   channel 

   element IEND.  Only one starting and ending water surface is allowed
   per 

   channel segment.  The water surface elevations are computed for the
   channel 

   elements between the ISTART and IEND elements based on the
   interpolations 

   of the channel length and the specified water surface elevations.  

   3.  Dividing the channel into segments may simplify reviewing the
   results.  Or-

   ganize the CHAN.DAT from upstream to downstream. The order of the grid 

   element numbers in the file is not important (e.g. upstream channel
   element 

   446 can precede downstream channel element 31). The channel grid
   elements 

   must be contiguous in each segment.

   4.  If channel geometry is being simulated with regression
   relationships (SHAPE = 

   ‘V’), then the area versus depth power relationships must be
   specified:

   A = ad

   b

   Where:

   A = area of the channel

   d = depth to thalweg

   a = coefficient

   b = exponent

   Similar relationships are required for wetted perimeter and top
   width.  There 

   is a limit of two channel geometry relationships per channel element.
    A sec-

   ond geometry relationship may be useful if there is a significant
   change in the 

   cross section (e.g. an island).  If two power relationships are used
   to represent a 

   natural cross section, then the maximum depth (EXCDEP) to which the
   first 

   | relationship applies must be specified. 
   | The second regression applies when the flow depth is greater than EXCDEP, 

   but does not include the lower flow area.  The two variable area
   cross section 

   relationships are unique and separate.  The total cross section flow
   area is the 

   sum of the lower flow and upper (second relationship) flow areas.
    The channel 

   top width is computed directly from the second relationship.  The
   area, wet-

   ted perimeter and top width are evaluated using the upper flow depth
   given 

.. container::
   :name: page96-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023950095.png
   86

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   by total depth - EXCDEP.  To analyze the
   upper channel geometry using the 

   XSEC program, only the cross section coordinates above the EXCDEP
   depth 

   | are used.
   | These channel geometry relationships apply only to flow depths that
     are less 

   than the channel depth (lower than the top of bank).  When the flow
   depth 

   exceeds the top of bank, then the channel geometry above bank is
   evaluated as 

   a rectangle.  Abrupt transitions between contiguous channel elements
   should 

   be avoided unless they actually exist.   

   5.  A preprocessor program XSEC is available in the FLO-2D
   subdirectory to de-

   termine the regression coefficient and exponents (A1, A2, A11, A22,
   B1, B2, 

   B11, B22, B2, C1,C11, C22) in Line 2b.

   6.  A cross section width can exceed the width of the grid element.  For example, 

   a channel cross section that is 100 ft wide can be used in a 20 ft
   grid system.  

   The model automatically determines the number of grid elements
   required by a 

   channel cross section.  If the cross section width exceeds 95% of
   the combined 

   bank elements width or if there is less than 5% floodplain surface
   area left in the 

   bank element after removing the channel surface area, the channel
   will extend 

   the right bank over another grid element looking downstream.

   7.  Set the channel roughness to a reasonable n-value and then set
   the FROUDC 

   variable to an appropriate value (e.g. 0.95 to ensure subcritical
   flow).  FLO-

   2D will adjust the roughness values according to the limiting Froude number 

   criteria (see the ROUGH.OUT file).  Changes to the channel n-values
   may be 

   accepted by replacing the CHAN.DAT file with the CHAN.RGH file.
    Just 

   delete the original CHAN.DAT file and rename the CHAN.RGH to CHAN.

   DAT.

   8.  The confluence can be made by the tributary joining either side
   of the main 

   channel.  List the tributary first and the main channel second in
   Line C.

   9.  Use the PROFILES program to review the channel slope and adjust
   the bed el-

   evations to create a more uniform average channel reach slope.  The
   PROFILES 

   program can interpolate cross sections and slope for surveyed cross
   sections.

   10.  The key to channel routing is to balance the relationship
   between the slope, 

   flow area and roughness.  Channel routing is more stable if the
   natural cross 

   section routing routine is used (SHAPE = N).  When one cross section
   is as-

   signed to several grid elements it will be necessary to interpolate
   both the slope 

   and the cross section geometry in the PROFILES program to create a smooth 

   average channel slope.  Review the PROFILES program instructions for
   cross 

   section and channel bed slope interpolation.  If there is more than
   one surveyed 

   cross section per channel element, use the one that has the greatest
   hydraulic 

   control to represent the channel.

.. container::
   :name: page97-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023960096.png
   87

   **D**

   **ata**

   ** I**

   **nPut**

   11.  At a channel confluence, the next downstream channel element bed
   elevation 

   must be lower than the confluence bed elevation creating a positive
   slope down-

   stream of the confluence.

   12.  If different bank elevations are assigned, the model automatically extends the 

   channel into separate grid elements, one grid element containing each
   bank.  

   The model may be required to do this anyway if the channel is wider
   than the 

   grid element.  

   13.  The first two channel elements in a segment should have a
   positive slope in the 

   downstream direction. This is important for inflow channel elements.
    There 

   should also be a
   positive slope into the channel outflow nodes.  This will im-

   prove the numerical stability around the inflow and outflow nodes.

   14.  After deleting a channel element, remove the cross section for
   that channel ele-

   ment from the XSEC.DAT file and renumbered in the PROFILES program.  

   If cross sections are mixed with other channel geometry (trapezoidal
   or rectan-

   gular), the cross section elements should be grouped into segments to
   identify 

   the reaches with similar channel geometry.

   15.  Eliminate channel elements that have a XLEN less than 50% of the
   SIDE (grid 

   element width).  This can be accomplished by connecting the channel
   elements 

   across the diagonal and eliminating the middle channel element.  

   16.  If the channel routing is unstable or numerically surging,
   reduce the Courant 

   number C in the TOLER. DAT by 0.1.

   17.  To improve the timing of the floodwave progression through the
   system, a 

   depth variable roughness can be assigned on a reach basis.  The basic
   equation 

   for the channel element roughness n

   d

    as function of flow depth is:

   n

   d

    = n

   b

    a e

   -(b depth/dmax)

   where:

   n

   b

    =  bankfull discharge roughness 

   depth = flow depth

   dmax = bankfull flow depth

   a = 1/e

   -b

   b = roughness adjustment coefficient prescribed by the user (0 to
   1.2)

   This equation prescribes that the variable depth channel roughness is
   equal to 

   the roughness at bankfull discharge.  If the user assigns a ROUGHADJ value 

   (from 0 to 1.2) as the roughness adjustment coefficient b for a given
   reach, the 

   roughness will increase with a decrease in flow depth.  The higher
   the coeffi-

   cient b, the greater the increase in roughness.  This roughness
   adjustment will 

   slow the progression of the floodwave by increasing the roughness for
   less than 

   bankfull discharge. The plane bed roughness set for bankfull
   discharge will not 

.. container::
   :name: page98-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023970097.png
   88

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   be affected.  For example, if the depth is 20% of the bankfull
   discharge and 

   the roughness adjustment coefficient b is set to 0.44,
   the hydraulic roughness 

   Manning’s n-value will be 1.4 times the roughness prescribed for
   bankfull flow.  

   Assigning a ROUGHADJ value may reduce high Froude numbers.

   A channel spatially variable shallow n-value assigned to the depths
   less than 0.2 

   ft (0.067 m) is defined by applying the ROUGHADJ to each channel
   reach.:

   SHALLOWN = ROUGHADJ / 2

   where:  ROUGHADJ is assigned to line 1 of each channel segment.

   18.  Instructions for creating the cross section channel
   geometry data files are out-

   lined in Lesson 14 of the Workshop Lessons.  The lessons are found in the 

   FLO-2D Pro Documentation folder.

   19.  Surveyed water surfaces can be automatically compared with the
   predicted wa-

   ter surface in the PROFILES program by creating a WSTIME.DAT file.
    This 

   file contains a list of the channel element, water surface elevation
   and time.  

   Create this file to calibrate the model to known water surface
   elevation data.  

   The time of the surveyed water surface elevation must correspond to
   the model 

   flood routing timing.

.. container::
   :name: page99-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023980098.png
   89

   **D**

   **ata**

   ** I**

   **nPut**

   CHANBANK.DAT File Variables 

     26    99 

   Line 1:  

   **LEFTBANK(K)   RIGHTBANK (K)   **

   *K = 1, number of channel elements*

   Notes:

   If ICHANNEL = 0 in the CONT.DAT file, omit this file.

   Line 1:  If a channel element width is contained within one grid
   element and no individual bank ele-

   ments are assigned then 

   **RIGHTBANK(K)**

    is set to zero.

   CHANBANK.DAT File Example

          26       99

          39      136

          54      156

          71      176

          90      196

         109      216

         127      236

         147      256

         167      276

         187      315

         207      336

         226      356

         247      377

         267      398

         286      418

         307      439

         327      460

         348      481

         369      502

   FILE:  CHANBANK.DAT 

   CHANNEL BANK DATA

.. container::
   :name: page100-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 2023990099.png
   90

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   LEFTBANK

   **i**

   **1 - NNOD**

   Left bank channel grid element. Assigned in CHAN.DAT as 

   the ICHANGRID variable.  See comments 1 to 3.  

   RIGHTBANK

   **i**

   **1 - NNOD**

   Right bank channel grid element corresponding the LEFT-

   BANK element.

   Variable Descriptions for the 

   CHANBANK.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   CHANBANK.DAT File 

       

   1.  The RIGHTBANK element is automatically assigned in the GDS or
   QGIS.  

   Make adjustments to the right bank channel element if the channel is
   too wide 

   or narrow by reassigning the right bank element in the GDS or
   QGIS.  It is 

   also assigned if unequal channel bank elevations are assigned in
   CHAN.DAT 

   regardless if the channel will fit into one grid element.  

   2.  The procedure for assigning the right bank element is to first select the left bank 

   element in the GDS or QGIS, open the channel segment editor box and
   then 

   assign the right bank element.  The GDS or QGIS will automatically
   check the 

   channel width to determine if the channel bank assignments are
   appropriate 

   and will report and required modifications in the ERROR.CHK file.

   3.  Channel right bank assignments are not required if the channel
   cross section 

   will fit in one grid element and no bank elevations are assigned in
   CHAN.

   DAT.  

.. container::
   :name: page101-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310000100.png
   91

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  XSEC.DAT 

   CROSS SECTION DATA

   XSEC.DAT File Variables

   X   1      X-CI-27.1 

   Line 1: 

   **XSECCHAR = ‘X’   NXSECUM(I)   XSECNAME(I)  I=1,   ..**

   ** **

   ** **

   **n number of cross sections**

   25.0  5234.90 

   Line 2: 

   **XI(I,J)   YI(I,J)   **

   30.0  5231.53 

   Line 2: 

   **XI(I,J)   YI(I,J)  **

   35.0  5230.20 

   Line 2: 

   **XI(I,J)   YI(I,J)  **

   Notes:

   If ICHANNEL = 0 in the CONT.DAT file, omit this file.

   Set SHAPE = ‘N’ (line 2d) in the CHAN.DAT file to use this file.

   Line 1:  This line is repeated for each cross section.

   Line 2:  This line is repeated for the Station, Elevation pairs.

   XSEC.DAT File Example

    X     1     X-CI-27.1

        

   0.0     

   5235.07

       

   10.0 

   5235.17

    25.0 5235.31

    30.0 5231.84

    ...  ...

    ...  ...

    288.0  5236.01

    294.0  5236.51

    313.0  5237.00

      X    2       CI-27.1

    25.0 5234.90

    30.0 5231.53

    35.0 5230.20

    40.0 5228.50

    45.0 5227.20

    50.0 5224.35

    ...  ...

.. container::
   :name: page102-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310100101.png
   92

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   NXSECNUM(I) 

   **i**

   **1**

   **to **

   **NNODC**

   Cross section number starting with 1 and ending with the last
   surveyed cross 

   section.  This number will be assigned to the channel element
   NXSECNUM 

   in CHAN.DAT (see comment 1).

   XI(I,J)

   **r**

   **0.0 - **

   Cross section station distance from the left end point (ft or m).
    The value of 

   XI can be either positive or negative. 

   XSECHAR

   **c**

   **X**

   Character ‘X’  that identifies Line 1. Variable is case sensitive and
   it 

   must be upper case.

   XSECNAME(I)

   **c**

   **Alpha **

   **Numeric**

   Cross section name (less than 15 characters, not case sensitive).
    This name is 

   for cross section ID purposes only and it is not used by the model..
    Do not 

   use spaces in the name.

   YI(I,J)

   **r**

   **0 - 30,000**

   **0 - 9,000**

   Cross section elevation (ft or m) at each station.  The value of YI
   can either 

   positive or negative indicating elevations below sea level.

   Variable Descriptions for the 

   XSEC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   XSEC.DAT File 

       

   1. 

   The NXSECNUM in XSEC.DAT and CHAN.DAT must match and be listed in
   order from 1 

   to N number of natural channel elements.  The natural channel
   elements in the CHAN.DAT file 

   must start at 1 and continue in sequence to NNODC from the top of the
   file to the end.  Use the 

   GDS, QGIS or PROFILES programs to interpolate a cross section to each
   channel element.

.. container::
   :name: page103-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310200102.png
   93

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  HYSTRUC.DAT 

   HYDRAULIC STRUCTURE  DATA

   HYSTRUC.DAT File Variables

    

   Line 1: 

   **STRUCHAR = ‘S’   STRUCTNAME   IFPORCHAN(I)   ICURVTABLE(I)**

   ** **

   ** **

   **INFLONOD(I)   OUTFLONOD(I)   INOUTCONT(I)   HEADREFEL(I)**

   ** **

   ** **

   **CLENGTH(I)   CDIAMETER(I)   **

   *I = number of structures*

   S Patagonia  1  0  1713  1827  0  4425.23  0.0  0.0 

    

   Line 2: 

   **STRUCHAR = ‘C’  HDEPEXC(I,J)   COEFQ(I,J)   EXPQ(I,J)  
   COEFA(I,J)**

   ** **

   ** **

   **EXPA(I,J)   **

   *I = number of structures, J = number of curves*

   * *

   Line 2: 

   **STRUCHAR = ‘B’  IBTYPE(I)   COEFFP(I)  C_PRIME_USER(I)   **

   ** **

   ** **

   **KF_COEF(I)   KWW_COEF(I)   KPHI_COEF(I)   KY_COEF(I)   **

   ** **

   ** **

   **KX_COEF(I)   KJ_COEF(I)  **

   *I = number of bridges in bridge routine*

   * *

   Line 3: 

   **STRUCHAR = ‘B’  BOPENING(I)   BLENGTH(I)   BN_VALUE(I)**

   ** **

   ** **

   **UPLENGTH12(I)   LOWCHORD(I)   DECKHT(I)   DECKLENGTH(I)   **

   ** **

   ** **

   **PIERWIDTH(I)   SLUICECOEFADJ(I)   ORIFICECOEFADJ(I)   **

   ** **

   ** **

   **COEFFWEIRB(I)   WINGWALL_ANGLE(I)   PHI_ANGLE(I)  
   LBTOEABUT(I)   **

   **  RBTOEABUT(I) **

   ** **

    

   *I = number of bridges in bridge routine*

   C  20.0  3.543  0.890

    

   Line 3: 

   **STRUCHAR = ‘R’  REPDEP(I,J)  RQCOEFQ(I,J)   RQEXP(I,J)   **

   ** **

   ** **

   **RACOEF(I,J)   RAEXP(I,J)   **

   *I = number of structures, J = number of curves*

   R  12.0  0.00  1.0

    

   Line 4: 

   **STRUCHAR = ‘T’  HDEPTH(I,J)  QTABLE(I,J)   ATABLE(I,J) **

   **  **

   *I = number of structures, J = number of datasets in table*

   T   0   0

    

   Line 5: 

   **STRUCHAR = ‘F’  TYPEC(I)  TYPEEN(I)  CULVERTN(I)  KE(I)   **

   ** **

   ** **

   **CUBASE(I)   MULTBARRELS(I)   **

   **  **

   *I = number of structures, Set ICURVTABLE = 2 in Line 1.*

   F   1   2  0.040   0.1   0.0   1

    

   Line 6: 

   **STRUCHAR = ‘D’ ISTORMDOUT(I), STORMDMAXQ(I), **

   **  **

   *I = number of drain structures.*

   D   4   15 

    

.. container::
   :name: page104-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310300103.png
   94

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   HYSTRUC.DAT File Example

   S   BridgeA   1   0   1713   1827   0    4425.23   0.0   0.0

   C   20.0   3.543   0.890  

   S   BridgeB   0   0   2503   2725   1   0.0   0.0   0.0

   C   5.0     25.023    1.035   

   C   10.0   30.00      1.4       

   R   12.0     0.00      1.0

   S   Wier   1   1   1856   1945   0   4421.18   0.0   0.0

   T   0.0            0.0

   T   5.0        250.0

   T   8.0      5500.0

   T   10.0    1000.0

   T   12.5    1500.0

   S CulvertA  1  2   4417    4562  0   0.0    100.    6.

     F   1   2   0.004    0.1    0.0  1

   FILE:  HYSTRUC.DAT

   HYDRAULIC STRUCTURE  DATA

   HYSTRUC.DAT File Notes

   Notes:

   If IHYDRSTRUCT = 0 in the CONT.DAT file, omit this  file.

   Line 2:  Include this line for rating curve.  Repeat this line for
   each rating 

   curve.

   Line 1, 2:  If CLENGTH(I) = 0, ignore COEFA(I,J) AND EXPA(I,J)

   Line 3:  If a replacement rating curve is required, include this
   line.

   Line 1, 3:  If CLENGTH(I) = 0, ignore RACOEF(I,J) and RAEXP(I,J).

   Line 5:  For generalized culverts (ICURVTABLE(I) = 2), if TYPEC(I) =
   2 

   (round pipe), CUBASE(I) = 0,   

   Line 4:  If a rating table is used, include this line.  Repeat for
   each depth and 

   discharge pair.

   Line 1, 4:  If CLENGTH(I) = 0, ignore ATABLE(I,J).

.. container::
   :name: page105-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310400104.png
   95

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ATABLE (I,J)

   **r**

   **0.01 - **

   When the long culvert routine is used (CLENGTH(I) > 1) must be in-

   cluded as data input.  QTABLEA(I,J)  is  the hydraulic structure flow
   area 

   for each headwater depth in the rating table (discharge).

   COEFA(I,J)

   **r**

   **0 - **

   When the long culvert routine is used (CLENGTH(I) > 1),.  COEFQ(I,J) 

   is the flow area rating curve coefficient where the flow area A is
   ex-

   pressed as a power function of the headwater depth.  A = COEFA(I,J)
   * 

   depth

   EXPA

   (I,J).

   COEFQ(I,J)

   **r**

   **0 - **

   Discharge rating curve coefficients as a power function of the
   headwater 

   depth.  Q = COEFQ(I,J) \* depth

   EXPQ(I,J)

    (see comment 1).  If COEFQ(I,J) 

   = 0, then the discharge is computed as normal depth flow routing.

   CDIAMETER(I,J)

   **r**

   **0.1 - **

   Circular culvert diameter (ft or m).  For the generalized culvert
   equations 

   CDIAMETER is the circular culvert diameter or the box culvert height 

   (see comment 12).

   CLENGTH(I)

   **r**

   **1 - **

   **1 - **

   Culvert length (ft or m).  When a long culvert is simulated (>500 ft
   or 

   152.4 m), CLENGTH must be assigned to that culvert’s length to
   activate 

   the long culvert routing routine.

   CUBASE(I)

   **r**

   **0 - **

   Flow width (ft or m) of box culvert for TYPEC(I) = 1.  For 

   a circular culvert, CUBASE = 0.

   CULVERTN(I)

   **r**

   **0.012 - **

   **0.25**

   Culvert Manning’s roughness coefficient.  Default = 0.03.

   EXPA(I,J)

   **r**

   **0 - **

   When the long culvert routine is used (CLENGTH(I) > 1), EXPQ(I,J)
   is  

   the hydraulic structure flow area exponent where the flow area is expressed 

   as a power function of the headwater depth.

   EXPQ(I,J)

   **r**

   **0 - **

   Hydraulic structure discharge exponent where the discharge is
   expressed as 

   a power function of the headwater depth.

   HDEPEXC (I,J)

   **r**

   **.01 - 1000**

   **0.25 - 300**

   Maximum depth that a given hydraulic structure rating curve is valid
   (ft 

   or m).

   HDEPTH(I,J)

   **r**

   **.01 - 1000**

   **0.25 - 300**

   Headwater depth for the structure headwater depth-discharge rating
   table 

   (ft or m) (see comment 2).

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page106-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310500105.png
   96

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   HEADREFEL(I)

   **r**

   **.01 - **

   **30,000**

   **.25 - 9,000**

   Reference elevation above which the headwater depth is determined
   for 

   either the discharge rating curve or rating table.  Set HEADREFEL(I)
   = 

   0.0 to use the existing channel bed or floodplain elevation for the
   reference 

   elevation to compute the headwater depth (ft or m).

   ICURVTABLE(I)

   **s**

   **0 = curve**

   **1 = table**

   **2 = culveq**

   | Set ICURVTABLE(I) =  0 for a structure rating curve.   
   | Set  ICURVTABLE(I) = 1 for a structure rating table.  
   | Set ICULVTABLE(I) = 2 to use the culvert equations (see comment 5).

   IFPORCHAN(I)

   **s**

   **0, 1, 2 or 3**

   IFPORCHAN(I) = 0; for a floodplain structure (shares discharge
   between 

   two floodplain elements).

   IFPORCHAN(I) = 1; for a channel hydraulic structure (shares
   discharge 

   between two channel elements).

   IFPORCHAN(I) = 2; for a floodplain to channel structure (shares dis-

   charge between a floodplain element {inflow} and channel structure
   {out-

   flow})(see comment 7).

   IFPORCHAN(I) = 3; for a channel to floodplain structure (shares 

   discharge between a channel {inflow} element and a floodplain
   element 

   {outflow}) (see comment 13).

   INFLONOD(I)

   **i**

   **1 - **

   **NNOD**

   Grid element containing the hydraulic structure or structure inlet.

   INOUTCONT(I,J)

   **s**

   **0 = inlet**

   **1 = revised**

   **2 = outlet / **

   **revised**

   INOUTCONT(I,J) = 0; to compute the discharge based on only the 

   headwater depth above the appropriate floodplain or channel bed
   eleva-

   tion (or reference elevation if assigned).   Suggested revisions are
   listed in 

   REVISED_RATING_TABLE.OUT.  No tailwater effects or potential 

   | upstream flow are considered.
   | INOUTCONT(I,J) = 1; reduced discharge for tailwater submergence, 

   , but does not  allow upstream flow.  Suggested rating  table
    revisions 

   | posted to REVISED_RATING\_ TABLE.OUT.  
   | INOUTCONT(I,J) = 2; reduced discharge for tailwater submergence.  

   Upstream flow is possible.  Suggested rating table revisions posted
   to 

   REVISED_RATING_TABLE.OUT.

   Necessary for all structure types if submergence and upstream flow
   is 

   required.

.. container::
   :name: page107-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310600106.png
   97

   **D**

   **ata**

   ** I**

   **nPut**

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ISTORMDOUT(I)

   **i**

   **1 - **

   **NNOD**

   Hydraulic structure outflow grid element number used to simulate a 

   simplified storm drain. ISTORMDOUT is a junction or outflow node 

   for a number of inflow nodes (see comment 11). 

   KE(I)

   **r**

   **0.01 - 1.0**

   Culvert entrance loss coefficient (see comment 9).

   MULTBARRELS(I)

   **i**

   **1 - 100**

   Multiple barrel option for generalized culvert equation.   

   The engine will multiply the Q by the number of barrels 

   (see comment 20).

   OUTFLONOD(I)

   **i**

   **1 - **

   **NNOD**

   Grid element receiving the hydraulic structure discharge (structure
   outlet). 

   OUTFLONOD does not have to be contiguous to INFLONOD grid 

   element.

   QTABLE(I,J)

   **r**

   **0.01 - **

   Hydraulic structure discharges for the headwater depths
   in the rating table 

   (discharge) (see comments 3 and 4).

   REPDEP(I,J)

   **r**

   **0.01 - **

   Flow depth (ft or m) that if exceeded will invoke the replacement
   structure 

   rating curve parameters for simulating a blockage or a change in the
   rating 

   curve.

   RACOEF(IJ)

   **r**

   **0 - **

   When the long culvert routine is used (CLENGTH(I) > 1), RACOEF(I,J) 

   is the structure rating curve flow area replacement coefficient.
    There should 

   be the same number of rating curve pairs of coefficients and
   exponents.

   RAEXP(IJ)

   **r**

   **0 - **

   When the long culvert routine is used (CLENGTH(I) > 1), RAEXP(I,J)
   is  

   the structure rating curve flow area replacement exponents.  There
   should 

   be the same number of rating curve pairs of coefficients and
   exponents.

   RQCOEF(I,J)

   **r**

   **0 - **

   Structure rating curve discharge replacement coefficients.  There
   should be 

   the same number of rating curve pairs of coefficients and exponents

   RQEXP(I,J)

   **r**

   **0 - **

   Structure rating curve discharge replacement exponents.  There should
   be 

   the same number of rating curve pairs of coefficients and exponents.

.. container::
   :name: page108-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310700107.png
   98

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   STRUCHAR

   **c**

   **S, C, R, T **

   **or D**

   | Character that identifies the use of Line 2, 3, 4 or 6 where: 
   | STRUCHAR = ‘S’ for the structure control, (Line 1); 

   STRUCHAR = ‘C’ for a rating curve (Line 2); 

   STRUCHAR = ‘R’ for replacement rating curve (Line 3); 

   STRUCHAR = ‘T’ for a rating table (Line 4);

    STRUCHAR = ‘F’ for culvert equations (Line 5);

    STRUCHAR = ‘D’ for storm drain (Line 6).

   Variable is case sensitive and it must be upper case.

   STORMDMAXQ(I)

   **r**

   **0 - **

   Maximum allowable discharge (conveyance capacity) of the collection 

   pipe represented by the ISTORMDOUT element. (cfs or cms)

   STRUCTNAME(I)

   **c**

   **Alpha **

   **Numeric**

   Hydraulic structure name (15 characters or less).  This name is for
   user 

   identification purposes only.   No spaces allowed in the name.

   TYPEC(I)

   **s**

   **1 = box**

   **2 = pipe**

   Culvert switch, either 1 or 2.  Set TYPEC(I) = 1 for a box culvert
   and 

   TYPEC(I) = 2 for a pipe culvert (see comment 8).

   TYPEEN(I)

   **s**

   **1, 2, 3**

   Culvert switch.  Set TYPEEN(I) for entrance type 1, 2, or 3. (see
   com-

   ment 8).

   STRUCHAR

   **c**

   **B**

   Character identifier for the bridge routine (see comment 16).

   IBTYPE

   **i**

   **1 - 4**

   Type of bridge configuration (see White Paper graphics)

   COEFF\*

   **r**

   **0.1 - 1.0**

   Overall bridge discharge coefficient – assigned or computed (default = 0.).  

   See comment 17.

   C_PRIME_USER\*

   **r**

   **0.5 - 1.0**

   Baseline bridge discharge coefficient to be adjusted with detail
   coefficients

   KF_COEF\*

   **r**

   **0.9 - 1.1**

   Froude number coefficient – assigned or computed (= 0.)

   KWW_COEF\*

   **r**

   **1.0 - 1.13**

   Wingwall coefficient – assigned or computed (= 0.)

   KPHI_COEF\*

   **r**

   **0.7 - 1.0**

   Flow angle with bridge coefficient – assigned or computed (= 0.)

   KY_COEF\*

   **r**

   **0.85 - 1.0**

   Coefficient associated with sloping embankments and vertical
   abutments 

   (= 0.)

   KX_COEF\*

   **r**

   **1.0 - 1.13**

   Coefficient associated with sloping abutments – assigned or computed (= 

   0.)

   KJ_COEF\*

   **r**

   **0.6 - 1.0**

   Coefficient associated with pier and piles – assigned or computer (=
   0.)

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page109-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310800108.png
   99

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   BOPENING

   **r**

   **0.0 - ∞**

   Bridge opening width (ft or m)

   BLENGTH

   **r**

   **0.0 - ∞**

   Bridge length from upstream edge to downstream abutment (ft or m)

   BN_VALUE

   **r**

   **0.030 - **

   **0.200**

   Bridge reach n-value

   UPLENGTH

   **r**

   **0.0 - ∞**

   Distance to upstream cross section unaffected by bridge backwater (ft
   or 

   m)

   LOWCHORD

   **r**

   **0.0 - ∞**

   Average elevation of the low chord (ft or m).  

   DECKHT

   **r**

   **0.0 - ∞**

   Average elevation of the top of the deck railing for overtop flow (ft
   or m)

   DECKLENGTH

   **r**

   **0.0 - ∞**

   Deck weir length (ft or m)

   PIERWIDTH

   **r**

   **0.0 - ∞**

   Combined pier or pile cross section width (flow blockage width in ft
   or 

   m)

   SLUICECOEFADJ

   **r**

   **0.0 - 2.0**

   Adjustment factor to raise or lower the sluice gate coefficient which
   is 0.33 

   for Yu/Z = 1.0.  See comment 18.

   ORIFICECOEF-

   ADJ

   **r**

   **0.0 - 2.0**

   Adjustment factor to raise or lower the orifice flow coefficient
   which is 

   0.80 for Yu/Z = 1.0

   COEFFWEIRB

   **r**

   **2.65 - 3.21 **

   Weir coefficient for flow over the bridge deck.  For metric:
    COEFFWI-

   ERB x 0.552.  Comment 19.

   WINGWALL_AN-

   GLE

   **r**

   **30⁰ - 60⁰**

   Angle the wingwall makes with the abutment perpendicular to the flow

   PHI_ANGLE

   **r**

   **0⁰ - 45⁰**

   Angle the flow makes with the bridge alignment perpendicular to the 

   flow

   LBTOEABUT

   **r**

   **ELEVA-**

   **TION**

   Toe elevation of the left abutment (ft or m)

   RBTOEABUT

   **r**

   **ELEVA-**

   **TION**

   Toe elevation of the right abutment (ft or m)

   \* If the coefficient is assigned 1.0, that bridge coefficient is 

   either not important or has no effect.

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page110-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202310900109.png
   100

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   HYSTRUC.DAT File 

       

   1.  There are two approaches for bridge flow, rating curve/table or
   computing the bridge flow hydraulics 

   directly as free surface, pressure flow or pressure and weir flow.  For the rating curves, the hydraulic 

   structure discharge between either floodplain or channel grid
   elements can be simulated as a function 

   of the headwater depth, Q = COEFQ*depth

   EXPQ

   , where COEFQ and EXPQ are specified coefficients 

   and exponents which are valid for a depth not to exceed HDEPEXC.  The
   grid elements containing 

   the structure inlet and outlets must be specified.  The inlet and
   outlet grid elements do not have to be 

   contiguous.  The structure discharge (such as a culvert, weir or
   bridge) may either inlet or outlet control 

   as long as the discharge is specified as power function of the
   headwater depth.  

   2.  When the headwater depth exceeds the specified depth (HDEPEXC)
   for which the original rating curve 

   relationship is valid, a second replacement relationship is invoked.
    These multiple relationships can be 

   used to specify structure blockage or a change in the rating curve.
    For example, if a height of 5 ft cor-

   responds to the top of a culvert for a discharge of up to 300 cfs, then a second rating curve relationship 

   for flows over a roadway could be based on a flow depths starting at
   6 ft above the culvert invert that 

   could correspond to a discharge of greater than 500 cfs.  Structure
   blockage can be simulated by setting 

   the replacement coefficient (RQCOEF) equal to zero.

   3.  If a hydraulic structure rating table is used, a linear
   interpolation between two headwater depths in the 

   rating table is applied to estimate the discharge for a headwater
   depth computed by the model. 

   4.  The rating table should always have the first pair of
   depth-discharge data as headwater depth = 0 and 

   discharge = 0 to enable interpolation with the next data pair in the
   rating table. 

   5.  The hydraulic structure may be any type of flow control such as a
   bridge, diversion, culvert, weir, road-

   way or spillway.  If a short culvert is simulated that is separated
   by more than one grid element, neither 

   the travel time or volume of storage in the culvert is considered.
    The discharge is computed at the 

   outflow element for the same timestep.  This is a relatively minor
   assumption that should not affect the 

   simulation unless the culvert can contain a significant portion of
   the flood volume in the entire model.

   6.  If the culvert is long (CLENGTH > 500 ft or 154 m),
   Muskingum-Cunge volume routing is applied. 

   The flow area for the culvert is required as given by the variables
   COEFA, EXPA, RACOEF, RAEXP 

   and ATABLE.  The model will automatically substitute use the long culvert volume routing when 

   CLENGTH > 1.

   Variable Descriptions for the 

   HYSTRUC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page111-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311000110.png
   101

   **D**

   **ata**

   ** I**

   **nPut**

   7.  If the hydraulic structure is a bridge, culvert or weir between
   two floodplain 

   elements, set IFPORCHAN = 0.  If the structure in a channel, set
   IFPOR-

   CHAN = 1.  If the structure such as a culvert or pump
   collects discharge from 

   a floodplain and discharges to a channel, set IFPORCHAN = 2.  Finally
   is the 

   hydraulic structure has an inlet in a channel element and an outlet
   in a flood-

   plain element, IFPORCHAN =3.  

   8.  The Department of Transportation generalized culvert equations
   can be used to 

   assess inlet and outlet control.   The type of culvert entrances
   are:. 

   BOX entrance: 

   type 1 - wingwall flare 30 to 75 degrees 

   type 2 - wingwall flare 90 or 15 degrees 

   type 3 - wingwall flare 0 degrees 

   PIPE entrance: 

   type 1 - square edge with headwall 

   type 2 - socket end with headwall 

   type 3 - socket end projecting

   9.  The culvert equations use the conventional entrance loss
   coefficients KE values 

   that be found in the literature.  

   10.  If INOUTCONT(I,J) = 0, then the hydraulic structure discharge is
   based sole-

   ly on the upstream water surface elevation ( headwater depth  above
   the refer-

   ence elevation which is either assigned or represents the node elevation).  This 

   is equivalent to inlet control for a culvert.  If INOUTCONT(I,J) = 1,
   then the 

   tailwater submergence  is evaluated.  As the tailwater elevation
   approaches the 

   upstream headwater elevation, the model adjusts the rating curve or
   table and 

   gradually reduces the discharge as the outlet becomes submerged.
    When the 

   switch INOUTCONT(I,J) = 2, submergence discharge reduction occurs
   and 

   if the tailwater elevation exceeds the headwater elevation then flow
   upstream is 

   possible.  When the hydraulic structure discharge is greater than the
   upstream 

   inflow, the headwater elevation decreases and the tailwater elevation
   increases.  

   As the two water surface elevations on each side of the structure
   equilibrate, the 

   submergence factor reduces the structure discharge.  This may occur
   because 

   of tailwater effects or because the structure discharge rating table
   was overesti-

   mated for the upstream flow conditions. The submergence modifications
   to the 

   rating table are reported in the REVISED_RATING_TABLES.OUT file.

   11.  By assigning ISTORMDOUT, the discharge from this outflow element
   will 

   represent the collective inflow from any
   number of upstream inflow elements 

   with the same outflow node.  The discharge in the outflow element ISTORMD-

   OUT can be limited to the maximum discharge value STORMDMAXQ. 

   When the STORMDMAXQ is exceeded, no additional inflow discharge will 

   be computed for successive downstream inflow nodes.  This simplified
   storm 

.. container::
   :name: page112-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311100111.png
   102

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   drain routine does not include any pipe flow routing and does not use
   the 

   storm drain component.  The purpose of this component is to estimate
   the col-

   lected discharge in a large series of culverts or a limited storm
   drain network.  It 

   will limit the potential inflow as the pipe capacity is reached
   without perform-

   ing a pipe network discharge calculation.  For complex pipe networks,
   use the 

   FLO-2D storm drain model.

   12.  CDIAMETER is primarily used to estimate the timing of flow
   through a long 

   culvert.  This is accomplished with a Muskingum-Cunge method of
   storage 

   routing.  When the culvert is longer than about 300 ft (100 m), the
   timing of 

   the flow in the culvert may not match the timing of the floodwave
   progression.  

   Generally, the amount of storage in the culvert is not significant
   compared to 

   the flood volume.  Use CDIAMETER for a box culvert width if the
   generalized 

   culvert equations are used.  When using other culvert shapes such as an oval, 

   define an approximate equivalent circular culvert diameter.  For
   multiple box 

   culverts, define an equivalent single box culvert width (CUBASE) and
   height 

   (CDIAMETER). 

   13.  A hydraulic structure can be set up to compute flow exchange
   from a channel 

   element to a floodplain node.  For example, a channel may share flow
   through 

   a weir structure to a retention basin represented by floodplain
   elements.

   14.  For hydraulic structures simulation of pumps, set the intake
   elevation as the 

   Head Reference Elevation.  The default value is
   zero.  This setting will use the 

   grid element elevation of the inlet node intake elevation for the
   pump.  That 

   may be incorrect and result in a negative head on the intake.

   15.  For generalized culverts, the INOUTCONT should be set to 0, 1,
   or 2.  The 

   tailwater conditions submergence and reversed flow directoin will be
   allowed 

   based on the switch position.  1 allows submergence and 2 allows flow
   in the 

   upstream direction.  

   16.  The bridge hydraulic routine replaces the need for rating curves
   or rating tables 

   and represents significant added detail in computing free surface
   flow, pressure 

   flow or combined pressure and weir discharge for flow over the deck.
    See the 

   White Paper “Bridge Hydraulics Component” for the details on the
   bridge flow 

   routine that is available in the FLO-2D Help folder.

   17.  In the bridge hydraulics component, the free surface flow is
   computed using 

   various coefficients that represent the bridge features impact on the
   flow as a 

   function of water surface elevation (such as piers).  The user can
   assign the coef-

   ficients directly or use the automated interpolation of the USGS coefficients 

   from the White Paper Appendix figures.  

   18.  Bridge pressure flow is computed as either sluice gate flow or
   orifice flow de-

   pending on the water surface elevation with respect to the bridge
   soffit.

.. container::
   :name: page113-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311200112.png
   103

   **D**

   **ata**

   ** I**

   **nPut**

   19.  When the water surface exceeds the bridge deck elevation,
   broadcrested weir 

   flow is computed.  This is added to the pressure flow to determine
   the total 

   discharge through the bridge.  It is recommended that the weir
   coefficient be 

   estimated on the low side to account for spaced rails, walkways,
   debris and 

   other non-uniform deck features.

   20.  If simulating culvert discharge using the generalized culvert
   equations with 

   multiple barrels or openings, input the geometry of a single barrel
   or opening 

   and the MULTBARRELS parameter at the end of line F.  It is assumed
   that 

   each culvert barrel has identical geometry and invert elevation.  If
   using only 

   one barrel, this variable is not added.

.. container::
   :name: page114-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311300113.png
   104

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  SUBMERGE_FACTOR.DAT

   SUBMERGENCE DATA

   SUBMERGE_FACTOR.DAT File Variables 

   1181   1.2 

   Line 1: 

   **CELL   SUBM_ADJ(I)**

   **  **

   *L = number of grid elements in each street segment.*

   Notes:

   If MSTREET = 0 in the CONT.DAT file, omit this file.

   SUBMERGE_FACTOR.DAT File Example

   1811      1.2

   1862      0.95

.. container::
   :name: page115-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311400114.png
   105

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CELL

   **i**

   **1 - NNOD**

   Grid element number of the inlet node.

   SUBM_ADJ(I)

   **r**

   **0.01 - 2**

   Submergence adjustment factor for increasing or decreasing the
   submer-

   gence factor when the headwater to tailwater relationship is almost
   level.  

   Typical values 0.85 to 1.5.   

   Variable Descriptions for the 

   SUBMERGE_FACTOR.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   SUBMERGE_FACTOR.DAT FILE     

                       

   1.  TWhen the tailwater water approaches
   the headwater surface elevation and the 

   headwater depth/tailwater depth approaches 1, then the submergence
   factor is 

   change is

    

   HSUBFACTOR = HSUBFACTOR - 0.01 \* SUBM_ADJ

    or

    

   HSUBFACTOR = HSUBFACTOR + 0.015 \* SUBM_ADJ

   2.  The submergence factor for hydraulic structures is not a DOT
   table but rather 

   it adjusts on the fly during runtime.  This is not new.  What is new
   is SUBM\_

   ADJ.  If SUBM_ADJ = 1.0, there is no change from the existing method.
    If a 

   SUBMERGE_FACTOR only has

    

   1811      1.0

    

   1862      1.0

   Then the an output file is written:  HYDRAULIC STRUCTURE SUBFAC-

   TORS.OUT with only the listed cells and subfactor data including
   discharge 

   but no subfactor acceleration.  This gives the user the follwoing
   choices:

   1.  No changes at all without the SUBMERGE_FACTOR.DAT file.  Every-

   | thing is exactly the way it is now.
   | 2.  Write out the subfactor changes for only the specified cells
     in the data file.  

   | No acceleration if SUBM_ADJ = 1.0.
   | 3.  Write out the subfactor changes and use the acceleration to
     increase the rate 

   of change in the subfactor SUBM_ADJ > 1.0 or decrease the rate of
   change:  

   SUBM_ADJ <  1.0. 

.. container::
   :name: page116-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311500115.png
   106

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  STREET.DAT 

   STREET DATA

   STREET.DAT File Variables 

   0.025  1  1.7  0.667  40 Line 1: 

   **STRMAN   ISTRFLO   STRFNO   DEPX   WIDST**

   N   MAIN 

   Line 2: 

   **STCHAR   =  ‘N’   STNAME**

   * *

   S   127   0   0   0 

   Line 3: 

   **STRCHAR = ‘S’  IGRIDN(L)  DEPX(L)  STMAN(L)  **

   ** **

   ** ELSTR(L)**

   W   1   40 

   Line 4: 

   **STRCHAR = ‘w’, ISTDIR(K)   WIDR(K)**

   * K = 1,8 street directions*

   W   2   50 

   Line 4: 

   **STRCHAR = ‘w’, ISTDIR(K)   WIDR(K)**

   * K = 1,8 street directions*

   W   4   50 

   Line 4: 

   **STRCHAR = ‘w’, ISTDIR(K)   WIDR(K)**

   * K = 1,8 street directions*

   S   128   0   0   0 

   Line 3: 

   **STRCHAR = ‘S’  IGRIDN(L)  DEPX(L)  STMAN(L)  **

   ** **

   ** ELSTR(L)**

   **  **

   *L = number of grid elements in each street segment.*

   Notes:

   If MSTREET = 0 in the CONT.DAT file, omit this file.

   If DEPEX, STMAN, ELSTR, and WDIR = 0 the global values from Line 1
   will be used.

   Each grid element should be listed only once in this file.

   Line 2 - 4:  Repeat these lines for each street.

   Line 4:  Repeat this line for the number of grid elements before
   repeating Line 3.

   STREET.DAT File Example

   0.025       1     1.7   0.667      40

   N  MAIN

   S127       0       0       0

   W              1      40

   W              2      50

   W              4      50

   S            128       0       0       0

   W              2      50

   W              4      50

   S            129       0       0       0

   W              2      50

   W              4      50

   S            131       0      0       0

   W              2      50

.. container::
   :name: page117-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311600116.png
   107

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   DEPX

   **r**

   **0.0 - 2.0**

   **0.0 - 0.6**

   Global street curb height (ft or m).  If the street curb height is
   exceeded by 

   the flow it will result in overland flow depth in the grid element
   containing 

   the street.  DEPX is used to assign a street curb height to all grid
   elements 

   (see comment 7).

   DEPEX(L)

   **r**

   **0.01 - 2**

   **0.25 - .6**

   Optional curb height (ft or m) for individual
   grid elements that supercedes 

   the global curb height DEPX.  Set DEPEX(L) = 0.0  to use DEPX.  

   ELSTR(L) 

   **r**

   **0 - 30,000**

   **0 - 9,000**

   Optional street elevation (ft or m).  This elevation will supercede
   the flood-

   plain grid element elevation. If ELSTR(L) = 0, the model will assign
   the 

   street elevation as the grid element elevation, FP(I,6) minus the
   curb height 

   DEPEX(L) or DEPX to the street elevation ELSTR(L) (see comment 3).  

   IGRIDN(L)

   **i**

   **1 - NNOD**

   Grid element number.  Each grid element should be listed only once in
   the 

   data file (see comment 6).

   ISTDIR(K)

   **i**

   **1 - 8**

   Street segment (flow direction) from the center of the grid 

   element to a neighboring element.  IITDIR(k) will vary from 

   | 1 to 8 according to the following compass directions:
   | 1 = north 

   5 = northeast

   2 = east 

   6 = southeast

   3 = south 

   7 = southwest

   4 = west 

   8 = northwest  

   ISTRFLO

   **s**

   **0 or 1**

   ISTRFLO = 1 specifies that the floodplain inflow hydrograph will enter the 

   streets rather than entering the overland portion of the grid
   element.

   STRCHAR

   **c**

   **N, S or W**

   Character ‘N’, ‘S’ or ‘W’ to identify either Line 2, 3 or 4.  

   STRFNO

   **r**

   **0.0 - 5**

   Maximum street Froude number.  When the computed Froude number for 

   the street flow exceeds STRFNO, the n-value is increased by 0.001 for
   that 

   grid node. The increased n-values are reported in the ROUGH.OUT and 

   STREET.RGH files

   STMAN(L)

   **r**

   **0.01 - 0.25**

   Optional spatially variable street n-value within a given grid
   element.  

   STMAN(L) supercedes the STRMAN value.  If STMAN(L) = 0, the global 

   value STRMAN will be assigned to the grid element street segment.

   STRMAN

   **r**

   **0.01 - 0.25**

   Global n-value for street flow which that is assigned to all the grid
   element 

   street segments (see comment 2).

   Variable Descriptions for the 

   STREET.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page118-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311700117.png
   108

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   STREET.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   STNAME

   **c**

   **Alpha **

   **Numeric**

   Character name of the street.  Up to 15 characters
   can be used.  The street 

   name is not used in the model.  No spaces allowed.  (see comment 1).

   WIDR(K)

   **r**

   **0.0 - 1,000**

   **0.0 - 300**

   Optional grid element street width in the ISTDIR direction.  If the
   grid 

   element contains more than one street, Line 4 must be repeated.  If a
   given 

   grid element has more than one street in one direction,
   modify WIDR(K) 

   to represent the combined widths of the streets.  Up to 8 street
   segments, 

   one for each of the 8 compass directions, can be assigned according
   to the 

   ISTDIR variable.  By setting WIDR(K) = 0.0, the WIDST global width
   will 

   be assigned to that street segment (see comments 4 and 5).    

   WIDST

   **r**

   **0.01 - **

   Global assignment of street width to all streets.  This value is
   superseded by 

   WIDR(K) when WIDR(K) is greater than zero (see comments 2 and 4).  

.. container::
   :name: page119-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311800118.png
   109

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   STREET.DAT FILE     

                       

   1.  The street name is provided for the user to separate the
   streets groups for easy 

   identification in the data file.  It is not used in the program.

   2.  The street depth, width and n-values can be assigned globally for
   all the street 

   elements. The street depth, width, n-value and elevation can be
   spatially vari-

   able for the individual grid elements. 

   3.  If the street elevation is different from the representative grid
   elevation assigned 

   in the FPLAIN.DAT file, it should be specified in line 3, otherwise
   the street 

   elevation will be the floodplain elevation minus the curb height.
    This elevation 

   is then used to determine the street slope.

   4.  The street width should be less than the width of the grid
   element.  The over-all 

   floodplain surface area of the grid after the streets are removed
   must be at least 

   5% of the original surface area (grid element width squared).  If
   there are nu-

   merous streets in the grid element that occupy all the grid element
   surface area, 

   consider leaving out the smaller less significant streets, reduce the street width 

   or transfer one or more streets segments to a neighboring grid
   element.  An-

   other option is to increase the grid element size and reassign the
   grid system. 

   5.  The street is assumed to extend from the center of the grid
   element to the grid 

   element boundary in the four compass directions plus the four
   diagonal direc-

   tions as specified by the variable ISTDIR(K).  A street that crosses
   the entire 

   grid element is assigned two street sections and directions in Line
   4.

   6.  Each grid element should be listed only once in the STREET.DAT
   file.  For 

   street intersections within the grid element, list all the street
   flow directions for 

   the first street, then skip that grid element for the succeeding
   crossing streets.

   7.  The street flow depth tolerance value TOLST below which no street
   flow rout-

   ing computations are performed is 0.03 ft or 0.01 meters.  This value
   is replaces 

   the floodplain tolerance TOL value in TOLER.DAT and it is hardwired into 

   the model. The user cannot adjust it.

.. container::
   :name: page120-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202311900119.png
   110

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  ARF.DAT 

   | FLOODPLAIN AREA AND WIDTH REDUCTION 
   | DATA

   ARF.DAT File Variables 

   S    0 

   Line 1: 

   **ITTCHAR = ‘S’   ARFBLOCKMOD **

   T   49 

   Line 1: 

   **ITTCHAR = ‘T’   ITTAWF(K)  **

   * *

   29  .2  .70  .50  1.0  0.  0.  0.  0.  0. Line 2: 

   **IDG(I)   ARF(I)   WRF(I,J)**

   **  **

   *K = number of totally blocked grid elements*

   * *

   * *

   *I = number of partially blocked grid elements*

   * *

   * *

   *J = 8 flow directions*

   Notes:

   If IWRFS = 0 in the CONT.DAT file, omit this file.

   Line 1:  Repeat this line for each totally blocked grid element.

   Line 2:  Repeat this line for each partially blocked grid element.

   ARF.DAT File Example

   S   0.

   T  540

   T  2502

   T  3818

   T  3861

   T  4435

   T  4766

      46  .1  0  .5  0  .5  0  0  0  0

      69  .3  0  0  0  0  0  0  0  0

      119  .4  .5  .7  1  0  0  0  0  0

      120  0  0  0  0  1  0  .2  0  0

      142  .2  .2  0  0  0  0  0  0  0

      161  .5  0  0  0  0  0  0  0  0

      162  .5  .7  .2  1  0  0  0  0  1

      163  .1  0  0  0  1  0  0  0  0

      182  .3  0  0  0  0  0  0  .3 0

      ....

.. container::
   :name: page121-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312000120.png
   111

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ARF(I)

   **r**

   **0 - 1**

   **or**

   **-1 - 0**

   Area reduction factors (ARF) is the percent of the grid element (I)
   area that 

   cannot be covered by surface flows.  Buildings or other physical
   features 

   within the grid element that cannot store flow volume are accounted
   by 

   using the ARF value.  The maximum ARF value is limited according to
   cell 

   | size (see comments 1 and 3). 
   | If the value is negative, the building collapse function is turned
     on (see com-

   ment 5).

   ARFBLOCKMOD

   **r**

   **0. - 1.**

   Global revision to the ARF = 1 value to the grid elements 

   that are total blocked from receiving any flow (ITTAWF ele-

   ments).  Setting IARFBLOCKMOD = 0.9 will change the 

   ARF = 1. to ARF = 0.9 for all the ITTAWF elements (see 

   comment 4).

   IGD(I)

   **i**

   **1 - **

   **NNOD**

    Partially blocked grid element numbers.  

   ITTAWF(I)

   **i**

   **1 - **

   **NNOD**

   Grid elements that will not receive any flow.  Each grid element is
   totally 

   blocked out and all ARF and WRF values are set equal to 1.0.  If
   this value 

   is negative, the building collapse feature is turned on for the
   entire cell (see 

   comment 5).

   ITTCHAR

   **c**

   **S, T**

   Set ITTCHAR = ‘S’ to identify Line 1.

   Set ITTCHAR = ‘T’ to identify Line 2.

   Variable is case sensitive and it must be upper case.

   Variable Descriptions for the 

   AFR.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page122-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312100121.png
   112

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   WRF(I,J)

   **r**

   **0 - 1**

   Width reduction factors (WRF).  The width reduction
   factor corresponds 

   to the percentage of flow width blocked due to obstruction in the
   eight flow 

   directions.  Assuming that the flow field is oriented with the north
   direction, 

   | use the following WRF assignment:
   | WRF(I,1) = North 

   WRF(I,2) = East

   WRF(I,3) = South

   WRF(I,4) = West

   WRF(I,5) = Northeast

   WRF(I,6) = Southeast

   WRF(I,7) = Southwest

   | WRF(I,8) = Northwest
   | where I is the grid element number (see comment 2).

   Variable Descriptions for the 

   AFR.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page123-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312200122.png
   113

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   ARF.DAT File

    

   1.  For a partially blocked grid element, those ARF and WRF values
   that are 0.0 

   must be entered.  The graphical assignment and editing of ARF and WRF
   val-

   ues are relatively easy in the GDS or QGIS programs.    

   2.  Each grid element can receive or discharge flow through eight
   sides.  Consider 

   each element to be an octagon.  Each WRF factor refers to the percent
   blockage 

   of one of the
   eight sides.  If blockage redundancy is written to ARF.DAT, the 

   model will use the more restrictive WRF value.

   3.  The maximum ARF value is dependent on the grid element size
   unless the 

   grid element is totally blocked out in Line 1 as a ITTAWF grid
   element.  This 

   insures that at least 5% of the grid element is left for flow
   storage.  ARF values 

   will be adjusted to prevent numerical instability.  The following
   table lists the 

   adjustment triggers.

   TABLE 4�2�  ARF VALUES TRIGGER MAX

   Grid Element Size

   Maximum ARF Reset to 1

   Cell Side > 50

   0.95

   20 < to < 50

   0.90

   20 > Cell Side

   0.85

    

   4.  Instead of completely blocking any flow from entering the ITTAWF
   ele-

   ments, assigning ARFBLOCKMOD < 1. will allow some flow storage in
   these 

   completely blocked elements.  This variable only modifies totally blocked ele-

   ments.

   5.  To assess the potential for building collapse, assign the totally
   blocked element 

   (-ITTAWF) or the partially blocked ARF value (-ARF) in ARF.DAT as a
   nega-

   tive value.  Each building element that could collapse must be
   assigned a nega-

   tive value.  If a building consists of multiple totally blocked
   elements (ITTAWF 

   ~ T-line in ARF.DAT), all of the ITTAWF grid element numbers must be 

   assigned as negative to completely remove the building. 

.. container::
   :name: page124-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312300123.png
   114

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  MULT.DAT

   MULTIPLE CHANNEL (RILL AND GULLY) DATA

   MULT.DAT File Variables

    

   Line 1: 

   **WMC   WDRALL   DMALL   NODCHNSALL   XNMULTALL **

     

   **SSLOPEMIN, SSLOPEMAX AVULD50**

   0   0.0   5.0   1   0.04   0.00   0.00   0.0

    1961   3.0   5.0   1   0.04    Line 2: 

   **IGRID(I)  WDR(I)  DM(I)  NODCHNS(I)   XNMULT(I)**

   ** **

   *I = number of grid elements with multiple channels*

   Notes:

   If MULTC = 0 in the CONT.DAT file, omit this file.

   If WDRALL = 0, no global assignment of the variables occurs.

   Line 3:  Repeat this line for each grid element revision.

   MULT.DAT File Example

    0   0.0   5.0   1   0.04   0.00   0.00   0.0

    1961   3.0   5.0   1   0.04

    1962   3.0   5.0   1   0.04

    1963   3.0   5.0   1   0.04

    1964   3.0   5.0   1   0.04

    1965   3.0   5.0   1   0.04

    1966   3.0   5.0   1   0.04

    1967   3.0   5.0   1   0.04

.. container::
   :name: page125-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312400124.png
   115

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   AVULD50

   **r**

   **0.00 - **

   **100.0**

   Bed material D50 sediment size fraction (mm).  Assignment of AVULD50 

   triggers the avulsion component that will allow a multiple channel to
   seek a 

   new path if the channel conveyance capacity is exceeded (see comment
   6).

   DM(K)

   **r**

   **0 - 1000**

   **0 - 300**

   Maximum depth of multiple channels for individual grid elements (ft
   or 

   m).  When the flow depth exceeds the multiple channel depth DM, the
   flow 

   width WDR of the gully is increased by the incremental width WMC
   (see 

   comments 2 and 3).  DM supersedes the DMALL depth assignment.

   DMALL

   **r**

   **0 - 1000**

   **0 - 300**

   Global assignment of the maximum depth to all grid elements (ft or
   m).

   IGRID(I)

   **i**

   **1 - **

   **NNOD**

   Floodplain grid element number (see comment 1).

   NODCHNS(K)

   **i**

   **0 - 100**

   Number of multiple channels assigned in each grid element.  If
   NODCHNS 

   is set equal to zero then the overland flow without multiple channels
   is as-

   sumed. NODCHNS supersedes NODCHNSALL value.

   NODCHNSALL

   **i**

   **1 - 100**

   Global assignment of the number of multiple channels to all grid
   elements.  

   SSLOPEMIN

   **r**

   **0. - 1.**

   Minimum slope that multiple channel assignments will be made at run-

   time.  

   SSLOPEMAX

   **r**

   **0. - 1.**

   Maximum slope that multiple channel assignments will be made at run-

   time.  

   WDR(K)

   **r**

   **0 - 1000**

   **0 - 300**

   Channel width for individual grid elements.  WDR supersedes
   WDRALL.   

   WDRALL

   **r**

   **0 - 1000**

   **0 - 300**

   Global assignment of the multiple channel width to all grid elements.
    If 

   WDRALL = 0, all global variables are set to zero.  

   WMC

   **r**

   **0 - 1000**

   **0 - 300**

    Incremental width by which multiple channels will be expanded when
   the 

   maximum depth DM is exceeded (see comments 2 and 4).

   XNMULT(K)

   **r**

   **0.01 - 0.5**

   Channel n-values for individual grid elements.  Supersedes XNMULTALL.

   XNMULTALL(K)

   **r**

   **0.01 - 0.5**

   Global assignment of the multiple channel n-values to all the grid
   elements.

   Variable Descriptions for the 

   MULT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page126-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312500125.png
   116

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   MULT.DAT File  

               

   1.  If a grid element is assigned multiple channels and, in addition,
   contains a main 

   channel or buildings such that the available floodplain surface
   storage area is 

   less than 50% of the original grid element surface area, then the
   model will 

   reset that grid element to overland sheet flow (i.e. no multiple channels).  The 

   program will automatically eliminate any multiple channels in grid
   elements 

   with streets. The available surface area and the assigned variable
   can be reviewed 

   in the SURFAREA.OUT output file.

   2.  If a multiple channel fills and is about to overflow, it is
   assumed that it is an 

   alluvial channel and will widen to accept more flow.  Thus when the
   flow depth 

   exceeds the maximum channel depth DM, the model increases the width by 

   WMC to maintain the channel conveyance.  The multiple channel will
   not 

   overflow on the floodplain, but will continue to widen until the
   gully is wider 

   than the grid element.  The flood routing will then revert to
   overland flow in 

   that element.  The following rules govern the assignment of the
   multiple chan-

   nel data:

    · When the flow depth exceeds the multiple channel (gully) depth,
   the 

   flow width of the gully is increased by the incremental width.

    · If it is desired to force the flow to stay in a channel of fixed
   width, set the 

   incremental width equal to zero.

    · If the number of multiple channels assigned in a grid element is
   set equal 

   to zero, overland sheet flow without multiple channels is assumed.

    · The spatially variable grid element data will supersede the global
   data.

   3.  If it is desired to force the flow to stay in a channel of fixed
   width, set the vari-

   able WMC = 0.  

   4.  The total flow width is determined by multiplying the number of
   channels in 

   each grid element by the corresponding width.  

   5.  SSLOPEMIN and SSLOPEMAX define a range of watershed slope in
   which 

   the multiple channel width will be expanded.  This will limit the
   channel width 

   growth to the middle portion of the basin
   and will not expand the other mul-

   tiple channels.  By expanding the channels for increased conveyance capacity, 

   the time of concentration can be reduced. The default SSLOPEMIN = SS-

   LOPEMAX = 0.0 will result in width increases for all multiple
   channels.

   6.  The avulsion component will be initiated if AVULD50 > 0.  When a
   multiple 

   channel conveyance capacity is exceeded in a given grid element, the
   model will 

   search the other flow direction neighbor elements without a
   multiple channel 

.. container::
   :name: page127-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312600126.png
   117

   **D**

   **ata**

   ** I**

   **nPut**

   and will create a multiple channel in that grid element based on width and 

   depth relationship as a function of bed material size (AVULD50).
    This will 

   continue in the downslope direction until the multiple channel
   conveyance ca-

   pacity is no longer exceeded.  For more information, see the avulsion
   discussion 

   white paper in the FLO-2D Handouts and Reference Manual. 

.. container::
   :name: page128-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312700127.png
   118

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  SIMPLE_MULT.DAT

   MULTIPLE CHANNEL DATA

   SIMPLE_MULT.DAT File Variables

   0.025 

   Line 1: 

   **XNMULTTRICHN **

    1961 

   Line 2:   

   **IMGRID(I)**

   ** **

   *I = number of grid elements with multiple channels*

   Notes:

   Line 2:  Repeat this line for each grid element revision.

   SIMPLE_MULT.DAT File Example

    0.060

    19612

    19625

    19458

      ...

.. container::
   :name: page129-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312800128.png
   119

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IMGRID(I)

   **i**

   **1 - NNOD**

   A character to define a new bridge cross section dataset.

   XNMULTTRICHN

   **r**

   **0.01 - 0.5**

   Global assignment of the multiple channel n-values to all the grid
   ele-

   ments.

   Variable Descriptions for the 

   SIMPLE_MULT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page130-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202312900129.png
   120

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   SIMPLE_MULT.DAT File

   1.  Similar to the conventional multiple channel option, the
   simplified multiple 

   channel switch IMULTC is set to 1 for the component to be activated.
    Again, 

   IMULTC is the fifth parameter in line 2 of the CONT.DAT file.

   2.  Flow is simulated in a small rectangular channel with an initial
   width of 2 ft 

   and depth of 1 foot.

   3.  If the flow depth exceeds the 1 ft deep rill channel, then the
   channel width is 

   expanded by 2 times the initial width of 2 ft.  The maximum allowed
   channel 

   width is 4 ft. 

   4.  When the maximum width of 4 ft is achieved and the flow depth
   exceeds the 

   maximum channel depth, the volume greater than the channel depth is
   distrib-

   uted back to the floodplain surface.

   | 5.  The channel bed elevation is 1 ft lower than the grid element
     elevation
   | 6.  If there is no surface area because of the area reduction value
     (ARF value) as-

   signment, the multiple channel routine is turned off for that grid
   element.

   7.  If the surface area of the grid element after removing the rill
   channel surface 

   area is less than 30% of the original grid element surface area, the
   multiple 

   channel routine is turned off for that grid element and the overland
   flow reverts 

   to sheet flow.

   | 8.  The maximum number of multiple channels within the grid element
     is one.
   | 9.  The shallow n-value for the rill channel is 0.100.
   | 10.  A single global n-value can be user specified to represent the
     rill channels.  
   | 11.  The original multiple channel routine can be combined with the
     simplified 

   component by simply created both multiple channel data files (MULT.DAT 

   and SIMPLE_MULT.DAT).

.. container::
   :name: page131-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313000130.png
   121

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  SED.DAT 

   MUDFLOW AND SEDIMENT TRANSPORT DATA

   SED.DAT File Variables 

    

   Line 1: 

   **SEDCHAR = ‘M’   VA   VB   YSA   YSB   SGSM   XKX  **

   M   0.000602   33.10   0.001720   29.50   2.74   0.00

    

   Line 2: 

   **SEDCHAR = ‘C’   ISEDEQG   ISEDSIZEFRAC   DFIFTY   SGRAD    **

   ** **

   ** **

   **SGST   DRYSPWT   CVFG   ISEDSUPPLY   ISEDISPLAY **

   | C   2   0.25   2.5   2.65    92.5   1   7232
   | Z   2   5.0   0.15 

   Line 3: 

   **SEDCHAR = ‘Z’   ISEDEQI   BEDTHICK   CVFI**

   P   0.062   0.010 

   Line 4: 

   **SEDCHAR = ‘P’   SEDIAM   SEDPERCENT**

   D    111   20.0  

   ** **

   Line 5:

   **  SEDCHAR = ‘D’   JDEBNOD   DEBRISV**

   E   1.0

   ** **

   Line 6:

   **  SEDCHAR = ‘E’   SCOURDEP**

   R   9366

   ** **

   Line 7:

   **  SEDCHAR = ‘R’   ICRETIN(N)   **

   *N = number of rigid bed nodes*

   S   23798   1    4.49   0.89

   ** **

   Line 8:

   **  SEDCHAR = ‘S’   ISEDGRID(N)   ISEDCFP(N)   ASED(N)**

   ** **

   ** **

   **BSED(N)   **

   *N = number of sediment supply rating curves.*

   N   0.062   0.052

   * *

   Line 9:

   * *

   **SEDCHAR = ‘N’   SSEDIAM   SSEDPERCENT**

   G    1    3 

   ** **

   Line 10: 

   ** SEDCHAR = ‘G’  ISEDUM  ISEDGROUP(N)  **

   **  **

   *N = number of sediment  groups*

   Notes:

   Only a sediment transport ISED or mudflow MUD simulation can be
   applied in a project model.

   If MUD = 0 in the CONT.DAT file, omit line 1.  

   If ISED = 0 in the CONT.DAT file, omit line 2, 3, 4, 6, 7, 8, and 9.

   If both MUD and ISED = zero in the CONT.DAT file, omit this file.

   Line 2:  If ISEDSIZEFRAC = 1, it is necessary to create a sediment
   group using Lines 3 and 4.

   Line 4:  Repeat this line for each size fraction.  Each group must
   have the same number of size fractions.

   Line 5:  If debris basin IDEBRV = 0 in the CONT.DAT file, ignore this
   line.

   Line 8, 9:  If ISEDSUPPLY = 0, ignore these lines.

.. container::
   :name: page132-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313100131.png
   122

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   SED.DAT File Example

   M   0.000602   33.10   0.001720   29.50   2.74    0.00   

   *(Mudflow)*

   *or*

   C  2  1  2.5  6.7  2.65  95.0  0.10  0  1961    

   *(Sediment Transport)*

   Z  2  1.  0.10

   P   0.074   0.058

   P   0.149   0.099

   P   0.297   0.156

   P   0.590   0.230

   P   1.19    0.336

   P   2.38    0.492

   P   4.76    0.693

   P   9.53    0.808

   E 1.0

   R 2062

   R 2063

   R 2114 

   R 2115

   R 2166

   R 2167

   S 1228 1  4.49   0.89

   N 0.074 0.022

   N 0.300 0.107

   N 0.600 0.232

   N 2.000 0.528

   N 4.750 0.748

   N 9.530 0.852

   N 19.050 0.926

   N 38.100 0.973

   N 76.200 1.000

   G    1    2

   G    2    2

   G    3    1

   G    4    2...

   FILE:  SED.DAT

   MUDFLOW AND SEDIMENT TRANSPORT DATA

.. container::
   :name: page133-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313200132.png
   123

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ASED(N)

   **r**

   **0 - **

   Sediment rating curve coefficient (see the BSED exponent below).

   BEDTHICK

   **r**

   **0 - 100**

   **0 - 30**

   Sediment bed thickness (ft or m) for sediment routing by size
   fraction.  The 

   available sediment volume for a size fraction within a grid element
   is defined 

   by the bed thickness times the floodplain or channel element surface
   area 

   times the percent size distribution.  The default bed thickness is 10
   ft (3 m) 

   for the floodplain if bed thickness is less than 0.1 ft.  If there is
   no available 

   sediment volume for a given size fraction, no further scour of the
   bed will 

   occur for that sediment size fraction (see comment 2).  

   BSED(N)

   **r**

   **0 - **

   Sediment rating curve exponent.  Q

   s

    = ASED\* Q

   w

    

   BSED

   where: 

   Q

   w

    is the water discharge (cfs or cms)

   Q

   s

    is the sediment supply (tons/day or kg/day). 

   CVFG

   **r**

   **0 - 0.2**

   Fine sediment volumetric concentration for overland, channel, and
   streets.  

   This value is superseded by CVFI in Line 3.  Concentration by volume
   of 

   sediment for sizes less than 0.0625 mm (sand-silt split).  This concentration 

   by volume generally ranges from 5% to 15% and is expressed as a decimal 

   (0.05 for 5% concentration by volume).  It is used only in Woo-MPM
   sedi-

   ment transport equation.

   CVFI

   **r**

   **0 - 0.2**

   This variable is the same as CVFG except that it represents the fine
   sediment 

   volumetric concentration for an individual channel segment(s).  CVFI
   su-

   persedes CVFG for a channel segment(s) as identified by ISEDN in
   CHAN.

   DAT.  CVFI represents the concentration by volume of sediment for
   sizes 

   less than 0.0625 mm (sand-silt split).  This concentration by volume
   gener-

   ally ranges from 5% to 15% and is expressed as a decimal (0.05 for 5%
   con-

   centration by volume).  It is used only in the Woo-MPM sediment
   transport 

   equation.

   DEBRISV

   **r**

   **0 - **

   Volume of the debris basin in ft

   3

    or m

   3

   .

   DFIFTY

   **r**

   **30625 - **

   Sediment size (D

   50

   ) in mm for sediment routing.

   DRYSPWT

   **r**

   **70 - 130**

   Dry specific weight of the sediment (lb/ft

   3

    or N/m

   3

   ).

   ICRETN

   **i**

   **1 - **

   **NNOD**

   Floodplain or channel grid elements with a rigid bed (e.g. spillway
   apron).

   Variable Descriptions for the 

   SED.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page134-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313300133.png
   124

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ISEDCFP(N)

   **s**

   **0 = fp**

   **1 = chan**

   ISEDCFP(N) = 0 for a floodplain sediment supply rating curve  

   ISEDCFP(N) = 1 for a channel sediment supply rating curve.

   ISEDEQG

   **i**

   **1 - 11**

   Transport equation number used in sediment routing for overland
   flow, 

   channels and streets (see comment 3). In Line 2 (Line ‘C’), ISEDEQG 

   will set the sediment transport equation for floodplain sediment
   routing 

   and channel routing.  In Line 3 (Line ‘Z’), ISEDEQI will set the
   sediment 

   transport equation for sediment routing by size fractions with a
   sediment 

   transport equation assigned to each group.  Set ISEDEQG or ISEDEQI
   as 

   follows for the appropriate sediment transport equation:

   ISEDEQ = 1 

   Zeller and Fullerton

   ISEDEQ = 2 

   Yang

   ISEDEQ = 3 

   Englund and Hansen

   ISEDEQ = 4 

   Ackers and White

   ISEDEQ = 5 

   Laursen

   ISEDEQ = 6 

   Toffaleti

   ISEDEQ = 7    

   Woo-MPM

   ISEDEQ = 8 

   MPM-Smart

   ISEDEQ = 9    

   Karim-Kennedy     

   | ISEDEQ = 10        Parker, Klingeman & McLean
   | ISEDEQ  = 11       Van Rijn 

   Variable Descriptions for the 

   SED.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page135-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313400134.png
   125

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ISEDEQI

   **i**

   **1 - 11**

   This variable is the same as ISEDEQG except that it represents the
   sediment 

   transport equation used for sediment routing by size fractions and it
   is used 

   to identify the sediment transport equation for a specific channel
   segment or 

   reach (comment 5).  This value supersedes ISEDEQG in Line 2.  In Line
   3 

   (Line ‘Z’), ISEDEQ will set the sediment transport equation for sediment 

   routing by size fractions with a sediment transport equation assigned
   to each 

   group.  If Line 3 and the following Line 4’s constitute only one
   group, then 

   all sediment routing on the floodplain, in the channel and in the
   streets will 

   use the same sediment size distribution.  If there is more than one
   group 

   of Line 3 and the following Line 4’s, then the first group will be
   define the 

   sediment size distribution for the floodplain, streets and any
   channel seg-

   ments where ISEDN = 1 in CHAN.DAT.  Successive channel segments 

   can identify another set of sediment size fractions by setting ISEDN
   = 2 or 

   higher.  This will permit the channel bed material to vary throughout the 

   river system.  The ISEDEQI equation numbers are the same as ISEDEQG 

   above.  The number of size fraction intervals must be identical for
   all sedi-

   ment groups (see comment 6). 

   ISEDISPLAY

   **i**

   **1 - **

   **NNOD**

   Grid element
   (channel or floodplain) for which the sediment transport ca-

   pacity for all the sediment transport equations will be listed by
   output inter-

   val TOUT in the SEDTRAN.OUT file.  Note that only one equation is 

   used in the actual sediment routing calculations, but the results of
   all equa-

   tions are presented in SEDTRAN.OUT.

   ISEDGRID(N)

   **i**

   **1 - **

   **NNOD**

   Grid element that will be a sediment supply node (channel or
   floodplain) 

   with a sediment rating curve.

   ISEDGROUP(N)

   **i**

   **1- NNOD**

   The sediment group ID for each set of size fraction data (see 

   comment 5).

   ISEDSIZEFRAC

   **s**

   **0 or 1**

   ISEDSIZEFRAC = 1,  The sediment routing will be performed by size
   frac-

   tion.  Requires data input from Lines 3 and 4 and Line 9 if a
   sediment supply 

   | is also input.  
   | ISEDSIZEFRAC = 0, No sediment routing by
     size fraction.  Sediment rout-

   ing is based on the median bed material size D

   50

   .  For this case, the default 

   bed thickness is 10 ft (3m) (see comment 1).

   Variable Descriptions for the 

   SED.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page136-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313500135.png
   126

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ISEDSUPPLY

   **s**

   **0 or 1**

   ISEDSUPPLY = 1 if a sediment rating curve will be used to define the
   sedi-

   ment supply to a channel reach or floodplain area.  

   ISEDUM

   **i**

   **1 - **

   **NNOD**

   Grid element  number for the sediment size fraction group. 

   JDEBNOD

   **i**

   **1 - **

   **NNOD**

   Grid element with the debris basin.  The grid element must be a node
   listed 

   in INFLOW.DAT (see comment 7).

   SCOURDEP

   **i**

   **0 - 100**

   **0 - 30**

   Maximum allowable scour depth (ft or m) for all floodplain elements.

   SEDCHAR

   **c**

   **M**

   **C**

   **Z**

   **P**

   **D**

   **E**

   **R**

   **S**

   **N**

   **G**

   | Character line identifier: 
   | SEDCHAR =  

   ‘M’ - Mudflow parameters in Line 1.  

   SEDCHAR =  

   ‘C’ - Sediment routing parameters in Line 2.  

   SEDCHAR =   

   ‘Z’ - Sediment routing by size fraction control     

     

   parameters in Line 3.  

   SEDCHAR =   

   ‘P’ - Sediment routing by size fraction 

     

   sediment distribution variables in Line 4.   

   SEDCHAR =   

   ‘D’ - Debris basin parameters in Line 5.  

   SEDCHAR =   

   ‘E’ - Sediment scour limitation parameter 

    

   in Line 6.  

   SEDCHAR =   

   ‘R’ - Rigid bed grid elements in Line 7.  

   SEDCHAR =   

   ‘S’ - Sediment supply rating curves in Line 8.

   SEDCHAR =   

   ‘N’ - Sediment supply rating curve size 

     

   fraction distribution in Line 9.

    SEDCHAR =            ‘G’ - Sediment group.

   Variable is case sensitive and it must be upper case.

   SEDIAM

   **r**

   **0 - **

   Representative sediment diameter (mm) for sediment routing by size
   frac-

   tion.  The sediment diameter corresponds to a given
   size fraction percent 

   finer and usually is a pan sieve size.

   SEDPERCENT

   **r**

   **0 - 1**

   Sediment size distribution percentage (expressed as a decimal).  The
   percent-

   age represents the percent of the bed material sediment that is finer
   than the 

   representative size diameter.  For example, SEDPERCENT = 0.456
   defines 

   that 45.6% of the sediment is finer than the 1 mm sediment size
   fraction.  

   The last entry should be 1.00 (100% of the sediment is smaller than
   the cor-

   responding sediment diameter).

   Variable Descriptions for the 

   SED.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page137-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313600136.png
   127

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   SGRAD

   **r**

   **1.0 - 10.**

   Sediment gradation coefficient (non-dimensional) for the sediment
   trans-

   port routine.

   SGSM

   **r**

   **2.5 - 2.8**

   Mudflow sediment specific gravity.

   SGST

   **r**

   **2.6 - 2.8**

   Sediment specific gravity.

   SSEDIAM

   **r**

   **0 - **

   Representative sediment supply diameter (mm) for sediment routing by
   size 

   fraction.  See SEDIAM parameter above.

   SSEDPERCENT

   **r**

   **0 - 1**

   Sediment supply size distribution percentage (expressed as a
   decimal).  

   SSEDPERCENT represents the percent of the sediment that is finer
   than 

   the representative size diameter.  See SEDPERCENT parameter above.

   VA

   **r**

   **0 - **

   Coefficient in the viscosity versus sediment concentration by volume
   rela-

   tionship.  The relationship is based on a viscosity given in poises (dynes-s/

   cm

   2

   ) for either the English or Metric system (see comment 4).

   VB

   **r**

   **0 - **

   Exponent in the viscosity versus sediment concentration by volume
   relation-

   ship.

   XKX

   **r**

   **24  - **

   **50,000**

   The laminar flow resistance parameter for overland flow.  This value
   should 

   range from 24 to 50,000 (see Table 8 in the FLO-2D Reference manual).
    It 

   is suggested that a value of 2,480 initially be used for mudflows.
    If a value 

   of XKX is entered, it will be used by the model.  If XKX = 0, then
   XKX is 

   computed by the following formulas where FPN is the floodplain grid
   ele-

   ment Manning’s n-value:     

                FPN < 0.01  XKX = 24

    0.01 < FPN < 0.25 

   XKX = 1,460,865.81\* (FPN)

   2.381

    0.25 < FPN 

   XKX = 2,480

   YSA

   **r**

   **0 - **

   Coefficient of the yield stress versus sediment concentration by
   volume rela-

   tionship.  The relationship is based on a yield stress given in
   dynes/cm2 for 

   either the English or Metric system.

   YSB

   **r**

   **0 - **

   Exponent of yield stress versus sediment concentration by volume
   relation-

   ship.

   Variable Descriptions for the 

   SED.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page138-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313700137.png
   128

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   SED.DAT File

   1.  Armouring is simulated for bed material sizes with a D

   90

    > 16 mm.  If D

   90 

   > 16 mm, then an armor exchange layer with a thickness (3 x D

   90

   ) is estab-

   lished.  Initially the exchange layer has the same sediment size
   distribution as 

   prescribed for the bed.  The volume and size distribution of each
   sediment size 

   fraction in the exchange layer is tracked on a timestep basis
   independent of the 

   remaining bed material size.  A potential armor sediment size D

   84

    is predicted 

   for the prescribed bed material size (see the armor discussion in
   chapter 4 of the 

   FLO- 2D Reference Manual).  If the computed D

   84

    grain size equals or exceeds 

   the predicted D

   84

    armor size then an armor layer is assumed that will protect 

   the smaller size sediment in bed from scour.  

   2.  While the bed thickness can be used to limit scour in the
   channel, it is sug-

   gested that a reasonable bed thickness be initially specified to
   determine if the 

   channel computes an unreasonable scour depth.   

   3.  To select an appropriate sediment routing equation refer to chapter 4 of the 

   FLO-2D Reference Manual.  If uncertain as to which equation may be
   best 

   suited to the project, Zeller and Fullerton or Yang’s equation will
   predict a 

   moderate sediment transport capacity for a wide range of field
   conditions.

   4.  Mudflow simulation is dependent on the appropriate selection of
   viscosity and 

   yield stress parameters.  Please review the mudflow discussion in
   Chapter 4 of 

   the FLO-2D Reference Manual to determine an appropriate viscosity and
   yield 

   stress relationship as function of sediment concentration.  There are
   also mud-

   flow guidelines available in the Handout documents.

   5.  The floodplain spatially variable sediment size fraction is
   assigned by sediment 

   groups (Lines 3, 4 and 10).  Line 10 (G) relates the cell number to
   the sediment 

   group.  Spatial variation can be assigned to the channel by segments
   using the 

   ISEDN parameter in the CHAN.DAT file. ISEDN is used to identify the
   sedi-

   ment group for each segment.  If there are two sediment groups as
   shown in the 

   above example data file, there could be one floodplain sediment size
   distribu-

   tion and one channel size distribution or there could be two channel
   segment 

   size distributions by using the first sediment group to represent one
   of the chan-

   nel segments as specified by the ISEDN variable in CHAN.DAT.  

   6.  It is important to note that each sediment group will have the
   identical size 

   fraction delineation.  The SEDIAM variable will be the same for all the groups 

   (i.e. the number of Line 4s in all groups will be the same).  If one
   group is 

   missing a specific size fraction, then the sediment percentage for
   that group 

   (SEDPERCENT variable) will either be the same as the previous value
   or only 

   slightly different (see the above example data file).

.. container::
   :name: page139-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313800138.png
   129

   **D**

   **ata**

   ** I**

   **nPut**

   7.  The debris basin volume is assigned to an inflow node.  The
   inflow node will 

   not compute discharge to downstream cells until the basin volume is
   exceeded.

.. container::
   :name: page140-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202313900139.png
   130

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  LEVEE.DAT

   LEVEE AND FAILURE DATA

   LEVEE.DAT File Variables

   0.00    0 

   Line 1: 

   **RAISELEV   ILEVFAIL  **

   * *

   L  1891 

   Line 2: 

   **LEVCHAR = ‘L’   LGRIDNO(L)   **

   *L = number of levee grid elements*

   D   4   5029.00

   * *

   Line 3:

   * *

   **LEVCHAR = ‘D’   LDIR(L,J)   LEVCREST(L,J)**

   **  **

   *L = number of levee grid elements   *

   * *

   * *

   *J = number of levee directions in grid element*

   F   1891

   ** **

   Line 4: 

   **LEVCHAR = ‘F’   LFAILGRID(LF)   **

   **  **

   *LF = number of failure grid elements*

   ** **

   Line 5: 

   **LEVCHAR = ‘W’   LFAILDIR(LF,LD)   FAILEVEL(LF,LD) **

   **  **

   **FAILTIME(LF,LD)   LEVBASE(LF,LD)   FAILWIDTHMAX(LF,LD)**

   **    **

   ** **

   **FAILRATE(LF,LD)   FAILWIDRATE(LF,LD)**

   **  **

   *LD = number of fail directions*

   * *

   * *

   *LF = number of failure grid elements*

   W 4  5019.5  27.0 10 1 2  0.5  

   C   FS3   0.5 

   Line 6:  

   **LEVCHAR = ‘C’   GFRAGCHAR   GFRAGPROB**

   P   3450   FS1   0.5 

   Line 7:  

   **LEVCHAR = ‘P’   LEVFRAGRID(LP)   LEVFRAGCHAR (LP)**

   ** **

   ** LEVFRAGPROB(LP)**

     

   *LP = number levee grid elements with fragility curve assignments*

   Notes:

   If LEVEE = 0 in the CONT.DAT file, omit this file.

   Line 2:  Repeat this line for each levee grid element.

   Line 3:  Repeat this line for each levee direction in a grid element.

   Line 4:  Repeat this line for each LEVEEFAILURE grid element.

   Line 5:  Repeat this line for each grid element failure direction.

.. container::
   :name: page141-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314000140.png
   131

   **D**

   **ata**

   ** I**

   **nPut**

   LEVEE.DAT File Example

       0.00    0

    L   1891

    D      4   5020.00

    L   1896

    D      6   5020.00

    L   1897

    D      2   5020.00

    D      3   5020.00

    D      5   5020.00

    D      6   5020.00

    L   1921

    D      1   5020.00

    D      4   5020.00

    D      8   5020.00

    L   1922

    D      8   5020.00

    L   1927

    D      2   5020.00

    D      6   5020.00

    L   ...  

   C    FS3          0.5

    P        3450  S1        0.5

    P        3558  S1        0.9

    P        3559  S2        0.7

    P        3669  S3        0.5

    P        3670  S4        0.5

    P        3782  C1        0.3

    P        3783  S1        0.5

    P        3815  J2         0.5

    P        3897  S1        0.5

    P       ...

   FILE:  LEVEE.DAT

   LEVEE DATA

.. container::
   :name: page142-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314100141.png
   132

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   LEVEE.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   FAILEVEL(LF,LD)

   **r**

   **0.01**

   ** to**

   ** **

   The maximum elevation of the prescribed levee failure if different
   than the 

   levee crest (LEVELEV).  Set FAILEVEL = 0 to fail the levee when over-

   topped.

   FAILRATE(LF,LD)

   **r**

   **0**

   **.01 - 1000**

   **0.25 - 300**

   The rate of vertical levee failure (ft/hr or m/hr).  Set failrate = 0
   for wall 

   collapse.

   FAILTIME(LF,LD)

   **r**

   **-99.0 to **

   **SIMUL**

   **-99.0**

   The duration (hr) that the levee will fail after the FAILEVEL
   elevation is 

   | exceeded by the flow depth.
   | If FAILTIME = 0.0 if the level erosion begins immediately when pipe
     eleva-

   | tion is exceeded.
   | If FAILTIME > 0.0, the start time for time to 1 ft and time to 2 ft
     is based 

   | on the model start time 0.0 hr.
   | If FAILTIME < 0.0, the start time for time to 1 ft and time to 2 ft
     is the first 

   | dam or levee breach time for multiple breaches.
   | If FAILTIME = -99.0, the start time for time to 1 ft and time to 2
     is the first 

   dam or levee breach time for multiple breaches and FAILTIME is reset
   to 

   0.0 hr.s (see comment 9).

   | FAILWIDRATE
   | (LF,LD)

   **r**

   **0**

   **.01 - 1000**

   **0.25 - 300**

   The rate at which the levee breach widens (ft/hr or m/hr).  Set
   failwidrate = 

   0 for wall collapse.

   | FAILWIDTHMAX
   | (LF,LD)

   **r**

   **0 - **

   The maximum breach width (ft or m).  The breach can extend into more 

   than one grid element direction if necessary and the failure width
   can be 

   larger than one grid element (see comment 3).

   GFRAGCHAR

   **c**

   **Alpha **

   **Numeric **

   Global levee fragility curve ID.  One letter (e.g. S) and one number
   (e.g. 3) 

   and must correspond to a levee fragility curve ID in the BREACH.DAT
   file.

   Variable is case sensitive and it must be upper case.

   GFRAGPROB

   **r**

   **0 - 1**

   Global levee fragility curve failure probability.  This is assigned
   to all levee 

   grid elements.  The levee fragility curves must be assigned in
   BREACH.

   DAT.

.. container::
   :name: page143-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314200142.png
   133

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   ILEVFAIL

   **s**

   **0, 1 or 2**

   | Switch to identify levee failure mode (see comment 6).
   | ILEVFAIL = 0 no levee failure. 

   ILEVFAIL = 1 prescribed level failure rates of breach opening or wall
   col-

   lapse.

   ILEVFAIL = 2 initiate the levee or dam breach failure routine.

   LDIR(L,IM)

   **i**

   **1 - 8**

   Flow direction (of the 8 possible overland flow directions) that will
   be cutoff 

   | by a levee in a given grid element.  The possible flow directions
     are:
   | 1 = north 

   5 = northeast

   2 = east 

   6 = southeast

   3 = south 

   7 = southwest

   4 = west 

   8 = northwest

   LEVBASE(LF,LD)

   **r**

   **0 or**

   **0 - **

   The prescribed final failure elevation.  Vertical failure growth
   stops at this 

   | elevation.  
   | Set LEVBASE = 0 if the levee fails to the floodplain elevation. 

   LEVCHAR(L)

   **c**

   **L, D, F, W, **

   **C or P**

   Character Identifier for Lines 2 - 7

   ‘L’   = Line 2

   ‘D’   = Line 3

   ‘F’    = Line 4

   ‘W’   = Line 5

   ‘C’    = Line 6

   ‘P’    = Line 7

   Variable is case sensitive and it must be upper case.

   LEVCREST(L,IM)

   **r**

   **.01 - **

   **30,000**

   **.25 - 9,000**

   The elevation of the levee crest (ft or m) (see comments 4 and 5).

   LFAILDIR(LF,LD)

   **i**

   **1 - 8**

   | The potential failure direction (see comment 3).
   | 1 = north 

   5 = northeast

   2 = east 

   6 = southeast

   3 = south 

   7 = southwest

   4 = west 

   8 = northwest

   Variable Descriptions for the 

   LEVEE.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page144-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314300143.png
   134

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   LEVFRAGRID(LP)

   **i**

   **1 - NNOD**

   Individual levee grid element with fragility curve assignment.  

   The fragility curves must be assigned in BREACH.DAT.

   LFAILGRID(LF)

   **i**

   **1 - NNOD**

   **or**

   **-1 to  **

   **-NNOD**

   | The floodplain grid element number with a levee that may
     potentially fail.  
   | LFAILGRID = 1 to NNOD; Prescribed failure starts at LFAILGRID.
   | LFAILGRID = -1 to -NNOD; Prescribed failure is globally assigned to
     all 

   levee elements (see comment 1).

   LGRIDNO(L)

   **i**

   **1 - NNOD**

   **or**

   **-1 to  **

   **-NNOD**

   | The grid element number containing the levee segment.
   | LGRIDNO = 1 to NNOD; default no overtop flows reported.
   | LGRIDNO = -1 to -NNOD; overtop flow rates reported to OVERTOP.

   OUT (see comment 8).

   RAISELEV

   **r**

   **0 - 100**

   **0 - 30**

   Incremental height (ft or m) that all the levee grid element
   crest elevations 

   are raised.

   Variable Descriptions for the 

   LEVEE.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page145-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314400144.png
   135

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   LEVEE.DAT File  

     

   1.  The prescribed levee failure criteria are as follows:  

   | a.  For the levee to fail when overtopped by the flow, set FAILELEV
     and FAILTIME = 0.
   | b.  To fail the levee at a specified elevation, set FAILELEV equal
     to the failure elevation.
   | c.  To fail the levee at a specified level below the top of the
     levee, set FAILELEV to a value less 

   than 10 ft and the levee will fail at an elevation equal to LEVCHREST
   - FAILELEV.

   d.  To fail the levee at a specific level below the crest after the
   water surface reaches FAILEVEL for 

   a cumulative duration, assign FAILTIME.

   e.  To fail the levee to a new base elevation that is different than
   the floodplain elevation, assign 

   LEVBASE. 

   f.  To fail a levee to a specified maximum width, set the
    FAILWIDTHMAX to the limiting 

   width.

   g.  To simulate instantaneous collapse, set the FAILRATE and
   FAILWIDRATE to zero (see 

   Comment 10).

   h.  Progressive levee failure is simulated by assigning a value to
   FAILRATE (ft/hr).  This computes 

   the new levee crest elevation as failure proceeds.  FAILRATE is a
   vertical rate of decrease in the 

   levee breach elevation.

   i.  If prescribed failure levee grid element is negative, the failure
   data for that element is assumed 

   to be global and applies to all the levee elements and blocked flow
   directions. In this case, the 

   failure data needs only to be assigned to one element. 

   2.  No multiple channels will be assigned to grid elements with
   levees.  Multiple 

   channels in a levee grid element are eliminated automatically by the
   model.

   3.  Each levee grid element can have up to eight failure directions.  The initial 

   breach width is hardwired as 1.0 ft (0.3 m).  The user specifies the
   maximum 

   anticipated breach width with the parameter FAILWIDTHMAX.  If the
   maxi-

   mum failure width is greater than the grid element side width, the
   breach will 

   extend into adjacent grid elements until the maximum failure width is
   reached 

   or the levee ends.

   4.  Flow over a levee is computed as broadcrested weir flow using a
   coefficient of 

   3.09 until the tailwater depth is 80% of the headwater depth.  The
   discharge 

   computation then reverts to overland flow based on the water surface
   elevations 

   on each side of the levee and the flow depth over the levee.

.. container::
   :name: page146-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314500145.png
   136

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   5.  Levee freeboard deficit is reported in the output file
   LEVEEDEFIC.OUT.  

   Five levels of freeboard deficit are listed in the file as follows:

   Level  0 

    > 3 ft

   1 

   2 ft < freeboard < 3 ft

   2 

   1 ft < freeboard < 2 ft

   3 

   freeboard < 1 ft

   4 

   levee overtopped

   6.  There two options for specifying levee or dam breach failure.
    Set ILEVFAIL = 

   1 to assess the breach failure with prescribed rates of breach
   opening vertically 

   and horizontally. Set ILEVFAIL = 2 to allow the model to simulate the
   breach 

   erosion failure.

   7.  Guidelines on levee failure can be found in the Handouts folder:
   C:\\ users\\

   public\\public documents\\FLO-2D PRO
   Documentation\\flo_help\\Handouts\\

   FLO-2D Levee, Dam, and Wall Failure Guidelines.pdf.

   8.  A report of the levee overtop discharge results are written to
   the LEVEEOVER-

   TOP.OUT file for any element that is listed with a negative grid
   element num-

   ber in the LEVEE.DAT file.

   9. 

   A distinction has been made for the start times of the Time to 1 ft
   and Time to 2 ft and Time to 

   Peak for levee and dam breach models. Two start times are now
   available.  The default start time 

   initiates when the model starts.  The alternate start time initiates
   when the levee or dam breach 

   begins. This is complicated if there are multiple levee or dam
   breaches.  It should also be noted 

   that inflow hydrographs or rainfall may not sync with a breach. There
   can only be one start time.  

   Distinguishing flows mixing from breaches, flood hydrographs,
   rainfall is impossible.

   10.  Wall failure procedures are defined in the guidelines listed
   above.  The proceedures for setting up 

   walls and wall failure, wall failure and grid element elevations,
   walls and ARFs, and the automatic 

   controls aplied by the FLO-2D engine are all explained in the
   guidelines. 

   11.  Levee failure criteria:

    

   ·

   Water surface elevawtion must be greater than the prescribed levee
   faiure elevation plus a 

   tolerance value of 0.1 ft or 0.03 m.

    

   ·

   Water surface elevation on the serervoir side of the levee must be
   higher than the downstream 

   water surface elevation.

    

   ·

   The water surface elevation minus the ground elevation (flow deopth)
   on the reservoir side 

   must be greater than the water surface elevation minus the ground
   elevation (flow depth) on 

   the downstream side of the dam or levee.

.. container::
   :name: page147-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314600146.png
   137

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  FPXSEC.DAT

   FLOODPLAIN CROSS SECTION DATA

   FPXSEC.DAT File Variables 

   P   0 

   Line 1: 

   **FPXSECHAR = ‘P’   NXPRT  **

   X  3  11  284  ... 

   Line 2: 

   **FPXSECHAR = ‘X’   IFLO(N)   NNXSEC(N)   NODX(N,J)   **

   **  **

   Notes:

   Line 2:  Repeat this line for each cross section.

   FPXSEC.DAT File Example

    P  0

   X 3 11 284 285 286 287 288 289 290 291 292 293 294

   X 3 14 808 809 810 811 812 813 814 815 816 817 818 819 820 821

   X 3 15 1097 1098 1099 1100 1101 1102 1103 1104 1105 1106 1107 1108
   1109 1110 1111

   X 3 10 1365 1366 1367 1368 1369 1370 1371 1372 1373 1374

   X 3 26 1857 1858 1859 1860 1861 1862 1863 1864 1865 1866 1867 1868
   1869 1870 1871 

   X 3 28 2491 2492 2493 2494 2495 2496 2497 2498 2499 2500 2501 2502
   2503 2504 2505 

   X 3 12 4224 4225 4226 4227 4228 4229 4230 4231 4232 4233 4234 4235

   X 2 8 7373 7303 7236 7180 7124 7068 7012 6956

   X 2 5 8233 8135 7941 7845 7749

   X 3 6 9000 9001 9002 9003 9004 9005

   X 3 ...

.. container::
   :name: page148-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314700147.png
   138

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT RANGE

   DESCRIPTION

   FPXSECHAR

   **c**

   **P or X**

   | Character line identifier for Lines 1 and 2, 
   | ‘P’   = Line 1

   ‘X’   = Line 2

   Variable is case sensitive and it must be upper case.

   IFLO(N)

   **i**

   **1 - 8**

   Defines the general direction that the flow is expected to cross the
   floodplain 

   | cross section (See comment 1).  IFLO is set to one of the
     following:
   | 1  flow to the north  

   5  flow to the northeast

   2  flow to the east   

   6  flow to the southeast

   3  flow to the south   

   7  flow to the southwest

   4  flow to the west   

   8  flow to the northwest

   If the output is desired from only one direction (i.e. without the
   discharge 

   components from the other component flow directions), set IFLO as
   nega-

   tive.  IFLO is set to the following:

   -1  flow from south only  -5  flow from southwest only

   -2  flow from west only  -6  flow from northwest only

   -3  flow from north only  -7  flow from northeast only

   -4  flow from east only 

   -8  flow from southeast only

   NODX(N,J)

   **i**

   **1 - NNOD**

   Array of grid elements that constitute a given floodplain cross
   section (see 

   comment 2 and 3).

   NNXSEC(N)

   **i**

   **1 - 1,000**

   Number of floodplain elements in a given cross section.  The selected
   cross 

   section grid elements do not have to extend across the entire grid
   system.  

   Only one grid element is necessary to constitute a floodplain cross
   section.  

   The cross section can include a channel element.  If one of the
   floodplain 

   cross section grid elements is a channel element, the cross section
   discharge 

   hydrograph reported in HYCROSS will include the channel element dis-

   charge.

   NXPRT

   **s**

   **0 or 1**

   If NXPRT = 1, the cross section summary information including cross
   sec-

   tion discharge, average cross section velocity, width and depth will
   be re-

   ported in the BASE.OUT file.

   Variable Descriptions for the 

   FPXSEC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page149-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314800148.png
   139

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   FPXSEC.DAT File

   1.  The floodplain grid elements can be combined to define a cross
   section across 

   a floodplain or alluvial fan.  Each floodplain cross section is
   assigned flow dis-

   charge in only one flow direction given by IFLO.  This direction
   includes the 

   flow contribution from the two contiguous directions.  The cross
   section rou-

   tine can be used to isolate the results for a single element.  The
   flow directions 

   and associated discharge components are as follows:

   TABLE 4.3.  CROSS SECTION FLOW DIRECTION

   Selected Cross Section Flow Direction

   Flow Direction Components added to the 

   Cross Section Discharge

   north = 1

   northeast 5 and northwest 8

   east =   2

   northeast 5 and southeast 6

   south = 3

   southeast 6 and southwest 7

   west =  4

   southwest 7 and northwest 8

   northeast =   5

   north 1 and east 2

   southeast =   6

   east 2 and south 3

   southwest =  7

   south 3 and west 4

   northwest =  8

   west 4 and north 1

   For the diagonal flow directions (5 thru 8), the discharge for the
   grid element 

   between the two diagonal corners will be added to the cross section
   total dis-

   charge for the selected flow direction.

   2.  If a grid element is listed more than once, the simulation will
   fail and the ER-

   ROR.CHK file will report the redundant element. 

   3.  The floodplain cross section grid elements can be selected
   graphically with the 

   GDS or QGIS programs.  See FLO-2D Plugin User Manual for
   instructions.

   4.  Select a flow direction perpendicular to the cross section only.
    For example, if 

   the cross section orientation is East to West, the flow direction
   should be North 

   or South only.

.. container::
   :name: page150-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202314900149.png
   140

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  BREACH.DAT 

   DAM AND LEVEE BREACH DATA

   BREACH.DAT File Variables

    

   Line 1: 

   **IBR = ‘B1’   IBREACHSEDEQN   GBRATIO   GWEIRCOEF   **

   **   GBREACHTIME**

   | B1   4    2.0    2.95   0.50
   |  

   Line 2: 

   **IBR = ‘G1’   GZU   GZD  GZC  GCRESTWIDTH   GCRESTLENGTH   **

   ** **

   ** **

   **GBRBOTWIDMAX   GBRTOPWIDMAX   GBRBOTTOMEL   **

   | G1   2.0    2.0   0.   5.   0.   0.   0.   1.5   
   |  

   Line 3: 

   **IBR = ‘G2’   GD50C   GPORC   GUWC   GCNC   GAFRC   GCOHC   **

   **   GUNFCC   **

   | G2   0.   0.   0.   0.    0.   0.   0.   
   |  

   Line 4: 

   **IBR = ‘G3’   GD50S   GPORS   GUWS   GCNS   GAFRS   GCOHS   GUNFCS**

   | G3   0.25   0.40   100.   0.06   30.   65.   0.
   |  

   Line 5: 

   **IBR = ‘G4’   GGRASSLENGTH   GGRASSCOND   GGRASSVMAXP   **

   ** **

   ** **

   **GSEDCONMAX   D50DF   GUNFCDF  **

   | G4   4.   1.   4.   0.   0.   0.
   |  

   Line 6: 

   **IBR = ‘B2’   IBREACHGRID   IBREACHDIR**

   | B2   4015   7
   |  

   Line 7: 

   **IBR = ‘D1’   ZU  ZD   ZC   CRESTWIDTH   CRESTLENGTH   **

   ** **

   ** **

   **BRBOTWIDMAX   BRTOPWIDMAX   BRBOTTOMEL   WEIRCOEF**

   D1   2.0     2.0      0.      8.      0.      0.     0.    83.25  
    3.05

   ** **

   Line 8:  

   **IBR = ‘D2’  D50C   PORC   UWC   CNC   AFRC   COHC   UNFCC**

   D2   0.      0.       0.      0.      0.      0.     0.    0.    0.  
     0.

   ** **

   Line 9: 

   **IBR = ‘D3’   D50S   PORS   UWS   CNS   AFRS   COHS   UNFCS**

   D3   0.25    0.40   100.      0.10   25.    100.     0.

   ** **

   Line 10: 

   **IBR = ‘D4’   BRATIO  GRASSLENGTH  GRASSCOND  GRASSVMAXP      **

   ** **

   ** **

   **SEDCONMAX   D50DF   UNFCDF  BREACHTIME**

   D4     0.       0.      0.      0.      0.     0.    0.

     

   Line 11: 

   **IBR = ‘F’   FRAGCHAR(I)   PRFAIL(I,J)   PRDEPTH(I,J)**

   ;

    

    

   I = number of levee fragility curves and J = number of points in each
   fragility curve

   F   S1  0.03  6.0

.. container::
   :name: page151-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315000150.png
   141

   **D**

   **ata**

   ** I**

   **nPut**

   BREACH.DAT File Example

   Notes:

   Line 1:  Required for a sediment erosion breach 

   Lines 2 - 5:  Global data required to locate a breach.  Not required
   for a prescribed 

   breach location.  

   Lines 6 - 10:  Optional data for prescribed breach location.  Repeat
   these lines for 

   each specified breach grid element. 

     Line 10:  Repeat this line for each fragility curve listing 

     B1   4.0   2.0    2.95     0.50

   G1  2.0     2.0      0.      5.      0.      0.     0.     3.    
   3.05

   G2  0.      0.       0.      0.      0.      0.     0.     

   G3  0.25    0.40   100.      0.06   30.     100.    0.

   G4  1.      0.       0.      0.      0.      0.     0.

   B2  4015   7

   D1  2.0     2.0      0.      8.      0.      0.     0.    83.25  
    3.05

   D2  0.      0.       0.      0.      0.      0.     0.    0.    0.  
     0.

   D3  0.25    0.40   100.      0.10   25.    100.     0.

   D4  2.      0.       0.      0.      0.      0.     0.    0.

   F S1  0.03  6.0

   F S1  0.15  3.5

   F S1  0.50  2.5

   F S1  0.85  1.0

   F S1  0.95  0.0

   F S2  0.03  9.0

   F S2  0.15  5.5

   F S2  0.50  4.0

   F S2  0.85  2.0

   F S2  0.98  0.0

   F S3  0.03 12.0

   F S3  ... 

   FILE:  BREACH.DAT

   DAM AND LEVEE BREACH DATA

.. container::
   :name: page152-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315100151.png
   142

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   AFRC

   **r**

   **0 - 50**

   Angle (degrees) of internal friction of the core material for failure
   of a specific 

   grid element flow direction.  Set AFRC = 0.0 for no core.

   AFRS

   **r**

   **0 - 50**

   Angle (degrees) of internal friction of the shell material for
   failure of a specific 

   grid element flow direction.

   BRATIO

   **r**

   **1 - 5**

   Ratio of the initial breach width to breach depth (see comments 2 and
   3).

   BRBOTTOMEL

   **r**

   **0 - **

   Initial breach or pipe bottom elevation (ft or m) (see comments 5 and
   6).

   BRBOTWIDMAX

   **r**

   **0 - **

   Maximum allowable breach bottom width (ft or m) as constrained by
   the 

   valley cross section.  Set BRBOTWIDWAX = 0.0 if the dam levee is
   contin-

   uous through adjoining grid elements (default = grid element octagon
   side).

   BREACHTIME

   **r**

   **- SIMULT **

   **to **

   **SIMULT**

   **-99**

   The cumulative duration (hrs) that the levee erosion will ini-

   tiate after the water surface exceeds the specified pipe eleva-

   | tion BRBOTTOMEL.
   | If BREACHTIME = 0 if the level erosion begins immedi-

   | ately when pipe elevation is exceeded.
   | If BREACHTIME > or = 0.0, the start time for time to 1 ft 

   | and time to 2 ft is based on the model start time 0.0 hr.
   | If BREACHTIME < 0.0, the start time for time to 1 ft and 

   time to 2 ft is the first dam or levee breach time for multiple 

   | breaches.
   | If BREACHTIME = -99.0, the start time for time to 1 ft and 

   time to 2 is the first dam or levee breach time for multiple 

   breaches and BEACHTIME is reset to 0.0 hr.

   BRTOPWIDMAX

   **r**

   **0 - **

   Maximum allowable breach top width (ft or m) as constrained by the
   val-

   ley cross section.  Set BRTOPWIDMAX = 0.0 if the levee is continuous 

   through adjoining grid elements (default = grid element octagon
   side).

   COHC

   **r**

   **0 - 750**

   **0 - 30,000**

   Cohesive strength (lb/ft

   2

    or N/m

   2

   ) of the levee or dam core material. If there 

   is no core, COHC = 0.

   COHS

   **r**

   **0 - 750**

   **0 - 30,000**

   Cohesive strength (lb/ft

   2

    or N/m

   2

   ) of the levee or dam shell material.  If there 

   is no core, COHS = 0. 

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page153-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315200152.png
   143

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CNC

   **r**

   **0.02 - 0.25**

   Manning’s n-value of the levee or dam core material.  If CNC = 0.,
   Man-

   ning’s n-value for the core material will computed from Strickler’s
   equa-

   tion.  

   If CNC > 1., the n-value will be computed from a Moody diagram (Darcy
   f 

   vs. D

   50

   ).  Set CNC = 0.0 for no core material. 

   CNS

   **r**

   **0.02 - 0.25**

   Manning’s n-value of the levee or dam shell material.  See comment 4.
   If 

   CNS = 0., Manning’s n-value for the shell material will computed
   from 

   Strickler’s equation. If CNS > 1., the n-value will be computed from
   a 

   Moody diagram (Darcy f vs. D

   50

   ). 

   CRESTLENGTH

   **r**

   **0 - **

   Length of the crest of the levee or dam (ft or m).  If CRESTLENGTH =
   0., 

   the crest length will default to the grid element octagon side.  If
   crest length 

   is greater than the grid element octagon side, it will be reset to
   the octagon 

   side length.

   CRESTWIDTH

   **r**

   **0 - **

   Crest width of the levee or dam (ft or m).  The crest width can be
   zero.

   D50C

   **r**

   **0.0625 - 2**

   Mean sediment size (D

   50

    in mm) of the levee or dam core material.

   D50S

   **r**

   **0.25 - 10**

   Mean sediment size (D

   50

    in mm) of the levee or dam shell material.

   D50DF

   **r**

   **1.0 - 100**

   Mean sediment size (D

   50

    in mm) of the top one foot (0.3 m) of the down-

   stream face (riprap material).  If D50DF = 0.0, then D50DF = D50S.

   FRAGCHAR

   **c**

   **S1, S2 ...**

   Fragility curve ID.  One letter and a number.  For example:  S1 is
   fragility 

   curve 1 for the Sacramento River (see comment 7). Variable is case
   sen-

   sitive and it must be upper case.

   GAFRC

   **r**

   **0 - 50**

   Global angle (degrees) of internal friction of the core material for
   the entire 

   levee or dam.  Set AFRC = 0.0 for no core.

   GAFRS

   **r**

   **0 - 50**

   Global angle (degrees) of internal friction of the shell material for
   the entire 

   levee or dam. 

   GBRBOTTOMEL

   **r**

   **0 - **

   Initial global breach or pipe bottom elevation (ft or m) for an
   unspecified 

   failure location. If the model will locate the failure grid element
   instead of 

   user specified failure location, then set GBRBOTTOMEL = distance
   below 

   the dam or levee crest elevation (ft or m).  In general, GBRBOTTOMEL
   be 

   less than 10 ft (3 m) (see comments 1 and 6).

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page154-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315300153.png
   144

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   GBRBOTWIDMAX

   **r**

   **0 - **

   Maximum allowable global breach bottom width (ft or m) as constrained
   by 

   the valley cross section for an unspecified failure location.  Set
   GBRBOT-

   WIDWAX = 0.0 if the levee is continuous through adjoining grid
   elements 

   (default = grid element octagon side). 

   GBREACHTIME

   **r**

   **0 - **

   The cumulative duration (hrs) that the levee erosion will initiate
   after the 

   water surface exceeds the specified pipe elevation BRBOTTOMEL.  GB-

   REACHTIME = 0 if the level erosion begins immediately when pipe
   eleva-

   tion is exceeded.

   GBRTOPWIDMAX

   **r**

   **0 - **

   Maximum allowable global breach top width (ft or m) as constrained by
   the 

   valley cross section for an unspecified failure location.
    GBRTOPWIDMAX 

   = 0.0 if the levee is continuous through adjoining grid elements
   (default = 

   grid element octagon side).

   GCOHC

   **r**

   **0 - 750**

   **0 - 30,000**

   Global cohesive strength (lb/ft

   2

    or N/m

   2

   ) of the levee or dam core material 

   for an unspecified failure location.  If there is no core, GCOHC =
   0. 

   GCOHS

   **r**

   **0 - 750**

   **0 - 30,000**

   Global cohesive strength (lb/ft

   2

    or N/m

   2

   ) of the levee or dam shell material 

   for an unspecified failure location.  

   GCNC

   **r**

   **0.03 - 0.1**

   Global Manning’s n-value of the levee or dam core material for an
   unspeci-

   fied failure location.  See comment 4. If GCNC = 0.0 and a core is
   present, 

   Manning’s n-value for the core material will computed from
   Strickler’s equa-

   tion.  This results in a very low n-value and is not recommended. If
   GCNC 

   > 1., the n-value will be computed from a Moody diagram (Darcy f vs.
   D

   50

   ).  

   Set GCNC = 0.0 for no core material.  

   GCNS

   **r**

   **0.03 - 0.1**

   Global Manning’s n-value of the levee or dam shell material for an
   unspeci-

   fied failure location.  See comment 4. If GCNS = 0., Manning’s
   n-value 

   for the shell material will computed from Strickler’s equation. This
   is not 

   recommended.  If GCNS > 1., the n-value will be computed from a
   Moody 

   diagram (Darcy f vs. D

   50

   ).  

   GCRESTLENGTH

   **r**

   **0 - **

   Global crest length of the levee or dam (ft or m) for an unspecified
   failure 

   location.  If GCRESTLENGTH = 0.0, the crest length will default to
   the 

   grid element octagon side.  If crest length is greater than the grid
   element 

   octagon side, it will be reset to the octagon side length.

   GCRESTWIDTH

   **r**

   **0 - **

   Global crest width of the levee or dam (ft or m) for an unspecified
   failure 

   location.  The crest width can be zero.

.. container::
   :name: page155-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315400154.png
   145

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   GD50C

   **r**

   **0.0625 - 2**

   Mean sediment size (D

   50

    in mm) of the levee or dam core material.

   GD50S

   **r**

   **0.25 - 10**

   Mean sediment size (D

   50

    in mm) of the levee or dam shell material.

   GD50DF

   **r**

   **1 - 100**

   Mean sediment size (D

   50

    in mm) of the top one foot (0.3 m) of the 

   downstream face (riprap material).  If GD50DF = 0.0, then GD50DF = 

   GD50S.

   GGRASSCOND

   **r**

   **0 - 1**

   Global condition of the grass on the downstream face of the levee or
   dam 

   for an unspecified failure location.  0.0 for a poor stand or no
   grass;1.0 for a 

   good stand of grass. 

   GGRASSLENGTH

   **r**

   **0 - 10**

   Global average length of grass (inches or mm) on downstream face for
   an 

   unspecified failure location.  Set GGRASSLENGTH =
   0.0 for no grass on 

   downstream face.

   GGRASSVMAXP

   **r**

   **3 - 6**

   **1 - 2**

   Global maximum permissible velocity (fps or mps) for a grass-lined
   down-

   stream face before the grass is eroded for an unspecified failure
   location.  

   Range:  3 to 6 fps (1 to 2 mps).  If no grass, set GGRASSVMAXP = 0.0.

   GPORC

   **r**

   **0.35 - 0.45**

   Global porosity of the levee or dam core material for an unspecified
   failure 

   location.  Typical range:  0.35 to 0.45.  Set GPORC = 0.0 for no core
   mate-

   rial.  

   GPORS

   **r**

   **0.35 - 0.45**

   Global porosity of the levee or dam shell material for an unspecified
   failure 

   location.  Typical range:  0.35 to 0.45. 

   GRASSCOND

   **r**

   **0 - 1**

   Condition of the grass on the downstream face of the levee or dam for
   a 

   prescribed failure location.  0.0 for a poor stand or no grass; 1.0
   for a good 

   stand of grass. 

   GRASSLENGTH

   **r**

   **0 - 1**

   **0 - 25**

   Average length of grass (inches or mm) on downstream face for a
   prescribed 

   failure location.  Set GRASSLENGTH = 0.0 for no grass on downstream 

   face.

   GRASSVMAXP

   **r**

   **3 - 6**

   **1 - 2**

   Maximum permissible velocity (fps or mps) for a grass-lined
   downstream 

   face before the grass is eroded for a prescribed failure location.
    Range: 3 to 6 

   fps (1 to 2 mps).  If no grass, set GRASSVMAXP = 0.0.

   GSEDCONMAX

   **r**

   **0.2 - 0.55**

   Global maximum sediment concentration by volume in the breach dis-

   charge for an unspecified failure location.  Typical range = 0.2 to
   0.55.  If 

   GSEDCONMAX = 0.0, a default value of 0.5 is used. 

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page156-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315500155.png
   146

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   GUNFCC

   **r**

   **1 - 20**

   Global sediment gradient, ratio of D

   90

    to D

   30

    of the levee or dam core ma-

   terial for an unspecified failure location.  If there is no core
   material, set 

   GUNFCC = 0.0.  If the there is core material and GUNFCC = 0.0, it is 

   reset to 10.0.

   GUNFCDF

   **r**

   **1 - 20**

   Global sediment gradient, ratio of D

   90

    to D

   30

    of the downstream face upper 

   one foot of material (riprap) for an unspecified failure location.
    If GUN-

   FCDF = 0.0: GUNDFCDF = GUNFCS  when GD50DF = 0.0 and GUN-

   DFCDF = 3.0 when GD50DF > 0.0. 

   GUNFCS

   **r**

   **1 - 20**

   Global sediment gradient, ratio of D

   90

    to D

   30

    of the levee or dam shell mate-

   rial for an unspecified failure location.  If GUNFCS = 0.0, the
   default value 

   is 10.0.

   GUWC

   **r**

   **85 - 120**

   **13,500 - **

   **19,000**

   Global unit weight (lb/ft

   3

    or N/m

   3

   ) of the levee or dam core material for an 

   unspecified failure location.  Set GUWC = 0.0 if there no core. 

   GUWS

   **r**

   **85 - 120**

   **13,500 - **

   **19,000**

   Global unit weight (lb/ft

   3

    or N/m

   3

   ) of the levee or dam shell material for an 

   unspecified failure location.  

   GWEIRCOEF

   **r**

   **2.85 - 3.05**

   Global weir coefficient for piping or breach channel weir for an
   unspecified 

   failure location.  Typical range:  2.85 – 3.05. 

   GZC

   **r**

   **0.1 - 10**

   Global average slope of the upstream and downstream face of the levee
   or 

   dam core material for an unspecified failure location.  GZC is
   expressed as a 

   ratio of the GZC (horizontal:1 (vertical).  For example:  GZC = 2.0
   repre-

   sents 2.0 horizontal to 1.0 vertical.  If there is no core set GZC =
   0.0

   GZD

   **r**

   **0.1 - 10**

   Global slope of the downstream face of the levee or dam for an
   unspecified 

   failure location.  GZD is expressed as a ratio of the GZD
   (horizontal : verti-

   cal).  For example: GZD = 2.0 represents 2.0 horizontal to 1.0
   vertical. 

   GZU

   **r**

   **0.1 - 10**

   Global slope of the upstream face of the levee or dam for an
   unspecified fail-

   ure location.  GZU is expressed as a ratio of the GZU (horizontal :
   vertical).  

   For example: GZU = 2.0 represents 2.0 horizontal to 1.0 vertical.

.. container::
   :name: page157-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315600156.png
   147

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IBR

   **c**

   **B1, B2, **

   **D1, D2, **

   **D3, D4, **

   **G1, G2, **

   **G3, G4 **

   **or F**

   Character line identifier:

   ‘G1-G4’ = global data

   ‘B1’ = Global data not related to local breach; 

   ‘B2’ = Grid element  and direction

   ‘D1-D4’ = individual prescribed grid element breach data.

   ‘F’ = fragility curve data

   Variable is case sensitive and it must be upper case.

   IBREACHDIR

   **i**

   **1 -  8**

   Direction of the specified breach failure in a given grid element.
    The possible 

   | flow directions are:
   | 1 = north 

   5 = northeast

   2 = east  

   6 = southeast

   3 = south 

   7 = southwest

   4 = west 

   8 = northwest

   IBREACHGRID

   **i**

   **1 - NNOD**

   Grid element of the specified breach failure location.  See comment
   8.

   IBREACHSEDEQN

   **i**

   **1 - 11**

   Sediment transport equation that is used to compute the 

   breach erosion.  Out of eleven transport equations in FLO-

   2D only Tofaletti and MPM-Woo are not available.  See the 

   list of sediment transport equation numbers in SED.DAT.

   PORC

   **r**

   **0.35 - 0.45**

   Porosity of the levee or dam core material for a prescribed grid
   element fail-

   ure location.  Set GPORC = 0.0 for no core material. 

   PORS

   **r**

   **0.35 - 0.45**

   Porosity of the levee or dam shell material for an prescribed grid
   element 

   failure location.  

   PRDEPTH

   **r**

   **0.0 - Levee **

   **Crest **

   **Height**

   Point of failure on the levee as defined by the distance or height
   below the le-

   vee crest (likely failure point according to the Corps of Engineers
   definition).  

   Assigned with a corresponding fragility curve failure probability
   PRFAIL.

   PRFAIL

   **r**

   **0.0 - 1.0**

   Levee fragility curve point of failure probability.  Range:  0.0 to
   1.0 where 

   80% indicates a higher probability of levee failure most likely
   corresponding 

   to a higher elevation on the levee (see the levee fragility curve
   discussion in 

   the FLO-2D Reference Manual).  A low value of 10% would indicate a 

   weak levee most likely corresponding to a levee piping failure close
   to the 

   toe of the levee.

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page158-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315700157.png
   148

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   SEDCONMAX

   **r**

   **0.20 - 0.55**

   Maximum sediment concentration by volume in the breach discharge for 

   a prescribed grid element failure location.  Typical range = 0.2 to
   0.55.  If 

   SEDCONMAX = 0.0, a default value of 0.5 is used.

   UNFCC

   **r**

   **1 - 20**

   Sediment gradient, ratio of D

   90

    to D

   30 

   of the levee or dam core material for 

   a prescribed grid element failure location.  If there is no core
   material, set 

   UNFCC = 0.0.  If the there is core material and UNFCC = 0.0, it is
   reset 

   to 10.0.

   UNFCDF

   **r**

   **1 - 20**

   Sediment gradient, ratio of D

   90

    to D

   30

    of the downstream face upper one 

   foot of material (riprap) for a prescribed grid element failure
   location.  If 

   UNFCDF = 0.0 : UNDFCDF = UNFCS when D50DF = 0.0 and UND-

   FCDF = 3.0 when D50DF > 0.0. 

   UNFCS

   **r**

   **1 - 20**

   Sediment gradient, ratio of D90 to D30 of the levee or dam shell
   material 

   for a prescribed grid element failure location.  If UNFCS = 0.0, the
   default 

   value is 10.0.

   UWC

   **r**

   **85 -120 **

   **13,500 - **

   **19,000**

   Unit weight (lb/ft

   3

    or N/m

   3

   ) of the levee or dam core material for a pre-

   scribed grid element failure location.  Set UWC = 0.0 if there no
   core.

   UWS

   **r**

   **85 - 120 **

   **13,500 - **

   **19,000**

   Unit weight (lb/ft

   3

    or N/m

   3

   ) of the levee or dam shell material for a pre-

   scribed grid element failure location.

   WEIRCOEF

   **r**

   **2.85 - 3.05**

   Weir coefficient for piping or breach channel weir for a prescribed
   grid ele-

   ment failure location.  Typical range:  2.85 – 3.05.

   ZC

   **r**

   **0.1 - 10**

   Average slope of the upstream and downstream face of the levee or dam
   core 

   material for a prescribed failure location. ZC is expressed as a
   ratio of the ZC 

   (horizontal : vertical).  For example:  ZC = 2.0 represents 2.0
   horizontal to 

   1.0 vertical.  If there is no core set ZC = 0.

   ZD

   **r**

   **0.1 - 10**

   Slope of the downstream face of the levee or dam for a prescribed
   grid ele-

   ment failure location.  ZD is expressed as a ratio of the ZD
   (horizontal : verti-

   cal).  For example: ZD = 2.0 represents 2.0 horizontal to 1.0
   vertical. 

   ZU

   **r**

   **0.1 - 10**

   Slope of the upstream face of the levee or dam for a prescribed grid
   element 

   failure location.  ZU is expressed as a ratio of the ZU (horizontal :
   vertical).  

   For example: ZU = 2.0 represents 2.0 horizontal to 1.0 vertical.

   Variable Descriptions for the 

   BREACH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page159-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315800158.png
   149

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   BREACH.DAT File

   1.  There is a choice of either identifying a global or local levee
   breach location.  If 

   the breach location is assigned locally, it is necessary to provide
   only the Local 

   (D-Lines) 5-8 in the BREACH.DAT file.  This data is entered in the
   Individual 

   tab of the GDS Breach dialog box.  If  the model  locates all the
   potential breach 

   locations based on the water surface elevation, then it is only
   necessary to as-

   sign the global parameters (G-Lines) in lines 1-4 and  the variable
   GBRBOT-

   TOMEL = vertical distance (ft or m) below the levee or dam crest
   elevation.  

   If the water surface elevation exceeds GBRBOTTOMEL, then a levee
   piping 

   failure will be initiated.  One or more breach locations can be
   prescribed and 

   still permit the model to determine any other potential breach
   locations to be 

   initiated by setting GBBOTTOMEL to value less than about 10 ft (3 m)
   below 

   the crest elevation.

   2.  Initial breach width to depth ratio (BRATIO) – if the assigned
   breach width to 

   depth ration is 0., then BRATIO = 2.

   | 3.  The initial piping width and depth is assumed to be 0.5 ft
     (0.15 m).  
   | 4.  The minimum and maximum Manning’s n-value permitted for the
     breach flow 

   resistance are 0.02 and 0.25, respectively.

   5.  The downstream pipe outlet at the toe of the dam or levee is hard
   coded to the 

   grid element floodplain elevation plus 1 ft (0.3 m). 

   6.  Breach discharge is computed if the upstream water surface
   elevation exceeds 

   the upstream breach pipe or channel bottom elevation plus the
   tolerance value 

   (TOL ~ 0.1 ft or 0.3 m).

   7.  The levee fragility curve ID is only one letter (e.g. S) and a
   number (e.g. 3) and 

   the data line begins with ID character ‘F’.  The levee fragility
   curve assignment 

   to the levee grid element is assigned in the LEVEE.DAT file. 

   8.  If Line 2 begins with G1, a global breach simulation is initiated to locate the 

   potential breach based on the water surface elevation.  If Line 2 has
   a B2 identi-

   fier, then a prescribed breach location will be simulated as defined
   by the breach 

   element and flow direction in Line B2 (global breach data is not
   required)

.. container::
   :name: page160-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202315900159.png
   150

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  FPFROUDE.DAT 

   FLOODPLAIN LIMITING FROUDE NUMBERS

   FPFROUDE.DAT File Variables

   F      1      0.65 

   Line 1:   

   **IFR = ‘F’   I    FROUDEFP (I = 1, NNOD)**

   FPFROUDE.DAT File Example

   F      1      0.65 

   F      2      0.88

   F      3      0.90

   F      43     0.90

   F      54     0.90 

   F      56     1.05

   F      107    0.90

   F      108    0.90

.. container::
   :name: page161-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316000160.png
   151

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IDUM

   **i**

   **1 - **

   **NNOD**

   Grid element number (I) of the floodplain grid system.

   IFR

   **c**

   **F**

   Character Line Identifier = ‘F’.  Variable is case sensitive and it
   must 

   be upper case.

   FROUDEFP

   **r**

   **0.1 - 2**

   Floodplain limiting Froude number.

   Variable Descriptions for the 

   FPFROUDE.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   FPFROUDE.DAT File

   1.  The spatially variable limiting Froude number supersedes the
   global limiting 

   Froude number (FROUDL) in CONT.DAT.

   2.  When FROUDEFP is exceeded the grid element roughness value will
   be 

   increased by 0.001 for the next timestep.  After a flood simulation,
   review 

   ROUGH.OUT to determine where FROUDEFP was exceeded and the maxi-

   mum n-values for that cell were computed.  Consider revising the
   n-values in 

   the MANNINGS_N.DAT file to match those in the ROUGH.OUT file.  This 

   will ensure that FROUDEFP is not exceeded. Rename the MANNINGS_N.

   RGH file to MANNINGS_N.DAT.

.. container::
   :name: page162-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316100161.png
   152

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  SWMMFLO.DAT 

   STORM DRAIN DATA FILE

   SWMMFLO.DAT File Variables

    

   Line 1:    

   **SWMMCHAR= ‘D’  SWMM_JT(I), SWMM_IDEN(I), INTYPE(I), **

   ** **

   ** **

   **SWMMlength(I), SWMMwidth(I), SWMMheight(I), SWMMcoeff(I), **

   **   FEATURE(I),CURBHEIGHT(I)**

      I = number of storm drain inlet nodes.

   D   14291   I37CP1WTRADL   2    13.00   1.00   0.42   2.30   0  
    0.00

    

   SWMMFLO.DAT  File Example

   D 14291     I37CP1WTRADL        2    13.00     1.00      0.42    
    2.30      0     0.00

   D 14481     I37CP2WTRADL        2    13.00     1.00      0.42    
    2.30      0     0.00

   D 13785     I14CP1WTRCLRL       2    20.00     1.00      0.42    
    2.30      0     0.00

   D 13968     I14CP2WTRCLRL       2    20.00     1.00      0.42    
    2.30      0     0.00

   D 14156     I15WTRCLRL              3    11.00     7.00      0.50    
    3.00      0     0.00

.. container::
   :name: page163-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316200162.png
   153

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CURBHEIGHT(I)

   **r**

   **0.0 - **

   Curb height used to calculate discharge on inlets for all IN-

   TYPE inlets.

   FEATURE(I)

   **i**

   **0, 1, or 2**

   Switch positions for FEATURE

   0 = Horizontal Inlet 

   1 = Vertical Inlet

   2 = Flapgate (see comment 2).

   INTYPE(I)

   **i**

   **1 - 5**

   Type of storm drain inlets (see comment 1).

   SWMMCHAR

   **c**

   **D**

   Character line identifier for the SWMM model inlets. Vari-

   able is case sensitive and it must be upper case.

   SWMMcoeff(I)

   **r**

   **2.50 - 3.50**

   Storm drain inlet weir discharge coefficients (see comment 

   2).

   SWMMheight(I)

   **r**

   **0.0 - 2.0**

   Type 1 and type 2 gutter inlets storm drain curb opening 

   | heights (typically less than 1 ft).
   | Type 3 grate inlets, SWMMheight = grate sag height. 
   | Type 5 manhole inlets, SWMMheight = surcharge depth.

   SWMM_JT(I)

   **i**

   **1 - NNOD**

   Grid elements that contains storm drain inlets or man-

   holes.

   SWMMlength(I)

   **r**

   **0.01 - **

   Type 1 and 2 - Storm drain inlet curb opening lengths 

   | along the curb. 
   | Type 3 and 5 grate (gutter) inlets, SWMMlength = grate 

   wetter perimeter or manhole wetted perimeter.

   SWMM_IDEN(I)

   **c**

   **Alpha **

   **Numeric**

   Storm drain inlet name. Inlet name in the SWMM.inp file.  

   Variable is not case sensitive.  No spaces in data.

   Start the name with an i or I to indicate an inlet: im or IM 

   for manholes. This is mandatory. (See comment 1)

   SWMMwidth(I)

   **r**

   **0 - **

   Type 2 storm drain inlet curb opening sag width. 

   Type 3 grate (gutter) inlets, SWMMwidth = grate opening 

   area.

   Type 5 manhole area.

   Variable Descriptions for the 

   SWMMFLO.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page164-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316300163.png
   154

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   SWMMFLO.DAT File

   1.  The Storm Drain Guidelines manual offers a comprehensive overview
   of storm 

   drain modeling using FLO-2D. The storm drain feature names 

   **must**

    begin 

   with an i or I to indicate an inlet, im or IM to indicate a manhole.
    This nam-

   ing convention will allow the GDS or QGIS and FLOPRO.EXE to identify 

   features that will connect to the surface for flow exchange.  The
   storm drain 

   naming feature need not be overly complicated because locating the
   features 

   is simple with the various attribute query tools available in QGIS.
    A simple 

   convention is to name inlets, junctions, outfalls and conduits so
   that they are 

   easily sorted.  For example.  i or I for inlets, im or IM for
   manholes, j or J for 

   junctions, o or O for outfalls.   

   2.  The SWMMFLO.DAT file is automatically generated by GDS or QGIS
   using 

   the SWMM.inp file data to locate the inlet position and transfer it
   to the FLO-

   2D grid system.  For an extensive discussion and guidelines, refer to
   the Storm 

   Drain Manual.  There are three storm drain inlet options:

   1)   Curb opening inlet at grade (Type 1)

   2)   Curb opening inlet depressed or sag (Type 2)

   3)   Grate or grate with gutter inlet (at grade or depressed - Type
   3)

   4)   Non-typical inlet e.g. headwall (Type 4)

   5)   Manhole with cover (Type 5)

   The storm drain inlet data requirements are:

   **Type 1 **

   - Curb opening inlet at grade

   Weir coefficient:   2.85 - 3.30 (suggested 3.00 English, 1.6 Metric)

   Curb opening length

   Curb opening height

   **Type 2**

    - Curb opening inlet with sag

   Weir coefficient:   2.30 (1.25 metric)

   Curb opening length

   Curb opening height

   Curb opening sag width

   **Type 3 **

   - Grate (or grate with gutter) inlet with/without sag

   Weir coefficient:   2.85 - 3.30 (suggested 3.00 English, 1.6 metric)

   Grate perimeter (not including curb side)

   Grate open area 

   Grate sag height (zero for at grade)

   **Type 4 **

   - Variable storm drain inlet geometry.

.. container::
   :name: page165-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316400164.png
   155

   **D**

   **ata**

   ** I**

   **nPut**

   Weir coefficient:  not required.

   The storm drain inlet rating table (line n with depth and discharge
   pairs) 

   is required in the SWMMFLORT data file.

   **Type 5 **

   - Manhole.

   Weir coefficient:   2.85 - 3.20

   Manhole perimeter

   Manhole flow area

   Surcharge depth

   Note:   Orifice flow coefficient = 0.67 (hardwired) for all cases.

.. container::
   :name: page166-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316500165.png
   156

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  SWMMFLORT.DAT 

   STORM DRAIN TYPE 4 RATING TABLE FILE

   SWMMFLORT.DAT File Variables

    

   Line 1: 

   **SWMMCHARRT=’D’   SWMM_JT(I)   STRUCTNAME_INLET**

   D   14292   I4-26

    

   Line 2: 

   **SWMMCHAR = ‘N’    DEPTHSWMMRT(J,K)   QSWMMRT(J,K)**

   N    0.0     0.0

    

   Line 1: 

   **SWMMCHARRT=’S’   SWMM_JT(I)   STRUCTNAME_INLET   CDIAMETER(I)**

   S   7545   I4-38   1.5   

    

   Line 2: 

   **SWMMCHAR = ‘F’   TYPEC(I)   TYPEEN(I)   CUBASE(I)**

   F   2   1   0

   SWMMFLORT.DAT File Example

   D   254765  I4-33

   N   0.00   0.00

   N   0.10   0.00

   N   1.46   10..00

   N   2.11   20.00

   N   2.72   3.00

   N   3.44  40.00

   N   4.35   50.00

   N   5.48  60.00

   N   6..79   70.00

   N   8.23   90.00

   N  11.85   100.00

   S  7545   I4-38   1.5

   F   2   1   0

    ...

.. container::
   :name: page167-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316600166.png
   157

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CDIAMETER(I)

   **r**

   **0 - **

   Circular culvert diameter or box culvert height.  TYPEC(I) 

   defines the culvert shape. (ft or m)

   CUBASE(I)

   **r**

   **0 - **

   1 = Box culvert width

   0 = No width for circular culvert.  Use CDIAMETER(I)

   (ft or m)

   DEPTH-

   SWMMRT (J,K)

   **r**

   **0 - **

   Flow depths for the discharge rating table pairs. (ft or m)

   QSWMMRT(J,K)

   **r**

   **0 - **

   Discharge values for the storm drain inlet rating table.

   (cfs or cms)

   STRUCTNAME\_

   INLET

   **c**

   **Alpha **

   **numeric**

   Name of the type 4 inlet.  No spaces allowed in the name.

   SWMMCHAR

   **c**

   **N, D, S, F**

   Character line identifier.

   N = New line for rating table.

   D = Rating table lines.

   S = New line for generalized culvert equation.

   F = Detailed line for generalized culvert equation.

   SWMM_JT(I)

   **i**

   **1 - NNOD**

   Grid elements with storm drain inlets.

   TYPEC(I)

   **s**

   **0, 1**

   | Culvert switch.  
   |    1 = rectangular
   |    2 = circular

   TYPEEEN(I)

   **s**

   **0, 1, 2**

   Culvert switch. Set TYPEEN(I) for entrance type 1, 2, or 3. 

   (see comment 3).

   Variable Descriptions for the 

   SWMMFLORT.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page168-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316700167.png
   158

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   SWMMFLORT.DAT File

   | 1.  The SWMMFLORT.DAT file lists the rating table data for Type 4
     inlets.
   | 2.  For an extensive storm drain component discussion and
     guidelines, refer to the 

   Storm Drain Manual.

   3.  The Department of Transportation generalized culvert equations
   can be used to 

   assess inlet and outlet control. The type of culvert entrances are:.

   a.  BOX entrance:

   | type 1 - wingwall flare 30 to 75 degrees
   | type 2 - wingwall flare 90 or 15 degrees
   | type 3 - wingwall flare 0 degrees

   b.  PIPE entrance:

   | type 1 - square edge with headwall
   | type 2 - socket end with headwall
   | type 3 - socket end projecting

.. container::
   :name: page169-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316800168.png
   159

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  SWMMOUTF.DAT 

   STORM DRAIN OUTFALL ID DATA FILE

   SWMMOUTF.DAT File Variables

    

   Line 1: 

   **OUTF_NAME(JT)   OUTF_GRID(JT)   OUTF_FLO2DVOL(JT)**

   **  **

   JT = Number of outfalls.

   OUTFALL1  14292    1

   SWMMOUTF.DAT File Example

   OUTFALL1  14292    1

   ...

.. container::
   :name: page170-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202316900169.png
   160

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   OUTF_NAME(JT)

   **c**

   **Alpha **

   **Numeric**

   Name of the feature.  Variable is not case sensitive.  No 

   spaces in the name. (see comment 1).

   OUTF_GRID(JT) 

   **i**

   **1 - NNOD**

   Grid element corresponding to the location of the outfall.

   OUTF\_

   FLO2DVOL(JT)

   **s**

   **0 or 1**

   Outfall discharge switch (see comments 2 and 3):

   0 = off all discharge removed from storm drain system.

   1 = on allows discharge to be returned to the FLO-2D 

   system.

   Variable Descriptions for the 

   SWMMOUTF.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   SWMMOUTF.DAT File

   1.  The list of outfall names and position should correspond to the
   SWMM.inp 

   file.  Do not add spaces to the name.

   2.  If the discharge cannot physically return to the surface, set the
   OUTF_FLO2D-

   VOL to 0.

   3.  If the flow in the storm drain system can return to the surface,
   set the switch to 

   the on position = 1.

.. container::
   :name: page171-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317000170.png
   161

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  SDCLOGGING.DAT 

   STORM DRAIN BLOCKAGE METHOD FILE

   SDCLOGGING.DAT File Variables

    

    

    Line 1:

   ** **

   **SWMMCHAR= ‘D’   SWMM_JT(I)   SWMM_IDEN(I) **

   ** **

   ** **

   **SWMM_CLOGFAC(I)   CLOGTIME(I)**

   **    **

   D   2694   I1   25   0.50

   SDCLOGGING.DAT File Example

   D       2694        I1      25   0.50

   D       3658        I1      25   0.50

   D        224         I1      25   0.50

   D       5286        I1      25   0.50

   D      10257       I1      25   0.50

   ...

.. container::
   :name: page172-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317100171.png
   162

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CLOGTIME(I)

   **r**

   **0 - **

   Time to initiate clogging specified by the user.  See com-

   ment 2. (hours)

   SWMM\_

   CLOGFAC(I)

   **r**

   **0 - 100.**

   Clogging factor for each inlet node.  The value is a percent-

   age (see comment 1). 

   SWMM_IDEN(I)

   **i**

   **Alpha **

   **Numeric**

   Grid element corresponding to the location of the inlet.

   SWMM_JT(I)

   **i**

   **1 - NNOD**

   Grid element with storm clogged storm drain inlets.

   SWMMCHAR= 

   ‘D’

   **c**

   **D**

   Character line identifier for the SWMM model inlets. Vari-

   able is case sensitive.

   Variable Descriptions for the 

   SDCLOGGING.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   SDCLOGGING.DAT File

   1.  The percent clogging is based on the available flow area of a
   storm drain inlet.  

   The metal portion of the inlet grate is not included.

   2.  The time to initiate clogging is based on the starting time of
   the model not the 

   time of inundation of the storm drain inlet.  

.. container::
   :name: page173-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317200172.png
   163

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  SWMMFLODROPBOX.DAT 

   STORM DRAIN BLOCKAGE METHOD FILE

   SWMMFLODROPBOX.DAT File Variables

   2694   19.635  Line 1:

   ** **

   **SWMMDBID   SWMMDROPBOX(I) **

    

    

   I = Number of drop box nodes.

   **  **

   SWMMFLODROPBOX.DAT File Example

   2694        19.566

   3658        19.566

   224          19.566

   5286        19.566

   10257      

   ...

.. container::
   :name: page174-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317300173.png
   164

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   **SWMMDBID**

   **i**

   **1 - NNOD**

   Grid element that contains the storm drain inlet.

   **SWMMDROPBOX**

   (I)

   **r**

   **0 - **

   Drob box surface area for inlet contain in grid element 

   SWMMDBID (ft

   2

    or m

   2

   )(see comment 1). 

   Variable Descriptions for the 

   SWMMFLODROPBOX.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   SWMMFLODROPBOX.DAT File

   1.  SWMMFLODROPBOX.DAT is a data file that can be used to increase
   the 

   dropbox surface area for inlets. The surface area is used in computing changes 

   in water level at inlets. This file allows the user to create a non
   uniform dropbox 

   surface area for those inlets that have a large inlet surface opening
   and which 

   default (12.566 ft

   2

    dropbox surface area  4 ft diameter) does not represent the 

   dropbox surface area.

    

   Pipe Diameter (ft)   

   Dropbox Surf Area (ft

   2

   )

   |  5   19.635
   |  6   28.274
   |  7   38.485
   |  8   50.265
   |  10 

     78.54

.. container::
   :name: page175-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317400174.png
   165

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  TOLSPATIAL.DAT 

   SPATIALLY VARIABLE TOLLERANCE VALUES

   TOLSPATIAL.DAT File Variables

   4554   0.12 

   Line 1:  

   **IDUM (I)  TOL**

   TOLSPATIAL.DAT File Example

   4554   0.5

   4556   0.5

   4557   0.5

   4889   0.5

   ...

.. container::
   :name: page176-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317500175.png
   166

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IDUM(I)

   **i**

   **1 - NNOD**

   Nodes that have a spatially variable TOL value.

   TOL

   **r**

   **0.001 - 5.**

   Spatially variable TOL value (ft or m) that can range from 

   0.001 ft to 5 ft (0.0003 m to 1.52 m)

   Variable Descriptions for the 

   TOLSPATIAL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   TOLSPATIAL.DAT File

   1.  The TOLSPATIAL.DAT file can be used to create spatially variable
   depres-

   sion storage.  The TOL value prescribes the flow depth for a
   floodplain or 

   channel grid element below which no flood routing will be
   performed.  It can 

   be assigned spatially variable for the entire grid system.  TOL is
   analogous to 

   a depression storage rainfall abstraction but also can be applied to study Low 

   Impact Development (LID) retention storage.  See the LID Reference
   white 

   paper and Reference Manual section.

.. container::
   :name: page177-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317600176.png
   167

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  WSURF.DAT 

   WATER SURFACE ELEVATION COMPARISON

   WSURF.DAT File Variables

   10 

   Line 1:

   ** NWSGRIDS**

   4025  200.25 

   Line 2: 

   **IGRIDXSEC(M)   WSELEV(M)   **

   WSURF.DAT File Example

   10

     139   4793.00   

    1521   4786.00  

    4099   4775.00  

    5713   4767.00  

    7611   4760.00  

    9183   4752.00  

   10751   4745.00 

   12442   4736.00 

   14079   4730.00 

   15977   4722.00 

   18061   4711.00 

.. container::
   :name: page178-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317700177.png
   168

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRIDXSEC(M)

   **i**

   **1 - NNOD**

   Nodes that have a known water surface elevation.

   NWSGRIDS

   **i**

   **1 - NNOD**

   Number of rows in the table of water surface elevations.

   WSELEV

   **r**

   **0 - **

   Water surface elevation at a given time. (ft or m)

   Variable Descriptions for the 

   WSURF.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   WSURF.DAT File

   1.  The WSURF.DAT file is used as a calibration tool.  It is set up
   with a known 

   peak water surface elevation.  When the model completes, a comparison
   file is 

   written.  It compares the high water mark to the max water surface
   elevation at 

   the corresponding node.  The engine will read this file if it is
   present.  There is 

   no need to turn on a switch.

   2.  The GDS does not build this file. It is created by the user in a
   text editor pro-

   gram.

.. container::
   :name: page179-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317800178.png
   169

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  WSTIME.DAT 

   WATER SURFACE ELEVATION COMPARISON

   WSTIME.DAT File Variables

   10 

   Line 1: 

   **NWSGRIDS**

   4025  200.25    12.5 

   Line 2: 

   **IGRIDXSEC(M)   WSELEVTIME(M)   WSTIME(M)**

   WSTIME.DAT File Example

   10

     139   4793.00   25

    1521   4786.00   25

    4099   4775.00   25

    5713   4767.00   25

    7611   4760.00   25

    9183   4752.00   25

   10751   4745.00   25

   12442   4736.00   25

   14079   4730.00   25

   15977   4722.00   25

   18061   4711.00   25

.. container::
   :name: page180-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202317900179.png
   170

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRIDXSEC(M)

   **i**

   **1 - NNOD**

   Nodes that have a known water surface elevation.

   NWSGRIDS

   **i**

   **1 - NNOD**

   Number of rows in the table.

   WSELEVTIME

   **r**

   **0 - **

   Water surface elevation at a given time. (hours)

   WSTIME

   **r**

   **0 - **

   Time of known watersurface elevation. (hours)

   Variable Descriptions for the 

   WSTIME.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   WSTIME.DAT File

   1.  The WSTIME.DAT file is used as a calibration tool.  It is set up
   with a known 

   water surface elevation and peak discharge time.  When the model
   completes, 

   a comparison file is populated.  It compares the high water mark to the
   maxi-

   mum water surface elevation at the corresponding node for a given
   time.  The 

   FLO-2D model will read this file if it is present.  

   2.  The GDS does not build this file. It is created by the user in a
   text editor pro-

   gram.

.. container::
   :name: page181-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318000180.png
   171

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  TIMDEPCELL.DAT 

   ARRAY OF GRID ELEMENTS FOR TIME OUTPUT

   TIMDEPCELL.DAT File Variables

   1521 

   Line 1:  

   **IGRID(I)**

   TIMDEPCELL.DAT File Example

     1521

    4099

    5713

    7611

    9183

   10751

   12442

   14079

   15977

   18061

.. container::
   :name: page182-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318100181.png
   172

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRID(I)

   **i**

   **1 - NNOD**

   Nodes selected to generate the variable time output.

   Variable Descriptions for the 

   TIMDEPCELL.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   TIMDEPCELL.DAT File

   1.  A time series of specific grid cell hydraulics can be created by
   generating the 

   TIMDEPCELL.DAT file with a list of the grid cells. Change the
   ITIMTEP 

   to 5 in the CONT.DAT file. Run the model to generate the TIMDEPCELL.

   OUT file. This output file contains the temporal hydraulic results
   for each grid 

   cell specified in the TIMDEPCELL.DAT file.

   2.  The GDS does not build this file. It is created by the user in a
   text editor.

.. container::
   :name: page183-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318200182.png
   173

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  SHALLOWN_SPATIAL.DAT 

   | ARRAY OF GRID ELEMENTS FOR SPATIALLY 
   | VARIABLE SHALLOW N

   SHALLOWN_SPATIAL.DAT File Variables

   1521    0.100 

   Line 1:  

   **IGRID(I)  SHALLOWN(I)**

   SHALLOWN_SPATIAL.DAT File Example

     1521    0.200

    4099    0.150

    5713    0.220

    7611    0.250

    9183    0.190

.. container::
   :name: page184-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318300183.png
   174

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRID(I)

   **i**

   **1 - NNOD**

   Nodes selected to assign spatially variable shallow n.

   SHALLOWN(I)

   **r**

   **0.01 - 0.99**

   Spatially variable shallow n-value (see comment 1)

   Variable Descriptions for the 

   SHALLOWN_SPATIAL File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page185-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318400184.png
   175

   **D**

   **ata**

   ** I**

   **nPut**

   Instructional Comments for the 

   SHALLOWN_SPATIAL File

   1.  To improve the timing of the floodwave progression through the
   grid system, a 

   depth variable roughness can be assigned.  The basic equation for the
   grid ele-

   ment roughness n

   d

    as function of flow depth is:

   n

   d

    = n

   b

    \*1.5 \* e 

   -(0.4 depth/dmax)

   where:

   n

   b

    =  bankfull discharge roughness 

   depth = flow depth

   dmax = flow depth for drowning the roughness elements and vegetation 

   (hardwired 3 ft or 1 m)

   This equation prescribes that the variable depth floodplain roughness
   is equal 

   to the assigned flow roughness for complete submergence of all
   roughness ele-

   ments (assumed to be 3 ft or 1 m).  This equation is applied by the
   model as a 

   default and the user can turn ‘off’ the depth roughness adjustment
   coefficient 

   for all grid elements by assigning AMANN = -99.  This roughness
   adjustment 

   will slow the progression of the floodwave.  It is valid for flow
   depths ranging 

   from 0.5 ft (0.15 m) to 3 ft (1 m).   For example, at 1 ft (0.3 m),
   the computed 

   roughness will be about 1.31 times the assigned roughness for a flow depth 

   of 3 ft. Assigning a ROUGHADJ value may reduce unexpected high
   Froude 

   | numbers.  
   | The following rules apply:

   | If the 
   | 0.0 < flow depth < 0.2 ft (0.06 m) 

   n = SHALLOWN value

   | 0.2 ft (0.06 m) < flow depth < 0.5 ft (0.15 m)  n = SHALLOWN/2.
   | 0.5 ft (0.15 m) < flow depth < 3 ft (1 m) 

   n = n

   b

    \*1.5 \* e

   -(0.4 depth/dmax)

   3 ft (1 m) < flow depth 

   n = n-value in  

    MANNINGS_N.DAT

.. container::
   :name: page186-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318500185.png
   176

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  GUTTER.DAT 

   FLOODPLAIN STREET ELEMENT GUTTER DATA

   GUTTER.DAT File Variables

   2  0.67   0.020 

   Line 1:    

   **STRWIDTH  CURBHEIGHT   STREET_n-VALUE**

   G   4525   25.0   0.67   0.025   8  Line 2: 

   **GUTTERCHAR   IGRID(I)   WIDSTR(I)     **

   ** **

   ** **

   ** **

   ** **

   ** **

   ** **

   **CURBHT(I)   XNSTR(I)   ICURBDIR(J=1-8)**

        I = number of grid elements with gutters

        J 

   = 

   curbside 

   flow 

   direction

   Notes:

   Repeat line 2 for each assigned gutter element.

   GUTTER.DAT File Example

   20.0   0.67   0.020   

   20   20.   0.67      0.025      1

   27   20.   0.67      0.030      1

   28   20.   0.67      0.025      1

   29   20.   0.67      0.020      1

   30   20.   0.67      0.020      1

   50   10.   0.67      0.025      5

.. container::
   :name: page187-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318600186.png
   177

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   CURBHEIGHT

   **r**

   **0 – 1**

   Global  assignment of the  curb height to all the gutter ele-

   ments (ft or m).  See comment 6.

   CURBHT(K)

   **r**

   **0 – 1**

   Individual gutter element curb height that supersedes 

   CURBHEIGHT (ft or m). 

   GUTTERCHAR

   **c**

   **G**

   Character line identifier for the gutter new line data.Vari-

   able is case sensitive and it must be upper case.

   ICURBDIR

   **i**

   **1 - 8**

   The side of the gutter element that the curb is located.  This 

   is one of the eight flow directions (see comment 2).  

   IGRID(I)

   **i**

   **1 - NNOD**

   Floodplain grid element number (see comment 1).

   STRWIDTH

   **r**

   **0 – 100**

   Global assignment of the street width to all gutter elements 

   (ft or m). 

   STREET_n-VALUE

   **r**

   **0.01 - 0.5**

   Global assignment of the street n-value to all gutter ele-

   ments.  See comment 4.

   WIDSTR(K)

   **r**

   **0 – 100**

   Street width for individual gutter elements. WIDSTR su-

   percedes STRWIDTH (ft or m).  See comment 3.

   XNSTR(K)

   **r**

   **0.01 - 0.5**

   Street n-values for individual gutter elements. Supersedes 

   STREET_n-value.

   Variable Descriptions for the 

   GUTTER File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page188-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318700187.png
   178

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   GUTTER File

   1.  The gutter elements are street elements defined by the floodplain (not street 

   component) where the flow in the street will be based on the gutter
   height and a 

   hard coded 2% cross slope in the street (triangular flow
   area).  This concentrates 

   the flow against the gutter and results in deeper flow depth and
   higher velocities 

   for floodwave movement.  The discharge in the gutter flow area
   defined by the 

   GUTTER.DAT file parameters is routed between gutter elements.  This
   gutter 

   routing algorithm is not the storm drain curb height option that only
   increases 

   the head on the storm drain inlet. For the curb height option, the
   flow is still 

   routed as a rectangular flow overland flow between street grid
   elements.

    ·

   The gutter is assign to one of the 8 sides of the gutter element.
   The 

   following rules govern the flow exchange of gutter street element
   with 

   the other elements when the flow depth in the gutter element exceeds 

   the tolerance value (TOL):

    ·

   The flow is exchanged with a contiguous gutter element based on the 

   flow depth against the curb.  

    ·

   The flow is shared with a street element without a gutter based on
   the 

   average depth between the two contiguous elements.  

    ·

   The flow is shared with a contiguous floodplain element that is not
   a 

   street and is not a curb flow direction based on the average flow
   depth 

   between the two contiguous elements.

    ·

   If the flow direction is the curb direction or one of the two
   diagonal 

   directions associated with the curb direction, the flow is first ex-

   changed to the sidewalk area within the gutter element when the flow 

   depth exceeds the curb height.  This exchange occurs in either direc-

   tion from the street to the sidewalk or from the sidewalk to the
   street.  

   After the internal flow exchange within the gutter element is com-

   plete the overland flow between the sidewalk area and the contiguous 

   floodplain element in the curb direction is exchanged based on the 

   average flow depth between the two grid elements.

   2.  If the street width (WIDSTR) exceeds the grid element width, then
   the street 

   width is limited to 0.90 times the grid element width to allow for the sidewalk 

   surface area.

.. container::
   :name: page189-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318800188.png
   179

   **D**

   **ata**

   ** I**

   **nPut**

   3.  The flow exchange between the gutter street elements is based on
   the Dept. 

   of Transportation gutter flow modification to account for the larger
   hydraulic 

   radius.  This essentially increases the steady uniform n-value for
   open prismatic 

   flow by about 5.3 times.  

   4.  The spatially variable or individual element assigned street
   width, curb height 

   and n-value supersede the global values.  

.. container::
   :name: page190-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202318900189.png
   180

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  BUILDING_COLLAPSE.DAT 

   BUILDING COLLAPSE PARAMETERS

   BUILDING_COLLAPSE.DAT File Variables

   0 

   Line 2:  

   **IARFSMASHGLOBAL**

   4025  1     

   Line 2:  

   **IG(M)  IARFSMASH(M)**

   **    **

   M = number of grid elements to be considered for collapse

       IG 

   = 

   grid 

   element

   BUILDING_COLLAPSE.DAT File Example

   0      

   4563   2

   6756   1

   23145  1

   23146  2

   23147  3

   25331  4

   26345  1

   …

.. container::
   :name: page191-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319000190.png
   181

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IG(M)

   **i**

   **1 - NNOD**

   Individual grid elements with building that are to be as-

   signed a vulnerability curve for potential collapse.

   IARFSMASHGLOBAL

   **i**

   **1 - 4**

   | Building global vulnerability curve (see Comment 1).
   | 1 = Poor

   2 = Moderate

   3 = Good

   4 = Clausen and Clark

   IARFSMASH

   **i**

   **1 - 4**

   | Individual global vulnerability curve (see Comment 1).
   | 1 = Poor

   2 = Moderate

   3 = Good

   4 = Clausen and Clark

   Variable Descriptions for the 

   BUILDING_COLLAPSE.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   BUILDING_COLLAPSE.DAT File

   1.  During a flood event or a mud/debris flow, it is possible that a
   building could 

   collapse and be removed.  To predict the collapse of a building
   during flood-

   ing vulnerability curves are applied.  The three vulnerability curves are poor or 

   highly susceptible to flood collapse (mobile homes), moderate for
   buildings 

   with foundations, and good for building with more substantial
   construction.  

   A fourth curve developed by Clausen and Clark in 1990 is also
   available.  Find 

   more information in the FLO-2D Pro Reference manual.

   2.  The building collapse routine can also be activated by
   assigning a negative value 

   to a completely blocked ARF value or to partially blocked ARF values
   in the 

   ARF.DAT file.

.. container::
   :name: page192-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319100191.png
   182

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  OUTRC.DAT 

   SURFACE WATER RATING TABLES

   OUTRC.DAT File Variables

   N   13562 

   Line 1: 

   **IVOLSTOCHAR   NNODSTOVO**

   P   1.25   20.5 

   Line 2: 

   **IVOLSTOCHAR   DEPTHRT(I,K)   VOLRT(I,K)**

   **    **

   I = Depths 

    

    

    

    

   K = Volume corresponding to I depths.

   OUTRC.DAT File Example

   N    25146

   P  0.00     0.00   

   P  1.00   5.25  

   P  2.00   25.2

   P  3.00   100.32

   P  4.00   180.5

   ...

   P 20.5    736.00 

   N  14079 

   P 0.00     0.00

   P 1.00     2.50

   ...

.. container::
   :name: page193-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319200192.png
   183

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRIDXSEC(M)

   **c**

   **N or P**

   N = Node line

   P = storage rating table pairs.

   NODDSTOVO

   **i**

   **1 - NNOD**

   Grid element with a storage volume rating table (see com-

   ment 1).

   DEPTHRT

   **r**

   **0 - **

   Increment flow depth for the volumetric rating table above 

   the lowest elevation in the grid element topographic data 

   base.

   VOLRT

   **r**

   **0 - **

   Volume for each incremental depth.

   Variable Descriptions for the 

   OUTRC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   OUTRC.DAT File

   1.  Grid element storage volume rating tables defines
   variable volume as a func-

   tion of flow depth instead of a cell having one uniform elevation.
    This enables 

   the digital terrain data base within to be represented.  The rating
   table depth is 

   based on the
   lowest elevation within the grid element.  At least 25 DTM points 

   are required to enable the rating table to be established.  The
   storage volume 

   rating table is generated by the GDS.  The FLO-2D model will read
   this file if 

   it is present.

.. container::
   :name: page194-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319300193.png
   184

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  CHAN_INTERIOR_NODES.DAT 

   ARRAY OF INTERIOR GRID ELEMENTS

   CHAN_INTERIOR_NODES.DAT File Variables

   1521 

   Line 1:  

   **IGRID(I)**

   CHAN_INTERIOR_NODES.DAT File Example

     1521

    4099

    5713

    7611

    9183

   10751

   12442

   14079

   15977

   18061

.. container::
   :name: page195-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319400194.png
   185

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IGRID(I)

   **i**

   **1 - NNOD**

   Nodes that represent the interior of the channel.  (see Com-

   ment 1)

   Variable Descriptions for the 

   CHAN_INTERIOR_NODES.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   CHAN_INTERIOR_NODES.DAT File

   1.  This list of cells are the cells that do not exchange flow with
   the grid system.  

   they are removed from the overland routing because they are overlaid
   by the 

   1-D channel.  The list is initially compiled when FLO-2D engine
   performs 

   system checks.  The data is written to the CHAN_INTERIOR_NODES.OUT 

   file but can be manually adjusted in a text editor so that any cell
   that is missing 

   from the list can be added.  Use NotePad,
   NotePad++, or UltraEdit to make 

   adjustments.

.. container::
   :name: page196-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319500195.png
   186

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  BRIDGE_XSEC.DAT 

   BRIDGE CROSS SECTIONS

   BRIDGE_XSEC.DAT File Variables

   X   6657 

   Line 1:    

   **XSECCHAR = 'X'   IBRIDGE(I)**

   0.00   957.08   954.11 

    

   Line 2: 

   **XUP(I,J)   YUP(I,J)   YB(I,J)    **

   BRIDGE_XSEC.DAT File Example

   X 6657

   0.00   957.08   954.11

   4.00   957.15   953.48

   10.01   957.16   952.04

   16.02   955.69   950.18

   20.02   954.13   949.50

   22.02   953.38   944.24

   28.03   950.24   942.80

   78.09   944.95   937.26

   88.10   949.16   937.69

   94.11   951.27   939.68

   98.11   953.63   940.94

   102.12   955.43   942.52

   110.12   956.13   945.75

   112.13   955.87   945.87

   118.13   955.86   948.39

   120.14   955.90   954.00

.. container::
   :name: page197-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319600196.png
   187

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   IBRIDGE(i)

   **I**

   **1 - NNOD**

   Nodes that represent upstream element of the hydraulic 

   structure.  (see Comment 1)

   XSECCHAR

   **c**

   **X**

   A character to define a new bridge cross section dataset.

   XUP(i,j)

   **r**

   **0 - **

   Station left bank to right bank in ft or m.

   YUP(i,j)

   **r**

   **0 - **

   Upstream cross section elevation ft or m.

   YB(i,j)

   **r**

   **0 - **

   Downstream cross section elevation ft or m.

   Variable Descriptions for the 

   BRIDGE_XSEC.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   BRIDGE_XSEC.DAT File

   | 1.  This is the grid element listed in HYSTRUC.DAT as an inflow
     node.
   | 2.  See the bridge manual to know where to measure the cross
     section data. 

.. container::
   :name: page198-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319700197.png
   188

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  TAILINGS.DAT

   TAILINGS DEPTH DATA

   TAILINGS.DAT File Variables

   7659   10 

   Line 1: 

   **JGRIDUMMY   TAILINGSDEPTH(I) **

   ** **

   *I = grid element that has a tailings depth assigned.*

   Notes:

   Line 1:  Repeat this line for each grid element has a tailings depth
   assigned.

   TAILINGS.DAT File Example

    7650  10

   7651   10

   7652   10

     ...

.. container::
   :name: page199-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319800198.png
   189

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   JGRIDUMMY

   **i**

   **1 - NNOD**

   A grid element for which a tailings depth is assigned.

   TAILINGSDEPTH

   **r**

   **0.01 - **

   Tailings depth for a specific grid element (ft or m).

   Variable Descriptions for the 

   TAILINGS.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   TAILINGS.DAT File

   1.  If tailings dam material is uniform, a single tailings dam depth
   or elevation is 

   written to INFLOW.DAT file in line R.  TAILINGSELEV is the 4th param-

   eter of R line INFLOW.DAT file.

   2.  Tailings.dat file is needed for a tailings dam material with no
   uniform depth. 

   One or multiple cells in the tailings dam storage area might have a
   different 

   tailings dam depth than uniform TAILINGSELEV read from INFLOW.DAT 

   file. 

.. container::
   :name: page200-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202319900199.png
   190

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  TAILINGS_CV.DAT

   TAILINGS  DATA

   TAILINGS_CV.DAT File Variables

   7659   995  0.50 

   Line 1: 

   **JGRIDUMMY   TAILINGSDEPTH(I)   XXXX**

   ** **

   *I = grid element that has a tailings depth assigned.*

   Notes:

   Line 1:  Repeat this line for each grid element has a tailings depth
   assigned.

   TAILINGS_CV.DAT File Example

    7650  10

   7651   10

   7652   10

     ...

.. container::
   :name: page201-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320000200.png
   191

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   JGRIDUMMY

   **i**

   **1 - NNOD**

   A grid element for which a tailings depth is assigned.

   TAILINGSDEPTH

   **r**

   **0.01 - **

   Tailings depth for a specific grid element (ft or m).

   CVTFP(J)

   **i**

   **0 - 0.65**

   Concentration of tailing material for a single grid element.

   Variable Descriptions for the 

   TAILINGS_CV.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   TAILINGS_CV.DAT File

   1.  TAILINGS_CV.DAT data file assigns flow depths and sediment
   concentra-

   tions to each FLO-2D grid cell within the tailing dam.  For the first
   computa-

   tion timestep, flow depths and tailings surface elevations are used
   to compute a 

   surface slope to initiate motion.  The tailings dam material begins
   to move as a 

   mudflow.  There is no water storage, so there is no two phase flow.  

   2.  The flow depth volume (in the TAILINGS_CV.DAT file) is summed up
   and 

   reported as INFLOW volume in the SUMMARY.OUT file. This can be com-

   pared to the known or estimated tailings dam volume.  It is
   contingent upon 

   the user to either assess the depth of the tailings by grid element
   or knowing 

   the tailings surface elevation and pre-dam topography to compute the
   tailings 

   depth as the difference between two surfaces in CAD or GIS. 

   3.  If storage volume vs stage data is available, this would allow
   the user to check 

   the volume associated with the depths in the TAILINGS_CV.DAT file.
    The 

   user should not use the project volume vs stage data because this
   makes all the 

   volume available at the toe of the dam and there is no routing of the
   mud-

   flow through the dam breach. Only a portion of the tailings will
   actually flow 

   through the breach.

.. container::
   :name: page202-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320100201.png
   192

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   FILE:  TAILINGS_STACK_DEPTH.DAT

   TAILINGS DEPTH DATA

   TAILINGS_STACK_DEPTH.DAT File Variables

   7659   10   5 

   Line 1: 

   **JGRIDUMMY   FPD(I)  FPD_MUD(I) **

   ** **

   *I = grid element that has a tailings depth assigned.*

   Notes:

   If IMUD = 0 or 1     FPD is water or tailings depth.

   If IMUD = 2     FPD is water depth and FPD_MUD is the tailings depth

   TAILINGS_STACK_DEPTH.DAT File Example

    7650  10   5

   7651   10    5

   7652   10   5

     ...

.. container::
   :name: page203-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320200202.png
   193

   **D**

   **ata**

   ** I**

   **nPut**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   JGRIDUMMY

   **i**

   **1 - NNOD**

   A grid element for which a tailings depth is assigned.

   **FPD(I)**

   **r**

   **0.01 - **

   Water or mud depth for a specific grid element (ft or m).

   **FPD_MUD(I)**

   **r**

   **0.01 - **

   Tailings depth for a specific grid element (ft or m).

   Variable Descriptions for the 

   TAILINGS_STACK_DEPTH.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

.. container::
   :name: page204-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320300203.png
   194

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   Instructional Comments for the 

   TAILINGS_STACK_DEPTH.DAT File

   1.  TAILINGS_STACK_DEPTH.DAT is used to simulate a static or seismic
   tail-

   ings dam failure where the tailings constitute the dam. This file
    will contain 

   the tailing grid elements, water depth on the surface of the tailings
   and tailings 

   depth.  If the tailings stack failure is only mudflow and not 2 phase
   flow, then 

   only the tailings depth will be listed in this file. This file can be imported to 

   QGIS or opened in an ASCII file program editor (WordPad) to revise
   or con-

   tour the tailings depths and this will now constitute the FLO-2D
   simulation 

   source volume.

   2.  The TAILINGS_STACK_DEPTH.DAT file can be created using a prepara-

   tion FLO-2D model simulation in the following sequence:

   i.  Create the tailings dam using the LEVEE.DAT to encompass the
   tailings 

   reservoir area.  The grid elevation is pre-dam construction.

   ii.  Assign the tailings stack depth using the R-line of INFLOW.DAT
   file to 

   assign the tailings elevation.

   iii.  Set the simulation time SIMUL = 0.001 hr. and the output
   interval 

   TOUT = 0.001 hr in CONT.DAT.

   iv.  Run the FLO-2D model to generate the TAILINGS_STACK_DEPTH.

   DAT file.

   v.  Rename the INFLOW.DAT to INFLOW1.DAT or some other name.

   vi.  Either turn the LEVEE switch off in CONT.DAT or select those
   levee 

   crest elements for removal using QGIS.

   vii.  Assign SIMUL = simulation model time with a representative TOUT
   = 

   0.1 or some other value. 

   viii. viii. Run the FLO-2D model again and the assigned stack depths will 

   begin to move at the initiation of the model.

   3.  A second option is to assign the TAILINGS_STACK_DEPTH.DAT in
   QGIS 

   and then follow steps vi thru viii above to initiate the stack
   failure.

.. container::
   :name: page205-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320400204.png
   195

   **D**

   **ata**

   ** I**

   **nPut**

   FILE:  LID_VOLUME.DAT

   LOW IMPACT DEVELOPMENT DATA FILE

   LID_VOLUME.DAT File Variables

   7659   10 

   Line 1: 

   **JGRIDUMMY   LIDVOLUMEMAX(J) **

   ** **

   *J = grid element that has a LID volume assigned.*

   Notes:

   Line 1:  Repeat this line for each grid element has an LID volume.

   LID_VOLUME.DAT File Example

    7650  10

   7651   10

   7652   10

     ...

.. container::
   :name: page206-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320500205.png
   196

   **c**

   **haPter**

   ** 4**

   **I**

   **nPut**

   ** f**

   **Iles**

   VARIABLE

   FMT

   RANGE

   DESCRIPTION

   JGRIDUMMY

   **i**

   **1 - NNOD**

   A grid element for which a tailings depth is assigned.

   LIDVOLUMEMAX

   **r**

   **0.01 - **

   A volume assinged to a grid element that acts as a sink. (ft

   2

    or m

   2

   ).

   Variable Descriptions for the 

   LID_VOLUME.DAT File

   (s) Switch   (i) = Integer variable   (r) = Real variable (c) =
   Character

   Instructional Comments for the 

   LID_VOLUME.DAT File

   1.  Assign a storage volume to a grid element(s) that must be filled
   before sharing 

   with other grid elements as overland flow.  The storage can represent any type 

   of LID facility.  For example, a group of grid elements can represent
   a rooftop 

   or building area. The assigned LID volume must be filled before the
   cell can 

   exchange with ground simulating a cistern that collects rainfall
   runoff.  Another 

   example is pervious pavers in a driveway or parking lot.

   2.  The LID volume may be a preferred method over assigning the
   TOLSPATIAL.

   DAT data to represent a LID storage volume because the flow depth
   will be not 

   added to the grid element when considering rainfall runoff
   distribution. 

.. container::
   :name: page207-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320600206.png
   CHAPTER 5

   Output Files and Options

   197

   Output Files

   **5.1 **

   **b**

   **asIc**

   ** G**

   **uIDelInes**

   ** **

   **for**

   ** u**

   **sInG**

   ** o**

   **utPut**

   ** f**

   **Iles**

   During the flood simulation, the user has two choices for viewing the
   model flood 

   progression: 

   | 1.  An output text screen
   | 2.  A graphical representation of the flood simulation.  

   The screen option is selected with the LGPLOT variable in the
   CONT.DAT file.  

   The text screen scrolls a list of the simulation time, minimum
   timestep and the vol-

   ume conservation data.  This screen enables the user to view the
   simulation runtime 

   speed and the volume conservation.  The second screen option is a
   color graphics 

   display of the grid element flow depth (area of inundation) along
   with the inflow hy-

   drograph.  After the flood simulation is complete, the hydraulic
   results are presented 

   | in output files that contain hydrographs, maximum flow depths and
     velocities. 
   | The conservation of flood volume (inflow equals outflow plus
     storage) should be 

   reviewed for each simulation. A summary of the inflow volume, final
   volumes left 

   on the floodplain (storage) and outflow from the grid system is
   presented in the 

   | SUMMARY.OUT file.
   | Output files are created with both spatial and temporal formats.
      Output files that 

   are listed in the order of the output intervals are temporal output
   and output files 

   listed in the order of the grid elements is spatial output.  Output data include wa-

   ter surface elevation, flow depth, velocity, discharge, impact
   pressure, specific en-

   ergy, sediment concentration and other variables.  Overland flow
   hydraulics may be 

   viewed as individual grid elements or the grid elements can be
   grouped together to 

.. container::
   :name: page208-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320700207.png
   198

   Chapter 5

   Output Files

   produce floodplain cross sections.  Summary tables listing maximum
   velocity and 

   flow depths and their times of occurrence appear at the end of the
   BASE.OUT file.    

   Review the CONT.DAT file description in Chapter 4 for more
   information about 

   | specifying output file formats.
   | The user is cautioned about specifying the output in too much
     detail which can 

   result in extremely large output files.  The output time interval
   TOUT and NO-

   PRTFP options in the CONT.DAT file can be assigned to limit the size
   of the 

   output files.  When NOPRTFP is set to 0, all the floodplain output
   data is written 

   to the BASE.OUT file for each output interval.  Setting NOPRTFP = 2
   will turn off 

   all of the temporal floodplain hydraulic output data.

   The user does not have to specify any output file names.  It is
   important to note 

   that each time the model is run, it will write over the existing
   output files and the 

   previous output file data will be lost.  To save any output files in
   anticipation of 

   subsequent simulation, the user should create another subdirectory.

   Use NotePad

   ©

    , NotePad++

   © 

   or any other ASCII editor to view the output files. A 

   brief description of all the output files follows: 

   Hint: 

   Each time a model is run 

   from a specific project 

   folder, all of the \*.OUT 

   files are rewritten. To 

   save the model results for 

   a simulation either make 

   copies of the output files 

   or copy the data files to a 

   new  project folder and 

   run the next simulation 

   from it.

   Table 5.1.  List of General \*.OUT Files and Unit Numbers

   File No.

   File Name

   File No.

   File Name

   2

   BASE.OUT

   19

   TIME.OUT

   11

   SUMMARY.OUT

   55

   SURFAREA.OUT

   Table 5.2.  List of 2-D Overland Output

   File No.

   File Name

   File No.

   File Name

   Depth

   Velocity

   20

   DEPTH�OUT

   118

   VELTIMEFP.OUT

   27

   DEPTHTOL�OUT

   641

   VELRESMAX.OUT

   28

   DEPTHDUR�OUT

   81

   FINALVEL.OUT

   62

   FINALDEP�OUT

   83

   FINALDIR.OUT

.. container::
   :name: page209-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320800208.png
   199

   Data Input

   Output Files

   Table 5.2.  List of 2-D Overland Output

   60

   DEPFP�OUT

   63

   VELDIREC.OUT

   General

   64

   VELFP.OUT

   45

   FLOODWAY�OUT

   1401

   VEL_X_DEPTH.OUT

   101

   IMPACT�OUT

   Discharge

   102

   STATICPRESS�OUT

   105

   MAXQHYD.OUT

   289

   INFIL_DEPTH�OUT

   106

   MAXQBYDIR.OUT

   82

   OUTNQ.OUT

   107

   MAXQRESOLVED.OUT

   92

   INTERGWS.OUT

   124

   MAXWSELEV.OUT

   67

   INFILHY.OUT

   Time

   104

   SPECENERGY.OUT

   21

   TIMDEP�OUT

   111

   FPINFILTRATION.

   OUT

   78

   TIMDEP_NC4�OUT

   Review

   181

   WSTIME�OUT

   1131

   EVACUATEDFP.OUT

   190

   TIMETWOFT�OUT

   1597

   FLOODPLAIN_CON-

   VERGENCE.OUT

   191

   TIMETOPEAK.OUT

   1598

   DEPRESSED_ELE-

   MENTS.OUT

   192

   TIMEONEFT.OUT

   22

   ROUGH.OUT

   193

   FLOODWAVETIME.OUT

   65

   SUPER.OUT

   528

   DEPTHDUR2.OUT

   288

   BUILDING_COL-

   LAPSE.OUT

   1921

   TIME_TO_ABOVE_BASE-

   FLOW.OUT

.. container::
   :name: page210-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202320900209.png
   200

   Chapter 5

   Output Files

   Table 5.4.  List of Hydraulic Structures Output

   File No.

   File Name

   70

   HYDROSTRUCT.OUT

   669

   HYDRAULIC STRUCTURE_RUNTIME WARNINGS.OUT

   910

   BRIDGE_FLOW_GEOMETRY.OUT

   912

   BRIDGE_DISCHARGE.OUT

   914

   BRIDGE_COEFFICIENTS.OUT

   671

   HYDRAULIC STRUCTURE SUBFACTORS.OUT

   Table 5.3.  List of 1-D Channel Output

   File No.

   File Name

   File No.

   File Name

   14

   CHANMAX.OUT

   94

   XSEC.OUT

   24

   VELOC.OUT

   103

   CONFLUENCE.OUT

   61

   DEPCH.OUT

   140

   CHANSEDSIZE.OUT

   66

   CHVOLUME.OUT

   113

   EVACUATEDCHAN.OUT

   74

   CHNBEDEL.OUT

   117

   VELTIMEC.OUT

   80

   HYCHAN.OUT

   261

   DEPCHFINAL.OUT

   87

   OVERBANK.OUT

   262

   VELCHFINAL.OUT

   90

   CHANSTABILITY.OUT

   263

   CHAN_INTERIOR\_

   NODES.OUT

   91

   XSECAREA.OUT

   345

   CHANLOSSES.OUT

   93

   CHANWS.OUT

   1596

   CHANNEL_CONVER-

   GENCE.OUT

.. container::
   :name: page211-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321000210.png
   201

   Data Input

   Output Files

   Table 5.5.  List of Levee and Breach Output

   File No.

   File Name

   File No.

   File Name

   59

   LEVEE.OUT

   1594 LOW_LEVEE_CREST_EL-

   EVATIONS.OUT

   160

   LEVOVERTOP.OUT

   1601 LEVOVERTOPMAX.OUT

   161

   LEVEEDEFIC.OUT

   1779

   CVFPMAX.OUT

   255

   BREACH.OUT

   GE#

   GE#_LEVFAIL.OUT

   1132

   DAMBREACH_VOLUME.

   OUT

   699

   PRESCRIBED_BREACH 

   Q.OUT

   Table 5.6.  List of Storm Drain Output

   File No.

   File Name

   File No.

   File Name

   1560

   SWMMQIN.OUT

   1574

   MANHOLEPOP.OUT

   1565

   SWMMOUTFIN.OUT

   SWMM.RPT

   1563

   FPRIMELEV.OUT

   SWMM.OUT

   1570

   SD MANHOLEPOPUP.

   OUT

   Table 5.7.  List of Multiple Channel Output

   File No.

   File Name

   File No.

   File Name

   25

   MULTCHN.OUT

   205

   MULTSTEEP.OUT

.. container::
   :name: page212-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321100211.png
   202

   Chapter 5

   Output Files

   Table 5.8.  List of Sediment Transport and Mudflow 

   Output

   File No.

   File Name

   File No.

   File Name

   17

   SEDFP.OUT

   88

   SEDTRAN.OUT

   18

   SEDCHAN.OUT

   139

   FPSEDSIZE.OUT

   77

   SEDCONSERV.OUT

   Table 5.9.  List of Two Phase Flow Output 

   File 

   No.

   File Name

   File No.

   File Name

   241

   VELOC_MUD.OUT

   831

   FINALDIR_MUD�OUT

   242

   CVTMAX.OUT

   811

   FINALVEL_MUD�OUT

   243

   CVTMAX_MUD.OUT 

   1771 FP_BED_CHANGE_MUD.OUT

   245

   CVTFINAL_MUD.OUT

   1773

   CVFPMAX.OUT                      

   361 DEPCHFINAL_MUD.OUT 1775

   FINALCVFP_MUD.OUT

   602

   DEPFPMAX_MUD.OUT

   1779

   CVFPMAX_MUD.OUT

   603

   DEPTHMAX_2PHASE\_

   COMBINED.OUT

   2070 2 PHASE SEDIMENT VOLUME 

   CONSERVATION.OUT

   611

   DEPCH_MUD.OUT

   2080

   FPWSEL_MUD.OUT

   622 FINALDEP_COMBO.OUT 6411

   VELFP_MUD.OUT

   621

   FINALDEP_MUD.OUT

   6412

   VELRESMAX_MUD.OUT

   631

   VELDIREC_MUD.OUT

.. container::
   :name: page213-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321200212.png
   203

   Data Input

   Output Files

   Table 5.10.  List of MODFLOW Output

   File No.

   File Name

   1237

   MODFLOW.OUT

   1238

   MODFLOW FP INFILTRATION VOLUMES.OUT

   1239

   MODFLOW FP INFILTRATION TOTALS.OUT

   1241

   MODFLOW CHANNEL INFILTRATION TOTALS.OUT

   1242

   FLO-2D MODFLOW FP RETURN EXCHANGE.OUT

   1243

   FLO-2D MODFLOW CH RETURN EXCHANGE.OUT

   1244

   FPMODFLOWELEV.OUT

   1245

   CHMODFLOWELEV.OUT

   12466

   FLO-2D MODFLOW INFILTRATION.OUT

   12477

   MODFLOW FLO-2D RECHARGE.OUT

   Table 5.11.  List of \*.RHG Files and Unit Numbers

   File 

   No.

   File Name

   File No.

   File Name

   108

   FPLAIN.RGH

   109

   CHAN.RGH

   110

   STREET.RGH

   208

   MULT.RGH

   309

   MANNINGS_N.RGH

   1572

   FPLAIN_SDELEV.RGH

   1573

   TOPO_SDELEV.RGH

.. container::
   :name: page214-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321300213.png
   204

   Chapter 5

   Output Files

   Table 5.12.  List of Batch Files and Unit Numbers

   File 

   No.

   File Name

   File 

   No.

   File Name

   195

   DEPFP_ANTERIOR.OUT

   213

   DIFF_VELOC.OUT

   196

   DIFF_DEPFP.OUT

   214

   VELTIMEFP_ANTERIOR.OUT

   197

   FINALDEP_ANTERIOR.OUT

   215

   DIFF_VELTIMEFP.OUT

   198

   DIFF_FINALDEP.OUT

   216

   VELTIMEC_ANTERIOR.OUT

   199

   ENDRUNBATCHTEST.OUT

   217

   DIFF_VELTIMEC.OUT

   206

   VELFP_ANTERIOR.OUT

   218

   DEPCH_ANTERIOR.OUT

   207

   DIFF_VELFP.OUT

   219

   DIFF_DEPCH.OUT

   209

   DEPTH_ANTERIOR.OUT

   220

   DEPCHFINAL_ANTERIOR.OUT

   210

   DIFF_DEPTH.OUT

   221

   DIFF_DEPCHFINAL.OUT

   212

   VELOC_ANTERIOR.OUT

   Table 5.13.  List of \*.TMP Files and Unit Numbers

   File 

   No.

   File Name

   File No.

   File Name

   8

   CHMAX2.TMP

   112

   OUTNQMAX.TMP

   12

   OUTNQ.TMP

   122

   HYSTREET.TMP

   13

   HYCHAN.TMP

   159

   LEVOVERTOP.TMP

   15

   HYCROSS.TMP

   254

   BREACH.TMP

   16

   CROSSQ.TMP

   1561

   SWMMQIN.TMP

   71

   HYDROSTRUCT.TMP

   1566

   SWMMOUTFIN.TMP

   76

   OUTNQ2.TMP

.. container::
   :name: page215-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321400214.png
   205

   Data Input

   Output Files

   *2 PHASE SEDIMENT VOLUME CONSERVATION.OUT  *

   Summary of the final disposition of the sediment volume.

   *BASE.OUT  *

   BASE.OUT is an all-inclusive output file. At the beginning of the
   file, the 

   inflow hydrographs are printed, then the time dependent output data
   fol-

   | lows.  
   | For each specified time output interval, the flow depth, velocity, water sur-

   face elevation and discharge for either the channel or the floodplain
   grid 

   | elements can be written.  
   | The outflow from the boundary grid elements is listed at the end of
     the 

   | time interval.  
   | After the final time output interval, a summary of all the grid
     elements 

   maximum depths, water surface elevations, velocities and the time of
   occur-

   | rence of the maximum values is printed.  
   | Finally, a summary table of the inflow, outflow and storage volumes
     at the 

   end of the file allows the user to review the conservation of mass
   and the 

   | ultimate disposition of all the water and sediment.  
   | For convenience, this conservation table is also written to a
     separate output 

   | file named SUMMARY.OUT that is more complete.  
   | There is so much output data in the BASE.OUT file that the user is
     en-

   couraged to avoid generating this file.  All of the text output in
   this file is 

   provided in individual ASCII xyz output files for plotting purposes
   and 

   the user will probably have little interest in the BASE.OUT format of
   the 

   | floodplain hydraulics for the individual grid elements. 
   | This output file can become large and it takes too long to write to
     it for 

   models with 500,000 grid elements or more.  Set NOPRTFP = 2 and it 

   will not be created.

    ·

   If NOPRTFP = 0, all the BASE.OUT floodplain flow data is 

   reported.

    ·

   If NOPRTFP = 1, the BASE.OUT floodplain outflow data is 

   not reported.

    ·

   If NOPRTFP = 2, the entire file is not created.

    ·

   If NOPRTFP = 3, only floodplain outflow data is reported to the 

   BASE.OUT file.

.. container::
   :name: page216-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321500215.png
   206

   Chapter 5

   Output Files

   *BINARY FILES*

   The following binary backup files are generated when IBACKUP = 1.
    These 

   files can be used to restart model after termination (either
   interrupted simu-

   lation or end of the simulation).  

    ·

   CHANBINARY.OUT

    ·

   CROSSBINARY.OUT

    ·

   FPLAINBINARY.OUT

    ·

   HYSTRUCBINARY.OUT

    ·

   SEDBINARY.OUT

    ·

   STREETBINARY.OUT

    ·

   VOLUMEBINARY.OUT

    ·

   XSECSEDBINARY.OUT

   *BATCH COMPARISON FILES*

   Running the batch processor will execute many projects in series and
   per-

   form automatic comparisons of the output data from previous runs.
    The 

   following files represent the comparison dataset.

    ·

   DEPFP_ANTERIOR.OUT

    ·

   DIFF_DEPFP.OUT

    ·

   FINALDEP_ANTERIOR.OUT

    ·

   DIFF_FINALDEP.OUT

    ·

   ENDRUNBATCHTEST.OUT

    ·

   VELFP_ANTERIOR.OUT

    ·

   DIFF_VELFP.OUT

    ·

   DEPTH_ANTERIOR.OUT

    ·

   DIFF_DEPTH.OUT

    ·

   VELOC_ANTERIOR.OUT

    ·

   DIFF_VELOC.OUT

    ·

   VELTIMEFP_ANTERIOR.OUT

    ·

   DIFF_VELTIMEFP.OUT

    ·

   VELTIMEC_ANTERIOR.OUT

    ·

   DIFF_VELTIMEC.OUT

    ·

   DEPCH_ANTERIOR.OUT

    ·

   DIFF_DEPCH.OUT

    ·

   DEPCHFINAL_ANTERIOR.OUT

    ·

   DIFF_DEPCHFINAL.OUT

    ·

   *BREACH.OUT*

   This file is generated when the erosion breach routine is activated
   for dams 

   or levees.  The output is listed by grid element number singular and
   tabular 

   results.  The initial and peak discharge is reported for each grid
   element 

.. container::
   :name: page217-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321600216.png
   207

   Data Input

   Output Files

   and the time each occurred.  The tabular data is reported for the
   breach 

   discharge as follows:

    ·

   Time - simulation time output

    ·

   Direction - breach direction 1-8 grid element directions

    ·

   Breach Q - total discharge through the breach and the end of the 

   interval (cfs or cms)

    ·

   Sediment discharge - total sediment through the breach at the 

   end of the interval (cfs or cms)

    ·

   Sediment concentration - concentration of sediment in the 

   breach

    ·

   Bottom width - breach width at the bottom of the dam or levee 

   at the output interval (ft or m)

    ·

   Top width - breach width at the top of the dam or levee at the 

   output interval (ft or m)

    ·

   Breach elevation - elevation of the bottom of the breach at the 

   output interval (ft or m)

   *BRIDGE_COEFFICIENTS.OUT*

   *BRIDGE_COEFFICIENTS.OUT*

   This file has the various discharge coefficients that are selected or
   computed.

    ·

   Time 

    ·

   Inflow node

    ·

   COEFFREEB(JB)

    ·

   COEFFPRIME(JB)

    ·

   KFB(JB)

    ·

   KWWB(JB)

    ·

   KPHIB(JB)

    ·

   KYB(JB)

    ·

   KXB(JB)

    ·

   KJB(JB)

   *BRIDGE_DISCHARGE.OUT*

   *BRIDGE_DISCHARGE.OUT*

   Bridge component output file.

    ·

   Time 

    ·

   Inflow node

    ·

   Free surface Q (cfs or cms)

    ·

   Orifice flow Q (cfs or cms)

    ·

   Orifice and deck weir flow Q (cfs or cms)

   *BRIDGE_FLOW_GEOMETRY.OUT*

   *BRIDGE_FLOW_GEOMETRY.OUT*

   Bridge flow area, wetted perimeter, and top width of the bridge cross sec-

   tions.

    ·

   US flow area (ft

   2

    or m

   2

   )

.. container::
   :name: page218-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321700217.png
   208

   Chapter 5

   Output Files

    ·

   US wetted perimeter (ft or m)

    ·

   US topwidth (ft or m)

    ·

   BR flow area (ft

   2

    or m

   2

   )

    ·

   BR wetted perimeter (ft or m)

    ·

   BR topwidth (ft or m)

    ·

   DS flow area (ft

   2

    or m

   2

   )

    ·

   DS wetted perimeter (ft or m)

    ·

   DS topwidth (ft or m)

   *BUILDING_COLLAPSE.OUT*

   *BUILDING_COLLAPSE.OUT*

   This file lists the grid elements with full or
   partial ARF values that will be 

   reset to 0.0 during the model run to simulate the collapse and
   removal of 

   buildings.  This occurs because the flood depth and velocity exceed
   the 

   building collapse criteria.  The following tabular data is printed:

    ·

   Grid element

    ·

   Time

    ·

   Velocity - velocity at the time of collapse (fps or mps)

    ·

   Depth - depth at the time of collapse (ft or m)

    ·

   Minimum collapse depth based on the velocity (ft or m)

   *CHAN_INTERIOR_NODES.OUT *

   A list of all the grid elements between the channel bank elements
   represent-

   ing the interior of the 1-D channel are listed in
   this file.  These elements 

   should reflecting the channel maximum depth when plotting maximum 

   channel depths in FLO-2D MapCrafter.  The channel bank elements are 

   not included in this file.

   *CHANBANKEL.CHK *

   This file reports the difference between the channel bank elevation
   and the 

   grid element elevation for each assigned bank elements.  If the bank
   eleva-

   tion difference exceeds the specified criteria, the floodplain
   elevation will be 

   reset to channel bank elevation at runtime.  This assumes that the
   surveyed 

   bank elevation is more accurate than the interpolated floodplain
   elevation.  

   The bank elevation difference criteria is:

    ·

   Channel grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Bank elevation (ft or m)

    ·

   Floodplain elevation (ft or m)

    ·

   Difference (ft or m)

   Channel bank elevation is different from the floodplain elevation by
   1 ft 

   or more.

.. container::
   :name: page219-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321800218.png
   209

   Data Input

   Output Files

   If the slope associated with the bank elevation difference based on
   the grid 

   element side width is greater than 0.01 (1%)

   *CHANMAX.OUT *

   The maximum discharge and stage for each channel element and the cor-

   responding time of occurrence is written to this file.  This file is
   useful for 

   finding channel cross sections that might be surging.  If the timing if the 

   maximum values do not correspond with the peak discharge, the
   channel 

   element may be surging.  The following columns are written:

    ·

   Node

    ·

   Max Q - Maximum discharge for channel element (cfs or cms)

    ·

   Time - Time of Qmax

    ·

   Max Stage - Maximum stage for channel element (ft or m)

    ·

   Time - Time of max stage

   *CHANNEL.CHK*

   When the channel cross section width exceeds the grid element width,
   the 

   cross section needs to extend into 1 or more neighboring elements.
    When 

   the channel surface area is 0.95 times the floodplain surface area
   the chan-

   nel needs to extend into 1 or more neighboring elements.  This file
   lists the 

   | necessary extensions.
   | If a channel right bank is placed on an interior channel element,
     this file 

   | lists the bank that needs to be repositioned.
   | The file lists any channel / levee conflicts that may need to be
     fixed.
   | If the channel cross section is R, T or V  (non-natural cross
     sections)  and 

   the channel is extended to more than one grid element and the bank
   eleva-

   tions are not assigned in CHAN.DAT.  This file lists the difference
   between 

   the right and left channel bank elevations based on the floodplain
   elevations 

   in two different bank elements.

   *CHAN.RGH*

   CHAN.RGH is a duplicate file of the CHAN.DAT file with the updat-

   ed Manning’s n-value changes that were reported in the ROUGH.OUT 

   file.  The
   maximum and final Manning’s n-value changes are listed in the 

   ROUGH.OUT file.  To accept the changes to Manning’s n-values, CHAN.

   RGH can be renamed to replace CHAN.DAT for the next FLO-2D flood 

   simulation.  This automates the spatial adjustment of n-values for
   channel 

   elements that exceed the limiting Froude number.

.. container::
   :name: page220-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202321900219.png
   210

   Chapter 5

   Output Files

   *CHANNEL_CONVERGENCE.OUT *

   This file lists the channel elements that failed to converge in three
   passes 

   of the routing algorithm.  The solution is then based on the
   diffusive wave 

   for that element and timestep only.  The output files reports:.  

    ·

   Time - time of failed convergence

    ·

   Grid element

    ·

   Depth - depth at time of failed convergence (ft or m)

    ·

   Velocity - various velocity terms in the solution algorithm (fps or 

   mps)

   *CHANSEDSIZE.OUT *

   The initial and final sediment size distribution by channel
   element is writ-

   ten to this file.  

   *CHANSTABILTY.OUT*

   This output file lists the channel grid elements that
   experienced significant 

   gains or losses of flow volume (0.1 af or 100 m

   3

   ).  These channel grid ele-

   ments may have volume conservation stability problems that could be
   relat-

   ed to surging, poorly matched roughness, slope and cross section
   geometry 

   or abrupt changes in cross section geometry.  When the channel
   volume 

   conservation for a simulation is not satisfactory, review this output
   file.  

   *CHANWS.OUT *

   This output file lists channel grid element, x-coordinate,
   y-coordinate and 

   maximum channel water surface elevation.  

    ·

   Grid

    ·

   Xcoord

    ·

   Ycoord

    ·

   Water surface elevation (ft or m)

   *CHMODFLOWELEV.OUT*

   Comparison between channel cross section cell elevation and MODFLOW 

   grid elevation.

    ·

   Grid element

    ·

   Channel bed elevation (ft or m)

    ·

   Modflow column

    ·

   Modflow row

    ·

   Modflow bed elevation (ft or m)

    ·

   Elevation difference (ft or m)

.. container::
   :name: page221-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322000220.png
   211

   Data Input

   Output Files

   *CHNBEDEL.OUT*

   The channel grid element number and the final channel bed elevation
   are 

   presented in this file.

    ·

   Grid element

    ·

   Elevation - final bed elevation (ft or m)

   *CHVOLUME.OUT*

   The channel volume distribution is listed in this output file
   including chan-

   nel inflow, channel outflow, overbank flow, return flow from the
   flood-

   plain, infiltration, channel storage and storm drain return flow.
    Review 

   this file along with the SUMMARY.OUT to determine if the channel
   flow 

   volume is being conserved.

    ·

   Time

    ·

   Inflow and rain - (acre ft or cm)

    ·

   Channel storage - (acre ft or cm)

    ·

   Channel outflow - (acre ft or cm)

    ·

   Overbank outflow - (acre ft or cm)

    ·

   Return inflow - (acre ft or cm)

    ·

   Infiltration - (acre ft or cm)

    ·

   Evaporation - (acre ft or cm)

    ·

   Outflow to storm drain - (acre ft or cm)

    ·

   Inflow from storm drain - (acre ft or cm)

    ·

   Volume conservation - (acre ft or cm)

   *CONFLUENCE.OUT*

   This file lists the channel elements that constitute a confluence as
   defined 

   by having three or more channel elements contiguous to a given
   channel 

   element.    

   *CROSSMAX.OUT*

   When the floodplain cross section analysis is requested by creating
   the FPX-

   SEC.DAT file, the CROSSMAX.OUT is created.   This file lists the
   maxi-

   mum discharge, maximum flow depth and time of occurrence for each
   grid 

   element specified in the cross section analysis.  It also list the
   total volume 

   in acre-ft for each cell.

   *CROSSQ.OUT*

   This file contains the grid element hydrographs for each of the
   floodplain 

   elements in the cross section.  The time and discharge are listed for
   each 

   output interval.

    ·

   Time

.. container::
   :name: page222-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322100221.png
   212

   Chapter 5

   Output Files

    ·

   Discharge - hydrograph for grid element (cfs or cms)

   *CVFPMAX.OUT*

   This file contains the floodplain fluid maximum sediment
   concentration 

   by volume.

    ·

   Grid element

    ·

   x-coord

    ·

   y-coord

    ·

   FP fluid max sediment concentration

    ·

   Time of FP fluid max concentration

   *CVFPMAX_MUD.OUT*

   This file contains the floodplain mudflow maximum sediment concentra-

   tion by volume.

    ·

   Grid element

    ·

   x-coord

    ·

   y-coord

    ·

   FP mudflow max concentration

   *CVTFINAL_MUD.OUT*

   This file contains the floodplain final mudflow sediment
   concentration by 

   volume.

    ·

   Grid element

    ·

   x-coord

    ·

   y-coord

    ·

   FP final mudflow concentration

   *CVTMAX.OUT*

   This file contains the channel fluid maximum sediment concentration
   by 

   volume.

    ·

   Grid element

    ·

   x-coord

    ·

   y-coord

    ·

   Channel fluid max concentration

   *CVTMAX_MUD.OUT*

   This file contains the channel mudflow maximum sediment
   concentration 

   by volume.

    ·

   Grid element

.. container::
   :name: page223-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322200222.png
   213

   Data Input

   Output Files

    ·

   x-coord

    ·

   y-coord

    ·

   channel mudflow max concentration

   *DAMBREACH_VOLUME.OUT *

   This file reports the dam breach discharge volume in acre-ft or cubic
   meters.  

   The data includes total volume for water and sediment.

    ·

   Time

    ·

   Volume hydrograph (af or cm)

   *DEBUGXX.OUT *

   This file reports all data related bugs and conflicts with an error
   code, grid 

   element and a description of the error, warning or conflict.  It is
   imported 

   by QGIS FLO-2D Plugin so users can visualize data error locations.

   *DEPRESSED_ELEMENTS.OUT *

   This file is generated at the end of the data input at runtime.
    Every grid 

   element elevation is checked with its neighbors’ elevations to see if
   it is de-

   pressed below the minimum difference of the DEPRESSDEPTH variable 

   in CONT.DAT and if so, it is listed in this file.  A value of
   DEPRESS-

   DEPTH = 3.0 ft is suggested which will help identify artificial
   ponded flow 

   conditions.  This depth will ignore minor small depression elements
   which 

   can fill and overview. 

    ·

   Grid element

    ·

   Minimum elevation difference - lowest elevation difference 

   between this element and its neighbors.   (ft or m)

   *Flow Depth Output Files*

   A series of files are created by FLO-2D in the format:  grid element
   num-

   ber, x- and y-coordinates, and the maximum flow depth.  These files
   can 

   be viewed with FLO-2D MapCrafter, MAXPLOT or programs or they can 

   be imported to a CADD or GIS program to create maximum flood depth 

   contours.  The following output files are created:

   CHNBEDEL.OUT - Channel bed elevations

   DEPCH.OUT - Maximum channel flow depths

   DEPCHFINAL.OUT - Final channel flow depths

   DEPFP.OUT - Maximum floodplain flow depths

   DEPTH.OUT - Maximum combined channel/floodplain flow depths

   DEPTHMAX_2PHASE_COMBINED.OUT - Maximum flow depth of 

   the combined two phase fluid and mudflows depth (added together). 

   DEPTHTOL.OUT  -  Maximum  combined  channel  and  floodplain  flow 

   depths greater than the TOL value.  Values less than the TOL
   value are set to 

.. container::
   :name: page224-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322300223.png
   214

   Chapter 5

   Output Files

   zero.  This file has the following format:  x- and y- coordinates, and maxi

   -

   mum flow depth.  No grid element numbers are included.

   FINALDEP.OUT - Final floodplain flow depths.

    

   ·

   Grid or Channel Left Bank Element

    

   ·

   Xcoord

    

   ·

   Ycoord

    

   ·

   Variable

   *Flow Depth Output Files for TWO-PHASE modeling.*

   DEPCH_COMBO.OUT  -  Combined  channel  fluid  and  mudflow  maxi

   -

   mum  flow  depths.  Channel  fluid  or  mudflow  max  depth  (whichever  is 

   greater).

   DEPCH_MUD.OUT - Channel maximum mudflow depth.

   DEPCHFINAL_MUD.OUT - Channel final mudflow depth.

   DEPFPMAX_MUD.OUT - Floodplain maximum mudflow depth.

   FINALDEP_COMBO.OUT  -  Combined  floodplain  fluid  and  mudflow 

   maximum flow depths. Floodplain fluid or mudflow max depth (whichever 

   is greater).

   FINDALDEP_MUD.OUT - Floodplain final mudflow depth.

   For each file, only the Grid element number, coordinates and
   variables are 

   listed.

    

   ·

   Grid or Channel Left Bank Element

    

   ·

   Xcoord

    

   ·

   Ycoord

    

   ·

   Variable

   *DEPTHDUR.OUT and DEPTHDUR2.OUT*

   DEPTHDUR.OUT contains the floodplain inundation duration data in-

   cluding the grid element number, grid element x- and y-coordinates
   and 

   duration of inundation in hours.  The selected depth of inundation
   for 

   which the duration (hrs) is computed is listed at the top of the
   file.  DEP-

   THDUR2.OUT is identical to DEPTHDUR.OUT except for a hardwired 

   depth of 2 ft.

    ·

   Grid

    ·

   Xcoord

    ·

   Ycoord

    ·

   Time

   *ERROR.CHK*

   The ERROR.CHK file contains data input error and warning messages
   and 

   some runtime error messages.  The backup data files (\*.BAC) can be
   re-

.. container::
   :name: page225-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322400224.png
   215

   Data Input

   Output Files

   viewed with this file to determine if the input data is being read
   properly 

   at runtime. When a simulation terminates immediately after being
   started, 

   check this file first for data input errors.  This file is defined in
   more detail 

   in the troubleshooting section chapter 7.

   *EVACUATEDCHAN.OUT*

   The channel elements that experience a complete evacuation of the
   channel 

   volume are listed in this output file.  The channel elements in this
   file should 

   be cross-correlated with those listed in TIME.OUT and VELTIMEC.

   OUT files.

    ·

   Element

    ·

   Number of evacuations

   *EVACUATEDFP.OUT*

   The floodplain elements that experience a complete evacuation of the
   flood-

   plain volume are listed in this output file. The floodplain elements
   in this 

   file should be cross-correlated with those preeminently listed in
   TIME.

   OUT and VELTIMEFP.OUT files.

    ·

   Element

    ·

   Number of evacuations

   *FINALCVFP_MUD.OUT*

   This file contains the final floodplain mudflow sediment
   concentration by 

   volume.

    ·

   Grid

    ·

   Xcoord

    ·

   Ycoord

    ·

   Floodplain final mudflow max concentration. 

   *FLO-2D MODFLOW CH RETURN EXCHANGE.OUT *

   Exchanged volume and corrected water surface elevation calculated
   based 

   on the MODFLOW volume returning to surface for CH cells.

    ·

   Time

    ·

   Grid element

    ·

   CH grid element

    ·

   CH depth (ft or m)

    ·

   Water exchange volume (ft

   3

    or m

   3

   )

    ·

   Grid area (ft

   2

    or m

   2

   )

    ·

   Groundwater volume to surface (ft

   3

    or m

   3

   )

    ·

   Column

    ·

   Row

.. container::
   :name: page226-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322500225.png
   216

   Chapter 5

   Output Files

    ·

   Ground water depth (ft or m)

    ·

   Added depth to CH bed elevation (ft or m)

   *FLO-2D MODFLOW FP RETURN EXCHANGE.OUT *

   Exchanged volume and corrected water surface elevation calculated
   based 

   on the MODFLOW volume returning to surface for FP cells.

    ·

   Time

    ·

   Grid element

    ·

   Surface depth (ft or m)

    ·

   Corrected surface depth (ft or m)

    ·

   Grid area (ft

   2

    or m

   2

   )

    ·

   Groundwater vollume to surface (ft

   3

    or m

   3

   )

    ·

   Column

    ·

   Row

    ·

   Ground water depth above surface depth (ft or m)

   *FLOODPLAIN_CONVERGENCE.OUT *

   This file lists the floodplain elements that failed to converge in
   three passes 

   of the routing algorithm.  The solution is then based on the
   diffusive wave 

   for that element and timestep only.  The output files reports:  

    ·

   Time - time of failed convergence

    ·

   Grid element

    ·

   Depth - depth at time of failed convergence (ft or m)

    ·

   Velocity - various velocity terms in the solution algorithm (fps or 

   mps)

   *FLOODWAVETIME.OUT*

   | This file has contains the following output:
   | Node    X-coord    Y-coord    Floodwave Arrival Time    Flood Time
        Peak 

   | Time    Deflood Time    Max WS
   | Each grid element is assigned a specific value of the above
     parameters at 

   the end of the simulation.  The maximum values are tracked during the 

   simulation on a computational timestep basis.  The
   following parameter 

   definitions are used:

    ·

   Floodwave Arrival Time:  Time in hours from when the breach 

   discharge exceeds 0.01 cfs or cms to when the floodplain grid 

   element flow depth exceeds 1 ft or 0.3 m.  If the grid element has 

   a channel assignment, the time when the channel flow depth be-

   comes one foot higher than the base flow (when breach discharge 

   > 0.01 cfs or cms) is reported.  

.. container::
   :name: page227-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322600226.png
   217

   Data Input

   Output Files

    ·

   Flood Time:  Time (hours) from when the breach discharge ex-

   ceeds 0.01 (cfs or cms) to when a given grid element flow depth 

   exceeds 2.0 ft or 0.67 m on the floodplain.  If the grid element 

   has a channel assignment, the time to when the flow exceeds the 

   lowest top of bank is reported.  

    ·

   Peak Time:  Time (hours) from when the breach discharge ex-

   ceeds 0.01 (cfs or cms) to when a given grid element flow depth 

   reaches a maximum depth.  If the grid element has a channel as-

   signment, the time to when the channel flow reaches a maximum 

   depth is reported.

    ·

   Deflood Time:  The time elapsed from the initial failure of the 

   dam until the grid element returns to its pre-flood water eleva-

   tion (0.1ft) prior to failure.  The dam breach initialization is 

   based on the first incremental change in flow depth greater than 

   the tolerance value (TOL). 

    ·

   Max WS:  The maximum water surface elevation for a given 

   floodplain grid element is reported.  If a channel is assigned to 

   the grid element, the maximum water surface elevation for either 

   the channel or the floodplain is reported. 

   *FLOODWAY.OUT*

   FLOODWAY.OUT is written when IFLOODWAY = 0.  This file lists the 

   grid element and the maximum floodplain water surface elevation.
    Follow-

   ing the base flood simulation in which FLOODWAY.OUT is written, the 

   then user sets IFLOODWAY = 1 and assigns a value for ENCROACH in 

   CONT.DAT.  For a floodway simulation, the model reads FLOODWAY. 

   OUT and does not share discharge between floodplain elements until
   the 

   computed water surface in FLOODWAY.OUT plus the ENCROACH 

   value is exceeded for a given grid element.  See the FLO-2D
   Reference 

   Manual for a discussion on the floodway routine.  

   *FPINFILTRATION.OUT*

   The total infiltration (ft or m) at the end of the simulation for
   each flood-

   plain element is written to this file with grid element x- and
   y-coordinates.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Total infiltration (ft or m)

   *FPMODFLOWELEV.OUT*

   Comparison between FP grid cells elevation and Modflow grid
   elevations.

.. container::
   :name: page228-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322700227.png
   218

   Chapter 5

   Output Files

    ·

   Grid element

    ·

   Elevation

    ·

   Modflow column

    ·

   Modflow row

    ·

   Modflow elevation

    ·

   Elevation difference

   *FPREV.NEW*

   This output file reports the differences in elevation between the rim
   eleva-

   tion in the SWMM.inp file and the FLO-2D grid element
   elevation.  This 

   file should be reviewed to evaluate the elevations representing the
   inlet ref-

   erence elevation.

    ·

   Grid element

    ·

   New grid element elevation (ft or m)

   *FPRIMELEV.OUT*

   This output file reports the differences in elevation between the rim
   eleva-

   tion in the SWMM.inp file and the FLO-2D grid element
   elevation.  This 

   file should be reviewed to evaluate the elevations representing the
   inlet ref-

   erence elevation.

    ·

   Grid element

    ·

   Floodplain elevation - grid element elevation (ft or m)

    ·

   Rim elevation - rim elevation of storm drain inlet or manhole (ft 

   or m)

    ·

   Difference (ft or m)

    ·

   New floodplain elevation - elevation the model uses (ft or m)

   *FPLAIN.RGH*

   This file contains the final Manning’s n-value changes for the
   floodplain 

   grid elements.  The maximum and final Manning’s n-values are
   reported 

   in the ROUGH.OUT.  If the changes are acceptable, FPLAIN.RGH can 

   be renamed to FPLAIN.DAT for the next FLO-2D flood simulation.  This 

   automates the spatial adjustment of n-values for floodplain elements
   that 

   exceed the limiting Froude number.

   *FPLAIN_SDELEV.RGH*

   This file contains the elevation adjusments that were automatically
   correct-

   ed when the FLO-2D engine compared the floodplain grid elements to
   the 

   storm drain rim and type 4 invert elevations.  To fully accept the
   changes 

   reported to fprimelev.new, replace FPLAIN.DAT with this file.  It is
   also 

   necessarry to replace the TOPO.DAT with TOPO_SDELEV.RGH.

.. container::
   :name: page229-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322800228.png
   219

   Data Input

   Output Files

   *FPSEDSIZE.OUT*

   The initial and final sediment size distribution for the floodplain
   grid ele-

   | ment is written to this file.
   | The file is arranged in tables by grid element.

    ·

   Grid element

    ·

   Sediment diameter. (mm)

    ·

   Percent finer initial

    ·

   Percent finer final

   *GRID#_LEVFAIL.OUT*

   Individual failure data for specific grid element.  The Grid# is the
   grid ele-

   | ment number.
   | The file is arranged in tables by grid element.

    ·

   Grid element

    ·

   Sedime

   *HYCHAN.OUT*

   This channel hydraulics output file contains a hydrograph for each
   channel 

   element and includes the time, elevation, depth, velocity, discharge
   and 

   sediment concentration.  The maximum discharge and stage are also
   listed 

   with their times of occurrence.  The following columns are printed
   for each 

   channel element.

    ·

   Time - output interval

    ·

   Elevation - watersurface elevation starting at bed elevation.

    ·

   Thalweg depth - average depth above the lowest point in the 

   channel for the duration of the output interval. (ft or m)

    ·

   Velocity - depth average velocity for cross section for the dura-

   tion of the output interval (fps or mps)

    ·

   Discharge - average discharge for the output interval (cfs or cms)

    ·

   Froude number - based on the average depth and velocity.

    ·

   Flow area - average flow area given by the average discharge 

   divided by the average velocity (sqft or sqm)

    ·

   Wetted Perimeter - average wetted perimeter for the cross section 

   for the duration of the output interval (ft or m)

    ·

   Hydraulic radius average flow area divided the average wetted 

   perimeter (ft or m)

    ·

   Top width - average top width for the duration of the output 

   interval (ft or m)

    ·

   Width to depth ratio - average width divided by the average 

   depth

    ·

   Energy slope - average water surface head plus the average 

   velocity head divided by the length of the channel between grid 

.. container::
   :name: page230-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202322900229.png
   220

   Chapter 5

   Output Files

   element centers

    ·

   Bed shear stress - average energy slope times the average hydrau-

   lic radius times gamma (specific weight of water)

    ·

   Surface area - average surface area of the channel (top width 

   times channel length) for the duration of the output interval 

   (sqft or sqm)

   *HYCROSS.OUT*

   The output interval time, top width, depth, velocity and discharge
   are listed  

   for each cross section.  The discharge passing the cross section of
   grid ele-

   ments is compiled as a hydrograph. The cross section maximum
   discharge 

   and the individual grid elements are written to the CROSSMAX.OUT 

   file..

    ·

   Time

    ·

   Flow width - distance between the first and last node (ft or m)

    ·

   Depth - average depth across the complete cross section (ft or m)

    ·

   Watersurface elevation (ft or m)

    ·

   Velocity - average velocity for the complete cross section (fps or 

   mps)

    ·

   Discharge - resolved and compiled discharge for the complete 

   cross section.  This is the most important value (cfs or cms).  If 

   mudflow is used, this is the total water discharge including mud-

   flow concentration.

    ·

   Concentration by volume  - mudflow concentration is written as 

   output when mudflow or 2 phase mudflow is used.

   *HYDROALL.OUT*

   This file is generated by the HYDROG.EXE. It is
   used internally and not 

   by the end user. 

   *HYDRAULIC STRUCTURE SUBFACTORS.OUT*

   The discharge hydrographs of all the hydraulic structures is
   presented in 

   this output file.   This file lists time and the discharge seen an
   the inlet and 

   at the outlet for each hydraulic structure.  If
   the values are negative in the 

   inlet, the water is moving from the outlet to the inlet as backwater.
    If the 

   discharge varies wildly, there could be surging.  The rating table or
   curve 

   might not match the cross sectional areas adjacent to the structures.

    ·

   Time

    ·

   Discharge inlet

    ·

   Discharge outlet

.. container::
   :name: page231-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323000230.png
   221

   Data Input

   Output Files

   *HYDROSTRUCT.OUT*

   The discharge hydrographs of all the hydraulic structures is
   presented in 

   this output file.   This file lists time and the discharge seen an
   the inlet and 

   at the outlet for each hydraulic structure.  If
   the values are negative in the 

   inlet, the water is moving from the outlet to the inlet as backwater.
    If the 

   discharge varies wildly, there could be surging.  The rating table or
   curve 

   might not match the cross sectional areas adjacent to the structures.

    ·

   Time

    ·

   Discharge inlet

    ·

   Discharge outlet

   *HYSTREET.OUT*

   The street flow hydrograph for the grid element that is coincidental to the 

   street and the cross section is recorded in this file. 

   *IMPACT.OUT*

   The units are pounds force per foot (newton per linear meter). This is the 

   impact force on a wall or feature of a unit length.  Multiple by the
   length of 

   the cell or the length of the dump to get the total maximum impact
   force on 

   the feature. Please note that this would be an impact force if the
   maximum 

   velocity were instantaneous on the wall or feature as in a frontal
   wave. If 

   the flow gradually increases on the wall and the maximum velocity
   occurs 

   with the flow going over the wall or feature then the impact force will be 

   mitigated.  The conservative approach to the impact force would consider 

   that the maximum velocity occurs in a frontal wave that would instanta-

   neously stop.  As the impact force is a one-time instantaneous
   maximum 

   value based on flow cessation is not temporally reported by output
   interval.  

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Impact - lbf/ft or N/m

   *INFILHY.OUT*

   The hydraulic conductivities are listed in this file to review their
   spatial 

   variation.  This file contains grid element number, x- and
   y-coordinates and 

   floodplain hydraulic conductivity.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Hydraulic conductivity

.. container::
   :name: page232-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323100231.png
   222

   Chapter 5

   Output Files

   *INFIL_DEPTH.OUT*

   This file will only write data if the limiting depth is used in the
   Green-Ampt 

   infiltration calculator.  If the global soil depth is not set, the
   spatial data 

   won’t be used and this file will be empty.  The file reports the soil
   depth in 

   ft and infiltration depth in ft.  Once the infiltration reaches the
   limiting soil 

   depth, the stop switch is activated and the infiltration is turned
   off for the 

   specified grid element.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Soil depth - assigned limiting infiltration soil depth (ft or m)

    ·

   Infiltration depth - total infiltration depth (ft or m)

    ·

   Stop - 0 or 1, where 1 = available infiltration depth was filled and 

   infiltration stopped

   *INTERGWS.OUT*

   NTERGWS.OUT lists the maximum floodplain water surface elevations.  

   Values less than TOL are set to zero.  Only grid elements and
   maximum 

   water surface elevations are listed; no coordinates are included.

    ·

   Grid element

    ·

   Water surface elevation (ft or m)

   *LEVEE.OUT*

   The LEVEE.OUT file contains a list of the grid elements with a levee
   that 

   failed.  Failure width, failure elevation, discharge from the levee
   breach and 

   the time of failure occurrence are listed.  The file shows failure
   expansion 

   into multiple directions and adjacent levee elements.  The total
   breach is 

   written to ge#_PRESCRIBED_BREACH.OUT.  This file also reports the 

   time at which the breach reaches the bottom of the grid elevation and
   the 

   flow for that direction changes from weir flow to overland flow.

    ·

   Grid element

    ·

   Direction - fail direction 1-8

    ·

   Water surface elevation (ft or m)

    ·

   Breach elevation (ft or m)

    ·

   Failure width (ft or m)

    ·

   Discharge for cutoff direction (cfs or cms)

    ·

   Avg Q for 10 timesteps (cfs or cms)

    ·

   Time (hrs)

   *LEVEEDEFIC.OUT*

   The levee freeboard deficit is listed in this file.  Five levels of
   freeboard defi-

   cit are reported:  

.. container::
   :name: page233-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323200232.png
   223

   Data Input

   Output Files

    

   0 = freeboard > 3 ft (0.9 m) 

    

   1 = 2 ft (0.6 m) < freeboard < 3 ft (0.9 m) 

    

   2 = 1 ft (0.3 m) < freeboard < 2 ft (0.6 m) 

    

   3 = freeboard < 1 ft (0.3 m)  

    

   4 = levee is overtopped by flow.  

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Levee deficit

   *LEVOVERTOP.OUT*

   The discharge hydrograph overtopping the levee within the grid
   element is 

   reported in this file.  Only those levee grid elements with a
   negative levee 

   element number in LEVEE.DAT will be reported when overtopped. The 

   discharge is combined for all the potential levee overtopping
   directions for 

   the grid element.  

    ·

   Grid element

    ·

   Discharge total

    ·

   Time - time of overtopping, 

    ·

   Discharge direction negative value means flow is moving from 

   the opposite grid to the grid with the levee assigned

   *LEVOVERTOP.OUT*

   The max discharge of the water overtopping the levee within the grid
   ele-

   ment is reported in this file.  Only those levee grid elements with a
   negative 

   levee element number in LEVEE.DAT will be reported when overtopped. 

   The discharge is combined for all the potential levee overtopping
   directions 

   for the grid element.  

    ·

   Grid element

    ·

   Discharge max (cfs or cms)

    ·

   Time - time of overtopping (hrs)

   *LOW_LEVEE_CREST_ELEVATIONS.OUT*

   Levee crest elevations that are less than a minimum difference above
   the 

   ground are list in this file.  The minimum elevation difference is
   the DE-

   PRESSDEPTH parameter in the CONT.DAT file.  This variable is used 

   to evaluate the minimum difference in the levee crest elevations
   compared 

   to the ground elevation on both sides of the levee.  If used with DE-

   PRESSED_ELEMENTS.OUT, the DEPRESSDEPTH variable either has 

   to be the same value or two separate
   independent simulations are required 

   for different values (use SIMUL = 0.1 or 0.01 hrs for each).  

    ·

   Grid element - element with the levee assigned

    ·

   Neighbor grid element - element across from the levee cutoff 

.. container::
   :name: page234-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323300233.png
   224

   Chapter 5

   Output Files

   direction

    ·

   Direction - levee cutoff direction 1-8

    ·

   Levee crest elevation (ft or m)

    ·

   Ground elevation (ft or m)

    ·

   Elevation difference (ft or m)

   *MANNINGS_N.RGH*

   MANNINGS_N.RGH is a duplicate file of the MANNINGS_N.DAT 

   file with the updated Manning’s n-value changes that were reported in
   the 

   ROUGH.OUT file.  The maximum and final Manning’s n-value changes 

   are listed in the ROUGH.OUT.

   *MAXQBYDIR.OUT*

   This output file lists the maximum floodplain grid element discharge
   ac-

   cording to the eight flow directions and the time of occurrence.  

    ·

   Grid element

    ·

   North - Qmax (cfs or cms) Time

    ·

   NE - Qmax (cfs or cms) Time

    ·

   East - Qmax (cfs or cms) Time

    ·

   SE - Qmax (cfs or cms) Time

    ·

   South - Qmax (cfs or cms) Time

    ·

   SW - Qmax (cfs or cms) Time

    ·

   West - Qmax (cfs or cms) Time

    ·

   NW - Qmax (cfs or cms) Time

   *MAXQHYD.OUT*

   This output file lists the maximum floodplain grid element discharge
   and 

   the associated hydraulics including:

    ·

   Grid element

    ·

   Time

    ·

   Maximum discharge (cfs or cms)

    ·

   Direction - direction max discharge was recorded 1-8

    ·

   Water surface 

    ·

   Depth (ft or m)

    ·

   Velocity (fps or mps)

    ·

   Combined Qmax (cfs or cms)

    ·

   Direction - direction max velocity 1-8

   *MAXQRESOLVED.OUT*

   The maximum discharge resolved by flow direction listed for all eight
   flow 

   directions regardless of the time of occurrence are reported to this
   file.  The 

.. container::
   :name: page235-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323400234.png
   225

   Data Input

   Output Files

   resolved flow direction maximum discharge includes the sum
   of the pri-

   mary flow direction and the two diagonal flow directions.

    ·

   Grid element

    ·

   North - Qmax (cfs or cms)

    ·

   NE - Qmax (cfs or cms)

    ·

   East - Qmax (cfs or cms)

    ·

   SE - Qmax (cfs or cms)

    ·

   South - Qmax (cfs or cms)

    ·

   SW - Qmax (cfs or cms)

    ·

   West - Qmax (cfs or cms)

    ·

   NW - Qmax (cfs or cms)

   *MAXWSELEV.OUT*

   Similar to DEPTH.OUT, this file contains grid element number,
   x-coordi-

   nate, y-coordinate, and the maximum water surface elevation of either
   the 

   floodplain or channel.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Water surface elevation (ft or m)

   *MODFLOW CHANNEL INFILTRATION TOTALS.OUT*

   Total aaccumulated volume of water that infiltrates from the CH to
   MOD-

   FLOW at each  MODFLOW timestep.

    ·

   Time

    ·

   Accumulated infiltration volume CH (ft

   3

    or m

   3

   )

   *MODFLOW CHANNEL INFILTRATION VOLUMES.OUT*

   Accumulated volume of water that infiltrates from CH to MODFLOW at 

   each Modflow timestep and for each cell.

    ·

   Time

    ·

   Grid element

    ·

   Accumulated infiltration volume CH (ft

   3

    or m

   3

   )

   *MODFLOW FP INFILTRATION TOTALS.OUT*

   Total aaccumulated volume of water that infiltrates from the FP to
   MOD-

   FLOW at each  MODFLOW timestep.

    ·

   Time

    ·

   Accumulated infiltration volume FP (ft

   3

    or m

   3

   )

.. container::
   :name: page236-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323500235.png
   226

   Chapter 5

   Output Files

   *MODFLOW FP INFILTRATION VOLUMES.OUT*

   Accumulated volume of water that infiltrates from FP to MODFLOW at 

   each Modflow timestep and for each cell.

    ·

   Time

    ·

   Grid element

    ·

   Accumulated infiltration volume FP (ft

   3

    or m

   3

   )

   *MULTCHN.OUT*

   The multiple channel routine routes the overland flow between grid
   ele-

   ments as concentrated channel flow (i.e. rill and gully flow). For
   grid ele-

   ments specified for multiple channel flow, overland flow
   only occurs within 

   the grid element and the flow between the elements is conveyed as
   gully 

   flow.  Once the flow enters the multiple channels, the channel will
   enlarge 

   to contain the flow.  This occurs when the flow depth exceeds the
   specified 

   channel depth. The channel increases by a specified incremental
   width.  Af-

   ter the peak discharge has passed and the flow depth is less than one
   foot, 

   the channel width will decrease until it reaches the original width.
    MUL-

   TCHN.OUT identifies multiple channel revisions including the maximum 

   width, final width and the original width for each grid element. The
   file has 

   the following format:

    ·

   Grid element

    ·

   Max width (ft or m)

    ·

   Depth (ft or m)

    ·

   Qmax (cfs or cms)

    ·

   of the 8 directions has inflow or outflow)

    ·

   WSEL=  Water Surface Elevation for each cell.

   *MULTSTEEP.OUT*

   This file lists the number of steep multiple channels found within
   the as-

   signed minimum and maximum slopes.

   *MULT.RGH*

   MULT.RGH is a duplicate file of the MULT.DAT file with the updat-

   ed Manning’s n-value changes that were reported in the ROUGH.OUT 

   file.  The
   maximum and final Manning’s n-value changes are listed in the 

   ROUGH.OUT.

   *#GE_PRESCRIBED_BREACH Q.OUT*

   This file reports the total breach discharge for the falure element
   and the 

   expansion elements.  The output is time and discharge.

    ·

   Time (hrs)

.. container::
   :name: page237-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323600236.png
   227

   Data Input

   Output Files

    ·

   Discharge (cfs or cms)

   *OUTNQ.OUT*

   The OUTNQ.OUT file is separated into two data areas.  The first
   section 

   contains a summary of the maximum discharge, time of peak and the
   dis-

   charge hydrograph for each floodplain outflow element. The second
   section 

   is column data that includes the following for each outflow node:

    ·

   Grid element

    ·

   Time (hrs)

    ·

   Discharge (cfs or cms)

   *OVERBANK.OUT*

   When the flow exceeds bankfull discharge and begins to inundate the
   flood-

   plain, the channel grid element and time of overbank flood occurrence
   are 

   written to this file.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Time

    ·

   Water surface elevation - elevation at time water goes overbank 

   (ft or m)

    ·

   Thalweg depth - depth at time water goes overbank (ft or m)

    ·

   Velocity - average velocity at time water goes overbank (fps or 

   mps)

    ·

   Discharge - q at time water goes overbank (cfs or cms)

    ·

   Overbank volume 

    ·

   Available floodplain area

   *REVISED_RATING_TABLE.OUT *

   This file reports suggested revisions to hydraulic structure rating
   tables 

   based on the inflow discharge to the hydraulic structure inlet
   floodplain or 

   channel element.  These revisions are usually the result of the
   rating table 

   being created with low n-values or because the rating table has
   insufficient 

   low depth stage-discharge pairs or the cross section do not match the
   rating 

   table data.

   *ROUGH.OUT*

   The ROUGH.OUT file reports the automated Manning’s n-value adjust-

   ment during model simulation including n-value change for exceeding
   the 

   Courant number and exceeding the limiting Froude. The user specifies
   a 

   maximum Froude number for overland, channel and street ?ow. When the 

   computed Froude number exceeds the defined maximum value for a given 

.. container::
   :name: page238-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323700237.png
   228

   Chapter 5

   Output Files

   grid element, the n-value for that grid element is increased by a
   value based 

   on the percent change in the n-value. During the falling limb of the
   hy-

   drograph when the Froude number is no longer exceeded, the n-value is 

   decreased by 0.0005 until the original n-value is reached. When the
   Cou-

   rant number timestep is exceeded consecutive times by the same grid
   ele-

   ment, then n-value is also increased. With increasing consecutive timestep 

   decrements, the increase in n-value decreases.  The maximum n-value,
   time 

   of occurrence, and original n-values for floodplain, channel and
   street are 

   listed in ROUGH.OUT by grid element.

   *SD MANHOLEPOPUP.OUT *

   SDManholePopUp.OUT is created when at least one manhole pops in the 

   storm drain system.  This file contains the following information:

    ·

   Xcoord

    ·

   Ycoord

    ·

   Grid element

    ·

   Manhole ID

    ·

   Time

    ·

   Pressure Head

    ·

   Rim elevation + Surcharge Elevation

    ·

   FLO-2D WSE.

   *SEDCHAN.OUT*

   The sediment transport routine will compute scour and deposition in
   the 

   channel.   

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Maximum deposition (ft or m)

    ·

   Maximum scour (ft or m)

    ·

   Final bed elevation difference (ft or m)

    ·

   Maximum water surface elevtion (ft or m)

   *SEDCONSERV.OUT*

   The sediment transport conservation summary is listed by output
   interval.

    ·

   Time

    ·

   Inflow (cuft or cum)

    ·

   Floodplain storage (cuft or cum)

    ·

   Channel storage (cuft or cum)

    ·

   Street storage (cuft or cum)

    ·

   Outflow (cuft or cum)

    ·

   Conservation total (cuft or cum)

.. container::
   :name: page239-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323800238.png
   229

   Data Input

   Output Files

    ·

   Conservation percent (cuft or cum)

   *SEDFP.OUT*

   Similar to the SEDCHAN.OUT file, the floodplain scour and deposition 

   are reported in the SEDFP.OUT file.  

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Maximum deposition (ft or m)

    ·

   Maximum scour (ft or m)

    ·

   Final bed elevation difference (ft or m) 

    ·

   Maximum water surface elevation (ft or m)

   *SEDTRAN.OUT*

   The sediment transport capacity (cfs or cms) computations for each of
   the 

   eleven sediment transport equations are listed by output interval in this file 

   for a single specified grid element. Set the variable to print the
   file in the 

   SED.DAT file or with the FLO-2D Plugin. 

    ·

   Zeller/Fullerton

    ·

   Yang

    ·

   Englund/Hansen

    ·

   Ackers/White

    ·

   Laursen

    ·

   Toffaleti

    ·

   MPM-Woo

    ·

   MPM-Smart

    ·

   Karim/Kennedy

    ·

   Parker/Klingemen/McClean

    ·

   Van Rijn

   *SPECENERGY.OUT*

   The specific energy is the sum of the depth plus the velocity head.
    This file 

   lists the maximum specific energy (ft or m) for a floodplain grid
   element 

   and includes grid element number, grid element x- and y-coordinates and 

   maximum specific energy.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Specific energy (ft or m)

.. container::
   :name: page240-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202323900239.png
   230

   Chapter 5

   Output Files

   *STATICPRESS.OUT*

   The spatially variable static force per linear foot for each floodplain element 

   is presented is this file by grid element number, x- and
   y-coordinates and 

   force per linear foot or meter.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Static pressure (lb/ft or N/m)

   *STORMDRAIN_ERROR.CHK*

   Storm drain error and warning messages are written to this file.  The
   er-

   ror/warnings related to conflicts between storm drain features and
   surface 

   components as well as the elevations checks are
   listed.  The Storm Drain 

   Guidelines manual has a troubleshooting section that will help
   determine 

   how the errors and conflicts can be corrected.

   *STREET.RGH*

   This file lists the final changes to Manning’s n-values for the
   street grid 

   elements.  The maximum and final Manning’s n-values are reported in
   the 

   ROUGH.OUT file. If the n-value changes are acceptable, STREET.RGH 

   can be renamed to STREET.DAT for the next FLO-2D flood simulation.  

   This automates the spatial adjustment of n-values for street
   elements that 

   exceeded the limiting Froude number.

   *STREET.OUT*

   Similar to DEPTH.OUT, this file contains the street element x- and y-

   coordinates and the maximum street flow depth.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Maximum street depth (ft or m)

   *STRELEV.OUT*

   Final street elevations used in the model simulation are listed in
   this file.

    ·

   Grid element

    ·

   Final street elevation (ft or m)

   *SUMMARY.OUT*

   This file lists the volume conservation summary table including the
   simula-

   tion output time interval, the minimum timestep and flood volume conser-

   vation.  It also reports the inflow hydrograph, rainfall,
   infiltration loss, and 

.. container::
   :name: page241-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324000240.png
   231

   Data Input

   Output Files

   outflow and storage volumes.  Review the volume conservation accuracy 

   | and the final distribution of volume in this file.
   | Mass balance information for the various flow components is
     reported.

    ·

   Inflows

    ·

   Inflow hydrograph volume

    ·

   Rainfall volume

    ·

   Storage

    ·

   Floodplain storage

    ·

   Channel storage

    ·

   TOL storage (see TOLER.DAT)

    ·

   Outflow

    ·

   Infiltration and interception

    ·

   Floodplain outflow

    ·

   Channel infiltration

   Storm drain exchange volume is reported

    ·

   Storm drain inflow

    ·

   Total inflow

    ·

   Total outflow

    ·

   Storm drain return flow

    ·

   Storm drain mass balance

   Storm drain volume data from swmm.rpt

    ·

   Wet weather inflow

    ·

   External inflow

    ·

   External outflow

    ·

   Return flow to surface

    ·

   Total storm drain storage

    ·

   Continuity error 

   Totals are reported

    ·

   Total outflow

    ·

   Total volume and storage

    ·

   Area of inundation data

    ·

   Wetted floodplain area

    ·

   Wetted channel area

   Project Specific Data

    ·

   Grid element size

    ·

   Total number of grid elements

    ·

   Grid System area (acres or m^2 and mi^2 or km^2)

   Average hydraulics

    ·

   Discharge (cfs or cms)

    ·

   Velocity (fps or cms)

.. container::
   :name: page242-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324100241.png
   232

   Chapter 5

   Output Files

    ·

   Flow area (ft^2 or m^2)

    ·

   Flow depth (ft or m)

    ·

   Flow width (ft or m)

   Computation data

    ·

   Total Computations

    ·

   Computer run time (hrs)

    ·

   Termination date and time

   *SUPER.OUT*

   Instead of writing the supercritical flow messages at runtime (and
   limiting 

   them to the first 100 or so instances), the maximum supercritical
   Froude 

   number (associated depth and time and number of occurrences) are
   tracked 

   and sorted by Froude number in descending order at model termination 

   for both floodplain and channel (at the bottom of the file). It also
   indicates 

   if the grid elements are hydraulic structures.  By correlating this file with 

   TIME.OUT, ROUGH.OUT, VELTIMEFP.OUT, the user can address 

   the problematic elements with greater insight.

    ·

   Grid element

    ·

   Max Froude number

    ·

   Depth (ft or m)

    ·

   Time

    ·

   Number of supercritical timesteps

   *SURFAREA.OUT*

   The SURFAREA.OUT lists the available flow surface area in each grid
   ele-

   ment.  The area reduction factors (ARF) remove a portion of the
   surface 

   area of a grid element to account for buildings or other features
   that occupy 

   the flow surface area.  Channels, streets and multiple channels also
   require 

   a portion of the floodplain surface.  The remaining floodplain
   surface area 

   is reported.  At the end of the
   file, the maximum area of floodplain inunda-

   tion (including the channel surface area) for the entire grid system
   is listed 

   by output time interval.  This can be an informative data file for
   the user.  

   The SURFAREA.OUT file enables a review of the surface area
   distribution 

   between the various components.  

    ·

   Grid element

    ·

   Arf-reduced area - total area minus the building

    ·

   Channel area - bank elements covered by part of the channel

    ·

   Street area - area covered by street component

    ·

   Mult channel area - area covered by mult channel

    ·

   Overland area - remaining area not covered by a component

    ·

   Mult channels - switch tells the user this element has a mult 

   channel.

.. container::
   :name: page243-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324200242.png
   233

   Data Input

   Output Files

   *SWMM.OUT*

   This is the binary file that contains the numerical results from a
   storm drain 

   simulation. Veiw it with the storm drain interface (GUI) to create
   the time 

   series plots and tables, profile plots, and statistical analyses.
    For more infor-

   mation look at: C:\\Users\\Public\\Documents\\FLO-2D PRO Documenta-

   tion\\flo_help\\Manuals\\FLO-2D Storm Drain Manual.pdf.

   *SWMM.RPT*

   This file contains the report information and the results of the
   storm drain 

   flood routing in ASCII Format. The storm drain model engine
   generates 

   this file. It is extensive and contains discharge hydrographs for
   every drain 

   inlet, outlet and conduit. The Storm Drain Guidelines manual is the
   best 

   resource for developing, troubleshooting and reviewing anything
   storm 

   drain related. For more information look at:
   C:\\Users\\Public\\Documents\\

   FLO-2D PRO Documentation\\flo_help\\Manuals\\FLO-2D Storm Drain 

   Manual.pdf.

   *SWMMOUTFIN.OUT*

   This file reports the storm drain outfall hydrographs for return flow
   to the 

   surface water system.  This file lists the grid element (or channel
   element 

   if applicable) followed by the time and discharge pairs. The Storm
   Drain 

   Guidelines manual is the best resource for
   developing, troubleshooting and 

   reviewing anything storm drain related. For more information look at:
   C:\\

   Users\\Public\\Documents\\FLO-2D PRO Documentation\\flo_help\\Manu-

   als\\FLO-2D Storm Drain Manual.pdf.

   *SWMMQIN.OUT *

   The discharge hydrograph and return flow (time, discharge and return
   flow) 

   into each storm drain inlet of the pipe network is reported in this
   file. Each 

   inlet has a discharge hydrograph and return flow reported each output
   in-

   terval TOUT timestep.  The Storm Drain Guidelines manual is the best 

   resource for developing, troubleshooting and reviewing anything
   storm 

   drain related.  For more information look at:
   C:\\Users\\Public\\Documents\\

   FLO-2D PRO Documentation\\flo_help\\Manuals\\FLO-2D Storm Drain 

   Manual.pdf  

   *SD ManholePopUp.OUT*

   This file reports the storm drain manhole nodes that have enough
   pressure 

   head to pop off the manhole cover.  The pop off presure head is an
   instan-

   taneous head that removes the manhole cover.  This pressure head can
   be 

   different to the reported pressure head in the SWMM.RPT file. 

.. container::
   :name: page244-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324300243.png
   234

   Chapter 5

   Output Files

    ·

   Manhole ID

    ·

   Popped time

    ·

   Pressure head pop off must be greater than the following:

    ·

   Rim and surcharge head

    ·

   FLO-2D water surface elevation

   *TIMDEP.OUT*

   This file contains grid element, flow depth, velocity and velocity
   direction 

   x and y and water surface elevation for each floodplain grid element at the 

   user specified time intervals (TIMTEP in CONT.DAT).  This file is
   also 

   required for a time-lapse simulation in the MAXPLOT and FLO-2D Map-

   | Crafter post-processor programs.
   | Time - output interval for time series.  Single value at the top of
     the col-

   umns.

    ·

   Grid element 

    ·

   Depth (ft or m)

    ·

   Velocity (sqrt(x^2+y^2)) (fps or mps)

    ·

   Velocity x - velocity vector x

    ·

   Velocity y - velocity vector y

    ·

   Water surface elevation (ft or m)

   *TIMDEPCELL.OUT*

   This file contains flow depth, velocity, and velocity direction x and
   y, and 

   water surface elevation for a set of grid elements defined by the
   TIMEDEP-

   CELL.DAT file.  The user specifies time intervals with TIMTEP in
   CONT.

   DAT.  

   *TIMDEP.HDF5*

   This binary output file contains grid element, flow depth, velocity
   and ve-

   locity direction x and y
   and water surface elevation for each floodplain grid 

   element at the user specified output time intervals (TIMTEP in CONT.

   DAT). This file is written in binary format (HDF5) and it has the
   same 

   results than the TIMDEP.OUT file.

   *TIMDEP_NC4.OUT*

   This file contains specific details for every grid element at each
   time series 

   output interval. The user specifies output time intervals with TIMTEP
   in 

   CONT.DAT. This is an ASCII file.

    ·

   Grid element

    ·

   Depth (ft or m)

    ·

   Qmax (cfs or cms)

.. container::
   :name: page245-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324400244.png
   235

   Data Input

   Output Files

    ·

   Qmax direction - grid element direction 1 - 8

    ·

   Vmax (fps or mps)

    ·

   Vmax direction - grid element direction 1 - 8

    ·

   Qnet - all flow in minus all flow out (cfs or cms)

    ·

   Surface Exchange - switch 0 or 1 identifies if cell had any flow 

   for the time interval

   *TIME.OUT*

   The timestep is controlled by the numerical stability criteria.  When
   the 

   stability criteria are exceeded for a particular grid element, the
   timestep is 

   decreased.  The grid elements with the highest number of timestep
   decreases 

   are written to the TIME.OUT file.  This file can be reviewed to
   determine 

   if a specific floodplain, channel or street node is
   consistently causing the 

   timestep decrease and what stability criteria is frequently being exceeded.  If 

   one grid element has caused significantly more timestep decreases
   than the 

   other grid elements, then its attributes and the attributes of the
   contiguous 

   grid elements should be carefully reviewed.  

    ·

   Grid element - floodplain, channel, or street

    ·

   Number of timestep decrements

    ·

   Percent change in depth

    ·

   CFL Stability criteria

    ·

   Dynamic wave stability criteria

   The file lists the last one hundred time step decreases and the node
   type.

   *TIMEONEFT.OUT*

   This file reports the grid element number, the x- and y-coordinates
   and the 

   initial time to one foot of depth.  The time to one foot of depth can
   be plot-

   ted in FLO-2D MapCrafter.  This file is typically used for dam and
   levee 

   breach analysis.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Time to one ft depth 

   *TIMETOPEAK.OUT*

   This file reports the grid element number, the x- and y-coordinates
   and the 

   time of occurrence of the maximum depth.  This time to maximum depth 

   can be plotted in FLO-2D MapCrafter.  While this file is typically
   used for 

   dam and levee breach analysis, it valid for general flood studies.

    ·

   Grid element

.. container::
   :name: page246-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324500245.png
   236

   Chapter 5

   Output Files

    ·

   Xcoord

    ·

   Ycoord

    ·

   Time to one ft max depth 

   *TIMETWOFT.OUT*

   This file reports the grid element number, the x- and y-coordinates
   and the 

   initial time to two feet of depth.  The time to two feet of depth can
   be plot-

   ted in FLO-2D MapCrafter.  This file is typically used for dam and
   levee 

   breach analysis.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Time to two ft depth 

   *TOPO_SDELEV.RGH*

   This file contains the elevation adjusments that were automatically
   cor-

   rected when the FLO-2D engine compared the floodplain grid elements 

   to the storm drain inlet rim and type 4 invert elevations.  To fully
   accept 

   the changes reported to fprimelev.new, replace TOPO.DAT with this
   file.  

   It is also necessarry to replace the FPLAIN.DAT with FPLSIN_SDELEV.

   RGH.

   *UPS-DOWS-CONNECTIVITY.OUT*

   This file reports the connectivity between the upstream domain grid
   ele-

   ments and the downstream domain grid elements. 

    ·

   Upstream grid element

    ·

   Downstream grid elements

   *Velocity Output Files *

   These files are similar to the DEPTH.OUT file.  These files contain
   the 

   x- and y-coordinates and maximum velocities and can be viewed with
   the 

   MAXPLOT or FLO-2D MapCrafter program.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Velocity in the channel element (fps or mps) 

   *The velocity output files include:*

   STVEL.OUT - Maximum street flow velocity;

   STVELDIR.OUT - Flow direction of the maximum street flow velocity;

   VELFP.OUT - Maximum floodplain flow velocity;

   VELOC.OUT - Maximum channel flow velocity;

.. container::
   :name: page247-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324600246.png
   237

   Data Input

   Output Files

   VELCHFINAL.OUT - Final channel flow velocities.;

   VELDIREC.OUT - Flow direction of the maximum floodplain flow veloc

   -

   ity.

   FINALVEL.OUT -Flow velocity at the end of the simulation.

   FINALDIR.OUT - Flow maximum velocity direction at the end of the 

   simulation.

   *The velocity output files related to 2-PHASE flow include:*

   FINALDIR_MUD.OUT - Floodplain final mudflow velocity direction.

   FINALVEL_MUD.OUT  -  Floodplain  final  mudflow  velocity  in  the  re

   -

   ported outflow direction.

   VELDIREC_MUD.OUT - Floodplain maximum mudflow velocity direc

   -

   tion. 

   VELFP_MUD.OUT - Floodplain maximum mudflow velocity in the re

   -

   ported outflow direction.

   VELOC_MUD.OUT - Channel maximum mudflow velocity.

   VELRESMAX_MUD.OUT - Floodplain maximum resolved mudflow ve

   -

   locity in the computed outflow direction.

   FPWSEL_MUD.OUT - Floodplain maximum mudflow water surface el

   -

   evation.

    

   ·

   Grid or Channel Left Bank Element

    

   ·

   Xcoord

    

   ·

   Ycoord

    

   ·

   Variable

   *VELTIMEC.OUT*

   This file lists the grid element number, maximum channel velocity and
   the 

   time of occurrence. It is sorted from highest to lowest velocity so
   that an 

   examination of the first several lines of output data will determine
   if there 

   are any unreasonably high maximum channel velocities.

    ·

   Grid element

    ·

   Vmax in the channel element (fps or mps)

    ·

   Time of occurrence

   *VELTIMEFP.OUT*

   This file lists the first 100 floodplain elements: number, maximum
   flood-

   plain velocity and the time of occurrence.  It is sorted from highest
   to lowest 

   velocity so that an examination of the first several lines of output
   data will 

   determine if there are any unreasonably high maximum floodplain
   veloci-

   ties.

    ·

   Grid element

    ·

   Vmax floodplain element (fps or mps)

    ·

   Depth floodplain element (ft or m)

.. container::
   :name: page248-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324700247.png
   238

   Chapter 5

   Output Files

    ·

   Time of occurrence

   *VELRESMAX.OUT*

   This file lists the maximum resolved velocities as a vector field.
    It is not 

   based on the 8-flow directions.

    ·

   Grid element

    ·

   Xcoord

    ·

   Ycoord

    ·

   Velresmax (fps or mps)

    ·

   Velxmax

    ·

   Velymax

   Flow velocities are computed in 8-directions for each grid
   element.  In the 

   figure below, the red arrows indicate inflow to the grid element (2-direc

   -

   tions) and the blue arrows represent outflow from the grid element (3-di

   -

   rections).  The remaining flow directions have zero discharge and velocities.  

   The arrow length indicates relative magnitude.  If the outflow velocities 

   from the grid element are resolved into x- and y- coordinate
   directions, the 

   components would be depicted by the blue arrows in the figure below.  The 

   resultant velocity vector for the outflow from the grid element would then 

   be represented by the green arrow.  

.. container::
   :name: page249-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324800248.png
   239

   Data Input

   Output Files

   *VELTIMEST.OUT*

   This file lists the street element number, maximum street velocity
   and the 

   time of occurrence.  It is sorted from highest to lowest velocity so
   that an 

   examination of the first several lines of output data will determine
   if there 

   are any unreasonably high maximum street velocities.

    ·

   Grid element

    ·

   Vmax street element (fps or mps)

    ·

   Time of occurrence

   *WSTIME.OUT*

   If the WSTIME.DAT file is created, the WSTIME.OUT file will be gener-

   ated listing the channel element number, time of the measured water sur-

   face elevation, measured water surface elevation at stated time,
   predicted 

   water surface elevation at stated time, difference between the water
   surface 

   elevations and the cumulative difference between the measured and pre-

   dicted water surfaces.  

   *XSECAREA.OUT*

   When the channel cross section option is invoked for channel routing,
   the 

   channel geometry data is written to this file.  It includes:  grid
   element, flow 

   area, top width and wetted perimeter for the lowest top of bank
   (bankfull 

   flow).

    ·

   Grid element

    ·

   Flow area of the cross section (sqft or sqm)

    ·

   Top width of the cross section (ft or m)

    ·

   Wetted Perimeter of the cross section (ft or m)

   *XSEC.OUT*

   This file is created by the channel sediment transport option (ISED =
   1 in 

   CONT. DAT and ISEDN = 1 for a channel segment in CHAN.DAT) for 

   natural cross section geometry data.  It contains the final cross
   section bed 

   elevations after scour and deposition have been computed.  The file
   looks 

   the same as XSEC.DAT with updated elevation data.   

.. container::
   :name: page250-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202324900249.png
   [240]

   This page is intentionally Blank.

.. container::
   :name: page251-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325000250.png
   **CHAPTER 6**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** P**

   **roGraMs**

   241

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   There are four post-processor programs:  FLO-2D MapCrafter, MAXPLOT, 

   HYDROG and PROFILES that display the output data graphically. FLO-2D 

   MapCrafter and MAXPLOT display the flood inundation depth and
   velocity 

   plots.  Channel flood simulations or floodplain cross sections are
   required to view 

   hydrographs in HYDROG. A channel model is also required to view the
   channel 

   water surface profiles in PROFILES. These programs can be initiated by clicking 

   on their names in the File pull down menu in the FLO-2D Plugin or by
   copying 

   the executable (\*.EXE) file into the project subdirectory and double
   clicking on 

   the program name in a file browser.

   **6.1 **

   **hYDroG **

   Channel output hydrographs, floodplain cross section hydrographs, and
   hydrau-

   lic structure hydrographs can viewed with the HYDROG program.  It
   displays 

   the hydrograph for every channel element in the system.  It will also
   list the 

   average channel hydraulic data for various reaches of river.  Gaging
   station hy-

   drograph data can be plotted along with the FLO-2D predicted
   hydrograph by 

   creating the optional HYDRO.DAT file in the following format:

.. container::
   :name: page252-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325100251.png
   242

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   HYDRO.DAT File Example

   Haynor

   13160     251

   0.00 1287.85

   1.00 1285.47

   2.00 1295.01

   3.05 1302.20

   ...

   HYDRO.DAT File Descriptors

   3   

   Line 1:  Number of gaging station with hydrograph data

   Haynor 

   Line 2: 

   Name of gaging station (10 letters)

   13160    251 

   Line 3:  Channel grid element and # of hydrograph pairs

   0.00   1287.85 

   Line 4:  Hydrograph pairs time(hours) discharge (cfs)

   1.00   1285.47  

   Line 4:  Hydrograph pairs time(hours) discharge (cfs) 

   Notes:

   Line 2 - 4:  These lines are repeated for each gaging station.

.. container::
   :name: page253-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325200252.png
   243

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   After opening HYDROG, click on either ‘Plot Channel Hydrographs’, ‘Plot Cross 

   Section Hydrographs,’ or ‘Compute Hydraulics’ in the Main Menu shown
   below:

   Click on ‘Plot Channel Hydrographs’ a dialog box appears to select
   either a channel 

   segment or element:

   After selecting the channel element and clicking ‘OK’, the hydrograph is plotted as 

   shown in the following figure.  Use the dialog box in the upper right
   portion of the 

   screen to select another channel element or to return to the channel
   element list or 

   main menu.

   Hint: 

   From the Main 

   Menu, other options 

   are to save the plot-

   ted hydrograph as a 

   bitmap image, send 

   the hydrograph to a 

   printer, or write the 

   hydrograph to an 

   ASCII file.

.. container::
   :name: page254-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325300253.png
   244

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   If the ‘Compute Hydraulics’ is selected from the
   Main Menu, the following dialog 

   box is displayed:

   After entering the three data fields in the dialog box (including the
   desired discharge 

   for computing the average channel hydraulics, mouse click ‘OK’ to display the fol-

   | lowing table:
   | This table displays the average discharge
     weighted hydraulic conditions for the given 

   discharge between the two channel elements (inclusive).   From this dialog box, se-

   lect a new discharge and add to the table or print this table to an
   ASCII file (HYDR.

   OUT).  

.. container::
   :name: page255-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325400254.png
   245

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   Similar hydrographs can plotted for floodplain cross section selected
   in the HY-

   CROSS.OUT and Hydraulic Structure hydrographs in HYDROSTRUCT.OUT.  

   If the file exists, the cross section hydrograph for the selected
   cross section elements 

   and flow direction will plotted using the second command on the Main
   Menu bar.

.. container::
   :name: page256-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325500255.png
   246

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   **6.3 **

   **flo-2D M**

   **aP**

   **c**

   **rafter**

   FLO-2D MapCrafter is the primary post processing tool for FLO-2D
   software.  It is 

   a QGIS plugin and can be accessed via the QGIS Plugin Directory using
   the Plugin 

   Manager.  The MapCrafter documentation is maintained on the
   MapCrafter wiki.  

   https://github.com/FLO-2DSoftware/FLO-2DMapCrafter.wiki.git

.. container::
   :name: page257-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325600256.png
   247

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   In addition to mapping FLO-2D results, MapCrafter can also help users
   design 

   map layouts for printing high resolution mapping pdfs.

.. container::
   :name: page258-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325700257.png
   248

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   **6.3 **

   **MaPPer P**

   **ro**

   MAPPER Pro is a post-processor program that creates
   high resolution maps and 

   plots of the FLO-2D model results including area of inundation, time
   variation 

   of hydraulic variables, maximum water surface elevations, duration of
   inundation, 

   impact force, static pressure, specific energy, sediment scour or
   deposition and oth-

   ers.  As of October 2023, the GDS and MAPPER Pro are now distributed
   separately 

   from FLO-2D.  These tools are aging and their Visual Basic code has
   an unknown 

   life limit via Microsoft.  If a
   user requires these tools, they can be downloaded via the 

   FLO-2D Shafefile account.  MAPPER Pro is a post-processing program
   for viewing 

   the FLO-2D simulation results. Three types of plots can be
   generated: 

    ·

   Grid element plots where each element is assigned a color depending
   on 

   the value of the selected plot variable. 

    ·

   Line and shaded contour maps based on the grid element values.  

    ·

   DTM point depth plots to generate detailed flow depth contour maps 

   based on grid element water surface elevations and DTM point ground 

   elevations.

   The MAPPER Pro manual describes the commands and tools and provides
   instruc-

   tion.  

   **6.4  **

   **MaxPlot  **

   The MAXPLOT program is a basic graphical tool to display the grid
   element maxi-

   mum depths and velocities.  MAXPLOT is a simple alternative to MAPPER
   Pro 

   that quickly displays plots of the maximum floodplain and channel
   depths, maxi-

   mum street velocity, final floodplain depths and others.  It is
   faster than MAPPER 

   Pro but has less graphical resolution and fewer display options.  Use
   MAXPLOT for 

   a quick overview of predicted flow depths and velocities.  By zooming
   in on a given 

   plot, the grid element number, maximum flow depth or velocity and the
   maximum 

   water surface elevation can be viewed.  The tool bar has options for
   view extents, 

   previous view, pan, a coarse flood contour and 3-D plot and an option
   to save the 

   view as a bitmap.

   MAXPLOT can be initiated by copying the program to the project folder and double 

   | clicking it.  After opening MAXPLOT a blank screen appears with a
     Main Menu:
   | Click on ‘Open’ to display the following the dialog box:

.. container::
   :name: page259-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325800258.png
   249

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   Activate one of the plots listed in the dialog box above by clicking
   on the radio 

   button in front of the plot option and clicking the ‘OK’ button.  Set
   limits on the 

   minimum and maximum depths or velocities to display.  The following
   plot displays 

   the combined channel and floodplain maximum flow depth for the Monroe
   project 

   example.  

.. container::
   :name: page260-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202325900259.png
   250

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   **6.5 **

   **ProfIles**

    The PROFILES program serves the dual purpose of being a pre- and
   post-processor 

   program for 1D channels.  As a post-processor program, it will
   display a channel 

   water surface and bed elevation for any FLO-2D simulation output
   interval.  In 

   order to view the predicted water surface elevation in PROFILES, it
   is necessary to 

   run a FLO-2D channel simulation first.  The PROFILES program has zoom
   and 

   | print options to assist in reviewing the results.  
   |  To view the predicted water surface profiles, click on
     ‘View Profiles’ in the Main 

   Menu and a dialog box appears:

   To view the predicted maximum water surface elevation profile, click
   on the radio 

   button labeled ‘Maximum Water Surface’ and click ‘OK’.  Plot the
   water surface at 

   any output interval by entering the time in the text box in the upper
   right corner.  

   The peak discharge can also be plotted as a function of the channel
   distance.  To 

   plot the surveyed or measured, the WSURF.DAT must be prepared.  The
   file for-

   mat is presented at the end of this section of the manual.

.. container::
   :name: page261-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326000260.png
   251

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   There are several options on the Main Menu.  Zoom in on given river
   reach, print 

   the image or label the distance along the channel in river miles.
    The zoom view is 

   shown in the following figure:

   If sediment transport has been simulated, PROFILES will plot the
   final bed eleva-

   tion and the cross section geometry changes associated with either
   scour or deposi-

   tion.  The image below displays sediment deposition and scour in a
   reach of the 

   Middle Rio Grande in New Mexico.

   Non-uniform sediment distribution on the channel bed can be viewed
   when the 

   channel flow is simulated.  The cross section plot below displays the
   final cross sec-

   tion elevations in red compared to the cross section elevations at
   the start of the 

   flood simulation shown in black.  This image can be expanded to full
   view.

.. container::
   :name: page262-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326100261.png
   252

   **c**

   **haPter**

   ** 6**

   **P**

   **ost**

   **-P**

   **rocessors**

   The user has an option in the water surface dialog box of plotting
   the surveyed water 

   surface and bed elevations along with the predicted values.  To
   plot the surveyed 

   water surface or channel bed elevation, the WSURF.DAT file must be
   created in 

   | the following format:
   | Optional WSURF.DAT file format:
   |  Please note that PROFILES also has options for editing the channel
     bed slope and 

   thalweg flow depth and for interpolating the slope and cross section
   geometry for 

   the cross section option.  Refer the section on Pre-Processor
   Programs for a discus-

   sion on these features.  

    

   WSURF.DAT File Descriptors

   2045 

   Line 1:  # of channel elements with a surveyed ws elev.

   4   4152.22 

   Line 2: 

   Grid Element   WS elevation

   8   4151.84 

   Line 2: 

   Grid Element   WS elevation

   ...

   Notes:

   Line 2:  This line is repeated for each channel element with a
   surveyed ws elevation.

   WSURF.DAT File Example

   2045

         4    4152.22

         8    4151.84

        12    4151.69

        15    4151.55

        19    4151.41

        ....

.. container::
   :name: page263-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326200262.png
   253

   **D**

   **ata**

   ** I**

   **nPut**

   **P**

   **ost**

   **-P**

   **rocessor**

   ** **

   **P**

   **rograms**

   The surveyed water surface can also be compared directly with the
   FLO-2D com-

   puted water surface in the WSTIME.OUT (see file description in the
   output file 

   section) by creating a WSTIME.DAT file.  The WSTIME.DAT file format
   is as 

   follows:

   | The WSTIME.OUT file will contain:
   | Channel element number., time of survey (hrs), surveyed water
     surface elevation, 

   computed water surface elevation, difference between the surveyed and computed 

   water surface and cumulative difference between the surveyed and
   computed water 

   surface elevations.

   WSTIME.DAT File Descriptors

   49   

   Line 1:  # of channel elements with a surveyed ws elev.

   117632   4658.95   240 

   Line 2: 

   Grid Element   WS elevation   Time

   117928   4655.80   240 

   Line 2: 

   Grid Element   WS elevation

   ...

   Notes:

   Line 2:  This line is repeated for each data set.

   WSTIME.DAT File Example

     49

     117632    4658.95     240

     117928    4655.80     240

     119882    4652.28     240

     120580    4650.36     240

     120915    4648.52     240

      ....

.. container::
   :name: page264-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326300263.png
   [254]

   This page is intentionally Blank.

.. container::
   :name: page265-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326400264.png
   **CHAPTER 7**

   **D**

   **ebuGGInG**

   ** **

   **anD**

   ** t**

   **rouble**

   ** s**

   **hootInG**

   ** **

   **the**

   ** D**

   **ata**

   ** f**

   **Iles**

   255

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   **7.1 **

   **t**

   **roubleshootInG**

   ** G**

   **uIDelInes**

   **Data Errors**

   Data input errors may result in the automatic termination of a
   simulation run 

   along with a Fortran error message.  The error message will report a
   ‘Unit’ number 

   that is associated with the FLO-2D file that contains the error.  The files are listed 

   in Table 4.1, Table 7.1, and Table 7.2.  

   Table 7.1  List of Misc Files and Unit Numbers

   Unit 

   No.

   File Name

   Unit 

   No.

   File Name

   47

   ARF�BAC

   398

   MANNINGS_N�BAC

   260

   BREACH�BAC

   2902

   MANNINGS_N_RES�BAC

   387

   BUILDING_COLLAPSE�BAC

   48

   MULT�BAC

   46

   CHAN�BAC

   51

   OUTFLOW�BAC

   40

   CONT�BAC

   42

   RAIN�BAC

   35

   EVAPOR�BAC

   1569

   SDCLOGGING�BAC

   41

   FPLAIN�BAC

   49

   SED�BAC

   121

   FPXSEC�BAC

   53

   STREET�BAC

   1610

   GUTTER�BAC

   1567

   SWMMFLO�BAC

   69

   HYSTRUC�BAC

   1564

   SWMMOUTF�BAC

   43

   INFIL�BAC

   29

   TOLER�BAC

   44

   INFLOW�BAC

   397

   TOPO�BAC

   58

   LEVEE�BAC

   2901

   TOPO_RES�BAC

.. container::
   :name: page266-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326500265.png
   256

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   **Troubleshooting:  Is the flood simulation running OK?**

   There are several indicators to help you identify modeling problems.
    The most 

   important one is volume conservation. The FLO-2D results should be reviewed 

   for volume conservation, surging, timestep decrements, and roughness
   adjustments 

   with limiting Froude numbers. 

   *Volume Conservation*

   Any hydraulics model that does not report on volume conservation
   should 

   be suspected of generating or losing volume. A review of the SUMMARY.

   OUT file will identify any volume conservation problems. This file
   will dis-

   play the time when the volume conservation error began to appear
   during 

   the simulation. Typically a volume conservation error greater 0.001
   percent 

   is an indication that the model could be improved. The file CHVOLUME.

   OUT will indicate if the volume conservation error occurred in the
   channel 

   routing instead of the overland flow component. Components should be 

   switched ‘off’ one at a time and the model simulation run again until
   the 

   volume conservation problem disappears.  This will identify which
   com-

   ponent is causing the difficulty. Some volume conservation problems
   may 

   be eliminated by slowing the model down (decreasing the timesteps)
   using 

   the numerical stability criteria.  Most volume conservation problems
   are an 

   indication of data errors.

   *Surging*

   It is possible for volume to be conserved during a flood simulation
   and still 

   have numerical surging. Numerical surging is the result of a mismatch
   be-

   tween flow area, slope and roughness.  It can cause an
   over-steepening of the 

   floodwave identified by spikes in the output hydrographs. Channel
   surging 

   can be identified by discharge spikes in the CHANMAX.OUT file or in
   the 

   HYDROG program plotted hydrographs. Predicted high maximum veloci-

   ties indicate surging. To identify floodplain surging, review the
   maximum 

   velocities in the MAXPLOT or Mapper post-processor program. You can 

   also review the VELTIMEC.OUT (channel) or VELTIMEFP.OUT (flood-

   plain) files for unreasonable maximum velocities. Surging can be
   reduced 

   or eliminated by adjusting (lowering) the stability criteria
   (DEPTOLFP or 

   WAVEMAX in TOLER.DAT) thus decreasing the timesteps. If decreasing 

   the timesteps fails to eliminate the surging, then individual grid
   element 

   topography, slope or roughness should be adjusted. This can be accom-

   plished in the GDS for floodplain flow.  For channel flow, the
   PROFILES 

   program can be used to make adjustments.  Increasing the flow
   roughness 

   will generally reduce or eliminate flow surging. For channel surging,
   abrupt 

   transitions in flow areas between contiguous channel elements should
   be 

.. container::
   :name: page267-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326600266.png
   257

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   avoided. Setting a lower limiting Froude number for a channel reach
   may 

   also help to identify the problem.

   *Sticky Grid Elements*

   When the flood simulation is running slowly, the TIME.OUT file can
   be 

   reviewed to determine which grid elements are causing the most
   timestep 

   decreases (‘sticky elements’). TIME.OUT lists the top twenty
   floodplain, 

   channel or street elements that caused the model to slow down. The
   file 

   also lists whether the timestep decreases occur with the percent
   change in 

   depth, Courant criteria or dynamic wave stability criteria.
   Adjustments can 

   be made in the stability criteria to more equably distribute the
   timestep 

   decreases. The model is designed to advance and decrement timesteps,
   so 

   there have to be grid elements listed in the TIME.OUT file. If one or
   two 

   grid elements have significantly more timestep decreases than the
   other ele-

   ments listed in the file, the attributes of the ‘sticky’ grid
   elements such as 

   topography, slope or roughness should be adjusted. The goal is to
   make the 

   | model run as fast as possible while avoiding numerical surging.
   | If a floodplain element is causing most of the timestep decreases,
     check 

   the SURFAREA.OUT file to determine how much surface area is left in 

   the floodplain element for flood storage. If the floodplain element
   contains 

   a channel bank, there may be very little surface area left for flood
   storage.  

   This will cause the model run slowly with exchanges the flow between
   the 

   channel and floodplain. To fix this problem:

    ·

   Remove other components from the channel bank element including 

   streets or ARF values.

    ·

   Shorten the channel length (XLEN in CHAN.DAT). This will in-

   crease the surface area in the channel bank floodplain elements.

    ·

   Decrease the channel cross section width in the PROFILES program.

   *Limiting Froude Numbers*

   There is a unique relationship between floodwave celerity and average
   flow 

   velocity described by the Froude number that should not be violated
   during 

   numerical flood routing.  This is a physical relationship between the
   kine-

   matic and gravitation forces. To use the limiting Froude number,
   estimate a 

   reasonable maximum Froude number for your flood simulation and
   assign 

   the value to either FROUDL (floodplain), FROUDC (channels) or STRF-

   NO (streets) variables. When the computed Froude number exceeds the 

   limiting Froude number, the n-value is increased by a small value (~
   0.001) 

   for the next timestep. This change in grid element n-value helps to
   create a 

   better match between the slope, flow area and n-value during the
   simula-

   tion. When the limiting Froude number is no longer exceeded,
   the n-value 

   is gradually decreased to the original value. The changes in the
   n-values 

.. container::
   :name: page268-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326700267.png
   258

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   during the simulation are reported in the ROUGH.OUT file. For the next 

   FLO-2D simulation, grid element n-value adjustments can be made
   using 

   the n-values reported in ROUGH.OUT.  The maximum n-values are also 

   reported in MANNINGS_M.RGH, CHAN.RGH and STREET.RGH 

   files that are created at the end of a simulation. These (\*.RGH)
   files can 

   then be renamed to data input files (\*.DAT)
   for the next flood simulation 

   (e.g. MANNINGS_N.RGH = MANNINGS_N.DAT).

   *Reviewing the results*

   FLO-2D results include the maximum area of inundation as displayed
   by 

   the maximum flow depth, temporal and spatial hydraulic results, channel or 

   floodplain cross section hydrographs and peak discharges.  The
   Mapper++ 

   program can used to review maximum flow depths, water surface
   elevations 

   or velocities.  The results can be plotted as either line contours or
   shaded 

   contours in Mapper++.  Look for any maximum velocities or flow
   depths 

   | that are unreasonable.  This may be an indication of numerical
     surging.  
   | The FLO-2D flood simulation can be terminated at any time during
     the 

   run by clicking Exit on the toolbar.  The simulation will terminate
   after 

   the current output interval is completed and the output files are
   generated 

   and saved.  This enables the user to check if the flood simulation is running 

   poorly (e.g. too slow or not conserving volume) and the simulation
   can be 

   stopped without losing the opportunity to review the output data.  

   **Make some adjustments**

   The following data file adjustments may improve the simulation and
   speed up the 

   model:

   *Spatial Variation of n-values*

   The most common cause of numerical surging is underestimated
   n-values. 

   Typical n-values represent steady, uniform flow.  Spatial variation
   of n-values 

   will affect the floodwave progression (travel time) and reduce
   surging, but 

   may not significantly impact the area of inundation (especially for
   longer 

   flood durations). Focus on the critical part of the project area when
   adjust-

   ing n-values and review TIME.OUT and ROUGH.OUT to complete the 

   n-value revisions.

   *Edit Topography*

   The interpolation of DTM points to assign elevations to grid elements
   is 

   not perfect even when the GDS filters are applied. It may be
   necessary to 

   adjust some floodplain grid element elevations when you review the
   re-

   sults. MAXPLOT and Mapper++ can be used to locate grid elements with 

   unreasonable flow depths that may constitute inappropriate depressions. 

   Floodplain depressions can sometimes occur along a river channel if
   too 

.. container::
   :name: page269-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326800268.png
   259

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   many floodplain DTM points located within the channel.

   *Floodplain Surface Area Reduction*

   The distribution of flood storage on the grid system can be
   influenced by as-

   signing area reduction factors (ARF’s) to represent loss of storage
   (i.e. build-

   ings). For large flood events, the assignment of individual grid
   element ARF 

   values will usually have minor impact on the area of inundation. For
   local 

   flooding detail, individual grid element ARF assignments may be
   justified.

   *Channel Cross Section Adjustments*

   Typically a surveyed cross section will represent five to ten channel
   ele-

   ments. Selecting a cross section to represent transitions between
   wide and 

   narrow cross sections requires engineering judgment. Use the
   PROFILES 

   program to interpolate the transition between surveyed cross
   sections.

   *Channel Slope Adjustments*

   Adverse channel slopes can be simulated by FLO-2D. Smoothing out an 

   irregular slope condition over several channel elements to represent
   reach 

   average slope conditions may speed up the simulation. Cross sections
   with 

   scour holes can result in local adverse slopes that misrepresent the average 

   reach conditions. Review the channel slope in PROFILES.

   *Street Flow*

   High street velocities may cause numerical surging and slow the
   simulation 

   down.  Assign reasonable limiting street Froude numbers to adjust the
   street 

   n-values.

   **Model Calibration and Replication of Flood Events**

   Estimating flood hydrology (both rainfall and flood hydrographs) can
   be difficult 

   when replicating historical floods. To match measured flood stages,
   high water 

   marks or channel discharges, first determine a reasonable estimate of
   the flood vol-

   ume, then concentrate on the model details such as n-values, ARF’s
   and street flow.  

   Flood volume is more important to flood routing than the peak
   discharge.

   **7.2 **

   **t**

   **rouble**

   ** s**

   **hootInG**

   ** t**

   **echnIQue**

   ** **

   When undertaking a new FLO-2D flood simulation, start simple and
   progressively 

   build in model component detail.  After the required data files have been prepared, 

   run a basic overland flood simulation. Review the results. If any
   issues arise consult 

   | the troubleshooting tips found in this chapter.
   | To debug the data files after a FLO-2D simulation, begin by
     reviewing the ER-

   ROR.CHK file.  All the data errors recognized by the model are
   reported in this file.  

   FLO-2D has an extensive data error and warning message system and the
   messages 

.. container::
   :name: page270-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202326900269.png
   260

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   are reported in ERROR.CHK as data inconsistencies are encountered.
    One of the 

   most common errors is missing data that will invoke an end-of-file
   error statement 

   to the screen.  This error occurs when the model is searching for
   more data than 

   is in the data file.  Another common error is to activate a component
   or process 

   switch without preparing the required data file.  For example, an error will occur if 

   the component switch ICHANNEL = 1 in the CONT.DAT file, but the data
   file 

   | CHAN.DAT is not available. 
   | One data error that is difficult to locate is the array allocation
     violation where the ar-

   ray index number becomes zero or larger than the assigned value.  For
   example, there 

   may be missing sediment concentrations in INFLOW.DAT for a mudflow simula-

   tion. This made a code error where a variable is not initialized to
   zero.   When this 

   type of error is encountered, the FLO-2D model is terminated with a
   FORTRAN 

   error message without indicating the file location or line entry of
   the error.  To lo-

   cate the data error, simplify the simulation and turn off all of the
   components and 

   turn them back on one at time until the error occurs again.  Reset
   simulation time 

   to the model time just after the error occurred to reduce time to
   debug the model.  

   If attempts to debug an error are ineffective, send a zipped copy of
   the data files to 

   | FLO-2D (contact@flo-2d.com) along with brief description of the
     problem.    
   | The user can create a set of backup data files to debug the model.
      Set IBACKUP  = 1 

   in the CONT.DAT file.  These backup files replicate the data files
   and will indicate 

   if the computer is reading the data files correctly.  The backup file
   should be identical 

   to the original data file except for spacing.  If the program
   terminates before reaching 

   the first output interval timestep, there is probably an error in the
   data files.  Start by 

   checking the \*.BAC files one by one.  If one of the files is not
   complete, this may be 

   | the location of the data error.   
   | Review the following files to analyze volume conservation problems: SUMMARY.

   OUT, CHVOLUME.OUT, CHANMAX.OUT, TIME.OUT, BASE.OUT, 

   ROUGH.OUT, CHANNEL.CHK, and SURFAREA.OUT.  See the ‘Pocket 

   Guide’ for further troubleshooting tips involving volume
   conservation, sticky grid 

   elements listed in the TIME.OUT file, and numerical surging.
    The instructional 

   comments at the end of each data file description in this manual
   contains a number 

   of guidelines to assist the user in creating or checking the data
   files.   

   **7.3 **

   **l**

   **Ist**

   ** **

   **of**

   ** c**

   **oMMon**

   ** D**

   **ata**

   ** e**

   **rrors**

   A list of the most common errors associated with running FLO-2D is
   presented 

   below and a table for troubleshooting runtime errors follows the
   list.  Whenever an 

   error is encountered, refer to the ERROR.CHK file first.  All of the
   \*.CHK files are 

   listed in Table 7.4.  The file descriptions can be referenced in
   Chapter 5.

.. container::
   :name: page271-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327000270.png
   261

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.2.  List of Common Data Errors

   | 1.  Missing data entries.  Insufficient data was provided to the
     model.
   | 2.  Switches were activated without the corresponding data or files
     (for ex-

   ample, see MUD, ISED, etc., in the CONT.DAT file).

   3.  There was missing or additional lines in a data file when switch
   is acti-

   vated.  Observe the \**\* Notes: \**\* in the file descriptions.

   4.  Percentages were expressed as a number instead of a decimal.  See the 

   description of XCONC in CONT.DAT or the HP(I,J,3) variable in IN-

   FLOW.DAT.

   5.  The IDEPLT grid element was improperly assigned in INFLOW.DAT 

   for the graphics mode.

   6.  Channel infiltration switch INFCHAN was not ‘turned on’ in the
   IN-

   FIL.DAT file.

   7.  Either one or both of channel and floodplain outflow elements
   were not 

   assigned for a given grid element.

   | 8.  The street width exceeded the grid element width.
   | 9.  The array size limitation for a variable was exceeded.
   | 10.  The available floodplain surface area was exceeded by
     assigning channels, 

   streets, ARF’s and/or multiple channels with too much surface area.  
   Re-

   view the SURFAREA.OUT.

   11.  The rainfall variable R_DISTRIB data was entered as total
   cumulative 

   rainfall instead of the percentage of the total rainfall (range 0.0
   to 1.0).

   12.  The ISEDN switch for channel sediment transport was not
   ‘turned on’ in 

   the CHAN.DAT file for the channel segment.

   **7.4 **

   **r**

   **untIMe**

   ** e**

   **rrors**

   The following guidelines are provided to assist the user in resolving
   runtime errors.  

   If the program stops executing after several output time intervals
   but has not reached 

   the prescribed simulation time, the problem grid element(s) may be
   listed at the end 

   of the BASE.OUT file.  The problem grid element may also be listed in
   the TIME.

   OUT file with the highest number of timestep decrements and it may
   appear in a 

   dialog box that appears on the screen when the simulation terminates.
    The user 

   should review the following data before revising the stability
   criteria: 

    ·

   Review the problematic grid element elevation and Manning’s n-value
   for 

   the listed grid element as well as the contiguous 8 grid elements
   neighbors.  

.. container::
   :name: page272-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327100271.png
   262

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   This can be done in the GDS program.

    ·

   Check the channel data to determine if the grid element contains a
   chan-

   nel and then check the relationship between the channel bed and bank 

   elevations and the floodplain elevation within the grid element.

    ·

   Review the floodplain area available within the grid element
   including loss 

   of floodplain area due to channels, streets, ARF’s or multiple
   channels in 

   the SURFAREA.OUT file.

   Most volume conservation and numerical stability problems are
   associated with 

   channel flow.  When constructing a channel system, it is often
   necessary to fabri-

   cate cross section geometry, estimate roughness or adjust channel bed
   slopes.  Mis-

   matched channel morphology parameters with an appropriate roughness
   are the 

   primary source of numerical stability problems.  To compute smoother
   hydraulics 

   between two channel grid elements, adjust the bed slope, cross
   section flow area or 

   roughness values.  Try to avoid abrupt changes in cross sections geometry from one 

   channel element to another.  The channel flow area for a natural
   channel (not a con-

   crete rectangular or trapezoidal channel geometry) should make a
   gradual transition 

   from a wide, shallow cross section to a narrow deep cross section.
    An actual cross 

   section transition may occur over several channel grid elements.
    Adjust the channel 

   geometry so that the maximum change in flow area between channel elements is  less 

   than 25%.  To address channel problems, consider the following
   measures:

    ·

   Increase the roughness in wide, shallow cross sections and decrease
   the 

   roughness in narrow deep channel grid elements.

    ·

   Reduce the difference between the cross section areas.  Avoid abrupt
   cross 

   section transitions between channel elements.  Adjust the channel
   cross 

   section geometry in the PROFILES.  Use PROFILES to re-interpolate 

   between surveyed cross sections.  

    ·

   Review and adjust the bed slope with the PROFILES program.  Adverse 

   bed slopes are OK but adverse spikes and dips are not.

    ·

   Select a longer channel length within the channel grid element.

.. container::
   :name: page273-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327200272.png
   263

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.3  List of \*.CHK Files and Unit Numbers

   Unit 

   No.

   File Name

   Unit 

   No.

   File Name

   7

   ERROR�CHK

   1234

   MODFLOW_ERROR�CHK

   56

   CHANNEL�CHK

   1577

   UNDERGROUNDOUTFALLS�CHK

   86

   CHANBANKEL�CHK

   1578

   RainCell�CHK

   194

   BATCH�CHK

   1580

   HDF5_Error�CHK

   333

   NOSHOW�CHK

   1590

   RainOneCell�CHK

   1571

   STORMDRAIN_ERROR�CHK

   8871

   ARF_ADJUSTMENT�CHK

   991

   DEBUG�CHK

.. container::
   :name: page274-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327300273.png
   264

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   **7.5 **

   **D**

   **ebuGGInG**

   ** e**

   **rrors**

   In addition to the following troubleshooting guide, refer to the
   ‘Getting Started 

   Guidelines’ at the begin of this manual and the Pocket Guide to
   assist in debugging 

   runtime errors.

   *Program will not run*

    ·

   Data errors.  Turn off the component switches until the model 

   runs. 

    ·

   The executable program was damaged.  Reload the program or 

   contact technical support.

    ·

   The model is not properly licensed.  Contact technical support. 

   *Program stops *

   The model run is terminated before the first timestep or after a few timesteps 

   with data file error indicated on the screen or in ERROR.CHK:

    ·

   Review the ERROR.CHK file or the data file identified by the 

   program error message.

    ·

   Review the backup file (\*. BAC).

    ·

   Review the List of Common Data Errors.

   *Program stops *

   The model run is terminated after several timesteps indicating a
   numerical 

   stability error.  The grid element causing the stability error is
   listed on the 

   screen instability dialog box or at the end of the BASE.OUT file.

   *Stability criteria were not met.  *

   Review and revise the elevation and roughness data for the indicated
   grid 

   element.  The ROUGH.OUT and TIME.OUT files will help to locate the 

   problem grid element.  Check the contiguous grid elements to the
   problem 

   element in the 8 directions as the problem may be with the neighbor
   ele-

   ment. 

   *Volume conservation*

   The volume conservation may indicate either a loss or gain of volume.
    A 

   review of the SUMMARY.OUT and CHVOLUME.OUT will reveal if the 

   | volume conservation error is in the channel or on the floodplain.
      Volume 
   | conservation problems are indication of data error.

.. container::
   :name: page275-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327400274.png
   265

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   *Discharge surging*

   Numerical surging (alternating from low to high discharges) is
   usually 

   associated with channel flow.  Floodplain surging can occur but is
   less 

   common. Review the maximum floodplain velocities in MAXPLOT and 

   in the VELTIMEC.OUT and VELTIMEFP.OUT files.  Unreasonable 

   maximum velocities should be addressed.  Other files to review for
   indi-

   cations numerical surging include CHANMAX.OUT, HYCHAN.OUT, 

   CHANSTABILTY.OUT, TIME.OUT, and ROUGH.OUT files.  The 

   | hydrograph plots in  the HYDROG program may display spikes to
     indicate 
   | surging.

   *  *

   It should be noted that surging may occur and the model may still 

   have relatively good volume conservation.  

   *Supercritical flow*

   *S*

   upercritical flow is not necessary a problem, but its occurrence
   should be 

   limited to conditions where it is expected such as in streets,
   concrete chan-

   nels or steep bedrock watersheds.  Supercritical flow on alluvial
   surfaces 

   should be avoided. 

   *Numerical Instability:*

   The channel surging may be related to numerical instability, abrupt
   chang-

   es in channel geometry, inappropriate slopes, supercritical flow or
   variable 

   mudflow sediment concentrations.  Mismatched slope, flow area and n-

   values are the most common causes of channel instability.  A
   combination 

   of revisions may improve numerical instability.  

    ·

   Abrupt changes in slope or severe adverse slope may cause in-

   stability.  Use the PROFILES program to fix irregular bed slope 

   conditions.  

    ·

   Review the cross section flow areas over several channel elements 

   in PROFILES.  Eliminate any abrupt changes in cross section 

   areas between channel elements.  If the surging occurs at low 

   flows, review only the bottom portion of the cross section not 

   the bankfull conditions.

    ·

   Decrease the channel Courant number in the TOLER.DAT file.  

   Decrease the Courant number in 0.1 increments until a reason-

   able lower limit of 0.2 is reached.  

    ·

   Insufficient floodplain area.  Small floodplain surface areas can 

   exacerbate unsteady flow.  Review SURFAREA.OUT and in-

   crease the available grid element surface area for flood storage.

    ·

   Increase the n-values for the grid elements in the vicinity of the 

   surging flow.  

.. container::
   :name: page276-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327500275.png
   266

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

    ·

   Adjust the floodplain grid element elevations around the prob-

   lem element.  

    ·

   Increase the channel length within the grid element.

    ·

   The hydraulic structure discharge rating curve or table may 

   be poorly matched with the upstream or downstream channel 

   hydraulics.  Review the hydraulic structure rating curve or table 

   and compare the  discharge values to those found in the HY-

   CHAN.OUT file for that particular channel element or the next 

   one upstream.

   *Unexpected supercritical flow on alluvial surfaces:*

    ·

   Adjust the limiting Froude number using the FROUDL variable 

   in the CONT.DAT file or the FROUDC variable in the CHAN.

   DAT.

    ·

   Increase the floodplain or channel roughness values.

    ·

   Modify the slope.  The grid elevations assigned by the GDS may 

   not be representative of the field condition.  Change the grid 

   element elevations to make the channel or floodplain slope more 

   uniform.

   *Variable mudflow sediment concentration:*

    ·

   Review the sediment concentration in the inflow hydrographs in 

   the INFLOW.DAT file.

    ·

   The relationships for viscosity and yield stress should fall with
   the 

   research data presented in the reference manual.  

   *FLO-2D simulation runs slow*

   Review the TIME.OUT file to identify the elements that have caused
   most 

   of the timestep reductions.  Small timesteps are the result of the
   model 

   continually exceeding the numerical stability criteria for a small
   group of 

   grid elements.  The change in flow depth for a timestep may be too
   large.  

   One of primary reasons for a slow flood simulation is that the
   relationship 

   between the discharge flux and grid element surface area is poor.
    The rate 

   of change in the discharge may be too high for the selected grid
   element 

   size. Increasing the grid element size is the best way to fix a very
   slow model.   

   Other solutions may include:

    ·

   Adjust the channel geometry in transition reaches.  

    ·

   Create a more uniform channel or floodplain slope.

    ·

   Revise the roughness values or limit the supercritical flow.

.. container::
   :name: page277-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327600276.png
   267

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

    ·

   Reduce the channel width, street width, ARF values or other 

   parameters to increase the floodplain surface area.  Review the 

   SURFAREA.OUT file.

    ·

   Increase the grid element size (a last resort).

   *Graphics display is not activated*

   The graphics display is controlled by three variables: LGPLOT and
   GRAP-

   TIM found in the CONT.DAT file and IDEPLT in INFLOW.DAT.  

   IDEPLT is the floodplain or channel inflow grid element whose hydro-

   graph will be plotted on the display.  

    ·

   Set LGPLOT = 2.  

    ·

   Check the GRAPTIM variable for an acceptable update interval.

    ·

   Make sure that the IDEPLT variable matches an inflow grid ele-

   ment and check to see that it has a hydrograph assigned to it in 

   INFLOW.DAT.

   *The inflow hydrograph does not plot in the graphics display*

    ·

   No hydrograph is associated with the IDEPLT variable.

    ·

   The hydrograph duration is too long.  Reduce the hydrograph 

   length.

    ·

   The rainfall duration is too long.  Reduce the rainfall time.

    ·

   Inappropriate peak discharge or total rainfall values distort the 

   scale for hydrograph plot.  

   *Program stops.  Excessive flow depths *

   If flow depths are excessive, then ponding or surging may be
   occurring.   

    ·

   Identify the problem element in MAXPLOT or in the end of the 

   BASE.OUT file.  

    ·

   Check TIME.OUT to determine if the problem element is also 

   causing the model to run slowly. 

    ·

   Check the elevation of the problem grid element in the TOPO.

   DAT or in the GDS.

    ·

   If the depressed element is a gravel pit or some other feature, 

   increase the n-value to decrease the  velocity (vertical overfall 

   velocity) into the pit. 

.. container::
   :name: page278-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327700277.png
   268

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   *Erratic discharge in the channel elements.  *

   A review of plotted hydrographs in HYDROG or an examination of the 

   CHANMAX.OUT or HYCHAN.OUT files will reveal if the flow dis-

   charge between contiguous channel elements is surging with spikes
   when a 

   | consistent rise or fall of the downstream discharge is expected.
   | Channel surging can be natural phenomena.  Rivers can rise and fall
     over 

   a few tenths of a foot in matter of seconds in reaches that are
   expanding 

   and contracting causing rapidly variable storage.  During high flow
   in a 

   large river, the variation in discharge associated with stage change
   on the 

   order of ~0.2 ft can be 1,000 cfs or more.    Review the
   numerical surging 

   troubleshooting.  If the channel surging is severe, the two
   conditions to 

   review are:

    ·

   Review the channel confluence and make the confluence pairs 

   are properly assigned.  See the CONFLUENCE.OUT file.  

    ·

   The channel grid elements in the CHAN.DAT file may be mis-

   identified.

   *Erratic flow in the floodplain grid elements.*

   Erratic flow in the floodplain grid elements is usually the result of
   errors 

   in the TOPO.DAT file.  This type of error generally occurs when the
   user 

   edits the TOPO.DAT file manually and adds, subtracts or moves grid
   ele-

   ments around.  Virtually all erratic flow conditions on the
   floodplain can be 

   corrected by revisions either to n-values or elevations in the GDS.

   *Channel extends through another channel element. *

   The right channel bank assignments are automated in the GDS.
    Multiple 

   left bank elements can be assigned to the same right bank on a river
   bend. 

   If a channel extends through a right bank element, the model will
   generate 

   | an error message reported in ERROR.CHK file.
   | The channel bank elements can be viewed in the GDS.  If there is a
     problem 

   with the channel bank alignment, simply revised the right bank
   element.  

   The right bank element can be any grid element if it does not cross
   another 

   connecting channel bank line.  

.. container::
   :name: page279-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327800278.png
   269

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   *Program stops; identifying one or more grid elements with too
   little floodplain *

   *surface.*

   The model will generate a message in ERROR.CHK if the channel right 

   bank has is too little surface storage area on the floodplain portion
   of the 

   element.  If this problem occurs and the floodplain surface is less
   than 5%, 

   then there are several solutions:

    ·

   Reduce the ARF value, multiple channel area or street area.

    ·

   The channel area can be reduced by decreasing the XLEN vari-

   able or top width, which is a function of the channel in the natu-

   ral channels, the side slopes, or the bottom width in the trapezoi-

   dal cross section or the width in the rectangular cross section.

    ·

   As a last resort the grid element size can be increased, but this 

   requires the re-generation of the grid system.

   *CADPTS.DAT error*

   If errors are reported in this file, delete CADPTS.DAT and
   FPLAIN.DAT 

   and run the model again. The FLOPRO.EXE will rewrite this file.

   **7.6 **

   **D**

   **ebuG**

   ** o**

   **utPut**

   ** t**

   **ables**

   The DEBUG.OUT file is created when the user runs the model in Debug
   model via 

   the QGIS Plugin.  The error codes in Tables 7.4, 7.5, and 7.6 are the
   codes used in 

   the Debug system.  They help identify data errors and data conflicts.
    These files are 

   generated as part of the preliminary data checks.  These error checks
   do not include 

   any simulation results.  Table 7.5 and 7.6 offer basic
   corrective actions for the errors.

   Table 7.4.  ERROR CODE CATEGORIES

   Error Code

   Error Category

   100

   Switches, Control Variables, Version

   200

   Boundary, Coordinate, Floodplain, Elevation

   300

   Stability Criteria

   400

   TOL

   500

   Roughness

   600

   Rainfall

   700

   Infiltration

.. container::
   :name: page280-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202327900279.png
   270

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.4.  ERROR CODE CATEGORIES

   800

   Inflow, Outflow

   1000

   Channel

   2000

   Hydraulic Structures

   3000

   Streets,  ARF/WRF

   4000

   Storm Drain

   5000

   Cross Sections

   6000

   Sediment, Mud

   7000

   Levees

   8000

   Multiple Channels

.. container::
   :name: page281-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328000280.png
   271

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

.. container::
   :name: page282-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328100281.png
   272

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.5.  BASIC ERROR CODES

   100

   Versions of the FLO-2D Pro and Storm Drain are Different� Please
   Check FLO-

   2D Build and Update Vc2005-Con�Dll

   Review engine file dates and flopro�exe and vc2005con�dll�  Make sure
   the file dates cor-

   respond to builds that are the same�  This may require Technical
   Support�

   100

   Floodway Switch = 1,Set Encroach in CONT�DAT

   To run a floodway simulation, set Floodway Switch = 1 and set the
   Encroach variable in 

   CONT�DAT�

   100

   Set NOPRTC to Only 0, 1, or 2 in CONT�DAT

   NOPRTC is a switch�  The positions are 0, 1 or 2�

   100

   For Graphical Display (Lgplot=2),Graptim must be Greater Than 0

   The variable Graphtim is missing in CONT�DAT�

   100

   Variable Xconc Exceeds 1

   The sediment concentration cannot be greater than 1�

   100

   Variable Xarf is Less Than 0 or Greater Than 1

   The Xarf variable must be a value between 0 and 1�

   100

   Variable Froudl Greater Than 9

   The Froudl variable should not be greater than 1�  

   100

   Variable Noprtfp is a Switch,Use Only 0,1,2 or 3

   NOPRTFP is a switch�  The positions are 0, 1 or 2�

   100

   Mudflow (Mud=1) and Conventional Sediment Transport (Ised=1) Cannot
   Be 

   Modeled in the Same Simulation�  Review CONT�DAT File

   Set either MUD or ISED to 0�

   100

   Grid Element 1 Has No Neighbor Grid Elements,Check the CADPTS�DAT 

   File

   If grid element number 1 does not have a neighbor, it is dangling or
   the coordinates are 

   wrong in TOPO�DAT�  Check the location of the cell�  Correct it by
   realigning the grid to 

   the computational domain�

   100

   If Displaying the Flood Graphics - Lgplot = 2 in CONT�DAT - Then
   Ideplt 

   must be Greater Than Zero in INFLOW�DAT

   Set ideplt to an inflow grid element number in inflow�dat�

   100

   If Only Writing Text Output to Screen - No Flood Graphics Lgplot = 0
   in 

   CONT�DAT - Set Ideplt = 0 in INFLOW�DAT

   For text mode, set lgplot = 0 and ideplt = 0�

   100

   Ideplt (INFLOW�DAT) must be an Inflow Node and the CONT�DAT Variable 

   Lgplot must be Set to 1

   Make sure Ideplt is a grid elment listed in inflow�dat�

   100

   Total Simulation Time of the Model Exceeds the Hydrograph Duration

   If the hydrograph ends before the simulation, make sure it is set to
   zero or the last dis-

   charge in the hydrograph will continue as steady flow�

   100

   If Ideplt is Listed As Inflow Node in the INFLOW�DAT File,Then Lgplot
   must 

   be 0 or 1

   Turn on the Lgplot and Graphtim to use Display Mode�

   200

   Grid Element Coordinates Exceed 1000000000� Reduce the Coordinate
   Values 

   Before Proceeding

   Check the coordinates in topo�dat�

.. container::
   :name: page283-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328200282.png
   273

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.5.  BASIC ERROR CODES

   100

   Versions of the FLO-2D Pro and Storm Drain are Different� Please
   Check FLO-

   2D Build and Update Vc2005-Con�Dll

   Review engine file dates and flopro�exe and vc2005con�dll�  Make sure
   the file dates cor-

   respond to builds that are the same�  This may require Technical
   Support�

   100

   Floodway Switch = 1,Set Encroach in CONT�DAT

   To run a floodway simulation, set Floodway Switch = 1 and set the
   Encroach variable in 

   CONT�DAT�

   100

   Set NOPRTC to Only 0, 1, or 2 in CONT�DAT

   NOPRTC is a switch�  The positions are 0, 1 or 2�

   100

   For Graphical Display (Lgplot=2),Graptim must be Greater Than 0

   The variable Graphtim is missing in CONT�DAT�

   100

   Variable Xconc Exceeds 1

   The sediment concentration cannot be greater than 1�

   100

   Variable Xarf is Less Than 0 or Greater Than 1

   The Xarf variable must be a value between 0 and 1�

   100

   Variable Froudl Greater Than 9

   The Froudl variable should not be greater than 1�  

   100

   Variable Noprtfp is a Switch,Use Only 0,1,2 or 3

   NOPRTFP is a switch�  The positions are 0, 1 or 2�

   100

   Mudflow (Mud=1) and Conventional Sediment Transport (Ised=1) Cannot
   Be 

   Modeled in the Same Simulation�  Review CONT�DAT File

   Set either MUD or ISED to 0�

   100

   Grid Element 1 Has No Neighbor Grid Elements,Check the CADPTS�DAT 

   File

   If grid element number 1 does not have a neighbor, it is dangling or
   the coordinates are 

   wrong in TOPO�DAT�  Check the location of the cell�  Correct it by
   realigning the grid to 

   the computational domain�

   100

   If Displaying the Flood Graphics - Lgplot = 2 in CONT�DAT - Then
   Ideplt 

   must be Greater Than Zero in INFLOW�DAT

   Set ideplt to an inflow grid element number in inflow�dat�

   100

   If Only Writing Text Output to Screen - No Flood Graphics Lgplot = 0
   in 

   CONT�DAT - Set Ideplt = 0 in INFLOW�DAT

   For text mode, set lgplot = 0 and ideplt = 0�

   100

   Ideplt (INFLOW�DAT) must be an Inflow Node and the CONT�DAT Variable 

   Lgplot must be Set to 1

   Make sure Ideplt is a grid elment listed in inflow�dat�

   100

   Total Simulation Time of the Model Exceeds the Hydrograph Duration

   If the hydrograph ends before the simulation, make sure it is set to
   zero or the last dis-

   charge in the hydrograph will continue as steady flow�

   100

   If Ideplt is Listed As Inflow Node in the INFLOW�DAT File,Then Lgplot
   must 

   be 0 or 1

   Turn on the Lgplot and Graphtim to use Display Mode�

   200

   Grid Element Coordinates Exceed 1000000000� Reduce the Coordinate
   Values 

   Before Proceeding

   Check the coordinates in topo�dat�

.. container::
   :name: page284-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328300283.png
   274

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.5.  BASIC ERROR CODES

   200

   Hydraulic Structure Channel Inflow must be a Channel Element

   Reposition the structure node onto a left bank node�

   200

   Time-Stage Elements Have a Stage Assigned that Was Less Than the
   Floodplain 

   or Channel Bed Elevation� Stage Was Reset to the Bed Elevation

   Check the invert elevation of the structure, the grid element
   elevation or the head refer-

   ence elevation�

   200

   If Ideplt is 0 in INFLOW�DAT and Irain is 0 in CONT�DAT,There is No
   Inflow 

   to Be Plotted� 

   Either Set Lgplot = 0,Assign Ideplt an Inflow Hydrograph in
   INFLOW�DAT,Or Set Irain 

   =1 in CONT�DAT and Assign the RAIN�DAT File

   300

   A Channel/Street Courant Number is Required in TOLER�DAT

   Set the correct Courant number�

   300

   If Istrflo in STREET�DAT is Set to 1,Then at Least One Inflow Node
   Must Have 

   a Street in It

   Check the STREET�DAT file�

   400

   Variable Tol Has an Inappropriate Value

   Check the TOL value�  It must be in a corect rangew�

   400

   Please Review If Tol = 0�05 Ft or 0�015 M With the Rainfall
   Abstraction

   Check the TOL variable and the Initial Abtraction variable�  The
   initial abstraction may 

   be too high�  See INFIL�DAT�

   500

   MANNINGS_N�DAT File Has a Mismatched Grid Element Number���Check 

   the End of this File

   The MANNINGS_N�DAT file might not be complete�

   500

   MANNINGS_N�DAT Files Does Not Exist� Create the File Before
   Proceeding

   Export MANINGS_N�DAT again�

   500

   The Spatially Variable Shallown Value is Outside the Range 0�010 to
   0�99

   Check the SPATIALSHALLOWN�DAT file�

   500

   N-Value is Less Than 0 or Greater Than 1

   Check the CONT�DAT file�

   600

   Line 2 in RAIN�DAT File Has to Be Reviewed For Spatially Variable
   Real Rain-

   fall Adjustments (Irainarf=1) With Rainarf Values

   Spatially variable data is missing�  Check RAIN�DAT�

   600

   Rtt must be Greater Than 0

   Check RAIN�DAT�

   600

   First Pair of the Rainfall Distribution Should Be 0� 0�

   Correct the first data pair of the rainfall distribution curve�  Set
   the first data pair to 0�0  

   0�0�

   600

   Date and Time in Raincell�Dat Must Have this Format: 06-15-2003
   14:00:00

   Check RAINCELL�DAT�

   700

   Variable Infmethod Line 1 in the INFIL�DAT is Either Missing or Not
   Cor-

   rectly Assigned

   Check INFIL�DAT�

   700

   To Use the Scs Curve Number Method For Infiltration You Must Have 

   Rainfall,Irain = 1 in CONT�DAT and RAIN�DAT File

   Check RAIN�DAT�

   700

   Variable Poros is Greater Than 1

   Check INFIL�DAT�

   700

   Variable Sati or Satf is Greater Than 1

   Check INFIL�DAT�

.. container::
   :name: page285-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328400284.png
   275

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.5.  BASIC ERROR CODES

   200

   Hydraulic Structure Channel Inflow must be a Channel Element

   Reposition the structure node onto a left bank node�

   200

   Time-Stage Elements Have a Stage Assigned that Was Less Than the
   Floodplain 

   or Channel Bed Elevation� Stage Was Reset to the Bed Elevation

   Check the invert elevation of the structure, the grid element
   elevation or the head refer-

   ence elevation�

   200

   If Ideplt is 0 in INFLOW�DAT and Irain is 0 in CONT�DAT,There is No
   Inflow 

   to Be Plotted� 

   Either Set Lgplot = 0,Assign Ideplt an Inflow Hydrograph in
   INFLOW�DAT,Or Set Irain 

   =1 in CONT�DAT and Assign the RAIN�DAT File

   300

   A Channel/Street Courant Number is Required in TOLER�DAT

   Set the correct Courant number�

   300

   If Istrflo in STREET�DAT is Set to 1,Then at Least One Inflow Node
   Must Have 

   a Street in It

   Check the STREET�DAT file�

   400

   Variable Tol Has an Inappropriate Value

   Check the TOL value�  It must be in a corect rangew�

   400

   Please Review If Tol = 0�05 Ft or 0�015 M With the Rainfall
   Abstraction

   Check the TOL variable and the Initial Abtraction variable�  The
   initial abstraction may 

   be too high�  See INFIL�DAT�

   500

   MANNINGS_N�DAT File Has a Mismatched Grid Element Number���Check 

   the End of this File

   The MANNINGS_N�DAT file might not be complete�

   500

   MANNINGS_N�DAT Files Does Not Exist� Create the File Before
   Proceeding

   Export MANINGS_N�DAT again�

   500

   The Spatially Variable Shallown Value is Outside the Range 0�010 to
   0�99

   Check the SPATIALSHALLOWN�DAT file�

   500

   N-Value is Less Than 0 or Greater Than 1

   Check the CONT�DAT file�

   600

   Line 2 in RAIN�DAT File Has to Be Reviewed For Spatially Variable
   Real Rain-

   fall Adjustments (Irainarf=1) With Rainarf Values

   Spatially variable data is missing�  Check RAIN�DAT�

   600

   Rtt must be Greater Than 0

   Check RAIN�DAT�

   600

   First Pair of the Rainfall Distribution Should Be 0� 0�

   Correct the first data pair of the rainfall distribution curve�  Set
   the first data pair to 0�0  

   0�0�

   600

   Date and Time in Raincell�Dat Must Have this Format: 06-15-2003
   14:00:00

   Check RAINCELL�DAT�

   700

   Variable Infmethod Line 1 in the INFIL�DAT is Either Missing or Not
   Cor-

   rectly Assigned

   Check INFIL�DAT�

   700

   To Use the Scs Curve Number Method For Infiltration You Must Have 

   Rainfall,Irain = 1 in CONT�DAT and RAIN�DAT File

   Check RAIN�DAT�

   700

   Variable Poros is Greater Than 1

   Check INFIL�DAT�

   700

   Variable Sati or Satf is Greater Than 1

   Check INFIL�DAT�

.. container::
   :name: page286-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328500285.png
   276

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.5.  BASIC ERROR CODES

   700

   Variable Rtimpf Exceeds 1�0� Do Not Enter As a Percent Use a Fraction

   Check INFIL�DAT�

   700

   Abstraction Exceeds the Total Rainfall (Impossible) For at Least One
   Grid Ele-

   ment and May Result in Volume Conservation Error

   Check spatial abstraction variable in INFIL�DAT�

   700

   Initial Abstraction > Tol (Depression Storage)� Consider (Not
   Required) Low-

   ering the Tol Value or Adjusting the Ia Value

   The TOL variable and IA variable can be summed to account for the
   initial abstraction�

   800

   There are Two Inflow Conditions Imposed at the Same Cell

   A cell is listed twice in INFLOW�DAT�  Check the file and remove one
   of the hydrgraphs�

   800

   This Grid Cell Has an Inflow and a Full ARF

   Reposition the inflow node�

   800

   This Grid Cell Has an Inflow and a Partial ARF

   Consider repositioning the inflow node�

   800

   The Following Cell Has an Inflow and a Hs

   Repostion the inflow node or the hydraulic structure inlet node�

   800

   The Following Cell Has an Inflow Fp on a Channel Left Bank Element

   Consider changing the inflow to channel inflow�

   800

   The Following Cell Has an Inflow Fp on a Channel Right Bank Element

   Consider moving the inflow node to the left bank and changing it to a
   channel node�

   800

   There are an Inflow Conditions Imposed on a Levee Element

   Check the levee Inflow condition�  Make sure the inflow is on the
   correct side of the levee 

   and make sure the cell elevtion is set correctly�

   800

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Reposition the inflow node�

   800

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Reposition the inflow node�

   800

   There are Two Inflow Conditions Imposed at the Same Cell

   A cell is listed twice in INFLOW�DAT�  Check the file and remove one
   of the hydrgraphs�

   800

   The Following Cell Has an Inflow Ch on a Channel Right Bank Element

   Move the inflow node to the left bank�

   800

   There are an Inflow Conditions Imposed on a Levee Element

   Check the levee Inflow condition�  Make sure the inflow is on the
   correct side of the levee 

   and make sure the cell elevtion is set correctly�

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Remove the extra line in OUTFLOW�DAT�

   800

   The Following Cell Has a Channel Outflow on a Channel Rigth Bank
   Element

   Move the outflow node left bank�

   800

   There are an Outflow Conditions Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Move the outflow node left bank�

   800

   The Following Cell Has an Outflow (Fp) on a Channel Left Bank or
   Rigth Bank 

   Element:

   It's OK for n FP outflow node to be on a left bank but not a right
   bank�

   800

   There is an Outflow Conditions Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are Two Stage Time Relationships Imposed at the Same Cell

   Remove one of the duplicate stage time conditions from OUTFLOW�DAT�

.. container::
   :name: page287-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328600286.png
   277

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.5.  BASIC ERROR CODES

   700

   Variable Rtimpf Exceeds 1�0� Do Not Enter As a Percent Use a Fraction

   Check INFIL�DAT�

   700

   Abstraction Exceeds the Total Rainfall (Impossible) For at Least One
   Grid Ele-

   ment and May Result in Volume Conservation Error

   Check spatial abstraction variable in INFIL�DAT�

   700

   Initial Abstraction > Tol (Depression Storage)� Consider (Not
   Required) Low-

   ering the Tol Value or Adjusting the Ia Value

   The TOL variable and IA variable can be summed to account for the
   initial abstraction�

   800

   There are Two Inflow Conditions Imposed at the Same Cell

   A cell is listed twice in INFLOW�DAT�  Check the file and remove one
   of the hydrgraphs�

   800

   This Grid Cell Has an Inflow and a Full ARF

   Reposition the inflow node�

   800

   This Grid Cell Has an Inflow and a Partial ARF

   Consider repositioning the inflow node�

   800

   The Following Cell Has an Inflow and a Hs

   Repostion the inflow node or the hydraulic structure inlet node�

   800

   The Following Cell Has an Inflow Fp on a Channel Left Bank Element

   Consider changing the inflow to channel inflow�

   800

   The Following Cell Has an Inflow Fp on a Channel Right Bank Element

   Consider moving the inflow node to the left bank and changing it to a
   channel node�

   800

   There are an Inflow Conditions Imposed on a Levee Element

   Check the levee Inflow condition�  Make sure the inflow is on the
   correct side of the levee 

   and make sure the cell elevtion is set correctly�

   800

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Reposition the inflow node�

   800

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Reposition the inflow node�

   800

   There are Two Inflow Conditions Imposed at the Same Cell

   A cell is listed twice in INFLOW�DAT�  Check the file and remove one
   of the hydrgraphs�

   800

   The Following Cell Has an Inflow Ch on a Channel Right Bank Element

   Move the inflow node to the left bank�

   800

   There are an Inflow Conditions Imposed on a Levee Element

   Check the levee Inflow condition�  Make sure the inflow is on the
   correct side of the levee 

   and make sure the cell elevtion is set correctly�

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Remove the extra line in OUTFLOW�DAT�

   800

   The Following Cell Has a Channel Outflow on a Channel Rigth Bank
   Element

   Move the outflow node left bank�

   800

   There are an Outflow Conditions Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Move the outflow node left bank�

   800

   The Following Cell Has an Outflow (Fp) on a Channel Left Bank or
   Rigth Bank 

   Element:

   It's OK for n FP outflow node to be on a left bank but not a right
   bank�

   800

   There is an Outflow Conditions Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are Two Stage Time Relationships Imposed at the Same Cell

   Remove one of the duplicate stage time conditions from OUTFLOW�DAT�

.. container::
   :name: page288-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328700287.png
   278

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.5.  BASIC ERROR CODES

   800

   The Following Cell Has Stage Time Relationship on a Channel Right
   Bank Ele-

   ment:

   Remove the ouflow from the right bank�

   800

   There are a Stage Time Outflow Condition Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are a Stage Time Relationship Imposed on an Outflow Cell

   800

   There are a Floodplain Outflow and a Stage Time Relationship at the
   Same Cell

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Delete one of the outflow nodes in OUTFLOW�DAT�

   800

   This Grid Cell Has an Outflow and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has an Outflow and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   This Grid Cell Has a Stage Time Relationship and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has a Stage Time Relationship and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   This Grid Cell Has an Outflow and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has an Outflow and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   An Inflow Hydrograph Has Been Assigned to a Channel Element (C-Line 

   in INFLOW�DAT) and There is No Channel Component (Ichannel = 0 in 

   CONT�DAT)

   Turn the channel switch on or reset the inflow node to floodplain�

   800

   First Pair of the Floodplain Hydrograph Should Be 0� 0� to
   Interpolate the First 

   Timestep

   Set the first data pair to 0�0 0�0 in the INFLOW�DAT�

   800

   No Inflow Discharge Specified For the Inflow Element

   Check INFLOW�DAT�

   800

   INFLOW�DAT Variable Ideplt must be an Inflow Node and an Inflow Node 

   - Khin - Variable in INFLOW�DAT must be Specified, CONT�DAT Variable 

   Inplot must be Set to 1

   To run in display mode, set the graphics mode in CONT�DAT and the
   plotting hydro-

   graph in INFLOW�DAT�

.. container::
   :name: page289-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328800288.png
   279

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.5.  BASIC ERROR CODES

   800

   The Following Cell Has Stage Time Relationship on a Channel Right
   Bank Ele-

   ment:

   Remove the ouflow from the right bank�

   800

   There are a Stage Time Outflow Condition Imposed on a Levee Element

   Make sure the outflow node is on the correct side of the levee�

   800

   There are a Stage Time Relationship Imposed on an Outflow Cell

   800

   There are a Floodplain Outflow and a Stage Time Relationship at the
   Same Cell

   800

   There are Two Outflow Conditions Imposed at the Same Cell

   Delete one of the outflow nodes in OUTFLOW�DAT�

   800

   This Grid Cell Has an Outflow and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has an Outflow and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   This Grid Cell Has a Stage Time Relationship and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has a Stage Time Relationship and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   This Grid Cell Has an Outflow and a Full ARF

   Delete the outflow node or the ARF�

   800

   This Grid Cell Has an Outflow and a Partial ARF

   Delete the ARF�

   800

   The Following Cell Has an Outflow and a WRF:

   Delete the WRF�

   800

   An Inflow Hydrograph Has Been Assigned to a Channel Element (C-Line 

   in INFLOW�DAT) and There is No Channel Component (Ichannel = 0 in 

   CONT�DAT)

   Turn the channel switch on or reset the inflow node to floodplain�

   800

   First Pair of the Floodplain Hydrograph Should Be 0� 0� to
   Interpolate the First 

   Timestep

   Set the first data pair to 0�0 0�0 in the INFLOW�DAT�

   800

   No Inflow Discharge Specified For the Inflow Element

   Check INFLOW�DAT�

   800

   INFLOW�DAT Variable Ideplt must be an Inflow Node and an Inflow Node 

   - Khin - Variable in INFLOW�DAT must be Specified, CONT�DAT Variable 

   Inplot must be Set to 1

   To run in display mode, set the graphics mode in CONT�DAT and the
   plotting hydro-

   graph in INFLOW�DAT�

.. container::
   :name: page290-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202328900289.png
   280

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   1000

   Inflow Fp on a Ch Interior Element

   Move inflow node or realign channel�

   1000

   Inflow Ch on a Ch Interior Element

   Move inflow node or realign channel�

   1000

   Outflow Ch on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Outflow Fp on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Stage Time Relationship on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Full ARF on a Ch Interior Element

   Delete ARF or realign channel�

   1000

   Partial ARF on a Ch Interior Element

   Delete ARF or realign channel�

   1000

   WRF on a Ch Interior Element

   Delete WRF or realign channel�

   1000

   Hs inlet on a Ch Interior Element

   Move hydraulic structure or realign channel�

   1000

   Hs outlet on a Ch Interior Element

   Move hydraulic structure of realing channel�

   1000

   Levee on a Ch Interior Element

   Realign levee or realign channel�

   1000

   Multiple Channel on a Channel Interior Element

   Realign multiple channel�  See reference manual�

   1000

   Channel Width is Greater Than the Element Width� Channel Left and
   Right 

   Bank Elements Should Be Separated

   Realign right bank� Extend right bank way from left bank�

   1000

   Channel Grid Element Will Require Separate Left and Right Bank
   Elements

   Realign right bank�

   1000

   Channel Extension Exceeds the Grid System Boundary

   Realign right bank�

   1000

   Channel Element Extends Into Interior of the Channel Element Instead
   Ex-

   tend the Channel Into Another Bank Element

   Realign right bank�

   1000

   Channel Element is Repeated in the CHAN�DAT File� Each Channel Ele-

   ment Should Only Be Listed Once

   Eliminate one of the repeated channel elements�  Tributary and Split
   flows should connect 

   along adjacent banks�

   1000

   Channel Right Bank Elements Need Some Adjustment Due to the Channel 

   Width� Set Right Bank Either Closer or Farther Away from the Left
   Bank 

   Element

   Realign right bank�

   1000

   Remaining Floodplain Surface Area on the Channel Bank Elements Needs
   to 

   Be Larger For Left Bank Element

   Extend right bank away from left bank�

   1000

   Data Error���Check the Channel Elements in the CHAN�DAT Files

   Review CHAN�DAT�  Load project in PROFILES�EXE to troubleshoot�

   1000

   Channel Extension For Grid Element Extends Into Another Channel
   Element

   Ralign right bank�

.. container::
   :name: page291-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329000290.png
   281

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   1000

   Inflow Fp on a Ch Interior Element

   Move inflow node or realign channel�

   1000

   Inflow Ch on a Ch Interior Element

   Move inflow node or realign channel�

   1000

   Outflow Ch on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Outflow Fp on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Stage Time Relationship on a Ch Interior Element

   Move outflow node or realign channel�

   1000

   Full ARF on a Ch Interior Element

   Delete ARF or realign channel�

   1000

   Partial ARF on a Ch Interior Element

   Delete ARF or realign channel�

   1000

   WRF on a Ch Interior Element

   Delete WRF or realign channel�

   1000

   Hs inlet on a Ch Interior Element

   Move hydraulic structure or realign channel�

   1000

   Hs outlet on a Ch Interior Element

   Move hydraulic structure of realing channel�

   1000

   Levee on a Ch Interior Element

   Realign levee or realign channel�

   1000

   Multiple Channel on a Channel Interior Element

   Realign multiple channel�  See reference manual�

   1000

   Channel Width is Greater Than the Element Width� Channel Left and
   Right 

   Bank Elements Should Be Separated

   Realign right bank� Extend right bank way from left bank�

   1000

   Channel Grid Element Will Require Separate Left and Right Bank
   Elements

   Realign right bank�

   1000

   Channel Extension Exceeds the Grid System Boundary

   Realign right bank�

   1000

   Channel Element Extends Into Interior of the Channel Element Instead
   Ex-

   tend the Channel Into Another Bank Element

   Realign right bank�

   1000

   Channel Element is Repeated in the CHAN�DAT File� Each Channel Ele-

   ment Should Only Be Listed Once

   Eliminate one of the repeated channel elements�  Tributary and Split
   flows should connect 

   along adjacent banks�

   1000

   Channel Right Bank Elements Need Some Adjustment Due to the Channel 

   Width� Set Right Bank Either Closer or Farther Away from the Left
   Bank 

   Element

   Realign right bank�

   1000

   Remaining Floodplain Surface Area on the Channel Bank Elements Needs
   to 

   Be Larger For Left Bank Element

   Extend right bank away from left bank�

   1000

   Data Error���Check the Channel Elements in the CHAN�DAT Files

   Review CHAN�DAT�  Load project in PROFILES�EXE to troubleshoot�

   1000

   Channel Extension For Grid Element Extends Into Another Channel
   Element

   Ralign right bank�

.. container::
   :name: page292-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329100291.png
   282

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   1000

   Channel Confluence Element Does Not Have Enough Connections, or a 

   Channel Segment is Beginning or Ending at a Main Channel Confluence
   Ele-

   ment

   Review confluence elements�  The tributary or split channel may not
   be close enough to 

   the main channel banks�

   1000

   Channel Extends Past the Levee System, Please Review the CHANNEL�

   CHK File and Make the Necessary Corrections

   Realign the channel or the levee�

   1000

   Inflow Channel Element is not a Channel Element in CHAN�DAT

   Move inflow node to a left bank or reset the node to floodplain or
   turn the channel switch 

   on�

   1000

   Channel Outflow Node Must Have a Lower Bed Elevation Than the Con-

   tiguous Upstream Channel Element to Compute a Normal Depth Outflow 

   Condition

   Review the channel invert elevation and make the necessary correction
   so that theoutflow 

   node can calulate normal depth�  The outflow invert elevation must be
   lower than that of 

   the upstream node�

   1000

   Channel Outflow Variable - Kout - in the OUTFLOW�DAT File must be a 

   Channel Element in the CHAN�DAT File

   Move the outflow node to a left bank, reset the node to floodplain or
   turn the channel 

   switch on�

   2000

   This Grid Cell Has a Hs Inlet and a Full ARF

   Move the hydraulic structure node�

   2000

   This Grid Cell Has a Hs Outlet and a Full ARF

   Move the hydraulic structure node�

   2000

   This Grid Cell Has a Hs Inlet and a Partial ARF

   Move the hydraulic structure node or reset the ARF to zero�

   2000

   This Grid Cell Has a Hs Outlet and a Partial ARF

   Move the hydraulic structure node or reset the ARF to zero�

   2000

   This Grid Cell Has a Hs on a Channel Rb Element

   Move the hydraulic structure to the left bank or change it to a
   floodplain structure�

   2000

   Inlet on a Full ARF Element

   Move Inlet

   2000

   Hydraulic Structure Has an Adverse Bed Slope� Outlet Invert is Higher
   Than 

   the Inlet Invert� Please Check to Ensure this is Correct

   Review inver elevations�  Apply elevation corrections if necessary� 
   Validate structure direc-

   tion�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inlet 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Has an Inflow or Outflow Element that is Not a
   Channel

   Move inlet node to the channel bank or change it to a floodplain
   structure�

   2000

   Hydraulic Structure Has a Name Length Longer Than 30 Characters� 

   Shorten the Name to Less Than 30 Characters

   2000

   A Hydraulic Structure Has Been Assigned to a Channel Element� 
   Channel is 

   turned off�

   (Ifporchan > 0 line S in HYSTRUC�DAT) and there is no channel
   component (Ichannel 

   = 0 in CONT�DAT)�  Turn on channel switch� 

   2000

   Hydraulic Structure Rating Curve, Rating Table, Or Generalized
   Culvert 

   Switch (Icurvtable) Does Not Match the Assigned Data

   Review HYSTRUC�DAT and set the switch to the correct position to
   match the assigned 

   data�

.. container::
   :name: page293-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329200292.png
   283

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   1000

   Channel Confluence Element Does Not Have Enough Connections, or a 

   Channel Segment is Beginning or Ending at a Main Channel Confluence
   Ele-

   ment

   Review confluence elements�  The tributary or split channel may not
   be close enough to 

   the main channel banks�

   1000

   Channel Extends Past the Levee System, Please Review the CHANNEL�

   CHK File and Make the Necessary Corrections

   Realign the channel or the levee�

   1000

   Inflow Channel Element is not a Channel Element in CHAN�DAT

   Move inflow node to a left bank or reset the node to floodplain or
   turn the channel switch 

   on�

   1000

   Channel Outflow Node Must Have a Lower Bed Elevation Than the Con-

   tiguous Upstream Channel Element to Compute a Normal Depth Outflow 

   Condition

   Review the channel invert elevation and make the necessary correction
   so that theoutflow 

   node can calulate normal depth�  The outflow invert elevation must be
   lower than that of 

   the upstream node�

   1000

   Channel Outflow Variable - Kout - in the OUTFLOW�DAT File must be a 

   Channel Element in the CHAN�DAT File

   Move the outflow node to a left bank, reset the node to floodplain or
   turn the channel 

   switch on�

   2000

   This Grid Cell Has a Hs Inlet and a Full ARF

   Move the hydraulic structure node�

   2000

   This Grid Cell Has a Hs Outlet and a Full ARF

   Move the hydraulic structure node�

   2000

   This Grid Cell Has a Hs Inlet and a Partial ARF

   Move the hydraulic structure node or reset the ARF to zero�

   2000

   This Grid Cell Has a Hs Outlet and a Partial ARF

   Move the hydraulic structure node or reset the ARF to zero�

   2000

   This Grid Cell Has a Hs on a Channel Rb Element

   Move the hydraulic structure to the left bank or change it to a
   floodplain structure�

   2000

   Inlet on a Full ARF Element

   Move Inlet

   2000

   Hydraulic Structure Has an Adverse Bed Slope� Outlet Invert is Higher
   Than 

   the Inlet Invert� Please Check to Ensure this is Correct

   Review inver elevations�  Apply elevation corrections if necessary� 
   Validate structure direc-

   tion�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inlet 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Has an Inflow or Outflow Element that is Not a
   Channel

   Move inlet node to the channel bank or change it to a floodplain
   structure�

   2000

   Hydraulic Structure Has a Name Length Longer Than 30 Characters� 

   Shorten the Name to Less Than 30 Characters

   2000

   A Hydraulic Structure Has Been Assigned to a Channel Element� 
   Channel is 

   turned off�

   (Ifporchan > 0 line S in HYSTRUC�DAT) and there is no channel
   component (Ichannel 

   = 0 in CONT�DAT)�  Turn on channel switch� 

   2000

   Hydraulic Structure Rating Curve, Rating Table, Or Generalized
   Culvert 

   Switch (Icurvtable) Does Not Match the Assigned Data

   Review HYSTRUC�DAT and set the switch to the correct position to
   match the assigned 

   data�

.. container::
   :name: page294-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329300293.png
   284

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   2000

   Hydraulic Structure must have a Culvert Area Coefficient and Exponent
   For 

   Routing in a Long Culvert�

   The clength and cdiameter was assigned,  assign the culvert area
   coefficient and exponent 

   so FLO-2D can simulate the culvert volume and travel time�

   2000

   Make Sure that the "Atable" Variable on Line 4 of the HYSTRUC�DAT
   File is 

   Included

   This table is required if clength and cdiameter are used in a Rating
   Table structure�

   2000

   First Data Pair of a Hydraulic Structure Rating Table Should Be
   0� 0� to Inter-

   polate the Next Data Pair

   Reset first row of table data to 0�00  0�00�

   2000

   Hydraulic Structure Rating Curve Stage Must Increase With Increasing
   Dis-

   charge

   The rating curve data has an error�  Check the data so the discharge
   increases with increas-

   ing stage�

   2000

   Rate of Change in the Following Hydraulic Structure Rating Tables May
   Be 

   Unreasonable - Rate of Change = 10 Times Previous Stage Rate of
   Change

   Check the rating table�  It may require more data pairs or it may be
   incorrect�

   2000

   If the Generalized Culvert Equations are Being Used� The Inoutcont
   Tailwater 

   Control is Not Necessary� Set Inoutcont = 0

   Set inoutcont to 0�

   2000

   Culvert Length Must Assign in the S-Line of the HYSTRUC�DAT If the 

   Generalized Culvert Equations are Being Used

   Assign culvert length and depth in the S line�

   2000

   Hydraulic Structure Inflow Node is Repeated More Than Once

   Review HYSTRUC�DAT�  Make sure each inflow node is only listed once� 
   If two nodes 

   are near each other, separate them by a grid elment�

   2000

   Hydraulic Structure Outflow Node is Repeated More Than Once Without 

   Assigning a D-Line Conveyance Capacity Limitation�

   Review HYSTRUC�DAT�  Make sure each outflow node is only listed
   once�  If two nodes 

   are near each other, separate them by a grid elment�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inflow 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Channel Outflow must be a Channel Element

   Check the position of the outlet element or make sure the channel
   switch is on in CONT�

   DAT�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inflow 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Channel Inflow Element must be a Channel Element

   Check the position of the outlet element or make sure the channel
   switch is on in CONT�

   DAT�

   2000

   Hydraulic Structure Inflow Element Cannot Be a Grid System Outflow
   Ele-

   ment

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

.. container::
   :name: page295-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329400294.png
   285

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   2000

   Hydraulic Structure must have a Culvert Area Coefficient and Exponent
   For 

   Routing in a Long Culvert�

   The clength and cdiameter was assigned,  assign the culvert area
   coefficient and exponent 

   so FLO-2D can simulate the culvert volume and travel time�

   2000

   Make Sure that the "Atable" Variable on Line 4 of the HYSTRUC�DAT
   File is 

   Included

   This table is required if clength and cdiameter are used in a Rating
   Table structure�

   2000

   First Data Pair of a Hydraulic Structure Rating Table Should Be
   0� 0� to Inter-

   polate the Next Data Pair

   Reset first row of table data to 0�00  0�00�

   2000

   Hydraulic Structure Rating Curve Stage Must Increase With Increasing
   Dis-

   charge

   The rating curve data has an error�  Check the data so the discharge
   increases with increas-

   ing stage�

   2000

   Rate of Change in the Following Hydraulic Structure Rating Tables May
   Be 

   Unreasonable - Rate of Change = 10 Times Previous Stage Rate of
   Change

   Check the rating table�  It may require more data pairs or it may be
   incorrect�

   2000

   If the Generalized Culvert Equations are Being Used� The Inoutcont
   Tailwater 

   Control is Not Necessary� Set Inoutcont = 0

   Set inoutcont to 0�

   2000

   Culvert Length Must Assign in the S-Line of the HYSTRUC�DAT If the 

   Generalized Culvert Equations are Being Used

   Assign culvert length and depth in the S line�

   2000

   Hydraulic Structure Inflow Node is Repeated More Than Once

   Review HYSTRUC�DAT�  Make sure each inflow node is only listed once� 
   If two nodes 

   are near each other, separate them by a grid elment�

   2000

   Hydraulic Structure Outflow Node is Repeated More Than Once Without 

   Assigning a D-Line Conveyance Capacity Limitation�

   Review HYSTRUC�DAT�  Make sure each outflow node is only listed
   once�  If two nodes 

   are near each other, separate them by a grid elment�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inflow 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Channel Outflow must be a Channel Element

   Check the position of the outlet element or make sure the channel
   switch is on in CONT�

   DAT�

   2000

   Hydraulic Structure Has a Reference Elevation that is Lower Than the
   Inflow 

   Node Bed Elevation

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

   2000

   Hydraulic Structure Channel Inflow Element must be a Channel Element

   Check the position of the outlet element or make sure the channel
   switch is on in CONT�

   DAT�

   2000

   Hydraulic Structure Inflow Element Cannot Be a Grid System Outflow
   Ele-

   ment

   Correct invert elevation or correct head reference elevation or set
   head reference elevation 

   to zero�

.. container::
   :name: page296-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329500295.png
   286

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   2000

   Hydraulic Structure Outflow Element Cannot Be a Grid System Outflow
   Ele-

   ment

   Move the outlet element to a node that is adjacent to the outflow
   node�

   3000

   The Following Cell Has a Full ARF on a Channel Left or Right Bank
   Element

   Realign the channel or eliminate the ARF�

   3000

   The Following Cell Has a Partial ARF on a Channel Left or Right Bank
   Ele-

   ment

   Delete the ARF�

   3000

   Street on an Outfall Element

   I don't know how to fix this�

   3000

   Full ARF on a 1D Street

   Realign street or delete ARF�

   3000

   Partial ARF on a 1D Street

   Delete ARF�

   3000

   Hs Inlet on a 1D Street

   Move hydraulic structure or realign street�

   3000

   Hs Outlet on a 1D Street

   Move hydraulic structure or realign street�

   3000

   Multiple Channel on a 1D Street

   Reposition multiple channel nodes or realign street�

   3000

   Gutter on a 1D Street

   Delete gutter or delete street�

   3000

   Variable Strman is Less Than 0 or Greater Than 1

   Assign street Manning’s N correctly�

   3000

   Variable Istrflo is a Switch, Use Only 0 or 1

   Apply variable correctly�

   3000

   Variable Depx must be Greater Than 0

   Assing street depth�

   3000

   Variable Widst must be Greater Than 0

   Assign street width�

   3000

   Variable Igridn must be Greater Than 0

   Assing correct Manning’s n value�

   3000

   Grid Elements are Defined More Than Once (Street�Dat) For a Street
   Inter-

   section Within a Grid Element

   Delete one of the misassigned street elements�

   3000

   Street Elements (Street�Dat) are Missing Line "W" in the Street�Dat
   File

   W lines are necessary to define the street direction in the cell� 
   Assign them as shown in 

   Lesson 11�

   3000

   Variable Istdir must be Greater Than 0 and Less Than or Equal to 8

   Add correct street direction�

   3000

   Variable Widr must be Greater Than 0

   Correct street width�

   3000

   Grid Element ARF Values Were Adjusted

   See ARF�DAT for automatic correction list�   ARFs were reasigned 1�0
   to Eliminate the 

   Potential For Instability Related to Small Surface Area� These are
   Reported to the ARF\_

   Adjustment�Chk File

.. container::
   :name: page297-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329600296.png
   287

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   2000

   Hydraulic Structure Outflow Element Cannot Be a Grid System Outflow
   Ele-

   ment

   Move the outlet element to a node that is adjacent to the outflow
   node�

   3000

   The Following Cell Has a Full ARF on a Channel Left or Right Bank
   Element

   Realign the channel or eliminate the ARF�

   3000

   The Following Cell Has a Partial ARF on a Channel Left or Right Bank
   Ele-

   ment

   Delete the ARF�

   3000

   Street on an Outfall Element

   I don't know how to fix this�

   3000

   Full ARF on a 1D Street

   Realign street or delete ARF�

   3000

   Partial ARF on a 1D Street

   Delete ARF�

   3000

   Hs Inlet on a 1D Street

   Move hydraulic structure or realign street�

   3000

   Hs Outlet on a 1D Street

   Move hydraulic structure or realign street�

   3000

   Multiple Channel on a 1D Street

   Reposition multiple channel nodes or realign street�

   3000

   Gutter on a 1D Street

   Delete gutter or delete street�

   3000

   Variable Strman is Less Than 0 or Greater Than 1

   Assign street Manning’s N correctly�

   3000

   Variable Istrflo is a Switch, Use Only 0 or 1

   Apply variable correctly�

   3000

   Variable Depx must be Greater Than 0

   Assing street depth�

   3000

   Variable Widst must be Greater Than 0

   Assign street width�

   3000

   Variable Igridn must be Greater Than 0

   Assing correct Manning’s n value�

   3000

   Grid Elements are Defined More Than Once (Street�Dat) For a Street
   Inter-

   section Within a Grid Element

   Delete one of the misassigned street elements�

   3000

   Street Elements (Street�Dat) are Missing Line "W" in the Street�Dat
   File

   W lines are necessary to define the street direction in the cell� 
   Assign them as shown in 

   Lesson 11�

   3000

   Variable Istdir must be Greater Than 0 and Less Than or Equal to 8

   Add correct street direction�

   3000

   Variable Widr must be Greater Than 0

   Correct street width�

   3000

   Grid Element ARF Values Were Adjusted

   See ARF�DAT for automatic correction list�   ARFs were reasigned 1�0
   to Eliminate the 

   Potential For Instability Related to Small Surface Area� These are
   Reported to the ARF\_

   Adjustment�Chk File

.. container::
   :name: page298-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329700297.png
   288

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   3000

   Impervious Area Represented By the Rtimp Percentage is Less Than the
   ARF 

   Value For at Least One Grid Element

   Impervious area should represent the building blockage and any other
   potential impervous 

   area�  It should be at least the same as the ARF value�

   3000

   A Channel Element Has One or More Street Segments� Remove the Street 

   Segments from this Element

   Realign the street or channel�   Review aerial images to assign
   channel or street alignment�

   4000

   Inlet on a Full ARF Element

   Move Inlet�

   4000

   Inlet on a Partial ARF Element

   Move Inlet�

   4000

   Outfall on a Full ARF Element

   Move Outfall or delete ARF�

   4000

   Outfall on a Partial ARF Element

   Move Oufall or delete ARF�

   4000

   Outfall on a Levee Element

   Review outfall position�  Make sure it is on the correct side of the
   levee� Review elevation�

   4000

   Inlet on a Levee Element

   Make sure the inlet is on the correct side of the levee�  Check the
   elevation of the cell so 

   that it matches he rim elevaiton of the inlet or the invert elevation
   of the type 4�

   4000

   Duplicate Inlet on SWMMFLO�DAT

   Delete the repeated inlet�

   4000

   Inlet on an Outfall

   Reposition the inlet or the outfall�

   4000

   Outfall on an Outfall

   Repostion one of the outfall nodes�

   4000

   Channel Rb on a Inlet Element

   Move the inlet to the left bank�

   4000

   Channel Rb on an Outfall Element

   Move the outfall to the left bank�

   4000

   Multiple Channel on a Inlet Element

   Reposition the inlet or the multiple channel�

   4000

   Multiple Channel on an Outfall Element

   Reposition the outfall or the multiple channel�

   4000

   There is a Levee and a Storm Drain Inlet Assigned to Grid Cell

   Make sure the inlet is on the correct side of the levee�  Check the
   elevation of the cell so 

   that it matches he rim elevaiton of the inlet or the invert elevation
   of the type 4�

   4000

   There is a Storm Drain Inlet Assigned to Completely Blocked Grid Cell

   Move the inlet or delete the ARF�

   4000

   There is a Storm Drain Outfall Assigned to Completely Blocked Grid
   Cell

   Move the outfall or delete the ARF�

   4000

   There is a Hydraulic Structure and a Storm Drain Inlet Assigned to
   Grid Cell

   Repostion the hydraulic strucure or the inlet�

   4000

   Storm Drain Inlet Has Invert Elevation Errors� Please Check Invert
   Elevation 

   and Rim Elevation For Node

   Do you mean Max Depth?

   4000

   Curb Opening Height must be Greater Than Zero� Please Revise SWMMF-

   LO�DAT File

   Review SWMMFLOW�DAT�

.. container::
   :name: page299-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329800298.png
   289

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   3000

   Impervious Area Represented By the Rtimp Percentage is Less Than the
   ARF 

   Value For at Least One Grid Element

   Impervious area should represent the building blockage and any other
   potential impervous 

   area�  It should be at least the same as the ARF value�

   3000

   A Channel Element Has One or More Street Segments� Remove the Street 

   Segments from this Element

   Realign the street or channel�   Review aerial images to assign
   channel or street alignment�

   4000

   Inlet on a Full ARF Element

   Move Inlet�

   4000

   Inlet on a Partial ARF Element

   Move Inlet�

   4000

   Outfall on a Full ARF Element

   Move Outfall or delete ARF�

   4000

   Outfall on a Partial ARF Element

   Move Oufall or delete ARF�

   4000

   Outfall on a Levee Element

   Review outfall position�  Make sure it is on the correct side of the
   levee� Review elevation�

   4000

   Inlet on a Levee Element

   Make sure the inlet is on the correct side of the levee�  Check the
   elevation of the cell so 

   that it matches he rim elevaiton of the inlet or the invert elevation
   of the type 4�

   4000

   Duplicate Inlet on SWMMFLO�DAT

   Delete the repeated inlet�

   4000

   Inlet on an Outfall

   Reposition the inlet or the outfall�

   4000

   Outfall on an Outfall

   Repostion one of the outfall nodes�

   4000

   Channel Rb on a Inlet Element

   Move the inlet to the left bank�

   4000

   Channel Rb on an Outfall Element

   Move the outfall to the left bank�

   4000

   Multiple Channel on a Inlet Element

   Reposition the inlet or the multiple channel�

   4000

   Multiple Channel on an Outfall Element

   Reposition the outfall or the multiple channel�

   4000

   There is a Levee and a Storm Drain Inlet Assigned to Grid Cell

   Make sure the inlet is on the correct side of the levee�  Check the
   elevation of the cell so 

   that it matches he rim elevaiton of the inlet or the invert elevation
   of the type 4�

   4000

   There is a Storm Drain Inlet Assigned to Completely Blocked Grid Cell

   Move the inlet or delete the ARF�

   4000

   There is a Storm Drain Outfall Assigned to Completely Blocked Grid
   Cell

   Move the outfall or delete the ARF�

   4000

   There is a Hydraulic Structure and a Storm Drain Inlet Assigned to
   Grid Cell

   Repostion the hydraulic strucure or the inlet�

   4000

   Storm Drain Inlet Has Invert Elevation Errors� Please Check Invert
   Elevation 

   and Rim Elevation For Node

   Do you mean Max Depth?

   4000

   Curb Opening Height must be Greater Than Zero� Please Revise SWMMF-

   LO�DAT File

   Review SWMMFLOW�DAT�

.. container::
   :name: page300-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202329900299.png
   290

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   4000

   Length must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Height must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Typical Weir Drain Coefficient: Range 2�8 to 3�2

   Review SWMMFLOW�DAT�

   4000

   Width or Height must be Greater  Than Zero

   Review SWMMFLOW�DAT�

   4000

   Typical Weir Drain Coefficient: 2�3

   Review SWMMFLOW�DAT�

   4000

   Perimeter must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Area must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Surcharge Depth must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   There is a Conflict Between Inlets in the SWMMFLO�DAT File and Sub-

   catchments in the SWMM�INP,Features in Both Lists Need to Be in the
   Same 

   Order

   Check the order of the inlets and the subcatchments�

   4000

   Inlets in the SWMMFLO�DAT File must be Identical to the Listed
   Inlets 

   Junction Table of SWMM�INP File

   Check the order of the inlets in SWMMFLOW�DAT and SWMM�INP�

   4000

   Multiple Inlets Assigned to One Grid Cell

   Reposition the inlet or delete it if it is a repeated line�

   4000

   There is a Type 4 Inlet (Review SWMMFLO�DAT File) that is Missing
   the 

   Rating Table in the SWMMFLORT�DAT File

   Add the table to SWMMFLOWRT�DAT�

   4000

   There is an Inflow Node and a Storm Drain Inlet Assigned to Grid Cell

   Reposition the inflow node or the inlet�

   4000

   There is an Inflow Node and a Storm Drain Outfall Assigned to Grid
   Cell

   Reposition the inflow node or the outfall�

   4000

   There is an Outflow Node and a Storm Drain Inlet Assigned to Grid
   Cell

   Respostion the inlet�

   4000

   There is an Outflow Node and a Storm Drain Outfall Assigned to Grid
   Cell

   Reposition the outfall or delete the outlet�

   4000

   Storm Drain Outfall Nodes are in Channel Interior Elements, Re-Assign
   to 

   the Channel Elements in CHAN�DAT

   Reposition the nodes to the left bank or reassign then grid element
   in SWMMFLO�DAT�

   5000

   Cross Section Element Can Only Be Assigned Once in the FPXSEC�DAT 

   File� 

   Remove repeated grid elements in FPXSEC�DAT� If the Cross Section
   Includes the Chan-

   nel Use Only the Left Bank Channel Element in CHAN�DAT

   6000

   Variable Xconc Should Not Be Assigned If Mudflow With a Sediment Con-

   centration is Assigned to the Inflow Hydrograph

   Do not assign Xconc in CONT�DAT�

   6000

   No Sediment Data in the SED�DAT File

   Check the SED�DAT file�

.. container::
   :name: page301-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330000300.png
   291

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   4000

   Length must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Height must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Typical Weir Drain Coefficient: Range 2�8 to 3�2

   Review SWMMFLOW�DAT�

   4000

   Width or Height must be Greater  Than Zero

   Review SWMMFLOW�DAT�

   4000

   Typical Weir Drain Coefficient: 2�3

   Review SWMMFLOW�DAT�

   4000

   Perimeter must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Area must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   Surcharge Depth must be Greater Than Zero

   Review SWMMFLOW�DAT�

   4000

   There is a Conflict Between Inlets in the SWMMFLO�DAT File and Sub-

   catchments in the SWMM�INP,Features in Both Lists Need to Be in the
   Same 

   Order

   Check the order of the inlets and the subcatchments�

   4000

   Inlets in the SWMMFLO�DAT File must be Identical to the Listed
   Inlets 

   Junction Table of SWMM�INP File

   Check the order of the inlets in SWMMFLOW�DAT and SWMM�INP�

   4000

   Multiple Inlets Assigned to One Grid Cell

   Reposition the inlet or delete it if it is a repeated line�

   4000

   There is a Type 4 Inlet (Review SWMMFLO�DAT File) that is Missing
   the 

   Rating Table in the SWMMFLORT�DAT File

   Add the table to SWMMFLOWRT�DAT�

   4000

   There is an Inflow Node and a Storm Drain Inlet Assigned to Grid Cell

   Reposition the inflow node or the inlet�

   4000

   There is an Inflow Node and a Storm Drain Outfall Assigned to Grid
   Cell

   Reposition the inflow node or the outfall�

   4000

   There is an Outflow Node and a Storm Drain Inlet Assigned to Grid
   Cell

   Respostion the inlet�

   4000

   There is an Outflow Node and a Storm Drain Outfall Assigned to Grid
   Cell

   Reposition the outfall or delete the outlet�

   4000

   Storm Drain Outfall Nodes are in Channel Interior Elements, Re-Assign
   to 

   the Channel Elements in CHAN�DAT

   Reposition the nodes to the left bank or reassign then grid element
   in SWMMFLO�DAT�

   5000

   Cross Section Element Can Only Be Assigned Once in the FPXSEC�DAT 

   File� 

   Remove repeated grid elements in FPXSEC�DAT� If the Cross Section
   Includes the Chan-

   nel Use Only the Left Bank Channel Element in CHAN�DAT

   6000

   Variable Xconc Should Not Be Assigned If Mudflow With a Sediment Con-

   centration is Assigned to the Inflow Hydrograph

   Do not assign Xconc in CONT�DAT�

   6000

   No Sediment Data in the SED�DAT File

   Check the SED�DAT file�

.. container::
   :name: page302-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330100301.png
   292

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   6000

   Error in Line 1 (M-Line) of the SED�DAT File

   Check the SED�DAT file for missing or incorrect mudflow data�

   6000

   Dry Weight of Sediment is Zero in the SED�DAT File and Thus the
   Porosity 

   is Also Zero

   Set the Dry Weight variable in SED�DAT�

   6000

   Sediment Size Exceeds the Recommended Value For the Application of
   the 

   Yang Equation

   Check the sediment size fractions in SED�DAT�

   6000

   Error in Line 2 (S-Line) of the SED�DAT File

   Check the sediment transport data in SED�DAT�

   6000

   Error in Z-Line of the SED�DAT File

   Check the sediment transport equation, bed thickness or volumetric
   concentration�

   6000

   Error in P-Line of the SED�DAT File

   Check the sediment diameter and percentage�

   6000

   Error in D-Line of the SED�DAT File

   Check the debris basin volume and the debris grid element number�

   6000

   Scourdep Variable in SED�DAT Line E Should Be Positive (>0�)

   Check the scour depth�  

   6000

   Error in E-Line of the SED�DAT File

   Check the scour depth�  

   6000

   Error in R-Line of the SED�DAT File

   Check the grid element numbers or position in the rigid bed cells�

   6000

   Error in S-Line of the SED�DAT File

   Check the sediment supply coefficient and exponent�

   6000

   Error in N-Line of the SED�DAT File

   Check the size distribution for sediment supply�

   6000

   Isedn variable is incorrect�

   Isedn Variable Must Equal One of the Sediment Size Fraction Groups in
   SED�DAT that 

   is Associated With a Sediment Transport Equation� Do Not Assign Isedn
   to a Sediment 

   Transport Equation Number

   7000

   There are a Levee Element on a Complete Blocked Element

   Consider repositioning or deleting the levee�

   7000

   There are a Levee Element on a Partial Blocked Element

   Make sure the levee is on the correct side of the cell�

   7000

   There are a Levee Element With a WRF

   Make sure the levee and WRF relationship is correct�

   7000

   This Grid Cell Has a Hs Inlet on a Levee Element

   Make sure the hydralic structure is on the correct side of the
   levee� Review the grid ele-

   ment elevation so that the water can get to and from the structure
   inlet and outlet nodes�

   7000

   This Grid Cell Has a Hs Outlet on a Levee Element

   Make sure the hydralic structure is on the correct side of the
   levee� Review the grid ele-

   ment elevation so that the water can get to and from the structure
   inlet and outlet nodes�

   7000

   This Grid Cell Has Two Levees

   Delete the repeaded levee�

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

.. container::
   :name: page303-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330200302.png
   293

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   6000

   Error in Line 1 (M-Line) of the SED�DAT File

   Check the SED�DAT file for missing or incorrect mudflow data�

   6000

   Dry Weight of Sediment is Zero in the SED�DAT File and Thus the
   Porosity 

   is Also Zero

   Set the Dry Weight variable in SED�DAT�

   6000

   Sediment Size Exceeds the Recommended Value For the Application of
   the 

   Yang Equation

   Check the sediment size fractions in SED�DAT�

   6000

   Error in Line 2 (S-Line) of the SED�DAT File

   Check the sediment transport data in SED�DAT�

   6000

   Error in Z-Line of the SED�DAT File

   Check the sediment transport equation, bed thickness or volumetric
   concentration�

   6000

   Error in P-Line of the SED�DAT File

   Check the sediment diameter and percentage�

   6000

   Error in D-Line of the SED�DAT File

   Check the debris basin volume and the debris grid element number�

   6000

   Scourdep Variable in SED�DAT Line E Should Be Positive (>0�)

   Check the scour depth�  

   6000

   Error in E-Line of the SED�DAT File

   Check the scour depth�  

   6000

   Error in R-Line of the SED�DAT File

   Check the grid element numbers or position in the rigid bed cells�

   6000

   Error in S-Line of the SED�DAT File

   Check the sediment supply coefficient and exponent�

   6000

   Error in N-Line of the SED�DAT File

   Check the size distribution for sediment supply�

   6000

   Isedn variable is incorrect�

   Isedn Variable Must Equal One of the Sediment Size Fraction Groups in
   SED�DAT that 

   is Associated With a Sediment Transport Equation� Do Not Assign Isedn
   to a Sediment 

   Transport Equation Number

   7000

   There are a Levee Element on a Complete Blocked Element

   Consider repositioning or deleting the levee�

   7000

   There are a Levee Element on a Partial Blocked Element

   Make sure the levee is on the correct side of the cell�

   7000

   There are a Levee Element With a WRF

   Make sure the levee and WRF relationship is correct�

   7000

   This Grid Cell Has a Hs Inlet on a Levee Element

   Make sure the hydralic structure is on the correct side of the
   levee� Review the grid ele-

   ment elevation so that the water can get to and from the structure
   inlet and outlet nodes�

   7000

   This Grid Cell Has a Hs Outlet on a Levee Element

   Make sure the hydralic structure is on the correct side of the
   levee� Review the grid ele-

   ment elevation so that the water can get to and from the structure
   inlet and outlet nodes�

   7000

   This Grid Cell Has Two Levees

   Delete the repeaded levee�

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

.. container::
   :name: page304-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330300303.png
   294

   **c**

   **haPter**

   ** 7**

   **t**

   **rouble**

   ** s**

   **hootInG**

   Table 7.6.  ADVANCED ERROR CODES

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   Channel Lb Rb on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

   8000

   Channel Lb Rb on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

   8000

   Levee on a Multiple Channel Element

   Make sure the multiple channel is on the correct side of the levee�

   8000

   Multiple Channel Element on a Multiple Channel Element

   Delete one of the repeated lines in MULT�DAT�

   8000

   Levee on a Multiple Channel Element

   Make sure the multiple channel is on the correct side of the levee�

   8000

   Multiple Channel Element on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

.. container::
   :name: page305-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330400304.png
   295

   **D**

   **ata**

   ** I**

   **nPut**

   **T**

   **rouble**

   ** S**

   **hoo**

   **T**

   **ing**

   Table 7.6.  ADVANCED ERROR CODES

   8000

   This Grid Cell Has an Inflow on a Multiple Ch Element

   Move the inflow node�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   This Grid Cell Has a Full/Partial ARF or WRF on a Multiple Ch Element

   Remove the ARF/WRF�

   8000

   Channel Lb Rb on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

   8000

   Channel Lb Rb on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

   8000

   Levee on a Multiple Channel Element

   Make sure the multiple channel is on the correct side of the levee�

   8000

   Multiple Channel Element on a Multiple Channel Element

   Delete one of the repeated lines in MULT�DAT�

   8000

   Levee on a Multiple Channel Element

   Make sure the multiple channel is on the correct side of the levee�

   8000

   Multiple Channel Element on a Multiple Channel Element

   A multiple channel cannot be assigned to a bank element�  See
   reference manual�

.. container::
   :name: page306-div

   .. image:: ./img/Data_Input_Manual_PRO_2023/Data Input Manual PRO 202330500305.png

