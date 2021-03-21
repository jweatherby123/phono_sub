import tools
import os

def DFTBp(input_file):
	print("Setting up DFTBp calculations...")

	tools.write_critic2(input_file)
	#Need to figure out how I'm gonna do th einput files, nmight be for another dya
	#make run a variable that can be used by the user
	run = True
	if run:
		run_dftbp()



def run_dftbp():
	print("Running DFTB+ calculation...")
	os.system("dftb+ > output")
