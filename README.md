# Mission Control AI - Sistema Inteligente de Monitoramento Espacial

O Mission Control AI é um sistema criado em Python com a finalidade de reproduzir o acompanhamento inteligente de uma missão espacial experimental. O programa executa análises automáticas dos dados operacionais da missão, detectando riscos, gerando alertas e elaborando relatórios minuciosos sobre a situação geral da operação.

# Nome da Missão e Equipe

Missão Artemis
Equipe: Artemis

# Contexto do Projeto

A indústria espacial depende de sistemas capazes de acompanhar continuamente o funcionamento de satélites, sondas e missões experimentais.

Durante uma missão espacial, diversos indicadores precisam ser analisados constantemente, como:

- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional

A partir dessas informações, o sistema consegue identificar falhas, calcular riscos operacionais e auxiliar na tomada de decisão da equipe responsável.

# Funcionalidades do Sistema

# Monitoramento Inteligente
Análise automática dos dados da missão em múltiplos ciclos operacionais.

# Sistema de Classificação
Cada indicador recebe um nível de risco:

- NORMAL
- ATENÇÃO
- CRÍTICO

# Pontuação de Risco
O sistema calcula automaticamente a pontuação total de risco de cada ciclo.

# Recomendações Automáticas
Quando falhas críticas são identificadas, o sistema gera recomendações de segurança em tempo real.

# Relatório Final Completo
Ao final da execução, o sistema apresenta:

- médias operacionais;
- risco médio da missão;
- ciclos críticos;
- tendência da missão;
- área mais afetada;
- conclusão operacional.
  
# Áreas Monitoradas

O sistema monitora os seguintes componentes:

- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional

# Regras de Negócio

# Temperatura Interna (°C)

- Abaixo de 18 °C → ATENÇÃO
- Entre 18 °C e 30 °C → NORMAL
- Entre 31 °C e 35 °C → ATENÇÃO
- Acima de 35 °C → CRÍTICO

# Comunicação com a Base (%)

- Abaixo de 30% → CRÍTICO
- Entre 30% e 59% → ATENÇÃO
- 60% ou mais → NORMAL
  
# Sistema de Energia (%)

- Abaixo de 20% → CRÍTICO
- Entre 20% e 49% → ATENÇÃO
- 50% ou mais → NORMAL
  
# Suporte de Oxigênio (%)

- Abaixo de 80% → CRÍTICO
- Entre 80% e 89% → ATENÇÃO
- 90% ou mais → NORMAL

# Estabilidade Operacional (%)

- Abaixo de 40% → CRÍTICO
- Entre 40% e 69% → ATENÇÃO
- 70% ou mais → NORMAL

# Classificação Geral da Missão

A pontuação total de risco define a classificação do ciclo:

 0 a 2 pontos: MISSÃO ESTÁVEL 
 3 a 5 pontos: MISSÃO EM ATENÇÃO 
 6 a 10 pontos: MISSÃO CRÍTICA 

# Recomendações Automáticas

O sistema gera recomendações automáticas quando falhas críticas são detectadas.

Exemplos:

- Verificar controle térmico da missão
- Restabelecer comunicação com a base
- Ativar modo de economia de energia
- Acionar protocolo de suporte à vida
- Reduzir operações não essenciais

# Análises Realizadas

O sistema também realiza:

- cálculo de médias dos sensores;
- identificação do ciclo mais crítico;
- cálculo do risco médio da missão;
- análise de tendência da missão;
- identificação da área mais afetada.

---
