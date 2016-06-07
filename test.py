import os
import csv
from rmgpy.molecule.molecule import Molecule
from rmgpy.rmg.model import Species
from rmgpy.rmg.model import CoreEdgeReactionModel
from rmgpy.rmg.main import RMG
from rmgpy import settings
from rmgpy.data.rmg import RMGDatabase

rmg = RMG()
rmg.database = RMGDatabase()
path = os.path.join(settings['database.directory'])
rmg.database.loadThermo(os.path.join(path,'thermo'))
rmg.reactionModel = CoreEdgeReactionModel()
rmg.initialSpecies = []

delimiter = '\t'
JtoCal = 1.0/4.184
fw = open('output_thermo.txt','w')
fw.write('Name\tSMILES\tH298\tS298\t300 K\t400 K\t500 K\t600 K\t800 K\t1000 K\t1500 K\tComment\n')

count = 0
spc_name = []
spc_smi = []

reader = csv.reader(open('TestSet.csv', 'r'))
for row in reader:
    k, v = row
    mol = Molecule().fromSMILES(v)
	spc, isNew = rmg.reactionModel.makeNewSpecies(mol)
#	rmg.reactionModel.addSpeciesToEdge(spc)
#	rmg.initialSpecies.append(spc)
#	spc_smi.append(v)
#	spc_name.append(k)
#	print k
#	count +=1
#
#i = 0
#for spc in rmg.initialSpecies:
#	tdt = rmg.database.thermo.getThermoDataFromGroups(spc)
#	#print tdt.comment
#	tempstr = spc_name[i] + delimiter + spc_smi[i] + delimiter + str(tdt.H298.value*JtoCal) + delimiter + str(tdt.S298.value*JtoCal)
#	tempstr = tempstr + delimiter + str(tdt.Cpdata.value[0]*JtoCal) + delimiter + str(tdt.Cpdata.value[1]*JtoCal) + delimiter + str(tdt.Cpdata.value[2]*JtoCal)
#	tempstr = tempstr + delimiter + str(tdt.Cpdata.value[3]*JtoCal) + delimiter + str(tdt.Cpdata.value[4]*JtoCal) + delimiter + str(tdt.Cpdata.value[5]*JtoCal)
#	tempstr = tempstr + delimiter + str(tdt.Cpdata.value[6]*JtoCal) + delimiter + tdt.comment + '\n'
#	fw.write( tempstr )
#	i +=1
#
#fw.close()
#
