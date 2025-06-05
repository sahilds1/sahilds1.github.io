Title: Cheat Sheet: Virtual Environments Using Conda
Date: 2020-08-10
Tags: python
Summary: Cheat Sheet: Virtual Environments Using Conda
Status: published

`conda` is a simple tool for managing virtual environments that's 
included in the `Miniconda` Python installation for data science 

Create a new environment named py35 with Python 3.5:

```
conda create --name py35 python=3.5
```

Activate it to use the Python version within it:
```
conda activate py35
```

See a list of all the environments you've created with Conda

```
conda env list
```