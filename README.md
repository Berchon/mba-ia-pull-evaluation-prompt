# MBA Engenharia de Software com IA - Desafio 02
## Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-v0.2%2B-green.svg)
![LangSmith](https://img.shields.io/badge/LangSmith-Prompt%20Hub-orange.svg)
![Status](https://img.shields.io/badge/Status-APROVADO%20(%E2%89%A5%200.8)-brightgreen.svg)

---

## Visão Geral do Projeto

Este projeto compreende a solução completa do **Desafio 02 do MBA em Engenharia de Software com IA**, cujo objetivo central é construir um pipeline ponta a ponta para **gestão, engenharia reversa, otimização e avaliação comparativa de prompts para LLMs**, integrando o ecossistema **LangChain** e a plataforma **LangSmith**.

O fluxo abrange o ciclo de vida completo de engenharia de prompts em nível de produção:
1. **Pull Automatizado:** Baixar uma versão inicial de baixa qualidade (`bug_to_user_story_v1`) publicada no LangSmith Prompt Hub.
2. **Engenharia de Prompt & Otimização:** Refatorar a instrução aplicando técnicas avançadas (*Role Prompting*, *Chain of Thought* estruturado em BDD/Gherkin e *Few-shot Learning* com múltiplos cenários) gerando a versão `bug_to_user_story_v2`.
3. **Testes Unitários e Validação Estrutural:** Garantir a conformidade estrutural do prompt via 6 testes automatizados com `pytest`.
4. **Push ao Hub:** Versionar e publicar o prompt otimizado como repositório público no LangSmith Prompt Hub.
5. **Avaliação Automatizada (LLM-as-a-Judge):** Avaliar o prompt contra um dataset de referência de 15 casos reais de bugs através de 5 métricas customizadas, atingindo pontuação $\ge 0.8$ (80%) em todas elas.

---

## Estrutura do Repositório

```text
mba-ia-pull-evaluation-prompt/
├── .env.example                  # Template das variáveis de ambiente necessárias
├── requirements.txt              # Dependências do projeto (LangChain, LangSmith, pytest, etc.)
├── INSTRUCTIONS.md               # Especificação e enunciado original do desafio
├── README.md                     # Documentação técnica oficial e relatório de entrega
│
├── prompts/
│   ├── bug_to_user_story_v1.yml  # Prompt inicial de baixa qualidade (obtido via pull)
│   └── bug_to_user_story_v2.yml  # Prompt otimizado com técnicas avançadas
│
├── datasets/
│   └── bug_to_user_story.jsonl   # Dataset com 15 casos (5 simples, 7 médios, 3 complexos)
│
├── src/
│   ├── pull_prompts.py           # Script para pull do prompt inicial do LangSmith Hub
│   ├── push_prompts.py           # Script para validação e push do prompt v2 ao Hub
│   ├── evaluate.py               # Script de avaliação automatizada via LangSmith
│   ├── metrics.py                # Implementação das 5 métricas de avaliação
│   └── utils.py                  # Funções utilitárias (YAML, validação, verificação de env)
│
└── tests/
    └── test_prompts.py           # 6 testes automatizados para validação do prompt v2
```

---

## Sumário

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Seção A: Técnicas Aplicadas (Fase 2)](#seção-a-técnicas-aplicadas-fase-2)
- [Seção B: Resultados Finais e Avaliação](#seção-b-resultados-finais-e-avaliação)
- [Seção C: Como Executar o Projeto](#seção-c-como-executar-o-projeto)
- [Seção D: Evidências no LangSmith](#seção-d-evidências-no-langsmith)

---

## Seção A: Técnicas Aplicadas (Fase 2)

### 1. Diagnóstico do Prompt Original (`v1`) vs. Estratégia de Refatoração (`v2`)

O prompt inicial (`bug_to_user_story_v1`) apresentava fragilidades severas que inviabilizavam seu uso em um fluxo ágil de engenharia:
- **Ausência de Papel e Contexto:** O modelo atuava sem persona definida, gerando respostas com preâmbulos conversacionais dispensáveis ("Aqui está sua User Story:", "Espero ter ajudado!").
- **Critérios de Aceitação Frágeis:** Não havia imposição do padrão BDD (*Given/When/Then*), resultando em listas genéricas de tarefas sem acionabilidade para QA.
- **Falta de Fidelidade Factual:** O modelo alucinava dependências de terceiros e modificava valores reais relatados no bug (rotas, queries SQL, códigos de status HTTP).
- **Inconsistência de Escopo:** Bugs simples recebiam respostas prolixas com arquiteturas desnecessárias, enquanto incidentes críticos multidimensionais eram tratados superficialmente.

Para superar essas deficiências e atingir notas superiores a **0.8** em todas as métricas (*Helpfulness*, *Correctness*, *F1-Score*, *Clarity* e *Precision*), a versão `prompts/bug_to_user_story_v2.yml` foi modelada com uma abordagem multicamada combinando **três técnicas principais** e diretrizes estritas de contenção factual.

---

### 2. Técnica Obrigatória: Few-shot Learning

#### Justificativa Técnica:
Modelos de linguagem respondem significativamente melhor a demonstrações explícitas de formato, densidade sintática e estilo do que a instruções puramente declarativas (*in-context learning*). Ao fornecer exemplos concretos de entrada e saída esperada alinhados às três classes de complexidade do dataset de teste (simples, médio e complexo), condicionamos o modelo a replicar exatamente a estrutura canônica sem desvios de formato.

#### Aplicação Prática no Prompt:
Foram incorporados **9 exemplos Few-shot completos** em `prompts/bug_to_user_story_v2.yml`, estruturados em uma matriz balanceada **3x3** perfeitamente alinhada às classes e casos do dataset de avaliação:
- **3 Exemplos Nível SIMPLE:** Casos pontuais cobrindo validação de senha/formulário, persistência de preferências de UI (tema) e divergência de contagem em métricas de dashboard;
- **3 Exemplos Nível MEDIUM:** Falhas com contexto de infraestrutura e persistência cobrindo concorrência/particionamento com erro HTTP 502, timeouts de serviços externos com HTTP 504 e deadlocks transacionais em banco de dados;
- **3 Exemplos Nível COMPLEX:** Incidentes críticos multidimensionais cobrindo concorrência e privacidade em agendamento, conformidade de dados sensíveis e segurança em fintech, e telemetria IoT com vazamento de memória e conexões saturadas.

Trecho ilustrativo extraído de `prompts/bug_to_user_story_v2.yml`:

```yaml
# Trecho Few-shot: Exemplo 1 (Simples - Dashboard Count)
Exemplo 1 (Bugs simples / UI / Dashboard):
Entrada:
  "O dashboard do painel admin está exibindo 50 usuários ativos quando na verdade só existem 42 usuários cadastrados no banco de dados. A lista mostra os 42, mas o card de métrica exibe 50."
Saída Esperada:
  Como um administrador visualizando o dashboard, eu quero ver a contagem correta de usuários ativos, para que eu possa tomar decisões baseadas em dados precisos.

  Critérios de Aceitação:
  - Dado que acesso o dashboard como admin
  - Quando visualizo a métrica de usuários ativos
  - Então o número exibido deve corresponder ao total real de usuários ativos
  - E o valor deve ser atualizado em tempo real
  - E deve incluir apenas usuários com status "ativo"
```

---

### 3. Técnica Adicional 1: Role Prompting (Persona e Contexto Operacional)

#### Justificativa Técnica:
A definição de uma persona de liderança técnica orienta os pesos semânticos do modelo, reduzindo a probabilidade de respostas genéricas. Ao calibrar a identidade como uma fusão de *Senior Technical Product Manager* e *QA Lead*, o modelo equilibra simultaneamente:
- O valor de negócio e a perspectiva do usuário final ("Como um... Eu quero... Para que...");
- O rigor analítico de testes, prevenindo ambiguidades e garantindo critérios testáveis por ferramentas de automação.

#### Aplicação Prática no Prompt:
```yaml
# 2. PAPEL E AUTORIDADE (ROLE PROMPTING)
Você é um Senior Technical Product Manager experiente, atuando com liderança técnica
e rigor de Engenharia de Qualidade (QA Lead) em uma empresa de tecnologia focada em
produtos digitais B2B e B2C de alta escala.

# 3. CONTEXTO OPERACIONAL
Sua organização desenvolve soluções críticas em múltiplos domínios, incluindo e-commerce, SaaS, ERP, CRM, gateways de pagamento e dashboards analíticos. Suas aplicações são
multiplataforma (Web, iOS, Android), adotam arquiteturas complexas (alta concorrência,
sistemas distribuídos e funcionamento offline-first) e manipulam dados sensíveis.
```

---

### 4. Técnica Adicional 2: Chain of Thought (CoT) Estruturado com BDD

#### Justificativa Técnica:
A transformação de relatos de bugs crus em histórias ágeis exige raciocínio em múltiplos estágios: identificar a causa raiz, mapear o ator prejudicado, isolar evidências técnicas e deduzir os cenários de teste necessários. A técnica de *Chain of Thought* (CoT) decompõe mentalmente a tarefa em etapas lógicas sequenciais antes da emissão da resposta final, garantindo que nenhum elemento crítico seja omitido.

#### Aplicação Prática no Prompt:
O prompt instrui o modelo a executar o seguinte raciocínio analítico:
1. **Triagem e Classificação:** Identificação do ator, domínio e nível na matriz de proporcionalidade (Simple, Medium ou Complex).
2. **Investigação Técnica e Preservação Literal:** Extração estrita de endpoints, queries SQL, trechos de logs, códigos HTTP e status sem modificações.
3. **Formulação Canônica da User Story:** Síntese focada no estado futuro ideal sem o bug.
4. **Definição dos Critérios de Aceitação em BDD:** Escrita padronizada em *Dado/Quando/Então/E* com atomicidade estrita (cada ação e consequência visual em linhas separadas).
5. **Checklist de Auto-validação:** Guardrail interno que valida zero preâmbulo e retenção literal antes da emissão.

---

### 5. Diretrizes Complementares: Matriz de Complexidade e Contenção Factual

Para assegurar estabilidade nas métricas de *Precision* e *Clarity*, foram estabelecidas regras explícitas de calibração:
- **Matriz de Proporcionalidade Estrutural:**
  - `SIMPLE`: Apenas a User Story canônica e 1 único cenário BDD sucinto (4 a 5 linhas). Proibido adicionar seções técnicas extras.
  - `MEDIUM`: User Story, critérios BDD abrangendo fluxo principal e tratamento de falhas, com seção de Contexto Técnico e Acessibilidade quando cabível.
  - `COMPLEX`: Estruturação temática abrangente (`=== USER STORY PRINCIPAL ===`, `=== CRITÉRIOS DE ACEITAÇÃO ===` agrupados por frentes A., B., C..., critérios técnicos e tarefas sugeridas).
- **Contenção Factual Estrita (Zero Hallucination):** Proibição categórica de inventar bibliotecas de terceiros (ex.: nomes de plugins ou bibliotecas inexistentes no relato) e preservação literal de entidades técnicas reais (queries, códigos de erro e valores numéricos).

