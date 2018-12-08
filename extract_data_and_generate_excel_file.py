import os
import errno
import xlrd
import xlsxwriter 
import subprocess

#custom file
import performance_extractor

'''
currentDirectory = os.getcwd()
try:
	os.makedirs('configurations')
except OSError as exc: #The exception raised should only be a "directory exists" one
	if exc.errno != errno.EEXIST:
		raise
'''

#Parameter excel file filepath. The file name should be "CONFIGURATIONS.xls"
excel_filepath = ('CONFIGURATIONS.xls')

#configurations workbook, sheet
configurations_wb = xlrd.open_workbook(excel_filepath)
configurations_sheet = configurations_wb.sheet_by_index(0)
configurations_sheet.cell_value(0, 0) 
  
# Extracting number of rows 
number_of_configurations = configurations_sheet.nrows

# Read in the file
with open('configuration_TEMPLATE.mm', 'r') as file :
  	filedata = file.read()

#Keys corresponding to the parameters, to be replaced in the generated configuration files
replaceKeys = ['CONFIG_INDEX_NO', 'ISSUE_WIDTH', 'MEM_LOAD', 'MEM_STORE', 'MEM_PFT', 'NUM_ALU', 'NUM_MPY', 'NUM_MEMORY', 'NUM_GPR', 'NUM_BR']

dict_col_index = {'ISSUE_WIDTH' : 0 }

#Keys corresponding to columns in the simulation result excel sheet
resultDict = {'CONFIG_INDEX_NO':0 , 'MATRIX_EXEC_CYCLES':1, 'MATRIX_TRACE1':2, 'CONV_EXEC_CYCLES':3, 'CONV_TRACE1':4 }

results_wb = xlsxwriter.Workbook('PERF_RESULTS.xlsx')
results_sheet = results_wb.add_worksheet()
for key in resultDict:
	results_sheet.write(0, resultDict[key], key)

for i in range(configurations_sheet.ncols):
	dict_col_index[configurations_sheet.cell_value(0,i)] = i

for i in range(1, number_of_configurations):
	#GENERATE CONFIGURATION FILE PER ROW OF THE "CONFIGURATIONS.xls" SHEET
	generate_configuration_file(i)
	
	#CALL BASH FILE TO SIMULATE ARCHITECTURE
	subprocess.call(['./RUNMATRIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.sh'])
	configuration_index = configurations_sheet.cell_value(i, dict_col_index['CONFIG_INDEX_NO'])
	results_sheet.write(i, resultDict['CONFIG_INDEX_NO'], configuration_index)

	#GET EXECUTION CYCLES COUNT FROM THE GENERATED FILES "ta.log.000"
	matrix_exec_cycles = performance_extractor.get_execution_cycles_count('./output_matrix.c/ta.log.000')

	#GET TRACE 1'S INSTRUCTION COUNT
	matrix_trace1_instruction_count = performance_extractor.get_trace_1_value('./output_matrix.c/pcntl.txt')

	#WRITE RESULTS IN THE RESULTS EXCEL SHEET
	results_sheet.write(i, resultDict['MATRIX_EXEC_CYCLES'], matrix_exec_cycles)
	results_sheet.write(i, resultDict['MATRIX_TRACE1'], matrix_trace1_instruction_count)


	subprocess.call(['./CONVVVVVVVVVVVVVVVSSASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS.sh'])

	convolution3x3_exec_cycles = performance_extractor.get_execution_cycles_count('./output_convolution_3x3.c/ta.log.000')
	convolution3x3_trace1_instruction_count = performance_extractor.get_trace_1_value('./output_convolution_3x3.c/pcntl.txt')
	results_sheet.write(i, resultDict['CONV_EXEC_CYCLES'], convolution3x3_exec_cycles)
	results_sheet.write(i, resultDict['CONV_TRACE1'], convolution3x3_trace1_instruction_count)


#CLOSE WORKBOOKS
configurations_wb.release_resources()
del configurations_wb
results_wb.close()

# Replace the keys in the template file with the "index" row's key values
def generate_configuration_file(index):
	filedata_config = filedata
	
	for key in replaceKeys:
		filedata_config = filedata_config.replace(key, str(int(configurations_sheet.cell_value(i, dict_col_index[key]))))
	
	with open('configuration.mm', 'w') as file:
		file.write(filedata_config)

def write_to_results_file(index):