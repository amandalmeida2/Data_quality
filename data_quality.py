
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
class Data_quality:

    def __init__(self,df) -> None:
        #Inicializa a classe com o DataFrame a ser analisado.
        self.df = df

    def nulos(self):
        print(f"--------------------------- \nContagem de nulos\n")
        print(self.df.isnull().sum().reset_index())
        print(f"--------------------------- \n")
    
    def unicos(self):
        print(f"--------------------------- \nContagem de únicos\n")
        print(self.df.nunique())
        print(f"--------------------------- \n")

    def contagem_categorica(self):
        print(f"--------------------------- \nContagem de valores para colunas categoricas")
        colunas_categorias = self.df.select_dtypes(include=['object', 'category']).columns        
        
        for coluna in colunas_categorias:
            print(f'\nColuna:{coluna}')
            print(self.df[coluna].value_counts())
            print(f"\n")

    def contagem_numericas(self):
        print(f"--------------------------- \nContagem de valores para colunas numéricas")
        print(self.df.describe())
        print(f"--------------------------- \n")

    def plotar_categoricas(self):
        colunas_categorias = self.df.select_dtypes(include=['object', 'category']).columns
        for coluna in colunas_categorias:
            plt.figure(figsize=(4,2))
            sn.countplot(x=coluna, data=self.df)
            plt.title(f'Coluna categorica: {coluna}')
            plt.xticks(rotation=45)
            plt.show()

    def plotar_numericas(self):
        colunas_numericas = self.df.select_dtypes(include = np.number ).columns
        for coluna in colunas_numericas:
            plt.figure(figsize=(4, 2))
            sn.histplot(self.df[coluna], kde=True)
            plt.title(f'Distribuição da coluna numérica: {coluna}')
            plt.show()

    def plot_dispersao(self):
        print("Gráficos de dispersão entre colunas numéricas")
   
        colunas_numericas = self.df.select_dtypes(include=['float64', 'int64']).columns
        if len(colunas_numericas) > 1:
            sn.pairplot(self.df[colunas_numericas])
            plt.title('Gráficos de dispersão entre colunas numéricas')
            plt.show()
        else:
            print("Não há pares suficientes de variáveis numéricas para gerar gráficos de dispersão.")
    
    def colunas_duplicadas(self):
        print(f"------------------------------\nColunas duplicadas:")

        duplicadas = self.df.T.duplicated()
        if duplicadas.any():

            print("Colunas duplicadas: ")
            print(self.df.columns[duplicadas])
            print("\n")
        else:
            print("Não há colunas duplicadas para este dataset")
    
    def linhas_duplicadas(self):
        print(f"------------------------------\nLinhas duplicadas:")
        duplicadas = self.df.duplicated()
        total_duplicadas = duplicadas.sum()
        print(f"O total de linhas duplicadas é: {total_duplicadas}")
        if total_duplicadas >1:
            print(self.df[duplicadas])
            print("\n")
        else:
            print("Não há linhas duplicadas para este dataset.")
            print("\n")

        
    def gerar_relatorio(self):
        self.nulos()
        self.unicos()
        self.contagem_categorica()
        self.contagem_numericas()
        self.plotar_categoricas()
        self.plotar_numericas()
        self.plot_dispersao()
        self.colunas_duplicadas()  
        self.linhas_duplicadas()  
   
