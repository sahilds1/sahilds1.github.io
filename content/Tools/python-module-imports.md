Title: Fixing Python module import errors using `sys.path`
Date: 2022-05-23  
Tags: python
Slug: python-module-imports
Summary: Fixing Python module import errors using `sys.path`
Status: draft


Python looks for modules in the directories listed in the variable `sys.path`

To make sure a directory is always on the Python `sys.path` list when you run Python
- Use the `PYTHONPATH` environment variable
- Make a Python package and install it

As a hack, put the directory on the Python sys.path

```
import sys
sys.path.append('code')
```

https://bic-berkeley.github.io/psych-214-fall-2016/sys_path.html