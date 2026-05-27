print("============================================================")
print("MISSION CONTROL AI")
print("============================================================")
print("Missão: Missão Artemis")
print("Equipe: Artemis")

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [15, 50, 64, 80, 81],
    [25, 89, 73, 92, 88],
    [32, 54, 49, 85, 60],
    [37, 20, 35, 80, 52],
    [42, 52, 17, 30, 33],
    [29, 68, 90, 90, 74]
]


print()


# =========================
# FUNÇÕES
# =========================

# Temperatura
def verificar_temperatura(valor):

    if valor < 18:
        return "ATENÇÃO", 1

    elif valor <= 30:
        return "NORMAL", 0

    elif valor <= 35:
        return "ATENÇÃO", 1

    else:
        return "CRITICO", 2


# comunicação
def verificar_comunicacao(valor):

    if valor < 30:
        return "CRITICO", 2

    elif valor <= 59:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0


# bateria
def verificar_bateria(valor):

    if valor < 20:
        return "CRITICO", 2

    elif valor <= 49:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0


# oxigenio
def verificar_oxigenio(valor):

    if valor < 80:
        return "CRITICO", 2

    elif valor <= 89:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0


# estabilidade
def verificar_estabilidade(valor):

    if valor < 40:
        return "CRITICO", 2

    elif valor <= 69:
        return "ATENÇÃO", 1

    else:
        return "NORMAL", 0


# classificação do ciclo
def classificar_missao(pontos_total):

    if pontos_total <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontos_total <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


# =========================
# VARIÁVEIS
# =========================

total_temp = 0
total_com = 0
total_bat = 0
total_oxi = 0
total_est = 0

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

maior_risco = 0
ciclo_mais_critico = 0

total_risco_missao = 0
ciclos_criticos = 0


# =========================
# CICLOS
# =========================

for ciclo, i in enumerate(dados_missao, start=1):

    recomendacoes = []

    print(f"CICLO {ciclo}")
    print("------------------------------------------------------------")

    temperatura = i[0]
    comunicacao = i[1]
    bateria = i[2]
    oxigenio = i[3]
    estabilidade = i[4]

    alerta_temp, pontos_temp = verificar_temperatura(temperatura)

    alerta_comi, pontos_comi = verificar_comunicacao(comunicacao)

    alerta_bat, pontos_bat = verificar_bateria(bateria)

    alerta_oxi, pontos_oxi = verificar_oxigenio(oxigenio)

    alerta_est, pontos_est = verificar_estabilidade(estabilidade)

    pontos_total = (
        pontos_temp +
        pontos_comi +
        pontos_bat +
        pontos_oxi +
        pontos_est
    )

    classificacao = classificar_missao(pontos_total)

    total_temp += pontos_temp
    total_com += pontos_comi
    total_bat += pontos_bat
    total_oxi += pontos_oxi
    total_est += pontos_est

    # SOMAS DAS MÉDIAS
    soma_temp += temperatura
    soma_com += comunicacao
    soma_bat += bateria
    soma_oxi += oxigenio
    soma_est += estabilidade

    # RISCO TOTAL DA MISSÃO
    total_risco_missao += pontos_total

    # CICLO MAIS CRÍTICO
    if pontos_total > maior_risco:
        maior_risco = pontos_total
        ciclo_mais_critico = ciclo

    # QUANTIDADE DE CICLOS CRÍTICOS
    if classificacao == "MISSÃO CRÍTICA":
        ciclos_criticos += 1

    if alerta_temp == "CRITICO":
        recomendacoes.append(
            "Verificar controle térmico da missão."
        )

    if alerta_comi == "CRITICO":
        recomendacoes.append(
            "Tentar restabelecer contato com a base."
        )

    if alerta_bat == "CRITICO":
        recomendacoes.append(
            "Ativar modo de economia de energia."
        )

    if alerta_oxi == "CRITICO":
        recomendacoes.append(
            "Acionar protocolo de suporte à vida."
        )

    if alerta_est == "CRITICO":
        recomendacoes.append(
            "Reduzir operações não essenciais."
        )

    print(areas_monitoradas[0], ":", temperatura, "°C |", alerta_temp)
    print(areas_monitoradas[1], ":", comunicacao, "% |", alerta_comi)
    print(areas_monitoradas[2], ":", bateria, "% |", alerta_bat)
    print(areas_monitoradas[3], ":", oxigenio, "% |", alerta_oxi)
    print(areas_monitoradas[4], ":", estabilidade, "% |", alerta_est)

    print()
    print(f"Pontuação de risco do ciclo: {pontos_total}")
    print(f"Classificação do ciclo: {classificacao}")

    print("Recomendações:")

    if len(recomendacoes) == 0:
        print("Nenhuma ação necessária.")

    else:
        for r in recomendacoes:
            print("-", r)




# =========================
# RELATÓRIO FINAL
# =========================
print()
print("============================================================")
print("RELATÓRIO FINAL DA MISSÃO")
print("============================================================")
print("Missão: Missão Artemis")
print("Equipe: Artemis")
print()
print("Quantidade de ciclos analisados:", len(dados_missao))
print()
media_temp = soma_temp / len(dados_missao)
media_com = soma_com / len(dados_missao)
media_bat = soma_bat / len(dados_missao)
media_oxi = soma_oxi / len(dados_missao)
media_est = soma_est / len(dados_missao)

print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")
print()

print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")

risco_medio = total_risco_missao / len(dados_missao)

print(f"Risco médio da missão: {risco_medio:.2f}")

print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print()

print("Tendência da missão:")

primeiro_ciclo = dados_missao[0]
ultimo_ciclo = dados_missao[-1]

# PRIMEIRO CICLO
_, p_temp1 = verificar_temperatura(primeiro_ciclo[0])
_, p_com1 = verificar_comunicacao(primeiro_ciclo[1])
_, p_bat1 = verificar_bateria(primeiro_ciclo[2])
_, p_oxi1 = verificar_oxigenio(primeiro_ciclo[3])
_, p_est1 = verificar_estabilidade(primeiro_ciclo[4])

pontos_primeiro = (
    p_temp1 +
    p_com1 +
    p_bat1 +
    p_oxi1 +
    p_est1
)

# ÚLTIMO CICLO
_, p_temp2 = verificar_temperatura(ultimo_ciclo[0])
_, p_com2 = verificar_comunicacao(ultimo_ciclo[1])
_, p_bat2 = verificar_bateria(ultimo_ciclo[2])
_, p_oxi2 = verificar_oxigenio(ultimo_ciclo[3])
_, p_est2 = verificar_estabilidade(ultimo_ciclo[4])

pontos_ultimo = (
    p_temp2 +
    p_com2 +
    p_bat2 +
    p_oxi2 +
    p_est2
)

if pontos_ultimo > pontos_primeiro:
    print("A missão apresentou tendência de piora.")

elif pontos_ultimo < pontos_primeiro:
    print("A missão apresentou tendência de melhora.")

else:
    print("A missão permaneceu estável em relação ao início.")

print()

print("Pontuação acumulada por área:")
print("Temperatura:", total_temp)
print("Comunicação:", total_com)
print("Energia:", total_bat)
print("Oxigênio:", total_oxi)
print("Estabilidade:", total_est)

print()

maior = max(
    total_temp,
    total_com,
    total_bat,
    total_oxi,
    total_est
)

print("Área mais afetada:")

if maior == total_temp:
    print("Temperatura interna")

elif maior == total_com:
    print("Comunicação com a base")

elif maior == total_bat:
    print("Sistema de energia")

elif maior == total_oxi:
    print("Suporte de oxigênio")

else:
    print("Estabilidade operacional")

print()
print("Conclusão:")

if risco_medio <= 2:
    print(
        "A missão apresentou desempenho estável durante todos os ciclos analisados. "
        "Os sistemas permaneceram operando dentro dos parâmetros esperados, "
        "sem riscos significativos para a operação."
    )

elif risco_medio <= 5:
    print(
        "A missão apresentou instabilidade relevante durante a operação. "
        "Apesar da tentativa de recuperação observada nos ciclos finais, "
        "ainda existem sistemas em estado de atenção que podem comprometer "
        "a segurança e a eficiência da missão. Recomenda-se manter o plano "
        "de contingência ativo, reforçar o monitoramento dos sistemas críticos "
        "e priorizar ações preventivas para evitar novas falhas operacionais."
    )

else:
    print(
        "A missão apresentou falhas críticas em múltiplos sistemas essenciais, "
        "indicando alto risco operacional. Os níveis de estabilidade da missão "
        "foram comprometidos em diversos ciclos, exigindo intervenção imediata "
        "da equipe responsável. Recomenda-se ativar protocolos de emergência "
        "e reduzir operações não essenciais até que os sistemas sejam estabilizados."
    )