# Data Quality Report
Este projeto contém um módulo Python para análise da qualidade de dados, semelhante a ferramentas como Pandas Profiling, YData Profiling e SweetViz. O módulo gera um relatório detalhado sobre o dataset fornecido, incluindo estatísticas descritivas e visualizações para colunas categóricas e numéricas, além de verificar a existência de valores duplicados e ausentes.

### Funcionalidades:

  **Contagem de valores nulos:** Identifica a quantidade de valores ausentes em cada coluna. <br>
  
  **Contagem de valores únicos:** Mostra o número de valores únicos por coluna.<br>

  **Distribuição de colunas categóricas:** Realiza a contagem de frequência dos valores em colunas categóricas.<br>

  **Análise descritiva das colunas numéricas:** Gera estatísticas como média, mediana, desvio padrão, entre outras, para colunas numéricas.<br>

  **Gráficos de distribuição:** Cria gráficos de distribuição para colunas categóricas e numéricas.<br>

  **Verificação de linhas duplicadas:** Identifica e conta o número de linhas duplicadas no dataset.<br>

  **Verificação de colunas duplicadas:** Verifica se há colunas duplicadas no dataset.<br>

### Estrutura do Projeto

  **data_quality.py:** Módulo principal que contém a classe Data_quality e suas funções de análise.<br>

  **Jupyter Notebook:** Exemplo de uso do módulo para gerar relatórios de análise de dados.<br>

### Como Usar

  - Certifique-se de ter o Python 3.x e a biblioteca pandas instalados.<br>

  - Coloque o arquivo data_quality.py no diretório do seu projeto.<br>

  - No seu notebook ou script Python, importe o módulo e carregue o dataset em um DataFrame:<br>
  ```python
    import pandas as pd
    from data_quality import Data_quality

    # Carrega o dataset em um DataFrame
    df = pd.read_csv("people_personality.csv")

    # Cria um relatório de qualidade dos dados
    report = Data_quality(df)
    report.gerar_relatorio() <br>
```
    
O código acima executará as análises e imprimirá um relatório detalhado sobre a qualidade dos dados.
