import pydbgen
from pydbgen import pydbgen
myDB=pydbgen.pydb()
myDB.gen_excel(num=15000, fields=['name','office_email','phone'], real_email=False, real_city=True, phone_simple=True, seed=None, filename='Tst.xlsx')
