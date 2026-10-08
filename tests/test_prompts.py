"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"


def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestPrompts:
    def setup_method(self):
        """Prepara os dados do prompt antes de cada teste."""
        data = load_prompts(str(PROMPT_FILE))
        self.prompt_data = data.get("bug_to_user_story_v2", data)

    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "system_prompt" in self.prompt_data, "Campo 'system_prompt' não encontrado no prompt v2"
        system_prompt = self.prompt_data.get("system_prompt")
        assert system_prompt is not None, "Campo 'system_prompt' é None"
        assert isinstance(system_prompt, str), "Campo 'system_prompt' deve ser uma string"
        assert len(system_prompt.strip()) > 0, "Campo 'system_prompt' está vazio"

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        system_prompt = self.prompt_data.get("system_prompt", "")
        has_role_indicator = (
            "você é um" in system_prompt.lower()
            or "você é uma" in system_prompt.lower()
            or "role prompting" in system_prompt.lower()
        )
        assert has_role_indicator, "O prompt não contém indicador de persona/papel ('Você é um...')"

        has_persona = any(
            role in system_prompt.lower()
            for role in ["product manager", "qa lead", "tech pm"]
        )
        assert has_persona, "O prompt não define uma persona clara (ex: Product Manager, QA Lead)"

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        pass

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        pass

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        pass

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])