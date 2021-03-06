# 从上下车点中获取在机场位置上下车的点
import pandas as pd
import os
start = []
end = []
fileNameU = "upA.csv"
fileNameD = "DOWNa.csv"
csv_dataU = pd.read_csv(fileNameU)
csv_dataD = pd.read_csv(fileNameD)

for j in range(1, csv_dataD.__len__() - 1):
    # print(csv_dataD.loc[j])
    if  csv_dataD['J'][j]<=121.81 and csv_dataD['J'][j]>=121.785 and csv_dataD['W'][j]<=31.159 and csv_dataD['W'][j]>=31.14:
        # print('------at airport------')
        start.append(csv_dataD.loc[j])
for j in range(1, csv_dataU.__len__() - 1):
    if   csv_dataU['J'][j]<=121.81 and csv_dataU['J'][j]>=121.785 and csv_dataU['W'][j]<=31.159 and csv_dataU['W'][j]>=31.14:
            end.append(csv_dataU.loc[j])
fileNameS = "DUresult/downAtAirport.csv"
fileNameE = "DUresult/upAtAirport.csv"
df = pd.DataFrame(start, columns=["ID", "status", "time", "J", "W"])
df.to_csv(fileNameS, index=False)
df = pd.DataFrame(end, columns=["ID", "status", "time", "J", "W"])
df.to_csv(fileNameE, index=False)
