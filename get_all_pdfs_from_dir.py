import os
import sys
import shutil

target_dir = '/home/diego/tmp_pdfs_to_papers'
mendeley_dir = '/home/diego/MendeleyDesktop'

num_pdfs = 0

print('Files not pdf. To be moved manually:')

for root, subdirs, files in os.walk(mendeley_dir):
    for paper in files:
        if paper.endswith('.pdf'):
            num_pdfs+=1
        else:
            print(root, subdirs, paper)

print('---')

answer=input('Proceed to move {} pds to {}?(y/n)[n]:'.format(num_pdfs, target_dir))

num_pdfs = 0
if (answer.lower()=='y'):
    if os.path.exists(target_dir):
        print('The target directory already exists. The scripts exits without moving a single pdf.')
    else:
        try:
            os.mkdir(target_dir)
        except OSError:
            print ("Creation of the directory %s failed" % target_dir)
        else:
             print ("Successfully created the directory %s " % target_dir)

    for root, subdirs, files in os.walk(mendeley_dir):
        for paper in files:
            if paper.endswith('.pdf'):
                file_path = os.path.join(root, paper)
                target_path = os.path.join(target_dir, paper)
                print('moving {}'.format(file_path))
                shutil.move(file_path, target_path)
                num_pdfs+=1

for root, subdirs, files in os.walk(mendeley_dir, topdown=False):
    if not subdirs and not files:
        os.rmdir(root)


print('{} pdfs moved!'.format(num_pdfs))
print('Empty directories were removed.')
