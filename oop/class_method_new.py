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

# This is expected in this type of Singleton version.
# I didn't user __call__. Will practice that a bit later
db.connect()
db2.connect()