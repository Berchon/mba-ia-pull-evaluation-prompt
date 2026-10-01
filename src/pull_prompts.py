"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def fetch_prompt_from_hub(prompt_name: str) -> Optional[ChatPromptTemplate]:
    """
    Busca um prompt remoto no LangSmith Prompt Hub com tratamento de erros de API/rede.
    """
    print(f"Baixando prompt do LangSmith Hub: {prompt_name}...")
    try:
        prompt = hub.pull(prompt_name)
        print(f"✓ Prompt '{prompt_name}' baixado com sucesso!")
        return prompt
    except Exception as e:
        error_msg = str(e).lower()
        if "404" in error_msg or "not found" in error_msg:
            print(f"❌ Erro: Prompt '{prompt_name}' não encontrado no LangSmith Hub (404).")
        elif "401" in error_msg or "unauthorized" in error_msg:
            print("❌ Erro de autenticação: LANGSMITH_API_KEY inválida ou sem permissão (401).")
        else:
            print(f"❌ Erro de conexão/API ao baixar '{prompt_name}': {e}")
        return None


def extract_prompt_data(prompt: ChatPromptTemplate) -> Optional[Dict[str, Any]]:
    """
    Extrai mensagens (system e user) do ChatPromptTemplate e formata o dicionário para YAML.
    """
    try:
        if not hasattr(prompt, "messages") or not prompt.messages:
            print("❌ Erro: Objeto de prompt não contém mensagens válidas.")
            return None

        system_prompt = ""
        user_prompt = ""

        for message in prompt.messages:
            template_text = getattr(getattr(message, "prompt", None), "template", "")
            msg_type = message.__class__.__name__.lower()
            if "system" in msg_type:
                system_prompt = template_text
            elif "human" in msg_type or "user" in msg_type:
                user_prompt = template_text

        return {
            "bug_to_user_story_v1": {
                "description": "Prompt para converter relatos de bugs em User Stories",
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "version": "v1",
                "created_at": "2025-01-15",
                "tags": ["bug-analysis", "user-story", "product-management"],
            }
        }
    except Exception as e:
        print(f"❌ Erro ao extrair dados do prompt: {e}")
        return None


def save_prompt_file(prompt_data: Dict[str, Any], output_path: str) -> bool:
    """
    Salva os dados do prompt formatados em arquivo YAML no disco.
    """
    try:
        print(f"Salvando prompt em {output_path}...")
        if save_yaml(prompt_data, output_path):
            print(f"✓ Prompt salvo com sucesso em: {output_path}")
            return True
        else:
            print(f"❌ Falha ao salvar arquivo YAML em: {output_path}")
            return False
    except Exception as e:
        print(f"❌ Erro inesperado ao gravar arquivo em '{output_path}': {e}")
        return False


def pull_prompts_from_langsmith() -> bool:
    """
    Orquestra o fluxo de download, extração e salvamento do prompt v1.
    """
    prompt_name = "leonanluppi/bug_to_user_story_v1"
    output_path = "prompts/bug_to_user_story_v1.yml"

    # 1. Busca o prompt remoto no LangSmith Hub
    prompt = fetch_prompt_from_hub(prompt_name)
    if not prompt:
        return False

    # 2. Extrai mensagens e formata a estrutura de dados
    prompt_data = extract_prompt_data(prompt)
    if not prompt_data:
        return False

    # 3. Salva o prompt formatado em arquivo YAML local
    return save_prompt_file(prompt_data, output_path)


def main():
    """Função principal"""
    print_section_header("PULL DE PROMPTS DO LANGSMITH HUB")

    if not check_env_vars(["LANGSMITH_API_KEY"]):
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
