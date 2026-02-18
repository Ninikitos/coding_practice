# __new__ dunder method is called before the class is being created.
# The most common use is to implement a Singleton pattern (one instance of class can exist)

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = None

    def connect(self):
        print(f'Connecting... User:{self.user} Password: {self.psw} Port: {self.port}')

    def close(self):
        print('Connection closed...')

    def read(self) -> str:
        return 'Data from DB'

    def write(self, data: str):
        return f'Writing {data} to BD...'

db = DataBase('root', '1234', 80)
db2 = DataBase('user_1', '4321', 73)

print(id(db))
print(id(db2))

# This Singleton implementation has a bug, db2 init values will be used
# even though db was the first one who was created.
db.connect()
db2.connect()