import os
import statistics

# Cria uma lista para armazenar as métricas de cada motor
metricas_motores = []

# Define o caminho para a pasta de dados
pasta_dados = os.path.join(os.getcwd(), 'TestesRPM', 'TesteRPM-LEGO')

# Loop pelos arquivos na pasta de dados
for arquivo in os.listdir(pasta_dados):
    # Verifica se o arquivo é um arquivo de texto
    if arquivo.endswith(".rtf"):
        # Lê os dados do arquivo
        with open(os.path.join(pasta_dados, arquivo), 'r') as f:
            dados = [float(linha) for linha in f]
        
        # Calcula as métricas estatísticas
        media = statistics.mean(dados)
        mediana = statistics.median(dados)
        moda = statistics.mode(dados)
        desvio_padrao = statistics.stdev(dados)
        coef_variacao = (desvio_padrao / media) * 100
        
        # Adiciona as métricas a lista de métricas de motores
        metricas_motores.append({
            "arquivo": arquivo,
            "media": media,
            "mediana": mediana,
            "moda": moda,
            "desvio_padrao": desvio_padrao,
            "coef_variacao": coef_variacao
        })

# Encontra o motor com o melhor desempenho (menor coeficiente de variação)
melhor_motor = min(metricas_motores, key=lambda x: x["coef_variacao"])

# Imprime as métricas de cada motor
for metricas in metricas_motores:
    print("Arquivo: ", metricas["arquivo"])
    print("Média: ", metricas["media"])
    print("Mediana: ", metricas["mediana"])
    print("Moda: ", metricas["moda"])
    print("Desvio Padrão: ", metricas["desvio_padrao"])
    print("Coeficiente de Variação: ", metricas["coef_variacao"])
    print()

# Imprime o melhor motor
print("O motor com melhor desempenho é o arquivo", melhor_motor["arquivo"], "com um coeficiente de variação de", melhor_motor["coef_variacao"])
