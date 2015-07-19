# Custom Python
Experimenting and messing with Python source code, inspired by two blog posts, [Replacing import with accio: A Dive into Bootstrapping and Python's Grammar](http://mathamy.com/import-accio-bootstrapping-python-grammar.html) and [Python internals: adding a new statement to Python](http://eli.thegreenplace.net/2010/06/30/python-internals-adding-a-new-statement-to-python/).

Make sure to set your python path to this custom one:
```
export PATH=$PWD/my_python/bin/python:$PATH
```

### Replace `print` with `shout`:
```python
>>> print "hello"
  File "<stdin>", line 1
    print 'hello'
                ^
SyntaxError: invalid syntax

>>> shout 'hello'
hello
```
