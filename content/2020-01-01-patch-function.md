Title: TIL: Knowing Where to Patch
Date: 2020-01-01
Category: Today I Learned
Status: published

For writing unit tests in Python, the `unittest.mock.patch` function changes the object that a name points to with  a mock object:

```
#my_module.py

from db import db_write

def foo():
  x = db_write()
  return x

#test.py

import my_module

@patch("my_module.db_write")
def test_foo(self, mock_write):
  x = my_module.foo()
  self.assertEqual(x, 10)

```

The system we're testing can use different names for the same object so we have to ensure we patch the name it is using:

```
#my_module.py

import db

def foo():
  x = db.db_write()
  return x

#test.py

@patch("my_module.db.db_write")

```

Via: [Lisa Roach - Demystifying the Patch Function - PyCon 2018](https://www.youtube.com/watch?v=ww1UsGZV8fQ)