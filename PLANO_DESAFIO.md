# Planejamento Detalhado: Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Este documento detalha o planejamento passo a passo com tasks e subtasks para cumprir 100% dos requisitos do desafio técnico.

---

## 1. Decisões Alinhadas

- **Provedor de LLM:** **Google Gemini** (`gemini-2.5-flash` para resposta e para avaliação, utilizando créditos de API do Google AI Studio).
- **Técnicas de Prompt Engineering:** **Few-shot Learning (obrigatório)** + **Role Prompting (Senior Agile Product Manager & QA Lead)** + **Chain of Thought (CoT estruturado em BDD/Gherkin)**.
- **Gestão do README:** O arquivo original `README.md` será renomeado para `INSTRUCTIONS.md` (preservando o enunciado na íntegra) e um novo `README.md` será criado focado 100% na entrega oficial exigida pelo desafio (Técnicas Aplicadas, Resultados Finais com tabelas comparativas e Como Executar).
- **Identificador de Usuário LangSmith Hub:** Será configurado diretamente no arquivo `.env` (`USERNAME_LANGSMITH_HUB`).
- **Arquivos Locais Ignorados:** `PLANO_DESAFIO.md` e `CHECKLIST.md` na raiz e adicionados ao `.gitignore`.

---

## 2. Diretrizes Obrigatórias de Governança e Git

1. **Resumo Prévio e Aprovação Antes de Iniciar:** Antes de começar qualquer Task e/ou Subtask, o assistente deve OBRIGATORIAMENTE apresentar um pequeno resumo do que será implementado, devolver o controle para o usuário e aguardar a aprovação explícita para iniciar.
2. **Branch por Task:** Toda e qualquer Tarefa (Task) deve ser desenvolvida OBRIGATORIAMENTE em uma branch própria criada a partir da `main` (ex: `feature/task-1.1-setup-venv`).
3. **Implementação Granular:** Cada item/subtask é implementado individualmente.
4. **Validação Obrigatória com o Usuário:** Antes de commitar para concluir uma subtask (ou item), o assistente SEMPRE deve questionar o usuário se ele concorda com a implementação realizada e se deseja alguma alteração.
5. **Commit por Subtask:** Uma vez validada e aprovada pelo usuário, a subtask é commitada na branch da feature com mensagem semântica.
6. **Atualização Obrigatória do Checklist por Subtask:** Após a finalização de uma subtask (e de cada item concluído), o arquivo `CHECKLIST.md` deve OBRIGATORIAMENTE ser atualizado marcando o respectivo item (`[x]`).
7. **Finalização da Task e Merge com a Main:** Ao finalizar com sucesso todas as subtasks da Task, o `CHECKLIST.md` deve OBRIGATORIAMENTE ser atualizado registrando a conclusão da task e, em seguida, é realizado o merge da branch da feature na branch `main`.
8. **Sequencialidade:** A próxima Task só poderá ser iniciada em uma nova branch após a conclusão do merge da Task anterior na `main`.



---

## 3. Estrutura de Tarefas e Subtarefas (WBS)


### Fase 1: Preparação do Ambiente, Dependências e Configurações

- **Tarefa 1.1: Configuração do Ambiente Virtual Python (`venv`) e Instalação de Dependências**
  - Subtask 1.1.1: Criar o ambiente virtual em `mba-ia-pull-evaluation-prompt/venv` (`python3 -m venv venv`).
  - Subtask 1.1.2: Instalar as dependências contidas em `requirements.txt` (`pip install -r requirements.txt`).
  - Subtask 1.1.3: Validar a instalação dos pacotes e módulos necessários (`langchain`, `langsmith`, `langchain-google-genai`, `pytest`).

- **Tarefa 1.2: Configuração de Variáveis de Ambiente e Credenciais (`.env`)**
  - Subtask 1.2.1: Criar o arquivo `.env` a partir de `.env.example`.
  - Subtask 1.2.2: Configurar as variáveis do LangSmith:
    - `LANGSMITH_TRACING=true`
    - `LANGSMITH_ENDPOINT=https://api.smith.langchain.com`
    - `LANGSMITH_API_KEY=<chave_langsmith>`
    - `LANGSMITH_PROJECT=prompt-optimization-challenge-resolved`
    - `USERNAME_LANGSMITH_HUB=<seu_username_langsmith>`
  - Subtask 1.2.3: Configurar as variáveis do Google Gemini:
    - `GOOGLE_API_KEY=<chave_google>`
    - `LLM_PROVIDER=google`
    - `LLM_MODEL=gemini-2.5-flash`
    - `EVAL_MODEL=gemini-2.5-flash`

- **Tarefa 1.3: Organização de Arquivos e Gitignore**
  - Subtask 1.3.1: Renomear `README.md` original para `INSTRUCTIONS.md`.
  - Subtask 1.3.2: Atualizar `.gitignore` adicionando `PLANO_DESAFIO.md`.

---

### Fase 2: Implementação do Pull de Prompts do LangSmith Hub

- **Tarefa 2.1: Implementação do script `src/pull_prompts.py`**
  - Subtask 2.1.1: Validar variáveis de ambiente obrigatórias (`LANGSMITH_API_KEY`) via `check_env_vars`.
  - Subtask 2.1.2: Implementar a função `pull_prompts_from_langsmith()`:
    - Fazer download do prompt `leonanluppi/bug_to_user_story_v1` usando `hub.pull`.
    - Extrair mensagens (system e user) e estruturar o dicionário de dados no padrão YAML.
    - Salvar o prompt localmente em `prompts/bug_to_user_story_v1.yml` com `save_yaml`.
  - Subtask 2.1.3: Implementar função `main()` com mensagens de status e tratamento de erros.

- **Tarefa 2.2: Execução e Validação do Pull**
  - Subtask 2.2.1: Executar `python src/pull_prompts.py`.
  - Subtask 2.2.2: Confirmar o arquivo gerado `prompts/bug_to_user_story_v1.yml`.

---

### Fase 3: Engenharia de Prompts - Otimização v2 (`bug_to_user_story_v2.yml`)

- **Tarefa 3.1: Modelagem e Redação de `prompts/bug_to_user_story_v2.yml`**
  - Subtask 3.1.1: Estruturar os metadados do YAML (`description`, `version: "v2"`, `techniques_applied`, `tags`).
  - Subtask 3.1.2: Aplicar **Role Prompting**: Senior Technical Product Manager & QA Lead.
  - Subtask 3.1.3: Aplicar **Chain of Thought (CoT)** passo a passo:
    1. Análise do relato de bug e causa raiz.
    2. Identificação do ator e valor de negócio.
    3. Formulação da User Story ("Como um... Eu quero... Para que...").
    4. Critérios de Aceitação em BDD ("Dado que... Quando... Então... E...").
    5. Contexto Técnico e tratamento de edge cases.
  - Subtask 3.1.4: Aplicar **Few-shot Learning (obrigatório)**: 2 a 3 exemplos completos cobrindo cenários simples, médios e complexos compatíveis com `datasets/bug_to_user_story.jsonl`.
  - Subtask 3.1.5: Regras estritas de formatação (Markdown, sem alucinações, sem `TODO`, separação limpa de system/user prompt).

---

### Fase 4: Testes Automatizados de Validação (`tests/test_prompts.py`)

- **Tarefa 4.1: Implementação dos 6 Testes Unitários com Pytest**
  - Subtask 4.1.1: `test_prompt_has_system_prompt` (verifica se `system_prompt` existe e não está vazio).
  - Subtask 4.1.2: `test_prompt_has_role_definition` (verifica persona/papel definido no prompt).
  - Subtask 4.1.3: `test_prompt_mentions_format` (verifica menção explícita ao formato de User Story / BDD / Markdown).
  - Subtask 4.1.4: `test_prompt_has_few_shot_examples` (verifica presença de exemplos Few-shot de entrada e saída).
  - Subtask 4.1.5: `test_prompt_no_todos` (garante ausência de `TODO` ou `[TODO]`).
  - Subtask 4.1.6: `test_minimum_techniques` (verifica se pelo menos 2 técnicas estão listadas nos metadados).

- **Tarefa 4.2: Execução e Validação dos Testes**
  - Subtask 4.2.1: Executar `pytest tests/test_prompts.py -v`.
  - Subtask 4.2.2: Garantir 100% de sucesso (6 testes passando).

---

### Fase 5: Implementação do Push de Prompts ao LangSmith Hub

- **Tarefa 5.1: Implementação de `src/push_prompts.py`**
  - Subtask 5.1.1: Validar variáveis de ambiente obrigatórias (`LANGSMITH_API_KEY` e `USERNAME_LANGSMITH_HUB`).
  - Subtask 5.1.2: Implementar `validate_prompt(prompt_data)` integrando `validate_prompt_structure()` de `src/utils.py`.
  - Subtask 5.1.3: Converter a especificação YAML em objeto `ChatPromptTemplate` do LangChain.
  - Subtask 5.1.4: Implementar `push_prompt_to_langsmith()` com identificador `{USERNAME_LANGSMITH_HUB}/bug_to_user_story_v2`, visibilidade pública (`new_repo_is_public=True`), tags e descrição.
  - Subtask 5.1.5: Implementar função `main()` com output detalhado no console.

- **Tarefa 5.2: Execução do Push e Validação no Hub**
  - Subtask 5.2.1: Executar `python src/push_prompts.py`.
  - Subtask 5.2.2: Verificar publicação pública no LangSmith Hub.

---

### Fase 6: Avaliação Automática das 5 Métricas e Iteração de Prompts

- **Tarefa 6.1: Execução da Avaliação com Gemini 2.5 Flash**
  - Subtask 6.1.1: Sincronização do dataset de 15 casos com o LangSmith (`{LANGSMITH_PROJECT}-eval`).
  - Subtask 6.1.2: Executar `python src/evaluate.py`.
  - Subtask 6.1.3: Obter notas para as 5 métricas: Helpfulness, Correctness, F1-Score, Clarity, Precision.

- **Tarefa 6.2: Ciclo de Iteração e Calibração (se necessário)**
  - Subtask 6.2.1: Analisar eventuais casos com score < 0.8 através do Tracing do LangSmith.
  - Subtask 6.2.2: Ajustar refinamentos no YAML `prompts/bug_to_user_story_v2.yml`.
  - Subtask 6.2.3: Reexecutar push (`python src/push_prompts.py`) e reavaliar (`python src/evaluate.py`).
  - Subtask 6.2.4: Atingir **todas as 5 métricas >= 0.8** e status `APROVADO`.

---

### Fase 7: Coleta de Evidências e Redação da Documentação Oficial

- **Tarefa 7.1: Redação do `README.md` Oficial da Entrega**
  - Subtask 7.1.1: Apresentação do projeto e links públicos.
  - Subtask 7.1.2: **Seção A: Técnicas Aplicadas (Fase 2)** com justificativas e exemplos práticos.
  - Subtask 7.1.3: **Seção B: Resultados Finais** com link público do LangSmith, tabela comparativa (v1 vs v2) e seções para screenshots.
  - Subtask 7.1.4: **Seção C: Como Executar** com comandos completos de ponta a ponta.
  - Subtask 7.1.5: **Seção D: Evidências no LangSmith** (dataset de 15 exemplos, execuções v2 com notas >= 0.8, tracing de 3 exemplos).

- **Tarefa 7.2: Verificação Final e Preparação para Git**
  - Subtask 7.2.1: Executar novamente os testes com `pytest`.
  - Subtask 7.2.2: Verificar `git status` e integridade geral do repositório.
