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
        # Lê os dados do arquivo a partir da segunda linha
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
            #"moda": moda,
            "desvio_padrao": desvio_padrao,
            "coef_variacao": coef_variacao
        })

# Encontra o motor com o melhor desempenho (menor coeficiente de variação)
#melhor_motor = min(metricas_motores, key=lambda x: x["coef_variacao"])

# Opção de ordenar em ordem crescente dos melhores
#ordenado_metricas = sorted(metricas_motores, key=lambda x: x["coef_variacao"])

# Encontra o motor com o melhor desempenho (maior média e desempate por coeficiente de variação)
melhor_motor = max(metricas_motores, key=lambda x: (x["media"], -x["coef_variacao"]))

# Opção de ordenar em ordem crescente dos melhores
ordenado_metricas = sorted(metricas_motores, key=lambda x: x["coef_variacao"], reverse=True)


print("\nOpções:\n1 - Listar em ordem crescente dos melhores\n2 - Imprimir informações completas de um arquivo específico")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    # Imprime as métricas de cada motor ordenado em ordem crescente dos melhores
    for metricas in ordenado_metricas:
        print("Arquivo: ", metricas["arquivo"])
        print("Média: ", metricas["media"])
        print("Mediana: ", metricas["mediana"])
        #print("Moda: ", metricas["moda"])
        print("Desvio Padrão: ", metricas["desvio_padrao"])
        print("Coeficiente de Variação: ", metricas["coef_variacao"])
        print()
elif opcao == 2:
    # Opção de imprimir as informações completas de um arquivo específico
    arquivo_escolhido = input("Digite o nome do arquivo que deseja ver as informações completas: ")
    for metricas in metricas_motores:
        if metricas["arquivo"] == arquivo_escolhido:
            print("Arquivo: ", metricas["arquivo"])
            print("Média: ", metricas["media"])
            print("Mediana: ", metricas["mediana"])
            #print("Moda: ", metricas["moda"])
            print("Desvio Padrão: ", metricas["desvio_padrao"])
            print("Coeficiente de Variação: ", metricas["coef_variacao"])
