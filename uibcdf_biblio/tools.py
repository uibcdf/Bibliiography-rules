
def set_keys_in_bib_file(input_file, output_file=None):

    from pybtex.database import parse_file
    from .keys import uibcdf_key
    from ._private_tools.file import output_file_from_input_file

    if output_file is None:
        output_file = output_file_from_input_file(input_file)

    bd = parse_file(input_file)

    for entry in list(bd.entries.keys()):

        new_key = uibcdf_key(bd.entries[entry])

        if new_key is not None:

            bd.entries[entry].key = new_key
            bd.add_entry(new_key, bd.entries.pop(entry))

    bd.to_file(output_file)

