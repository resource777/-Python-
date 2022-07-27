from datetime import datetime
import pandas as pd
import numpy as np

info = pd.read_csv("taxis.csv")

len = len(info)
info['boardingtime']=np.nan
for i in range(len):
    info['boardingtime'][i] = datetime.strptime(info['dropoff'][i],"%Y-%m-%d %H:%M:%S") - datetime.strptime(info['pickup'][i],"%Y-%m-%d %H:%M:%S")

print(info)
