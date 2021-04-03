Installation
------------

The latest "stable" version of MolSysMT can be installed from the UIBCDF Anaconda channel:

```bash
conda -c uibcdf uibcdf_biblio
```

The former beta version is nothing but a quenched version from the main github repository of this project which it is done from time to time with few scruples. The raw code fully alive can be installed from this github repo as follows:

```bash
git clone https://github.com/uibcdf/UIBCDF_biblio.git
cd UIBCDF_biblio
python setup.py develop
```

In the first two cases, MolSysMT can be uninstalled with conda:

```bash
conda remove uibcdf_biblio
```

But if you installed MolSysMT straight from its github central repository, do the following to uninstall it:

```bash
pip uninstall uibcdf_biblio
```

