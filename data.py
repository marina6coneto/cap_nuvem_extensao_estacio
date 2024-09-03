import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded Excel file
file_path = 'cap_nuvem_response.xlsx'

# Read the Excel file
data = pd.read_excel(file_path)

# Listar os nomes das colunas da planilha para identificar possíveis diferenças
colunas = data.columns
colunas.tolist()

# Função para gerar gráficos de pizza
def gerar_grafico_pizza(coluna, titulo):
    plt.figure(figsize=(8, 8))
    data[coluna].value_counts().plot.pie(autopct='%1.1f%%', colors=plt.cm.Paired(range(len(data[coluna].unique()))))
    plt.title(titulo)
    plt.ylabel('')
    plt.show()

# Função para gerar gráficos de barras
def gerar_grafico_barras(coluna, titulo):
    plt.figure(figsize=(10, 6))
    data[coluna].value_counts().plot.bar(color='skyblue')
    plt.title(titulo)
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()


gerar_grafico_pizza('Qual seu gênero?',
                    'Distribuição de Gênero')
gerar_grafico_pizza('Qual é o seu nível de conhecimento em computação em nuvem?',
                    'Nível de Conhecimento em Computação em Nuvem')
gerar_grafico_pizza('Você possui alguma certificação em computação em nuvem? ',
                    'Certificação em Computação em Nuvem')
gerar_grafico_pizza('Qual é a sua principal motivação para aprender sobre computação em nuvem? ',
                    'Motivação para Aprender sobre Computação em Nuvem')
gerar_grafico_pizza('Você já participou de algum treinamento ou curso sobre computação em nuvem? ',
                    'Participação em Treinamento sobre Computação em Nuvem')
gerar_grafico_pizza('Qual é o seu nível de escolaridade? ',
                    'Nível de Escolaridade')
gerar_grafico_pizza('Qual é a sua faixa etária? ',
                    'Faixa Etária')
gerar_grafico_barras('Quais tópicos de computação em nuvem você gostaria de aprender mais? (Selecione todos que se aplicam) ',
                     'Tópicos de Computação em Nuvem Desejados')
gerar_grafico_barras('Qual plataforma de nuvem você utiliza com mais frequência? ',
                     'Plataforma de Nuvem Mais Utilizada')
gerar_grafico_barras('Quais são os principais desafios que você enfrenta ao trabalhar com computação em nuvem? (Selecione todos que se aplicam) ',
                     'Desafios ao Trabalhar com Computação em Nuvem')
gerar_grafico_barras('Qual formato de capacitação você prefere? ',
                     'Formato de Capacitação Preferido')


