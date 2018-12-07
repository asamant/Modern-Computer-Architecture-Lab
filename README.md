#README FOR THE MCA PROJECT FILES

#COMPONENTS

#1 EXCEL FILE CONTAINING CONFIGURATION PARAMETER INFORMATION

An excel file needs to be present in the root directory, and should have exactly one "Sheet" with the following format:

CONFIG_INDEX_NO		ISSUE_WIDTH		MEM_LOAD		MEM_STORE		MEM_PFT		NUM_ALU		NUM_MPY		NUM_MEMORY		NUM_GPR		NUM_BR

The data in each column must correspond to the respective configuration's parameters.
CONFIG_INDEX_NO should be at (1, A).

#