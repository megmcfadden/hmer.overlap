from overlap import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

pairs= pd.read_table('tene_sub_filenames.txt')
print(pairs)
