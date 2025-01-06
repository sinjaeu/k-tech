import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# f1 = pd.read_csv('food1.csv')
# f2 = pd.read_csv('food2.csv')
# f3 = pd.read_csv('food3.csv')
# f4 = pd.read_csv('food4.csv')
# f5 = pd.read_csv('food5.csv')
# f6 = pd.read_csv('food6.csv')

# l1 = pd.read_csv('LOData1.csv')
# l2 = pd.read_csv('LOData2.csv')
# l3 = pd.read_csv('LOData3.csv')
# l4 = pd.read_csv('LOData4.csv')
# l5 = pd.read_csv('LOData5.csv')

# LOData = {}

# lof_2 = {}

# flag = True

# lo_cnt = 0

# cnt = 0

# fd = pd.concat([f1, f2, f3, f4, f5, f6], axis = 0, ignore_index = True)
# lod = pd.concat([l1, l2, l3, l4, l5], axis = 0, ignore_index = True)
# lod = lod.dropna().reset_index(drop = True)

# lo = fd['NGST_QY'].sum()

# lof = {}
# for i in range(len(fd['SE_ID'])):
#     if fd['SC_GRAD_VLUE'][i] not in lof:
#         lof[fd['SC_GRAD_VLUE'][i]] = fd['NGST_QY'][i]
#     else:
#         lof[fd['SC_GRAD_VLUE'][i]] += fd['NGST_QY'][i]

# for i in lof.keys():
#     lof_2[i] = lof[i]

# # DataFrame 생성: 사전의 키를 인덱스로 사용
# lof_2_df = pd.DataFrame.from_dict(lof_2, orient='index', columns=['Quantity']).reset_index()

# # 인덱스 열의 이름을 'Food'로 변경
# lof_2_df.rename(columns={'index': 'Food'}, inplace=True)

# # CSV 파일로 저장
# lof_2_df.to_csv('lof_2.csv', encoding='utf-8', index=False)

# for i in range(len(lod)):
#     if lod['FOOD_NM'][i] not in LOData:
#         LOData[lod['FOOD_NM'][i]] = [lod['FDINGR_NM'][i]]
#     else:
#         for j in LOData[lod['FOOD_NM'][i]]:
#             if lod['FDINGR_NM'][i] == j:
#                 flag = False
#                 break
#         if flag:
#             LOData[lod['FOOD_NM'][i]].append(lod['FDINGR_NM'][i])

LOD1 = pd.read_csv('LOData_1(수정).csv')
LOD2 = pd.read_csv('LOData_2(수정).csv')
LOD3 = pd.read_csv('LOData_3(수정).csv')

LOData = pd.concat([LOD1, LOD2, LOD3], ignore_index=True)

lof = pd.read_csv('lof_2.csv')
print(lof.info())

merged_data = pd.merge(LOData, lof, left_on='FOOD_NM', right_on='Food', how='left')

merged_data = merged_data.drop(columns=['Food'])
print(merged_data.info())

merged_data.to_csv('main_data.csv', encoding='utf-8', index=False)