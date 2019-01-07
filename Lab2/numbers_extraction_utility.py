# IF NEED BE, INCLUDE SHEBANG LINE CORRESPONDING TO THE INSTALLED PYTHON VERSION

# IMPORTS
import re
import xlsxwriter

#REGEX FOR MATCHING THE EXPRESSION FOR SLICE REGISTER COUNT; check group 3
slice_registers_regex = re.compile('(\s+)Number of occupied Slices:(\s+)((\d|,)*)(\s+)out of')

#REGEX FOR MATCHING THE EXPRESSION FOR SLICE LUT COUNT; check group 3
slice_LUTs_regex = re.compile('(\s+)Number of Slice LUTs:(\s+)((\d|,)*)(\s+)out of')                     

#REGEX FOR MATCHING THE EXPRESSION FOR RAMB36E1 COUNT; check group 3
ramb36_num_regex = re.compile('(\s+)Number of RAMB36E1/FIFO36E1s:(\s+)((\d|,)*)(\s+)out of')

#REGEX FOR MATCHING THE EXPRESSION FOR RAMB18E1 COUNT; check group 3
ramb18_num_regex = re.compile('(\s+)Number of RAMB18E1/FIFO18E1s:(\s+)((\d|,)*)(\s+)out of')

#REGEX FOR MATCHING THE EXPRESSION FOR DSP48E1s COUNT; check group 3
dsp_num_regex = re.compile('(\s+)Number of DSP48E1s:(\s+)((\d|,)*)(\s+)out of')

#REGEX FOR MATCHING THE EXPRESSION FOR THE AVERAGE CYCLE COUNT; check group 3
cycle_count_regex = re.compile('(\s*)Average:(\s+)(\d+)(\s+)cycles')

#REGEX FOR MATCHING THE EXPRESSION FOR THE ENERGY VALUE; check group 3
energy_regex = re.compile('(\s*)Average:(\s+)((\d|.)*)(\s+)mJ')

# OPEN THE FILE 'area.txt' AND MATCH STRINGS USING REGEX, LINE BY LINE
# IF MATCHES ARE FOUND, WE'VE RETRIEVED THE CORRESPONDING VALUES
# We're treating the values as strings since some of the numbers include commas or decimal points
dict_numbers = {"SLICE_REGS":"0", "SLICE_LUTs":"0", "RAMB36":"0", "RAMB18":"0", "DSP_NUM":"0", "AVG_CYCLE_NUM":"0", "AVG_ENERGY":"0"}

def get_area_numbers(filepath='area.txt'):
    with open(filepath, 'r') as file:
    	count = 0
        line = file.readline()
        while line:
            if slice_registers_regex.match(line):
                slice_registers_num = slice_registers_regex.match(line).group(3)
                dict_numbers["SLICE_REGS"] = slice_registers_num
                count+=1

            if slice_LUTs_regex.match(line):
                slice_LUTs_num = slice_LUTs_regex.match(line).group(3)
                dict_numbers["SLICE_LUTs"] = slice_LUTs_num
                count+=1

            if ramb36_num_regex.match(line):
                ramb36_num = ramb36_num_regex.match(line).group(3)
                dict_numbers["RAMB36"] = ramb36_num
                count+=1

            if ramb18_num_regex.match(line):
                ramb18_num = ramb18_num_regex.match(line).group(3)
                dict_numbers["RAMB18"] = ramb18_num
                count+=1

            if dsp_num_regex.match(line):
                dsp_num = dsp_num_regex.match(line).group(3)
                dict_numbers["DSP_NUM"] = dsp_num
                count+=1

            if count==5:
            	return dict_numbers

            line = file.readline()

def get_perf_numbers(filepath='performance.txt'):
    with open(filepath, 'r') as file:
        line = file.readline()
        while line:
            if cycle_count_regex.match(line):
                cycle_count = cycle_count_regex.match(line).group(3)
                dict_numbers["AVG_CYCLE_NUM"] = cycle_count
                return dict_numbers

            line = file.readline()

def get_energy_numbers(filepath='energy.txt'):
    with open(filepath, 'r') as file:
        line = file.readline()
        while line:
            if energy_regex.match(line):
                energy_value = energy_regex.match(line).group(3)
                dict_numbers["AVG_ENERGY"] = energy_value
                return dict_numbers

            line = file.readline()


# CALL THE METHODS FOR EXTRACTING THE RELEVANT NUMBERS
get_area_numbers()
get_perf_numbers()
get_energy_numbers()

#Overwrites "SIMULATION_RESULTS.xlsx" if it exists already, creates a new file otherwise
results_wb = xlsxwriter.Workbook('SIMULATION_RESULTS.xlsx')
results_sheet = results_wb.add_worksheet()

#Create first row of the results excel sheet with the column headers
cnt = 0
for key in dict_numbers:
    results_sheet.write(0, cnt, key)
    results_sheet.write(1, cnt, dict_numbers[key])
    cnt += 1

#CLOSE WORKBOOK
results_wb.close()
