from contextlib import closing
import sqlite3

def upgrade_tabela_teste() -> None:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')

            cursor.execute('''
                CREATE TABLE Teste(
                    id_teste INTEGER primary key AUTOINCREMENT 
                    )''')
            conn.commit()
def downgrade_tabela_teste() -> None:
    with sqlite3.connect('BridgeHub.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''DROP TABLE IF EXISTS Teste''')
            conn.commit()


upgrade_tabela_teste()
downgrade_tabela_teste()