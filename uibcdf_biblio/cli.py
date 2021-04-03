import click
from . import tools

@click.group()
def main():
    """
    Simple CLI for UIBCDF_biblio
    """
    pass

@main.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('output_file', '-to', type=click.Path(exists=False))
def set_keys(input_file, output_file=None):
    return tools.set_keys_in_bib_file(input_file, output_file)


if __name__ == "__main__":
    main()


