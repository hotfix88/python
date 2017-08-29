#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Author:      fyso@163.com
 DateTime:    2017-08-29 22:05:58
 Description: Description
"""
__author__ = 'FengYang'


# 有了PIL，处理图片易如反掌。随便找个图片生成缩略图：
from PIL import Image

im = Image.open('Rushmore.jpg')
print im
print im.format, im.size, im.mode

im.thumbnail((400, 200))
im.save('thumb.jpg', 'JPEG')


im = Image.open('thumb.jpg')
print im
print im.format, im.size, im.mode

# 其他常用的第三方库还有MySQL的驱动：MySQL-python，
# 用于科学计算的NumPy库：numpy，
# 用于生成文本的模板工具Jinja2，等等。
# 

import numpy as np

import mysql

import jinja2





# 如果我们要添加自己的搜索目录，有两种方法：
import sys
print sys.path
#一是直接修改sys.path，添加要搜索的目录 这种方法是在运行时修改，运行结束后失效。
sys.path.append('c:\\temp')
print sys.path

# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。



'''
# D:\Git\python\lxf\ch05module>pip list
 
adodbapi (2.6.0.7)
alabaster (0.7.6)
astroid (1.3.6)
Babel (2.1.1)
backports-abc (0.4)
backports.ssl-match-hostname (3.4.0.2)
baresql (0.7.2)
bcolz (0.11.4)
beautifulsoup4 (4.4.1)
blaze (0.8.3)
blosc (1.2.8)
bloscpack (0.9.0)
bokeh (0.10.0)
Bottleneck (1.0.0)
bqplot (0.4.2)
brewer2mpl (1.4.1)
castra (0.1.6)
certifi (2015.9.6.1)
cffi (1.3.0)
click (5.0)
colorama (0.3.3)
configparser (3.5.0b2)
cvxopt (1.1.7)
cx-Freeze (4.3.4)
cycler (0.9.0)
cyordereddict (0.2.2)
Cython (0.23.4)
cytoolz (0.7.4)
dask (0.7.5)
datashape (0.4.7)
db.py (0.4.4)
decorator (4.0.4)
dill (0.2.4)
docopt (0.6.2)
docutils (0.12)
enum34 (1.0.4)
Flask (0.10.1)
formlayout (1.0.15)
funcsigs (0.4)
functools32 (3.2.3.post2)
greenlet (0.4.9)
guidata (1.7.0b6)
guiqwt (3.0.0b7)
h5py (2.5.0)
holoviews (1.3.2)
husl (4.0.3)
ipykernel (4.1.1)
ipyparallel (4.0.2)
ipython (4.0.0)
ipython-genutils (0.1.0)
ipython-sql (0.3.7.1)
ipywidgets (4.1.0)
itsdangerous (0.24)
jedi (0.8.1)
Jinja2 (2.8)
joblib (0.9.2)
jsonschema (2.5.1)
julia (0.1.1.8)
jupyter (1.0.0)
jupyter-client (4.1.1)
jupyter-console (4.0.3)
jupyter-core (4.0.6)
Keras (0.2.0)
llvmlite (0.6.0)
lmfit (0.9.1)
locket (0.2.0)
logilab-common (1.1.0)
lxml (3.4.4)
Markdown (2.6.2)
MarkupSafe (0.23)
matplotlib (1.5.0rc3)
mingwpy (0.1.0b3)
mistune (0.7.1)
mpld3 (0.2)
multipledispatch (0.4.8)
mysql-connector-python (2.0.4)
nbconvert (4.0.0)
nbformat (4.0.1)
netCDF4 (1.2.1)
networkx (1.10)
nltk (3.0.5)
nose (1.3.7)
notebook (4.0.6)
numba (0.20.0)
numexpr (2.4.4)
numpy (1.9.3)
numpydoc (0.5)
oct2py (3.3.3)
odo (0.3.4)
pandas (0.17.0)
pandas-datareader (0.2.0)
param (1.3.2)
partd (0.3.2)
path.py (8.1.2)
patsy (0.4.0)
pep8 (1.6.2)
pg8000 (1.10.2)
pickleshare (0.5)
Pillow (3.0.0)
pip (9.0.1)
pkginfo (1.2.1)
prettytable (0.7.2)
psutil (3.2.2)
PuLP (1.5.9)
py (1.4.30)
PyAudio (0.2.9)
pybars3 (0.9.1)
pycparser (2.14)
pyflakes (0.9.2)
Pygments (2.0.2)
pylint (1.4.3)
PyMeta3 (0.5.1)
pymongo (3.0.3)
pyodbc (3.0.10)
PyOpenGL (3.1.1b1)
pyparsing (2.0.3)
PyQt4 (4.11.4)
PyQtdesignerplugins (1.1)
pyqtgraph (0.9.10)
PyQwt (5.2.1)
pyserial (2.7)
pystache (0.5.4)
pytest (2.8.2)
python-dateutil (2.4.2)
python-hdf4 (0.9)
PythonQwt (0.4.0)
pytz (2015.6)
pywin32 (219)
PyYAML (3.11)
pyzmq (14.7.0)
qtconsole (4.1.0)
redis (2.10.3)
reportlab (3.2.0)
requests (2.8.1)
requests-toolbelt (0.4.0)
rope (0.10.2)
rpy2 (2.7.2)
Rx (1.2.3)
scikit-image (0.11.3)
scikit-learn (0.16.1)
scilab2py (0.6)
scipy (0.16.1)
seaborn (0.7.0.dev0)
setuptools (18.4)
simplegeneric (0.8.1)
simplejson (3.8.0)
singledispatch (3.4.0.3)
six (1.10.0)
snowballstemmer (1.2.0)
Sphinx (1.3.1)
sphinx-rtd-theme (0.1.9)
spyder (3.0.0.dev0)
SQLAlchemy (1.0.9)
sqlite-bro (0.8.10)
sqlparse (0.1.16)
statsmodels (0.6.1)
sympy (0.7.6.1)
tables (3.2.2)
Theano (0.7.0)
toolz (0.7.4)
tornado (4.2.1)
traitlets (4.0.0)
twine (1.6.3)
twitter (1.17.1)
ViTables (2.1)
Werkzeug (0.10.4)
wheel (0.26.0)
winpython (1.2)
xlrd (0.9.4)
XlsxWriter (0.7.7)
xray (0.6.1)
'''
 





























































