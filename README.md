# Custom Python
Experimenting and messing with Python (v2.7) source code, inspired by two blog posts, [Replacing import with accio: A Dive into Bootstrapping and Python's Grammar](http://mathamy.com/import-accio-bootstrapping-python-grammar.html) and [Python internals: adding a new statement to Python](http://eli.thegreenplace.net/2010/06/30/python-internals-adding-a-new-statement-to-python/).

First step is to clone and install. Details as to why we need this intermediary version of Python can be read in this [article](http://mathamy.com/import-accio-bootstrapping-python-grammar.html)
```
git clone git@github.com:dr4ke616/custom_python.git
cd intermediary_python/
./configure --with-pydebug
make clean && make -s -j2
cd bin/
export PATH=`pwd`:$PATH
```

Now we go to the my_python directory and install the new version
```
cd ../../my_python
./configure --with-pydebug
make clean && make -s -j2
cd bin/
export PATH=`pwd`:$PATH
cd ../../
```

We can test now with:
```
python test_custom_python.py
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

Checkout `test_custom_python.py` for some more examples
