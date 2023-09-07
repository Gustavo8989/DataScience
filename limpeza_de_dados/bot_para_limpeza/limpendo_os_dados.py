import pandas as pd 
import numpy as np  




class robo:
  def __init__(self,dados):
    self.dados = dados
    self.dados = pd.read_csv(dados)
  def removendo_dados_nulos(self):
    #limpando dados nulos
    self.v_f = self.dados.isnull().sum() > 200
    self.v_f = v_f.loc[v_f == True]
    for self.c in self.v_f.index:
      df.drop(self.c,inplace=True,axis=1)
  def substituindo_media(self):
    # Pegando a media desse valores e colocando no lugar dos valores nulos
    media_median = df.isnull().sum() > 0
    media_median = media_median.loc[media_median == True]
    for j in media_median.index:
      media = df[j].mean()
      mediana = df[j].median()
      # Aplicando a media nos dados ausentes
      teste = df[j].fillna(media,inplace=True) #Talvez não estaja funcionando
  def identificando_outlirs(self):
    '''
    quartil_um = entregas['delivery_distance_meters'].quantile(0.25)
    quartil_tres = entregas['delivery_distance_meters'].quantile(0.75)
    distancia = quartil_tres - quartil_um
    limite_inferior = quartil_um - 1.5 * distancia
    limite_superior = quartil_tres + 1.5 * distancia
    '''
