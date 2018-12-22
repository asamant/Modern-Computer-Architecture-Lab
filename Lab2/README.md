This directory consists of files relevant to the second lab assignment for the course "Modern Computer Architectures".

### Numbers extraction utility

The numbers extraction utility is a Python file used for extracting relevant numbers for area, performance, and energy usage corresponding to the simulations run.

It runs a series of regex matches over the files "area.txt", "performance.txt", and "energy.txt" and stores the extracted numbers in an Excel sheet (which is generated in the same directory as the aforementioned files). The .py file must be present in the same directory (/results) and has been tested with Python2.7

- Needs pip to be installed
- Needs xlsxwriter to create the Excel file

The Excel files are created in each of the /results directories when the .py file is run, and hence there is an Excel file per simulation. The numbers will have to be manually copied from the sheet and merged through Excel for comparison.
