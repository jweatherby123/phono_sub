#!/usr/bin/env python3.8
 
import header
import codes
import argparse as arg
import os
import time

def main():
	intro_text(version)
	start_time = start_up()
	user_file = get_input()
	code = get_code()
	select_code(code,user_file)
	final(start_time)
	


def intro_text(version):
	header.header(version)
	header.things_im_working_on()

def start_up():
	start_time = time.time()
	return start_time
	


def get_input():
	#I'll need to get this working
	parser = arg.ArgumentParser()
	parser.add_argument("--input","-i", help="User-specified input file")
	parser.parse_args()

	
	print("Using CIF file in directory")
	print("")
	
	n = 0
	for file in os.listdir():
		if n == 2:
			print("There is more than one CIF file present.")
			print("Please either specify the file you want with the -i flag or remove one from the \
current directory")
			exit()
		if file.endswith(".cif"):
			n = n + 1
			user_file = file


	print("Input file is: " + user_file)
	print("")

	return user_file


def get_code():

#Can either define user_file from input -i or found one automatically
	
	supp_codes = { "D":"DFTBp", "Q":"QE", "C":"CRYSTAL17" }
	not_implemented = ["Q","C"]
	print("Please choose which code you would like to use.")
	print("DFTB+ [D] | QE [Q] | CRYSTAL17 [C]")
	
	code_user_input = input("")
	while code_user_input not in ["D", "Q", "C"]:
		print("You've selected an invalid option. Please try again.")
		print("")
		code_user_input = input("")

	if code_user_input in not_implemented:
		print("That code is not yet implemented, sorry.")
		print("Exiting...")
		exit()

	print("Selected " + supp_codes[code_user_input])
	return supp_codes[code_user_input] 


def select_code(code,input_file):
	if code == "DFTBp":
		codes.DFTBp(input_file) 
	elif code == "QE":
		codes.QE(input_file)
	elif codes == "CRYSTAL17":
		codes.CRYSTAL(input_file)

def final(start_time):
	final_time = time.time() - start_time
	print("Job finished successfully!")
	print("Finished in " + str(round(final_time,2)) + "s.") 

	



version = 0.2

if __name__ == "__main__":
 main()
