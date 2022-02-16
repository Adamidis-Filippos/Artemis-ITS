from Worker_informations import Worker
import pandas as pd
import numpy as np
import glob2

import pandas as pd
import numpy as np







path = r'C:\Users\santo\Desktop\Artemis ITS\Data'
filenames = glob2.glob(path+"/*.csv")

for filename in filenames:

    Xi = ["Weather","Driver+Operator","Pflasterstein","depth","direction changes", "cuts","damages","meters made"]
    df = pd.read_csv(filename, sep = ",", header =None,skiprows=1,names= Xi, index_col = False)

    weather = []
    Driver_Operator = []
    pflasterstein = []
    depth = []
    direction_changed = []
    cuts = []
    damages = []
    meters_made = []


    for i in df.index:
        weather.append(float(str(df['Weather'][i]).replace(",", ".")))
        Driver_Operator.append(float(str(df['Driver+Operator'][i]).replace(",", ".")))
        pflasterstein.append(float(str(df['Pflasterstein'][i]).replace(",", ".")))
        depth.append(float(str(df['depth'][i]).replace(",", ".")))
        direction_changed.append(float(str(df['direction changes'][i]).replace(",",".")))
        cuts.append(float(str(df["cuts"][i]).replace(",",".")))
        damages.append(float(str(df["damages"][i]).replace(",",".")))
        meters_made.append(float(str(df["meters made"][i]).replace(",",".")))

print(df)



