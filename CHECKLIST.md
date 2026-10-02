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
- [x] **Subtask 1.2.3:** Configurar credenciais do Google Gemini (`GOOGLE_API_KEY`, `LLM_PROVIDER=google`, `LLM_MODEL=gemini-2.5-flash`, `EVAL_MODEL=gemini-2.5-flash`).
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
- [ ] **Subtask 3.1.3:** Aplicar técnica **Chain of Thought (CoT)** passo a passo com estrutura BDD.
- [ ] **Subtask 3.1.4:** Aplicar técnica **Few-shot Learning (obrigatória)** com 2-3 exemplos completos alinhados ao dataset.
- [ ] **Subtask 3.1.5:** Validação de regras (Markdown, sem `TODO`, separação limpa System/User Prompt).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-3.1-prompt-v2-optimization` na `main`.*

---

## Fase 4: Testes Automatizados de Validação (`tests/test_prompts.py`)

### Tarefa 4.1: Implementação dos 6 Testes com Pytest
- **Branch:** `feature/task-4.1-prompt-tests`
- [ ] **Subtask 4.1.1:** Implementar `test_prompt_has_system_prompt`.
- [ ] **Subtask 4.1.2:** Implementar `test_prompt_has_role_definition`.
- [ ] **Subtask 4.1.3:** Implementar `test_prompt_mentions_format`.
- [ ] **Subtask 4.1.4:** Implementar `test_prompt_has_few_shot_examples`.
- [ ] **Subtask 4.1.5:** Implementar `test_prompt_no_todos`.
- [ ] **Subtask 4.1.6:** Implementar `test_minimum_techniques`.
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-4.1-prompt-tests` na `main`.*

### Tarefa 4.2: Execução dos Testes Automatizados
- **Branch:** `feature/task-4.2-run-validation-tests`
- [ ] **Subtask 4.2.1:** Executar `pytest tests/test_prompts.py -v`.
- [ ] **Subtask 4.2.2:** Garantir aprovação de 100% dos testes (6 testes passando).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-4.2-run-validation-tests` na `main`.*

---

## Fase 5: Implementação do Push de Prompts ao LangSmith Hub

### Tarefa 5.1: Implementação de `src/push_prompts.py`
- **Branch:** `feature/task-5.1-push-prompts-script`
- [ ] **Subtask 5.1.1:** Validar variáveis de ambiente obrigatórias (`LANGSMITH_API_KEY`, `USERNAME_LANGSMITH_HUB`).
- [ ] **Subtask 5.1.2:** Implementar `validate_prompt()` com `validate_prompt_structure()`.
- [ ] **Subtask 5.1.3:** Construir `ChatPromptTemplate` a partir do YAML otimizado.
- [ ] **Subtask 5.1.4:** Implementar `push_prompt_to_langsmith()` público (`new_repo_is_public=True`) no padrão `{USERNAME_LANGSMITH_HUB}/bug_to_user_story_v2`.
- [ ] **Subtask 5.1.5:** Implementar função `main()` com output visual e códigos de retorno.
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-5.1-push-prompts-script` na `main`.*

### Tarefa 5.2: Execução do Push e Validação no Hub
- **Branch:** `feature/task-5.2-validate-push-execution`
- [ ] **Subtask 5.2.1:** Executar `python src/push_prompts.py`.
- [ ] **Subtask 5.2.2:** Confirmar publicação pública no LangSmith Hub.
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-5.2-validate-push-execution` na `main`.*

---

## Fase 6: Avaliação Automática das 5 Métricas e Iteração

### Tarefa 6.1: Execução da Avaliação com Gemini 2.5 Flash
- **Branch:** `feature/task-6.1-evaluate-prompts`
- [ ] **Subtask 6.1.1:** Verificar sincronização dos 15 casos do dataset com o LangSmith.
- [ ] **Subtask 6.1.2:** Executar `python src/evaluate.py`.
- [ ] **Subtask 6.1.3:** Analisar notas das 5 métricas (Helpfulness, Correctness, F1-Score, Clarity, Precision).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-6.1-evaluate-prompts` na `main`.*

### Tarefa 6.2: Ciclo de Iteração e Calibração (se necessário)
- **Branch:** `feature/task-6.2-prompt-refinement`
- [ ] **Subtask 6.2.1:** Analisar eventuais casos com score < 0.8 via Tracing do LangSmith.
- [ ] **Subtask 6.2.2:** Ajustar o prompt em `prompts/bug_to_user_story_v2.yml`.
- [ ] **Subtask 6.2.3:** Reexecutar push (`python src/push_prompts.py`) e avaliação (`python src/evaluate.py`).
- [ ] **Subtask 6.2.4:** Garantir **todas as 5 métricas >= 0.8** e status `APROVADO`.
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-6.2-prompt-refinement` na `main`.*

---

## Fase 7: Coleta de Evidências e Redação da Documentação Oficial

### Tarefa 7.1: Redação do `README.md` Oficial da Entrega
- **Branch:** `feature/task-7.1-official-readme`
- [ ] **Subtask 7.1.1:** Criar novo `README.md` com cabeçalho e visão geral do projeto.
- [ ] **Subtask 7.1.2:** Redigir **Seção A: Técnicas Aplicadas (Fase 2)** com justificativas e exemplos.
- [ ] **Subtask 7.1.3:** Redigir **Seção B: Resultados Finais** com tabela comparativa v1 vs v2 e link público.
- [ ] **Subtask 7.1.4:** Redigir **Seção C: Como Executar** com comandos e pré-requisitos completos.
- [ ] **Subtask 7.1.5:** Redigir **Seção D: Evidências no LangSmith** (checklist, screenshots e traces).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-7.1-official-readme` na `main`.*

### Tarefa 7.2: Verificação Final e Garantia de Qualidade
- **Branch:** `feature/task-7.2-final-verification`
- [ ] **Subtask 7.2.1:** Executar `pytest tests/test_prompts.py` e validar aprovação de 100%.
- [ ] **Subtask 7.2.2:** Validar `git status` (confirmar que `.env`, `PLANO_DESAFIO.md` e `CHECKLIST.md` estão no `.gitignore` e árvore limpa).
- [ ] *Validação com o usuário realizada antes de cada commit.*
- [ ] *Merge da branch `feature/task-7.2-final-verification` na `main`.*
