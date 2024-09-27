
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
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

    def gerar_relatorio(self):
        self.nulos()
        self.unicos()
        self.contagem_categorica()
        self.contagem_numericas()
        self.plotar_categoricas()
        

