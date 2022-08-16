# Importando biblioteca JSON
import json

# Local do diretório JSON
f = open('F:\\PROJETOS\\Teste_JR\\Teste_JobRotation\\FATURAMENTO_DISTRIBUIDORA\\dados.json')

# Lendo os dados do arquivo JSON e salvando num dicionário
dados = json.load(f)

# variáveis
aux = 0; maior = 0; menor = 0; soma = 0; media = 0


for dia in dados:

    # Lendo os valor de faturamento que não são zero.
    if (dia['valor']) != 0:
        aux = dia['valor']

        # O maior faturamento
        if (aux > maior):
            maior = aux
            # Verificando o dia
            if(dia['dia'] == dia['dia'] ):
                diaM=dia['dia']
        # O menor faturamento
        if(menor == 0):
            menor = aux
            # Verificando o dia
            if(dia['dia'] == dia['dia'] ):
                diaMn=dia['dia']
    
        elif (aux < menor):
            menor = aux

        # Soma do faturamento
        soma += dia['valor']

print('No dia '+ str (diaMn)+' do mês o menor faturamento foi de R$ ' + str(menor) +'.')
print('No dia '+ str (diaM)+' do mês o maior faturamento foi de R$' + str(maior) + '.')



# Dividindo a soma pelo número de dias para obter a média
media = soma / len(dados)

# Criando variável para armazenar os dias que o faturamento foi acima da média
diasFaturamento = ''

for i in dados:
    if (i['valor']) != 0:
        # Caso o valor do faturamento do dia for maior que a média, salva o número do dia na String
        if (i['valor']) > media:
           diasFaturamento += (str(i['dia']) + ' ')
        
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ' + diasFaturamento)