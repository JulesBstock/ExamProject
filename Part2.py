import os
import glob
import pandas as pd
import numpy as np

path = "C:/Users/jules/Documents/M2/Python/ExamProject/Data"
allfiles = glob.glob(os.path.join(path,"*.csv"))


np_array_list = []
for file in allfiles:
    df = pd.read_csv(file, index_col=None)
    np_array_list.append(df.as_matrix())

comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)

print(big_frame)