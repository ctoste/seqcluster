.. _installation:


installation
--------

`seqcluster-helper`_ provides 
a python framework to run a whole pipeline for small RNA (miRNA + others).

Install first bcbio-nextgen and cutadapter after install conda if you want an isolate env::

    wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    bash Miniconda-latest-Linux-x86_64.sh -b -p ~/install/seqcluster/anaconda
    ~/install/seqcluster/anaconda/conda install pip
    ~/install/seqcluster/anaconda/conda install -c https://conda.binstar.org/bcbio bcbio-nextgen
    ~/install/seqcluster/anaconda/pip install cutadapt
    ~/install/seqcluster/anaconda/pip install matplotlib
    ~/install/seqcluster/anaconda/pip install -U cython


Remember to add the new python into your path every time you want to user seqcluster. 
If you already have `conda` in your system, just type::

    ~/install/seqcluster/anaconda/conda install -c https://conda.binstar.org/bcbio bcbio-nextgen

If you need to install bedtools, samtools and star, follow these steps::

   git clone https://github.com/Homebrew/linuxbrew.git  ~/install/seqcluster/linuxbrew
   cd ~/install/seqcluster/linuxbrew/bin
   ln -s `which gcc gcc-4.4`
   PATH = ~/install/seqcluster/linuxbrew/bin:$PATH
   brew tab homebrew/science
   brew tab chapmanb/homebre-cbl
   brew install bedtools
   brew install samtools
   brew install star-rna
   

Then you can get seqcluster::

    ~/install/seqcluster/anaconda/pip install seqcluster

or the developement version::

    git clone https://github.com/lpantano/seqcluster
    cd seqcluster
    ~/install/seqcluster/anaconda/python setup.py install

Link binary to brew installation or to any folder is already in your path::

    ln -s ~/install/seqcluster/anaconda/bin/seqcluster ~/install/seqcluster/linuxbrew/bin/.

You can install the python framework for the full small RNA analysis (`seqcluster-helper`_)::

    brew install https://github.com/lpantano/seqcluster-helper/blob/master/seqbuster.rb
    brew install fastqc

And finally clone this repository and type::

    python setup.py install
    ln -s ~/install/seqcluster/anaconda/bin/seqcluster-helper.py ~/install/seqcluster/linuxbrew/bin/.
    ln -s ~/install/seqcluster/anaconda/bin/seqcluster-installer.py ~/install/seqcluster/linuxbrew/bin/.


if you get problem with pythonpy: `pip install pythonpy`

Install isomiRs package for R using devtools:: 

    devtools::install_github('lpantano/isomiRs', ref='develop')

To install all packages used by the report::

    Rscript -e 'source(https://raw.githubusercontent.com/lpantano/seqcluster/master/scripts/install_libraries.R)'
    
    
.. _seqcluster-helper: https://github.com/lpantano/seqcluster-helper/blob/master/README.md


**check installation**

`seqcluster-installer.py --check` will tell you if all dependencies are installed and ready to use the framework
