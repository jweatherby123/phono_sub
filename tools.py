import os
from env import env_variables

def write_critic2(input_file):
	with open("cri", "w") as f:
		f.write("crystal " + str(input_file) + "\n")
		f.write("newcell primitive\n")
		f.write("write geo.gen\n")
			
	os.system("critic2 < cri > cro")
	os.remove("cri")
	os.remove("cro")
		
	
def write_dftbp(forces="1E-5"):
	atom_list = get_atom_list("geo.gen")
	hubbard_deriv = { "H":"-0.1857", "C":"-0.1492", "N":"-0.1535", "O":"-0.1575", "F":"-0.1623", "S":"-0.11", "P":"-0.14" } 
	angular_momentum_max = { "H":"s", "C":"p", "N":"p", "O":"p", "F":"p", "S":"d", "P":"d" }


	with open("dftb_in.hsd", "w") as f:
		f.write("Geometry = GenFormat {\n")
		f.write(" <<< \"geo.gen\"\n")
		f.write("}\n")
		f.write("\n")
		f.write("Driver = ConjugateGradient {\n")
		f.write(" MovedAtoms = 1:-1\n")
		f.write(" MaxForceComponent = " + str(forces) + "\n") #Check that DFTB+ can accept 0.001
		f.write(" MaxSteps = -1\n")
		f.write(" OutputPrefix = \"geom.out\"\n")
		f.write(" LatticeOpt = Yes\n")
		f.write("}\n")
		f.write("\n")
		f.write("Hamiltonian = DFTB {\n")
		f.write(" ThirdOrderFull = Yes\n")
		f.write(" Scc = Yes\n")
		f.write(" HubbardDerivs {\n")	
		for i in range(len(atom_list)):
			f.write("  " + str(atom_list[i]) + " = " + str(hubbard_deriv[atom_list[i]]) + "\n") 
		f.write(" }\n")
		f.write(" SlaterKosterFiles = Type2FileNames {\n")
		f.write("  Prefix = \"" + str(env_variables.sk_path) + "\"\n")
		f.write("  Separator = \"-\"\n")
		f.write("  Suffix = \".skf\"\n")
		f.write(" }\n")
		f.write(" MaxAngularMomentum {\n")
		for i in range(len(atom_list)):
			f.write("  " + str(atom_list[i]) + " = \"" + str(angular_momentum_max[atom_list[i]]) + "\"\n")
		f.write(" }\n")
		f.write(" Dispersion = DftD3 {\n")
		f.write(" Damping = BeckeJohnson {\n")
		f.write("  a1 = 0.746\n")
		f.write("  a2 = 4.191\n")
		f.write(" }\n")
		f.write("  s6 = 1.0\n")
		f.write("  s8 = 3.209\n")
		f.write(" }\n")
		f.write(" HCorrection = Damping {\n")
		f.write("  Exponent = 4.00\n")
		f.write(" }\n")
		f.write(" KPointsAndWeights = SupercellFolding {\n")
		f.write("  4   0   0\n")
		f.write("  0   4   0\n")
		f.write("  0   0   4\n")
		f.write("  0   0   0\n")
		f.write(" }\n")
		f.write("}\n")
		f.write("\n")
		f.write("Options {\n")
		f.write(" WriteResultsTag = Yes\n")
		f.write("}\n")
		f.write("\n")
		f.write("Analysis {\n")
		f.write(" CalculateForces = Yes\n")
		f.write("}\n")

def get_atom_list(file):
	atom_list = []
	with open(file, "r") as get_atom_file:
		lines = get_atom_file.readlines()
	
	atom_list = lines[1].split()

	return atom_list
