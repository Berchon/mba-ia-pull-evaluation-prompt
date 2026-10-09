"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts estruturalmente
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)
"""

import os
import sys
from typing import Optional, Dict, Any, Tuple, List
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header, validate_prompt_structure

load_dotenv()


def validate_prompt(prompt_data: dict) -> Tuple[bool, List[str]]:
    """
    Valida estrutura básica e regras de negócio de um prompt.

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    if "bug_to_user_story_v2" in prompt_data:
        prompt_data = prompt_data["bug_to_user_story_v2"]

    return validate_prompt_structure(prompt_data)


def load_prompt_file(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Carrega o arquivo YAML local do prompt.

    Args:
        file_path: Caminho do arquivo YAML do prompt

    Returns:
        Dicionário com os dados do prompt ou None em caso de falha
    """
    print(f"Carregando prompt de: {file_path}...")
    prompt_data = load_yaml(file_path)
    if not prompt_data:
        print(f"❌ Falha ao carregar o arquivo YAML do prompt: {file_path}")
        return None
    return prompt_data


def validate_and_report_prompt(prompt_data: dict) -> bool:
    """
    Valida o prompt e exibe feedback formatado caso haja inconsistências.

    Args:
        prompt_data: Dicionário contendo os dados do prompt

    Returns:
        True se válido, False caso contrário
    """
    print("Validando estrutura do prompt...")
    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print("❌ Erros de validação encontrados no prompt:")
        for err in errors:
            print(f"   - {err}")
        return False

    print("✓ Estrutura do prompt validada com sucesso!")
    return True


def build_chat_prompt_template(prompt_data: dict) -> ChatPromptTemplate:
    """
    Constrói um ChatPromptTemplate do LangChain a partir dos dados do prompt.

    Args:
        prompt_data: Dicionário contendo os dados do prompt

    Returns:
        Instância de ChatPromptTemplate com system e human messages
    """
    if "bug_to_user_story_v2" in prompt_data:
        prompt_data = prompt_data["bug_to_user_story_v2"]

    system_prompt = prompt_data.get("system_prompt", "")
    user_prompt = prompt_data.get("user_prompt", "{bug_report}").strip()

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", user_prompt),
    ])


def upload_to_hub(
    repo_name: str,
    prompt_template: ChatPromptTemplate,
    description: str,
    tags: List[str]
) -> Optional[str]:
    """
    Executa a requisição de rede para publicar o prompt no LangSmith Hub.

    Args:
        repo_name: Identificador no Hub (owner/prompt_name)
        prompt_template: Objeto ChatPromptTemplate a ser publicado
        description: Descrição do repositório/prompt
        tags: Lista de tags do prompt

    Returns:
        URL do prompt publicado ou None se ocorrer erro
    """
    try:
        print(f"Enviando prompt para o LangSmith Hub: {repo_name}...")
        url = hub.push(
            repo_full_name=repo_name,
            object=prompt_template,
            new_repo_is_public=True,
            new_repo_description=description,
            tags=tags
        )
        print("✓ Push realizado com sucesso!")
        print(f"🔗 URL no Hub: {url}")
        return url
    except Exception as e:
        print(f"❌ Erro de comunicação com o LangSmith Hub ao publicar '{repo_name}': {e}")
        return None


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Prepara e publica o prompt no LangSmith Hub com verificação defensiva.

    Args:
        prompt_name: Nome do repositório/prompt (ex: 'usuario/bug_to_user_story_v2')
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    # Cláusula de guarda: validação defensiva antes do upload
    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print(f"❌ Abortando push de '{prompt_name}': dados do prompt inválidos.")
        for err in errors:
            print(f"   - {err}")
        return False

    inner_data = prompt_data.get("bug_to_user_story_v2", prompt_data)
    prompt_template = build_chat_prompt_template(inner_data)
    description = inner_data.get("description", "Prompt otimizado v2")
    tags = inner_data.get("tags", [])

    url = upload_to_hub(
        repo_name=prompt_name,
        prompt_template=prompt_template,
        description=description,
        tags=tags
    )
    return url is not None


def run_push_flow(prompt_file: str, repo_name: str) -> bool:
    """
    Orquestra o carregamento, validação e publicação do prompt no Hub.

    Args:
        prompt_file: Caminho do arquivo YAML local
        repo_name: Identificador do repositório no Hub

    Returns:
        True se o fluxo foi concluído com sucesso, False caso contrário
    """
    prompt_data = load_prompt_file(prompt_file)
    if not prompt_data:
        return False

    if not validate_and_report_prompt(prompt_data):
        return False

    return push_prompt_to_langsmith(repo_name, prompt_data)


def main() -> int:
    """Função principal que orquestra a execução do script."""
    print_section_header("PUSH DE PROMPTS AO LANGSMITH HUB")

    # 1. Validar variáveis de ambiente obrigatórias
    if not check_env_vars(["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]):
        return 1

    username = os.getenv("USERNAME_LANGSMITH_HUB")
    prompt_file = "prompts/bug_to_user_story_v2.yml"
    repo_name = f"{username}/bug_to_user_story_v2"

    try:
        success = run_push_flow(prompt_file, repo_name)
        if success:
            print("\n" + "=" * 50)
            print("✅ PUSH CONCLUÍDO COM SUCESSO!")
            print(f"Prompt publicado em: {repo_name}")
            print("=" * 50 + "\n")
            return 0
        else:
            print("\n" + "=" * 50)
            print("❌ FALHA NO PUSH DO PROMPT")
            print("Verifique os logs acima para identificar a causa.")
            print("=" * 50 + "\n")
            return 1

    except Exception as e:
        print(f"\n❌ Erro inesperado durante a execução do push: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
