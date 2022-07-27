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
                    try:
                        existe = consultar_endereco_id(id)
                        if existe != False:
                            usuario['endereco'] = existe
                    except:
                        return usuario
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
                try:
                    existe = consultar_endereco_id(result[i][0])
                    if existe != False:
                        usuario['endereco'] = existe
                except:
                    todos_usuarios['id: ' + str(result[i][0])] = usuario
                todos_usuarios['id: ' + str(result[i][0])] = usuario


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

def add_cep(cep, logradouro, complemento, bairro,localidade,uf,ibge,gia,ddd,siafi,id) -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT fk_id_usuario FROM Endereco WHERE fk_id_usuario = ?''', (id,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Endereco (cep, lougradoro,complemento,bairro,localidade,uf,ibge,gia,ddd,siafi,fk_id_usuario)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)''', (cep, logradouro, complemento,bairro,localidade,uf,ibge,gia,ddd,siafi,id))
                return {"message": "Endereco adicionado com sucesso"}
            else:
                return {"message": "Este usuario já adicionou um endereço"}

def atulizar_endereco(valor, id_usuario, tipo):
    with sqlite3.connect('BridgeHub.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''SELECT cep FROM Endereco WHERE fk_id_usuario  = ?''', (id_usuario,))
                result = cursor.fetchone()
                if result[0] == valor:
                    return False
                else:
                    cursor.execute('''UPDATE Endereco SET cep = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                    return True

        if tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET lougradoro = ? WHERE cep  =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET complemento = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 4:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET bairro  = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 5:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET localidade = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 6:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET uf = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 7:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET ibge = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 8:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET gia = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 9:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET ddd = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

        elif tipo == 10:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Endereco SET siafi = ? WHERE fk_id_usuario =?''', (valor, id_usuario,))
                conn.commit()

def consultar_endereco_id(id) -> int:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Endereco WHERE fk_id_usuario = ?''', (id,))
            result = cursor.fetchall()
            if result is None:
                return False
            else:
                endereco_usuario = {}
                for i in range(len(result)):
                    endereco_usuario['cep'] = result[i][1]
                    endereco_usuario['lougradoro']=result[i][2]
                    endereco_usuario['complemento']=result[i][3]
                    endereco_usuario['bairro']=result[i][4]
                    endereco_usuario['localidade'] = result[i][5]
                    endereco_usuario['uf'] = result[i][6]
                    endereco_usuario['ibge'] = result[i][7]
                    endereco_usuario['gia '] = result[i][8]
                    endereco_usuario['ddd'] = result[i][9]
                    endereco_usuario['siafi  '] = result[i][10]
                    return endereco_usuario