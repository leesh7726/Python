import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=.;"
                        "Database=Company;"
                        "uid=sa;pwd=Pa$$w0rd")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Dept')

for row in cursor:
    print('row = %r' % (row,))
    print(type(row))
