#!/usr/bin/env python

tags_file = 'tags.txt'
header_tags_file = '# Keywords to tag papers'
keywords = []

with open(tags_file) as fff:

    counter = 0
    for line in fff:
        if not line.startswith('#') and line!='\n':
            keyword = line.lower()
            if keyword not in keywords:
                keywords.append(line.lower())
                counter += 1

keywords = sorted(keywords)


with open(tags_file, "w") as fff:
    fff.write(header_tags_file)
    fff.write('')
    for keyword in keywords:
        fff.write(keyword)

print('{} keywords sorted in {}'.format(counter, tags_file))
