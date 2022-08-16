# função para calcular porcentagem
def porcentagem (estado, total):
    return round(((100*estado)/total),2)

# Valores dos faturamentos
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# faturamentos TOTAL
total = sp + rj + mg + es + outros

# faturamentos
print("Faturamento de SP: " + str(porcentagem(sp, total)) + '%')
print("Faturamento de RJ: " + str(porcentagem(rj, total)) + '%')
print("Faturamento de MG: " + str(porcentagem(mg, total)) + '%')
print("Faturamento de ES: " + str(porcentagem(es, total)) + '%')
print("Outros faturamentos: " + str(porcentagem(outros, total)) + '%')
