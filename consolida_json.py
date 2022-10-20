import requests
import os
import json
import time
import pandas as pd

arquivos = ['pesquisa_1.json',
'pesquisa_10.json',
'pesquisa_100.json',
'pesquisa_101.json',
'pesquisa_102.json',
'pesquisa_103.json',
'pesquisa_104.json',
'pesquisa_105.json',
'pesquisa_106.json',
'pesquisa_107.json',
'pesquisa_108.json',
'pesquisa_109.json',
'pesquisa_11.json',
'pesquisa_110.json',
'pesquisa_111.json',
'pesquisa_112.json',
'pesquisa_113.json',
'pesquisa_114.json',
'pesquisa_115.json',
'pesquisa_116.json',
'pesquisa_117.json',
'pesquisa_118.json',
'pesquisa_119.json',
'pesquisa_12.json',
'pesquisa_120.json',
'pesquisa_121.json',
'pesquisa_122.json',
'pesquisa_123.json',
'pesquisa_124.json',
'pesquisa_125.json',
'pesquisa_126.json',
'pesquisa_127.json',
'pesquisa_128.json',
'pesquisa_129.json',
'pesquisa_13.json',
'pesquisa_130.json',
'pesquisa_131.json',
'pesquisa_132.json',
'pesquisa_133.json',
'pesquisa_134.json',
'pesquisa_135.json',
'pesquisa_136.json',
'pesquisa_137.json',
'pesquisa_138.json',
'pesquisa_139.json',
'pesquisa_14.json',
'pesquisa_140.json',
'pesquisa_141.json',
'pesquisa_142.json',
'pesquisa_143.json',
'pesquisa_144.json',
'pesquisa_145.json',
'pesquisa_146.json',
'pesquisa_147.json',
'pesquisa_148.json',
'pesquisa_149.json',
'pesquisa_15.json',
'pesquisa_150.json',
'pesquisa_151.json',
'pesquisa_152.json',
'pesquisa_153.json',
'pesquisa_154.json',
'pesquisa_155.json',
'pesquisa_156.json',
'pesquisa_157.json',
'pesquisa_158.json',
'pesquisa_159.json',
'pesquisa_16.json',
'pesquisa_160.json',
'pesquisa_161.json',
'pesquisa_162.json',
'pesquisa_163.json',
'pesquisa_164.json',
'pesquisa_165.json',
'pesquisa_166.json',
'pesquisa_167.json',
'pesquisa_168.json',
'pesquisa_169.json',
'pesquisa_17.json',
'pesquisa_170.json',
'pesquisa_171.json',
'pesquisa_172.json',
'pesquisa_173.json',
'pesquisa_174.json',
'pesquisa_175.json',
'pesquisa_176.json',
'pesquisa_177.json',
'pesquisa_178.json',
'pesquisa_18.json',
'pesquisa_19.json',
'pesquisa_2.json',
'pesquisa_20.json',
'pesquisa_21.json',
'pesquisa_22.json',
'pesquisa_23.json',
'pesquisa_24.json',
'pesquisa_25.json',
'pesquisa_26.json',
'pesquisa_27.json',
'pesquisa_28.json',
'pesquisa_29.json',
'pesquisa_3.json',
'pesquisa_30.json',
'pesquisa_31.json',
'pesquisa_32.json',
'pesquisa_33.json',
'pesquisa_34.json',
'pesquisa_35.json',
'pesquisa_36.json',
'pesquisa_37.json',
'pesquisa_38.json',
'pesquisa_39.json',
'pesquisa_4.json',
'pesquisa_40.json',
'pesquisa_41.json',
'pesquisa_42.json',
'pesquisa_43.json',
'pesquisa_44.json',
'pesquisa_45.json',
'pesquisa_46.json',
'pesquisa_47.json',
'pesquisa_48.json',
'pesquisa_49.json',
'pesquisa_5.json',
'pesquisa_50.json',
'pesquisa_51.json',
'pesquisa_52.json',
'pesquisa_53.json',
'pesquisa_54.json',
'pesquisa_55.json',
'pesquisa_56.json',
'pesquisa_57.json',
'pesquisa_58.json',
'pesquisa_59.json',
'pesquisa_6.json',
'pesquisa_60.json',
'pesquisa_61.json',
'pesquisa_62.json',
'pesquisa_63.json',
'pesquisa_64.json',
'pesquisa_65.json',
'pesquisa_66.json',
'pesquisa_67.json',
'pesquisa_68.json',
'pesquisa_69.json',
'pesquisa_7.json',
'pesquisa_70.json',
'pesquisa_71.json',
'pesquisa_72.json',
'pesquisa_73.json',
'pesquisa_74.json',
'pesquisa_75.json',
'pesquisa_76.json',
'pesquisa_77.json',
'pesquisa_78.json',
'pesquisa_79.json',
'pesquisa_8.json',
'pesquisa_80.json',
'pesquisa_81.json',
'pesquisa_82.json',
'pesquisa_83.json',
'pesquisa_84.json',
'pesquisa_85.json',
'pesquisa_86.json',
'pesquisa_87.json',
'pesquisa_88.json',
'pesquisa_89.json',
'pesquisa_9.json',
'pesquisa_90.json',
'pesquisa_91.json',
'pesquisa_92.json',
'pesquisa_93.json',
'pesquisa_94.json',
'pesquisa_95.json',
'pesquisa_96.json',
'pesquisa_97.json',
'pesquisa_98.json',
'pesquisa_99.json']


with open('base_full/pesquisa_1.json', 'r') as jsonFileLeitura:
  dadosJson = json.load(jsonFileLeitura)
  df_principal = pd.json_normalize(dadosJson['data'])
  df_tweet = pd.json_normalize(dadosJson['includes']['tweets'])
  df_place = pd.json_normalize(dadosJson['includes']['places'])
  df_user =  pd.json_normalize(dadosJson['includes']['users'])

for aqruivo in arquivos:
    with open('base_full/'+aqruivo, 'r') as jsonFileLeitura:
      dadosJson = json.load(jsonFileLeitura)
      df_bufer = pd.json_normalize(dadosJson['data'])

      if dadosJson['includes'].get('users'):
          df_user_buffer = pd.json_normalize(dadosJson['includes']['users'])
      if dadosJson['includes'].get('places'):
          df_place_buffer = pd.json_normalize(dadosJson['includes']['places'])
      if dadosJson['includes'].get('tweets'):
          df_tweet_buffer = pd.json_normalize(dadosJson['includes']['tweets'])

    
    df_principal = df_principal.append(df_bufer, ignore_index=True)
    df_tweet = df_tweet.append(df_tweet_buffer, ignore_index=True)
    df_place =  df_place .append(df_place_buffer, ignore_index=True)
    df_user = df_user.append(df_user_buffer, ignore_index=True)  
    

#df_principal.to_excel('base_exemplo_chamada_principal.xlsx')
#df_tweet.to_excel('base_exemplo_tweet.xlsx')
#df_place.to_excel('base_exemplo_place.xlsx')
#df_user.to_excel('base_exemplo_user.xlsx')

df_principal.to_csv('base_exemplo_chamada_principal.csv')
df_tweet.to_csv('base_exemplo_tweet.csv')
df_place.to_csv('base_exemplo_place.csv')
df_user.to_csv('base_exemplo_user.csv')
