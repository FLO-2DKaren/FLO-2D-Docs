.. _export_multiple_domains:

Export Multiple Domains
========================

.. image:: ../../img/Export-Multiple-Domains/expmultdom001.png

This tool will export the \*.DAT files for selected or all subdomains. Once the multiple domains have been created and schematized use this button to export the domains.


.. image:: ../../img/Export-Multiple-Domains/expmultdom003.png

The export process has many options that are outlined below.

Method 1 - Export using MULTDOMAIN.DAT
-------------------------------------------

Method 1 is the preferred method for exporting subdomains because it uses the simplified MULTDOMAIN.DAT connectivity file. Using the MULTDOMAIN.DAT method eliminates the need to export CADPTS_DSxx.DAT and eliminates the need to 
create complex Boundary Conditions (BCs) for each subdomain. The MULTDOMAIN.DAT file contains the connectivity for all subdomains in a single file.



1. Click the
Export multiple domains button and select the MULTDOMAIN.DAT method.

.. image:: ../../img/Export-Multiple-Domains/expmultdom005.png

2. Select the folder to export the domains.  The folder will contain the \*.DAT files and if needed the MULTDOMAIN.DAT file.

.. image:: ../../img/Export-Multiple-Domains/expmultdom005a.png

Method 2 - Export using ONLY MULTDOMAIN.DAT
---------------------------------------------

Use this method to export ONLY MULTDOMAIN.DAT file.  This allows the end user to review the MULTDOMAIN.DAT file without exporting the subdomains. 

1. Click the
   Export Only MULDOMAIN.DAT button

.. image:: ../../img/Export-Multiple-Domains/expmultdom009.png

2. Select the folder to export the domains.  Notice that the folder will only contain the MULTDOMAIN.DAT files if applicable.

.. image:: ../../img/Export-Multiple-Domains/expmultdom009a.png

Method 3 - Export using CADPTS.DAT
---------------------------------------------

This method will export the CADPTS_DSxx.DAT file for each subdomain.  
This method is useful if the user wants to export the subdomains using the **LEGACY multiple domain method**.  That method requires a 
CADPTS.DAT of downstream connected domains and an OUTFLOW.DAT with connecting Boundary Conditions for each upstream subdomain.

1. Click the
   Export CADPTS.DAT button.  

.. image:: ../../img/Export-Multiple-Domains/expmultdom006.png

2. Select the folder to export the domains.  Note the CADPTS_DSxx.DAT files will be exported to the selected folder.

3. Note that the OUTFLOW.DAT files are also exported with the correct upstream Boundary Conditions for each subdomain.

.. image:: ../../img/Export-Multiple-Domains/expmultdom006a.png

Method 4 - Export using ONLY CADPTS.DAT
---------------------------------------------
This method will export the CADPTS_DSxx.DAT file for each subdomain.
This method is useful if the user wants to review the CADPTS_DSxx.DAT files without exporting the subdomains.

1. Click the
   Export Only CADPTS button

.. image:: ../../img/Export-Multiple-Domains/expmultdom007.png

2. Select the folder to export the domains.

.. image:: ../../img/Export-Multiple-Domains/expmultdom007a.png

Method 5 - Export using No Connectivity
---------------------------------------------

This method will export the subdomains without any connectivity information. This is useful for exporting subdomains so that 2D or 1D 
data files can be reviewed without the need for connectivity information.  

1. Click the
   Export No Connectivity button

.. image:: ../../img/Export-Multiple-Domains/expmultdom008.png

2. Select the folder to export the domains.

.. image:: ../../img/Export-Multiple-Domains/expmultdom008a.png