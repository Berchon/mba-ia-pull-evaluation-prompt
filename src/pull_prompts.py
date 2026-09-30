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
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()


def pull_prompts_from_langsmith():
    """
    Faz download do prompt v1 do LangSmith Hub.

    Returns:
        ChatPromptTemplate baixado ou None em caso de falha.
    """
    prompt_name = "leonanluppi/bug_to_user_story_v1"
    print(f"Baixando prompt do LangSmith Hub: {prompt_name}...")

    try:
        prompt = hub.pull(prompt_name)
        print(f"✓ Prompt '{prompt_name}' baixado com sucesso!")
        return prompt
    except Exception as e:
        print(f"❌ Erro ao baixar prompt '{prompt_name}': {e}")
        return None


def main():
    """Função principal"""
    print_section_header("PULL DE PROMPTS DO LANGSMITH HUB")

    if not check_env_vars(["LANGSMITH_API_KEY"]):
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
