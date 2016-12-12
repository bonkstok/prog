from sqlalchemy import *

db = create_engine('sqlite:///tutorial.db')
db.echo = False
metadata = BoundMetaData(db)

users = Table('users', metadata,
	Column('user_id', Integer, primary_key=True),
	Column('name', String(40)),
	Column('age', Integer),
	Column('password', String),
	)
users.create()
i = users.insert()
i.execute(name='Mary', age=30,password='secret')
i.execute({'name' : 'Johny', 'age':42},
			{'name' : 'Susan', 'age':57},
			{'name' : 'Lieke', 'age':69})

s = users.select()
rs = s.execute()
row = rs.fetchone()
print('ID:', row[0])
print('Name:', row['name'])
print('Age:', row.age)
print('Name:', row[users.c.password])

for row in rs:
	print(row.name, 'is', row.age, 'years old')
