import re

#REGEX FOR MATCHING THE EXPRESSION FOR EXECUTION CYCLE COUNT
exec_cycle_regex = re.compile('Execution Cycles: (\s+)(\d+) \((.*)\)\n')

#REGEX FOR EXTRACTING TRACE 1's DATA FROM THE THIRD TABLE
instruction_regex = re.compile('Execution Cycles: (\s+)1 (\s+)(\d+)(\s+)(\d+)(\s+)(\d+)(\s+)(\d+)\n')

filepath_execution_cycles = 'ta.log.000'
filepath_trace = 'pcntl.txt'

# OPEN THE FILE 'ta.log.000' AND MATCH STRINGS USING REGEX, LINE BY LINE
# IF A MATCH IS FOUND, WE'VE RETRIEVED THE NUMBER OF EXEC CYCLES
def get_execution_cycles_count(filepath='ta.log.000'):
    with open(filepath, 'r') as file:
        line = file.readline()
        while line:
            if exec_cycle_regex.match(line):
                exec_cycles_num = int(exec_cycle_regex.match(line).group(2))
                return exec_cycles_num

            line = file.readline()

#OPEN THE GENERATED FILE "pcntl.txt" AND ITERATE THROUGH ITS LINES
#THE SECOND COLUMN IN THE ROW CORRESPONDING TO TRACE 1 IS THE REQUIRED VALUE
#HACKHACK: WE KNOW THERE ARE THREE TABLES IN THE GENERATED FILE, AND HENCE THE COUNT COMPARISON
def get_trace_1_value(filepath='pcntl.txt'):
    with open(filepath, 'r') as file:
        line = file.readline()
        count = 0
        while line:
            if exec_cycle_regex.match(line):
                count++
                if (count==3)
                    instructions_num = int(instruction_regex.match(line).group(3))
                    return instructions_num

            line = file.readline()