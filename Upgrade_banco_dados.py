from contextlib import closing
import sqlite3

def upgrade() -> None:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')

            cursor.execute('''
                CREATE TABLE Endereco(
                    cep VARCHAR (8)primary key  ,
                    lougradoro VARCHAR (45) ,
                    complemento VARCHAR (45) ,
                    bairro VARCHAR (45) ,
                    localidade VARCHAR (45) ,
                    uf VARCHAR (45) ,
                    ibge VARCHAR (45) ,
                    gia VARCHAR (45),
                    ddd VARCHAR (45),
                    siafi VARCHAR (45),
                    fk_id_usuario INTEGER NOT NULL,
                    FOREIGN KEY(fk_id_usuario) REFERENCES Usuario (id_usuario)
                    )''')
            conn.commit()


