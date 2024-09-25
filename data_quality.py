
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
class Data_quality:

    def __init__(self,df) -> None:
        #Inicializa a classe com o DataFrame a ser analisado.
        self.df = df

    def nulos(self):
        print("contagem de nulos")
        print(self.df.isnull().sum)
        print("\n")
    
    def unicos(self):
        print("Contagem de únicos")
        print(self.df.unique())
        print("\n")

    def contagem_categorica(self):
        print("Contagem de valores para colunas categoricas")
        colunas_categorias = self.df.select_dtype(include=['object', 'category']).columns
        
        for coluna in colunas_categorias:
            print(f'\nColuna:{coluna}')
            print(self.df[coluna].value_counts())

    def contagem_numericas(self):
        print("Contagem de valores para colunas numéricas")
        print(self.df.describe())

    def gerar_relatorio(self):
        self.nulos()
        self.unicos()
        self.contagem_categorica()
        self.contagem_numericas()
        

