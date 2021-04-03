from setuptools import setup, find_packages
from numpy.distutils.core import setup
from numpy.distutils.extension import Extension
#from molsysmt.version import __version__ as msm_version
#import distutils.extension

version = '0.0.1'
extensions_list=[]

setup(
    name='uibcdf_biblio',
    version=version,
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'uibcdf_biblio': 'uibcdf_biblio'},
    packages=find_packages(),
    ext_modules=extensions_list,
    package_data={'uibcdf_biblio': []},
    scripts=[],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/UIBCDF_biblio',
    license='MIT',
    description="---",
    long_description="---",
    entry_points={'console_scripts': ['uibcdf_biblio = uibcdf_biblio.cli:main']}
)

