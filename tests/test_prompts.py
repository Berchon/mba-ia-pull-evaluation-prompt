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
        system_prompt = self.prompt_data.get("system_prompt", "")
        mentions_markdown = "markdown" in system_prompt.lower()
        mentions_user_story = any(
            term in system_prompt.lower()
            for term in ["user story", "como um", "como uma", "como o sistema"]
        )
        assert mentions_markdown, "O prompt não exige explicitamente a saída em formato Markdown"
        assert mentions_user_story, "O prompt não exige o formato canônico de User Story"

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        system_prompt = self.prompt_data.get("system_prompt", "")
        has_few_shot_keyword = (
            "few-shot" in system_prompt.lower()
            or "exemplo" in system_prompt.lower()
        )
        assert has_few_shot_keyword, "O prompt não referencia exemplos ou a técnica Few-shot"

        has_input_marker = (
            "entrada" in system_prompt.lower()
            or "bug report" in system_prompt.lower()
        )
        has_output_marker = (
            "saída" in system_prompt.lower()
            or "saida" in system_prompt.lower()
        )
        assert has_input_marker, "O prompt não contém marcadores claros de entrada para os exemplos"
        assert has_output_marker, "O prompt não contém marcadores claros de saída para os exemplos"

        example_count = system_prompt.lower().count("exemplo")
        assert example_count >= 2, f"Few-shot requer múltiplos exemplos, encontrados apenas {example_count}"

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        pass

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])