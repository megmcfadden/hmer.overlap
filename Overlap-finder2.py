from overlap2 import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

in= pd.read_table('tene_sub_filenames_in.txt')
out=pd.read_table('tene')
pairs=list(zip(in,out))
print(pairs)


#find_hmer(pairs,'/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_2_sub.txt')
