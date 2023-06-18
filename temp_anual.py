print("\nPrograma que colhe a temperatura média anual e retorna:\n\
Temperatura média anual e os meses com temperatura acima da média\n")

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto',
         'setembro', 'outubro', 'novembro', 'dezembro']
temp_coletada = {}  # Chave criada para armazenar a coleta de inputs
acima_media = {}  # Chave criada para armazenar os valores acima da média

for i in range(12):
    # Função para rodar todos os meses e para cada mês coletar os inputs
    valor = float(input(f"Temp no mês {meses[i].capitalize()}: "))
    # Coleta o valor em formato de float, utiliza o indice da lista para exibir o mês correspondente
    temp_coletada[meses[i]] = valor  # Para cada valor lido na lista de meses, atribui a temp digitada

media = sum(temp_coletada.values()) / len(temp_coletada)
# Calcula a média das temperaturas digitadas

for mes, temperatura in temp_coletada.items():
    # Itera sobre os valores coletados e cria um novo dict com os valores acima da média
    if temperatura > media:
        acima_media[mes] = temperatura

print(f"\nA temperatura média foi de: {media:4.2f}°C\n")
print(f"Meses em que a temperatura foi acima da média: \n")
for mes, temp in acima_media.items():
    # Itera sobre o dict acima_media e separa os valores para imprimir no formado pretendido
    print(f"Temp de {temp}°C em {mes.capitalize()}")
