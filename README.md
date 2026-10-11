# MBA Engenharia de Software com IA — Desafio 02
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
