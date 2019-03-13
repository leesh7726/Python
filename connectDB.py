import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=.;"
                        "Database=Company;"
                        "uid=sa;pwd=Pa$$w0rd")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Dept')
names = []

for row in cursor:
    print('row = %r' % (row,))
    print(type(row))
    names.append(row[1])


print(names)

cursor.execute('SELECT * FROM Dept')

names2 = [row[1] for row in cursor]
print (names2)

