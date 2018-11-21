## Virtuel Env
### Start the python virual enviroment (Python 3.5)
```
$ source venv/bin/activate
```

Update the virual env

```
$ curl https://bootstrap.pypa.io/get-pip.py | python
```

oder
```
$ pip install --upgrade pip
```

install Python 3.5 dependencies
```
$ pip install pytest
$ pip install sphinx
$ pip install pytest-cov Pillow wheel
```

Install pyglet Module
```
$ pip install pyglet astropy numpy
```

Quit the VM (only use if needed)
```
$ deactivate
```

### Run App Aufgabe 1
```
$ cd aufgabe_1
$ python auf1A.py 1 0 4 5
```
The programm args are the started point (x0, y0) and endpoint (x1, y1).
Possible coordinats are for the x-achses {0:5} and y-achses {0:5}.