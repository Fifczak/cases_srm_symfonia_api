import os

SERVER = os.environ.get('SERVER')
PORT = os.environ.get('PORT')
DATABASE = os.environ.get('DATABASE')
USR = os.environ.get('USR')
PWD = os.environ.get('PWD')


import pymssql  
import pandas as pd

try:
    session = pymssql.connect(server=SERVER, user=USR, password=PWD, database=DATABASE, port = PORT)  
except pymssql._pymssql.OperationalError as err:
    print(err)
    print('!!!!!!!!!!!')
    print('DATABASE CONNECTION ERROR')
    print('!!!!!!!!!!!!!')
    session = None