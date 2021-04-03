
def output_file_from_input_file(input_file):

    from pathlib import Path

    aux = Path(input_file)
    output_file = aux.with_name(aux.stem+'_uibcdf'+aux.suffix)

    return output_file

