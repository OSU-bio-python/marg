'''
To prepare your data files to work with this script: 
(1) Open in Excel, delete all rows at the top save as a .csv file
Don't forget to move the file into the same directory as this script
The next three lines import some scripting tools that do not normally load with python
'''
print(__doc__)
import argparse


parser = argparse.ArgumentParser(description='Do training.')
parser.add_argument(
            '--pos_vecs_file',
            required=True,
            type=str,
            help='')

parser.add_argument(
            '--neg_vecs_file_set',
            required=True,
            type=str,
            help='')

parser.add_argument(
           '--out_base',
            type=str,
            help='')

parser.add_argument(
            '--k_folds',
            type=int,
            default=str,
            help='')

parser.add_argument(
            '--kernal',type=str,default="RBF",
             help='')

args = parser.parse_args()
pos_vecs_file     = args.pos_vecs_file



#from itertools import *
#from operator import *
#from decimal import *

#The next step may not be needed.
#Calling 'os' allows python to interact with your operating system and understand its organization.
#The script can now read files in directories.
#This is useful so you can process more than one of these files at once.
import os
#The next two lines determine where the script is stored and what files are stored with it.
#The script needs to be stored in a directory with your .csv files.
#The directory can contain other files, too, but none of those should be .csv files
directory = os.getcwd()
directory_list = os.listdir(directory)

#This is my dictionary
markersDict = {}
dict_csv_file_name = "input_dict.csv"
in_file_name  = "FLW_f2010_QTLstats.csv" 
out_file_name = "outputfile_1.csv"


for line in open(dict_csv_file_name,'r'):
    marker_number,marker_name = line.strip().split(",")
    assert not marker_number in markersDict, marker_number
    markersDict.update({marker_number:marker_name})
   

dataout = file(out_file_name,"w")
for line in open(in_file_name, "r" ):
        
    linelist = line.strip().split(",")
    linelist.append(markersDict[ linelist[2]+"_"+linelist[3]  ])
    linelist.append(markersDict[ linelist[2]+"_"+linelist[5]  ])        
    linelist.append(markersDict[ linelist[2]+"_"+linelist[8]  ])

    dataout.write(",".join(linelist)+"\n")  

dataout.close()

