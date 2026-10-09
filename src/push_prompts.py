"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header, validate_prompt_structure

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt (ex: 'usuario/bug_to_user_story_v2')
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        inner_data = prompt_data.get("bug_to_user_story_v2", prompt_data)
        prompt_template = build_chat_prompt_template(inner_data)
        description = inner_data.get("description", "Prompt otimizado v2")
        tags = inner_data.get("tags", [])

        print(f"Enviando prompt para o LangSmith Hub: {prompt_name}...")
        url = hub.push(
            repo_full_name=prompt_name,
            object=prompt_template,
            new_repo_is_public=True,
            new_repo_description=description,
            tags=tags
        )
        print(f"✓ Push realizado com sucesso!")
        print(f"🔗 URL no Hub: {url}")
        return True
    except Exception as e:
        print(f"❌ Erro ao enviar prompt '{prompt_name}' ao LangSmith Hub: {e}")
        return False



def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    # Trata tanto o formato desempacotado quanto empacotado sob o nome do prompt
    if "bug_to_user_story_v2" in prompt_data:
        prompt_data = prompt_data["bug_to_user_story_v2"]

    return validate_prompt_structure(prompt_data)


def build_chat_prompt_template(prompt_data: dict) -> ChatPromptTemplate:
    """
    Constrói um ChatPromptTemplate a partir dos dados do prompt.

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


def main():
    """Função principal que orquestra o push do prompt."""
    print_section_header("PUSH DE PROMPTS AO LANGSMITH HUB")

    # Subtask 5.1.1: Validar variáveis de ambiente obrigatórias
    if not check_env_vars(["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]):
        return 1



if __name__ == "__main__":
    sys.exit(main())
