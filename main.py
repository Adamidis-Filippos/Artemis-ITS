import pandas as pd
import numpy as np
import glob2
from sklearn import linear_model

import pandas as pd
import numpy as np







path = r'C:\Users\santo\Desktop\Artemis ITS\Data'
filenames = glob2.glob(path+"/*.csv")

for filename in filenames:

    Xi = ["Weather","Driver+Operator","Pflasterstein","depth","workers","changes in digging", "cuts", "damages", "meters made"]
    df = pd.read_csv(filename, sep = ",", header =None,skiprows=1,names= Xi, index_col = False)

    df = df.fillna(0)
    weather = []
    Driver_Operator = []
    pflasterstein = []
    depth = []
    workers = []
    changes_in_digging = []
    cuts = []
    damages = []
    meters_made = []


    for i in df.index:
        weather.append(float(str(df['Weather'][i]).replace(",", ".")))
        Driver_Operator.append(float(str(df['Driver+Operator'][i]).replace(",", ".")))
        pflasterstein.append(float(str(df['Pflasterstein'][i]).replace(",", ".")))
        depth.append(float(str(df['depth'][i]).replace(",", ".")))
        workers.append(float(str(df['workers'][i]).replace(",", ".")))
        changes_in_digging.append(float(str(df['changes in digging'][i]).replace(",", ".")))
        cuts.append(float(str(df["cuts"][i]).replace(",", ".")))
        damages.append(float(str(df["damages"][i]).replace(",", ".")))
        meters_made.append(float(str(df["meters made"][i]).replace(",", ".")))

        X = df.iloc[:, 1:7].values
        y = df.iloc[:, 8].values
    #np.array(list(zip(a,b)))
    features = np.array(list(zip(weather, Driver_Operator, pflasterstein, depth, workers, cuts, damages))) #  features
    label= np.array(list(meters_made))
    model = linear_model.LinearRegression()
    model.fit(features, label)


    print(model.coef_)
    print(model.intercept_)
    print(model.predict([[4,2,0,55,10,1,0]]))

    def input_features():
        kairos = input("Temperature this day")
        odhgos_xeirisths = input("Presence of Driver and operator")
        pavele = input("type of stein")
        vathos = input("depth this day")
        ergates = input("how many workers worked today?")
        tomes = input("how many cuts were made?")
        vlaves = input("how many cables were damages?")
        list_for_prediciton = np.array(list([kairos, odhgos_xeirisths, pavele, vathos, ergates, tomes, vlaves])).reshape(1,-1)
        return list_for_prediciton

    prediction = model.predict(input_features())
    print(prediction)
