import pandas as pd
"""
Test=pd.read_csv('Data_txt.txt',)
print(Test.head(10))
print('------------------------------------------')
"""
ruta="./"
tabla=pd.read_csv(ruta+'Data_Asignacion_X.csv',sep=',',encoding='utf-8')
print(tabla)
print('------------------------------------------')
print(tabla.info())
print('------------------------------------------')
print(tabla[['Nom_Territorio','Cantidad']].groupby('Nom_Territorio').describe())
print('------------------------------------------')
print(tabla['Nom_Territorio'].value_counts())
print('------------------------------------------')
filtro=tabla[tabla['Nom_Territorio']=='CAQUETA']
print(filtro.head())
print('------------------------------------------')
filtro=tabla[(tabla['Nom_Territorio']=='CAQUETA') & (tabla['Cantidad']>300)]
print(filtro.head())
print('------------------------------------------')

filtro=tabla.query("Nom_Territorio == 'CAQUETA'").query("Cantidad > 300").head()
print(filtro.head())
print('------------------------------------------')

filtro=tabla.loc[(tabla['Nom_Territorio']== 'CAQUETA') & (tabla['Cantidad']>300), :].head()
print(filtro.head())
print('------------------------------------------')
print(filtro.describe())
print('------------------------------------------')
filtro.to_csv('Data_filtrada_24-05-2024.csv',sep=',',index=False)
filtro.to_parquet('Data_filtrada_24-05-2024.parquet')
print('------------------------------------------')
