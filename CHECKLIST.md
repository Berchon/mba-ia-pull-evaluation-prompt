# Checklist de Execução - Desafio 02

> **Diretrizes de Governança e Git (Obrigatórias):**
> 1. **Resumo Prévio e Aprovação Antes de Iniciar:** Antes de começar qualquer Task e/ou Subtask, o assistente deve OBRIGATORIAMENTE apresentar um pequeno resumo do que será implementado, devolver o controle para o usuário e aguardar a aprovação explícita para iniciar.
> 2. **Branch por Task:** Cada Tarefa (Task) é implementada OBRIGATORIAMENTE em uma branch própria criada a partir da `main` (ex: `feature/task-X.Y-<nome>`).
> 3. **Implementação Granular:** Cada item/subtask é implementado individualmente.
> 4. **Validação Antes do Commit:** Antes de commitar uma subtask/item, o desenvolvedor SEMPRE deve questionar o usuário se ele concorda com a implementação e se deseja alterar algo.
> 5. **Commit por Subtask:** A cada subtask/item aprovado, efetuar o commit na branch da feature.
> 6. **Atualização Obrigatória do Checklist por Subtask:** Após a finalização de cada subtask (e de cada item concluído), o checklist deve OBRIGATORIAMENTE ser atualizado marcando o respectivo item (`[x]`).
> 7. **Atualização Obrigatória do Checklist por Task:** Ao finalizar uma task, o checklist deve OBRIGATORIAMENTE ser atualizado registrando a conclusão da tarefa.
> 8. **Merge com a Main:** Ao finalizar todas as subtasks da Task e atualizar o checklist, realizar o merge da branch da feature com a `main`.
> 9. **Sequencialidade:** A próxima Task só inicia após o merge da Task anterior estar concluído na `main`.



---

## Fase 1: Preparação do Ambiente e Configurações

### Tarefa 1.1: Configuração do Ambiente Virtual Python (`venv`) e Instalação de Dependências
- **Branch:** `feature/task-1.1-setup-venv`
- [x] **Subtask 1.1.1:** Criar ambiente virtual em `mba-ia-pull-evaluation-prompt/venv` (`python3 -m venv venv`).
- [x] **Subtask 1.1.2:** Instalar dependências de `requirements.txt` (`pip install -r requirements.txt`).
- [x] **Subtask 1.1.3:** Validar integridade dos módulos instalados (`langchain`, `langsmith`, `langchain-google-genai`, `pytest`, `pyyaml`).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-1.1-setup-venv` na `main`.*

### Tarefa 1.2: Configuração de Variáveis de Ambiente e Credenciais (`.env`)
- **Branch:** `feature/task-1.2-env-configuration`
- [x] **Subtask 1.2.1:** Criar `.env` a partir de `.env.example`.
- [x] **Subtask 1.2.2:** Configurar credenciais do LangSmith (`LANGSMITH_TRACING`, `LANGSMITH_ENDPOINT`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`, `USERNAME_LANGSMITH_HUB`).
- [x] **Subtask 1.2.3:** Configurar credenciais do Google Gemini (`GOOGLE_API_KEY`, `LLM_PROVIDER=google`, `LLM_MODEL=gemini-3.5-flash-lite`, `EVAL_MODEL=gemini-3.5-flash-lite`).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-1.2-env-configuration` na `main`.*

### Tarefa 1.3: Organização de Arquivos e Git
- **Branch:** `feature/task-1.3-file-organization`
- [x] **Subtask 1.3.1:** Renomear `README.md` original para `INSTRUCTIONS.md` (preservando o enunciado).
- [x] **Subtask 1.3.2:** Confirmar `.gitignore` com `PLANO_DESAFIO.md`, `CHECKLIST.md` e `.env`.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-1.3-file-organization` na `main`.*

---

## Fase 2: Implementação do Pull de Prompts do LangSmith Hub

### Tarefa 2.1: Implementação Completa de `src/pull_prompts.py`
- **Branch:** `feature/task-2.1-pull-prompts-script`
- [x] **Subtask 2.1.1:** Validar variáveis de ambiente obrigatórias com `check_env_vars(["LANGSMITH_API_KEY"])`.
- [x] **Subtask 2.1.2:** Implementar `pull_prompts_from_langsmith()` baixando `leonanluppi/bug_to_user_story_v1` via `hub.pull`.
- [x] **Subtask 2.1.3:** Extrair mensagens e metadados e salvar em `prompts/bug_to_user_story_v1.yml` com `save_yaml()`.
- [x] **Subtask 2.1.4:** Implementar função `main()` com logging e tratamento de erros.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-2.1-pull-prompts-script` na `main`.*

### Tarefa 2.2: Execução e Validação do Pull
- **Branch:** `feature/task-2.2-validate-pull-execution`
- [x] **Subtask 2.2.1:** Executar `python src/pull_prompts.py`.
- [x] **Subtask 2.2.2:** Validar o arquivo gerado `prompts/bug_to_user_story_v1.yml`.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-2.2-validate-pull-execution` na `main`.*

---

## Fase 3: Engenharia de Prompts - Otimização v2 (`bug_to_user_story_v2.yml`)

### Tarefa 3.1: Modelagem e Redação de `prompts/bug_to_user_story_v2.yml`
- **Branch:** `feature/task-3.1-prompt-v2-optimization`
- [x] **Subtask 3.1.1:** Estruturar metadados do YAML (`description`, `version: "v2"`, `techniques_applied`, `tags`).
- [x] **Subtask 3.1.2:** Aplicar técnica **Role Prompting** (Senior Technical Product Manager & QA Lead).
- [x] **Subtask 3.1.3:** Aplicar técnica **Chain of Thought (CoT)** passo a passo com estrutura BDD.
- [x] **Subtask 3.1.4:** Aplicar técnica **Few-shot Learning (obrigatória)** com 2-3 exemplos completos alinhados ao dataset.
- [x] **Subtask 3.1.5:** Validação de regras (Markdown, sem `TODO`, separação limpa System/User Prompt).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-3.1-prompt-v2-optimization` na `main`.*

---

## Fase 4: Testes Automatizados de Validação (`tests/test_prompts.py`)

### Tarefa 4.1: Implementação dos 6 Testes com Pytest
- **Branch:** `feature/task-4.1-prompt-tests`
- [x] **Subtask 4.1.1:** Implementar `test_prompt_has_system_prompt`.
- [x] **Subtask 4.1.2:** Implementar `test_prompt_has_role_definition`.
- [x] **Subtask 4.1.3:** Implementar `test_prompt_mentions_format`.
- [x] **Subtask 4.1.4:** Implementar `test_prompt_has_few_shot_examples`.
- [x] **Subtask 4.1.5:** Implementar `test_prompt_no_todos`.
- [x] **Subtask 4.1.6:** Implementar `test_minimum_techniques`.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-4.1-prompt-tests` na `main`.*

### Tarefa 4.2: Execução dos Testes Automatizados
- **Branch:** `feature/task-4.2-run-validation-tests`
- [x] **Subtask 4.2.1:** Executar `pytest tests/test_prompts.py -v`.
- [x] **Subtask 4.2.2:** Garantir aprovação de 100% dos testes (6 testes passando).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-4.2-run-validation-tests` na `main`.*

---

## Fase 5: Implementação do Push de Prompts ao LangSmith Hub

### Tarefa 5.1: Implementação de `src/push_prompts.py`
- **Branch:** `feature/task-5.1-push-prompts-script`
- [x] **Subtask 5.1.1:** Validar variáveis de ambiente obrigatórias (`LANGSMITH_API_KEY`, `USERNAME_LANGSMITH_HUB`).
- [x] **Subtask 5.1.2:** Implementar `validate_prompt()` com `validate_prompt_structure()`.
- [x] **Subtask 5.1.3:** Construir `ChatPromptTemplate` a partir do YAML otimizado.
- [x] **Subtask 5.1.4:** Implementar `push_prompt_to_langsmith()` público (`new_repo_is_public=True`) no padrão `{USERNAME_LANGSMITH_HUB}/bug_to_user_story_v2`.
- [x] **Subtask 5.1.5:** Implementar função `main()` com output visual e códigos de retorno.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-5.1-push-prompts-script` na `main`.*

### Tarefa 5.2: Execução do Push e Validação no Hub
- **Branch:** `feature/task-5.2-validate-push-execution`
- [x] **Subtask 5.2.1:** Executar `python src/push_prompts.py`.
- [x] **Subtask 5.2.2:** Confirmar publicação pública no LangSmith Hub.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-5.2-validate-push-execution` na `main`.*

---

## Fase 6: Avaliação Automática das 5 Métricas e Iteração

### Tarefa 6.1: Execução da Avaliação com gemini-3.5-flash-lite
- **Branch:** `feature/task-6.1-evaluate-prompts`
- [x] **Subtask 6.1.1:** Verificar sincronização dos 15 casos do dataset com o LangSmith.
- [x] **Subtask 6.1.2:** Executar `python src/evaluate.py`.
- [x] **Subtask 6.1.3:** Analisar notas das 5 métricas (Helpfulness, Correctness, F1-Score, Clarity, Precision).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-6.1-evaluate-prompts` na `main`.*

### Tarefa 6.2: Ciclo de Iteração e Calibração (se necessário)
- **Branch:** `feature/task-6.2-prompt-refinement`
- [x] **Subtask 6.2.1:** Analisar eventuais casos com score < 0.8 via Tracing do LangSmith.
- [x] **Subtask 6.2.2:** Ajustar o prompt em `prompts/bug_to_user_story_v2.yml`.
- [x] **Subtask 6.2.3:** Reexecutar push (`python src/push_prompts.py`) e avaliação (`python src/evaluate.py`).
- [x] **Subtask 6.2.4:** Garantir **todas as 5 métricas >= 0.8** e status `APROVADO`.
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-6.2-prompt-refinement` na `main`.*

---

## Fase 7: Coleta de Evidências e Redação da Documentação Oficial

### Tarefa 7.1: Redação do `README.md` Oficial da Entrega
- **Branch:** `feature/task-7.1-official-readme`
- [x] **Subtask 7.1.1:** Criar novo `README.md` com cabeçalho e visão geral do projeto.
- [x] **Subtask 7.1.2:** Redigir **Seção A: Técnicas Aplicadas (Fase 2)** com justificativas e exemplos.
- [x] **Subtask 7.1.3:** Consolidar **Seção B: Resultados Finais** com dados reais, tabela e evidências.
  - [x] **Subtask 7.1.3.1:** Executar avaliação comparativa de `v1` e `v2` com `gemini-3.1-flash-lite` no dataset de 15 casos.
    - [x] **Subtask 7.1.3.1.1:** Confirmar configurações no `.env` (`LLM_MODEL=gemini-3.1-flash-lite`, `EVAL_MODEL=gemini-3.1-flash-lite`, credenciais do Gemini e LangSmith).
    - [x] **Subtask 7.1.3.1.2:** Apontar temporariamente `evaluate.py` para avaliar o prompt `v1` (`leonanluppi/bug_to_user_story_v1`).
    - [x] **Subtask 7.1.3.1.3:** Executar a avaliação da `v1` contra os 15 casos do dataset e registrar notas individuais e as notas médias. *(v1: Helpfulness: 0.88 | Correctness: 0.84 | F1: 0.83 | Clarity: 0.91 | Precision: 0.86 | Média: 0.8640)*
    - [x] **Subtask 7.1.3.1.4:** Restaurar `evaluate.py` para avaliar o prompt `v2` (`joao-da-silva/bug_to_user_story_v2`).
    - [x] **Subtask 7.1.3.1.5:** Executar a avaliação da `v2` contra os 15 casos e registrar as notas médias finais consolidadas. *(v2: Helpfulness: 0.92 | Correctness: 0.93 | F1: 0.95 | Clarity: 0.92 | Precision: 0.91 | Média: 0.9252)*
  - [x] **Subtask 7.1.3.2:** Atualizar a tabela comparativa e o texto da Seção B no `README.md`.
    - [x] **Subtask 7.1.3.2.1:** Atualizar a documentação no `README.md` substituindo a menção a `gemini-2.5-flash` por `gemini-3.1-flash-lite`.
    - [x] **Subtask 7.1.3.2.2:** Preencher a tabela comparativa da Seção B com os valores médios reais exatos obtidos nos 15 experimentos para v1 e v2.
    - [x] **Subtask 7.1.3.2.3:** Atualizar a análise técnica dos resultados e as variações percentuais ($\Delta$) reais entre v1 e v2.
  - [x] **Subtask 7.1.3.3:** Criar diretório `docs/images/` e registrar as imagens reais de evidência.
    - [x] **Subtask 7.1.3.3.1:** Criar fisicamente o diretório `docs/images/`.
    - [x] **Subtask 7.1.3.3.2:** Obter e salvar a captura de tela da visão geral operacional e FinOps v1 e v2 (`overview-v1.png`, `overview-v2.png`).
    - [x] **Subtask 7.1.3.3.3:** Obter e salvar a captura de tela do dataset de avaliação com os 15 casos sincronizados (`dataset.png`).
    - [x] **Subtask 7.1.3.3.4:** Obter e salvar a captura de tela do tracing detalhado de execução e evaluators (`trace-v1.png`, `trace-v2.png`) e do prompt v2 no Hub (`prompt-v2.png`).
    - [x] **Subtask 7.1.3.3.5:** Validar a renderização correta de todas as imagens no `README.md`.
  - [x] **Subtask 7.1.3.4:** Validar e atualizar as URLs do LangSmith Hub (`joao-da-silva`) e do projeto.
    - [x] **Subtask 7.1.3.4.1:** Validar a URL pública do prompt v2 no LangSmith Hub para o usuário `joao-da-silva`.
    - [x] **Subtask 7.1.3.4.2:** Identificar a URL funcional do projeto/experimento com o workspace/organização correspondente no LangSmith.
    - [x] **Subtask 7.1.3.4.3:** Atualizar os links no `README.md` e testar a acessibilidade dos links.
- [x] **Subtask 7.1.4:** Redigir **Seção C: Como Executar** com comandos e pré-requisitos completos.
- [x] **Subtask 7.1.5:** Redigir **Seção D: Evidências no LangSmith** (checklist, screenshots e traces).
- [x] *Validação com o usuário realizada antes de cada commit.*
- [x] *Merge da branch `feature/task-7.1-official-readme` na `main`.*

### Tarefa 7.2: Verificação Final e Garantia de Qualidade
- **Branch:** `feature/task-7.2-final-verification`
- [ ] **Subtask 7.2.1:** Executar `pytest tests/test_prompts.py` e validar aprovação de 100%.
- [ ] **Subtask 7.2.2:** Validar `git status` (confirmar que `.env`, `PLANO_DESAFIO.md` e `CHECKLIST.md` estão no `.gitignore` e árvore limpa).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-7.2-final-verification` na `main`.*
