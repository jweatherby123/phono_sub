import os

def write_critic2(input_file):
	with open("cri", "w") as f:
		f.write("crystal " + str(input_file) + "\n")
		f.write("newcell primitive\n")
		f.write("write dftb_in.hsd\n")
			
	os.system("critic2 < cri > cro")
	os.remove("cri")
	os.remove("cro")
		
	
