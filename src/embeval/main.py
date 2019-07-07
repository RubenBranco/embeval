from embeval.core.commands import cli
from embeval.core.commands.semantic_similarity import semantic_similarity


if __name__ == "__main__":
    cli.add_command(semantic_similarity)
    cli()
