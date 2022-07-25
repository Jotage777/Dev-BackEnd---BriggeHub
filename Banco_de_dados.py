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
                cursor.execute('''INSERT INTO Usuario (nome, email,telefone)
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
            if result is None:
                return {"message": "Não existe esse usuario na base de dados"}
            else:
                usuario = {}
                for i in range(len(result)):
                    usuario['id'] = result[i][0]
                    usuario['nome']=result[i][1]
                    usuario['email']=result[i][2]
                    usuario['telefone']=result[i][3]
                    return usuario


def consultar_todos_usuarios() -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario''')
            result = cursor.fetchall()
            todos_usuarios = {}
            for i in range(len(result)):
                usuario = {}
                usuario['nome'] = result[i][1]
                usuario['email'] = result[i][2]
                usuario['telefone'] = result[i][3]
                todos_usuarios['id: '+str(result[i][0])] = usuario

            return todos_usuarios

def deletar_usuario(id)->int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('''DELETE FROM Usuario WHERE id_usuario = ?''', (id,))
                conn.commit()
            except:
                return {"message": "Ocorreu um erro"}
            finally:
                return {"message": "Usuario excluido"}