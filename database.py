import psycopg2

print("connecting")

### use psycopg2 to connect to our DB which hopefully is running locally on our machine 

conn = psycopg2.connect("dbname=playground user=postgres password=password")
print("connected")

### if we have a website people need to login . almost any DB has a "users" table . lets create in the DB 

