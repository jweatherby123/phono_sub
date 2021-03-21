#!/usr/bin/env python3.8
 
import header

def main():
	intro_text(version)
	start_up()


def intro_text(version):
	header.header(version)
	header.things_im_working_on()

def start_up():
	codes = { "D":"DFTB+", "Q":"QE", "C":"CRYSTAL17" }
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
		print("")
		exit()

	print("Selected " + codes[code_user_input])





version = 0.2

if __name__ == "__main__":
 main()
