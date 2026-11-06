import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

def conectar():
    required = ("DB_USER", "DB_PASSWORD")
    missing = [name for name in required if name not in os.environ]
    if missing:
        raise RuntimeError(
            "Configure as variáveis de ambiente: " + ", ".join(missing)
        )

    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.getenv("DB_NAME", "clinica")
    )
def executar(sql, params=()):
    #Operações INSERT, UPDATE e DELETE
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(sql, params)
        conexao.commit()
        return cursor.lastrowid, cursor.rowcount
    except mysql.connector.Error as erro:
        conexao.rollback()
        print("Erro:", erro)
        return None, 0
    finally:
        cursor.close()
        conexao.close()

def consultar(sql, params=()):
    #Função destinada a consultas select
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(sql, params)
        return cursor.fetchall()
    except mysql.connector.Error as erro:
        print("Erro:", erro)
        return []
    finally:
        cursor.close()
        conexao.close()