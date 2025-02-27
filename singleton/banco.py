import os
from pymongo import MongoClient
from dotenv import load_dotenv

class Banco:
    _instance = None #armazena a instancia que deve ser unica

    def __new__(cls):
        if not cls._instance:
            load_dotenv()
            try:
                cls._instance = super(Banco, cls).__new__(cls)
                cls._instance._client = MongoClient(
                    host=os.getenv("host"),
                    port=int(os.getenv("PORT")),
                    username=os.getenv("USER"),
                    password=os.getenv("PASSWORD")
                )
                database_name = os.getenv('DATABASE')
                cls._instance._db = cls._instance._client[database_name]
            except Exception as e:
                print(e)
                return None
        return cls._instance
    

if __name__ == '__main__':
    """
    Criamos dois objetos de conexao ao MongoDB
    cada print irá exibir o objeto e seu endereço de memória
    ambos objetos vão estar no mesmo endereco de memória por conta o padrao Singleton
    """
    con1 = Banco()
    print(con1)
    con2 = Banco()
    print(con2)