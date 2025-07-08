# Refreshing/Basic Knowledge - Python

Introduction to Python for Bioinformatics - available at [Refreshing/Basic Knowledge - Python](https://github.com/andersonavilasantos/pythonBasicKnowledge-).

## Objectives

This page provides essential resources for those new to Python or looking to refresh basic concepts, particularly in the context of Bioinformatics.

## Prerequisites

Basic familiarity with programming or computational logic is recommended but not required.

## Attribution

These tutorials are adapted from *Introduction to Python for Maths* by [Andreas Ernst](http://users.monash.edu.au/~andreas), originally available at [https://gitlab.erc.monash.edu.au/andrease/Python4Maths.git](https://gitlab.erc.monash.edu.au/andrease/Python4Maths.git), and from [Python4Bioinformatics](https://github.com/kipkurui/Python4Bioinformatics). The original version was written by Rajath Kumar and is available at [https://github.com/rajathkumarmp/Python-Lectures](https://github.com/rajathkumarmp/Python-Lectures).

These notes have been extensively revised and updated for the *EANBiT Introduction to Python for Bioinformatics* course facilitated by [Caleb Kibet](https://twitter.com/calkibet), Audrey Mbogho, and Anthony Etuk.

## Quick Introduction to Jupyter Notebooks

Throughout this course, we will be using Jupyter Notebooks. Although the HPC you will use already has Jupyter installed, the following instructions will help you set it up on your own computer.

### Introduction

Jupyter Notebook is an interactive computing environment that enables users to create notebooks containing comprehensive, reproducible computational records. These notebooks facilitate collaboration and may include:

* Executable code
* Interactive widgets
* Visual plots
* Descriptive text
* Mathematical equations
* Images
* Videos

The name "Jupyter" is derived from Julia, Python, and R, the primary languages supported.

Using Jupyter Notebooks enhances transparency and reproducibility, promoting open science, especially in Bioinformatics.

### Installation

1. [Download Miniconda](https://www.anaconda.com/download/) for your specific OS:

   * **Linux:** `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
   * **Mac:** `curl https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`

2. Run the installer:

   * **Linux:** `bash Miniconda3-latest-Linux-x86_64.sh`
   * **Mac:** `bash Miniconda3-latest-MacOSX-x86_64.sh`

3. Follow the installation prompts, accepting defaults if unsure.

4. Restart your terminal to complete the installation.

5. Verify the installation:

   ```
   conda list
   ```

   If the command isn't recognized, add Anaconda to your PATH:

   ```
   export PATH=~/miniconda3/bin:$PATH
   ```

Create a dedicated conda environment for reproducible analysis:

```
conda create -n summerschool python=3.11 pandas matplotlib jupyter ipykernel -y


```

Activate your environment:

```
source activate summerschool
```

Install JupyterLab:

* Using conda:

```
conda install -c conda-forge jupyterlab
```

* Using pip:

```
pip3 install jupyter
```

### Troubleshooting

* **Conda command not found:** Ensure Miniconda is added to your PATH using the command above.
* **Installation issues:** Check your internet connection, permissions, or refer to [Miniconda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

For additional help, contact Anderson Santos at [anderson.santos@ufz.de](mailto:anderson.santos@ufz.de).

### How to Learn from this Resource

Download the notebooks from [Refreshing/Basic Knowledge - Python](https://github.com/andersonavilasantos/pythonBasicKnowledge-):

```
git clone https://github.com/andersonavilasantos/pythonBasicKnowledge-.git
```

Alternatively:

```
wget https://github.com/andersonavilasantos/pythonBasicKnowledge-/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
```

Launch Jupyter Lab:

```
jupyter lab
```

Jupyter notebooks contain cells with Python code. Execute cells using `Shift-Enter` or `Ctrl-Enter`.

### Further Help

Explore the [official Jupyter introduction](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb) and [Jupyter tips](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).

A recommended introductory Python book: [Think Python](http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf).

## Python for Bioinformatics

### Introduction

Python is a user-friendly, modern programming language ideal for beginners. It is interpreted, allowing rapid development, and includes extensive libraries for scientific computing and web services.

These lectures use Jupyter notebooks, mixing Python code with explanations. Run notebooks on a web server or locally.

### Contents

This course includes several notebook-based sessions:

**Session 1**

* [01](Intro-to-Python/01.ipynb) Basic data types (numbers, strings)

**Session 2**

* [02](Intro-to-Python/02.ipynb) String manipulation
* [03](Intro-to-Python/03.ipynb) Lists and Tuples
* [04](Intro-to-Python/04.ipynb) Dictionaries

**Session 3**

* [05](Intro-to-Python/05.ipynb) Control flow (`if`, `for`, `while`, `try`)
* [06](Intro-to-Python/06.ipynb) Functions
* [07](Intro-to-Python/07.ipynb) Scripting
* [08](Intro-to-Python/08.ipynb) Data analysis with Pandas
* * [8.1](Intro-to-Python/08.1.ipynb) Data Types and Formats
* * [8.2](Intro-to-Python/08.2.ipynb) Data Workflows and Automation
* * [8.3](Intro-to-Python/08.3.ipynb) Making Plots 
* [09](Intro-to-Python/09.ipynb) Reproducible research

Quick syntax reference: [Quick Reference Card](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html).
Detailed tutorial: [Python Official Tutorial](https://docs.python.org/3/tutorial/).

## License

Licensed under the Creative Commons Attribution 3.0 Unported License. See [license details](http://creativecommons.org/licenses/by/3.0/).
