import os
import sqlite3

db = os.path.join(os.path.dirname(__file__), 'hw5_example.db')
"""
sql = '''SELECT port_number FROM ServerPorts
         INNER JOIN ServerTypes
         WHERE ServerTypes.type_name='apache';'''
"""
sql = '''
         SELECT * FROM ServerPorts
         INNER JOIN ServerTypes
         WHERE ServerTypes.type_name='apache';
'''
conn = sqlite3.connect(db)
result = conn.execute(sql).fetchall()

print(result)

conn.close()