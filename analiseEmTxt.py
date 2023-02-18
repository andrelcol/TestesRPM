import os
import statistics

# Cria uma lista para armazenar as métricas de cada motor
metricas_motores = []

# Define o caminho para a pasta de dados
pasta_dados = os.path.join(os.getcwd(), 'TestesRPM', 'TesteRPM-LEGO')
pasta = "/home/andre/Desktop/lego/TestesRPM/TesteRPM-LEGO"

# Loop pelos arquivos na pasta de dados
for arquivo in os.listdir(pasta):
    # Verifica se o arquivo é um arquivo de texto
    if arquivo.endswith(".txt"):
        # Lê os dados do arquivo
        with open(os.path.join(pasta, arquivo), 'r') as f:
            dados = [float(linha) for linha in f.readlines()[1:]]
        
        # Calcula as métricas estatísticas
        media = statistics.mean(dados)
        mediana = statistics.median(dados)
        #moda = statistics.mode(dados)
        desvio_padrao = statistics.stdev(dados)
        coef_variacao = (desvio_padrao / media) * 100
        
        # Adiciona as métricas a lista de métricas de motores
        metricas_motores.append({
            "arquivo": arquivo,
            "media": media,
            "mediana": mediana,
        #    "moda": moda,
            "desvio_padrao": desvio_padrao,
            "coef_variacao": coef_variacao
        })

# Encontra o motor com o melhor desempenho (maior média, menor coeficiente de variação)
ordenado_metricas = sorted(metricas_motores, key=lambda x: (x["media"], -x["coef_variacao"]), reverse = True)

# Imprime as métricas de cada motor no arquivo "informacoes.txt"
with open("informacoes.txt", "w") as f:
    for metricas in ordenado_metricas:
        f.write(f"Arquivo: {metricas['arquivo']}\n")
        f.write(f"Média: {metricas['media']}\n")
        f.write(f"Mediana: {metricas['mediana']}\n")
    #    f.write(f"Moda: {metricas['moda']}\n")
        f.write(f"Desvio Padrão: {metricas['desvio_padrao']}\n")
        f.write(f"Coeficiente de Variação: {metricas['coef_variacao']}\n\n")

    # Imprime o melhor motor no arquivo "informacoes.txt"
    melhor_motor = ordenado_metricas[0]
    f.write(f"O motor com melhor desempenho é o arquivo {melhor_motor['arquivo']} com uma média de {melhor_motor['media']} e um coeficiente de variação de {melhor_motor['coef_variacao']}")
