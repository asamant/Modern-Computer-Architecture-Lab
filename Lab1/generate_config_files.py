import os
import errno
import xlrd

currentDirectory = os.getcwd()
try:
	os.makedirs('configurations')
except OSError as exc: #The exception raised should only be a "directory exists" one
	if exc.errno != errno.EEXIST:
		raise

#Directory where the generated configurations should be placed
rel_directory=os.path.join(currentDirectory, 'configurations')

#Parameter excel file filepath. The file name should be "CONFIGURATIONS.xls"
excel_filepath = ('CONFIGURATIONS.xls')

#workbook, sheet
wb = xlrd.open_workbook(excel_filepath)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0) 
  
# Extracting number of rows 
number_of_configurations = sheet.nrows

# Read in the file
with open('configuration_TEMPLATE.mm', 'r') as file :
  	filedata = file.read()

#Keys corresponding to the parameters, to be replaced in the generated configuration files
replaceKeys = ['ISSUE_WIDTH', 'MEM_LOAD', 'MEM_STORE', 'MEM_PFT', 'NUM_ALU', 'NUM_MPY', 'NUM_MEMORY', 'NUM_GPR', 'NUM_BR']

dict_col_index = {'ISSUE_WIDTH' : 0 }

for i in range(sheet.ncols):
	dict_col_index[sheet.cell_value(0,i)] = i

for i in range(1, number_of_configurations):
# Replace the target string
	filedata_config = filedata
	for key in replaceKeys:
		filedata_config = filedata_config.replace(key, str(int(sheet.cell_value(i, dict_col_index[key]))))
		with open('./configurations/configuration.mm', 'w') as file:
			file.write(filedata_config)