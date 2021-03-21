import tools
import os

def DFTBp(input_file):
	print("Setting up DFTB+ calculation...")

	tools.write_critic2(input_file)
	tools.write_dftbp(forces="1E-5")

	run = True
	if run:
		run_dftbp()



def run_dftbp():
	print("Running DFTB+ calculation...")
	os.system("dftb+ > output")
