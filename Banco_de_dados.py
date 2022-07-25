from contextlib import closing
import sqlite3


def criar_BD() -> None:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')

            cursor.execute('''
                CREATE TABLE Usuario(
                    id_usuario INTEGER primary key AUTOINCREMENT ,
                    nome VARCHAR (45) NOT NULL ,
                    email VARCHAR (45) NOT NULL ,
                    telefone VARCHAR (20) NOT NULL
                    )''')
            conn.commit()
def add_usuario(nome: str, email: str, telefone: str) -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT email FROM Usuario WHERE email = ?''', (email,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Jogos (nome, email,telefone)
                VALUES(?,?,?)''', (nome, email, telefone))
                conn.commit()
            else:
                conn.commit()

def atulizar_usuario(valor, id_usuario, tipo):
    with sqlite3.connect('BridgeHub.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET nome = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''SELECT email FROM Usuario WHERE email = ?''', (valor,))
                result = cursor.fetchone()
                if result is None:
                    cursor.execute('''UPDATE Usuario SET email = ? WHERE id_usuario =?''', (valor, id_usuario,))
                    conn.commit()
                else:
                    conn.commit()

        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET telefone = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()

def consultar_usuario_id(id) -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario WHERE id_usuario = ?''', (id,))
            result = cursor.fetchall()
            id = result[0][0]
            if id is None:
                print("Não existe esse username na base de dados")
                conn.commit()
            else:
                return id
                conn.commit()

def consultar_todos_usuarios() -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario''')
            result = cursor.fetchall()
            return result
            conn.commit()

def deletar_usuario(id)->int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('''DELETE FROM Usuario WHERE id_usuario = ?''', (id,))
                conn.commit()
            except:
                print("erro")
            finally:
                print("Registro excluido")