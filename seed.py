import server
import model
import os

os.system('dropdb pt')
os.system('createdb pt')

model.connect_to_db(server.app)
model.db.create_all()

if __name__ == '__main__':
    print("we're in seed")