import re

def key_uibcdf(entry):

    new_key = None

    entry_type = entry.original_type

    if entry_type=='article':

        first_family_name = entry.persons['author'][0].last_names[0]
        new_key = re.sub('[^a-zA-Z0-9_-]', '', first_family_name)

        year = entry.fields['year']
        new_key += year

        title = entry.fields['title'][1:-1]
        title_first_word = title.split(' ')[0]
        title_first_word = re.sub('[^a-zA-Z0-9_-]', '', title_first_word)
        title_alphanum = re.sub('[^a-zA-Z0-9_-]', '', title)
        new_key += title_first_word
        new_key += '_'
        new_key += title_alphanum[-2:]

        if 'doi' in entry.fields:
            doi = entry.fields['doi']
            last_part_doi = doi.split('/')[-1]
            new_key += last_part_doi[0]
            new_key += last_part_doi[-1]


    else:
        print('eh!', entry_type)

    return new_key
