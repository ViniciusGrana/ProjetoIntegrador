import mysql.connector
import pandas as pd


def conexao(query):
    try:
        # Estabelecendo a conexão com o banco de dados
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,  # Porta como um número inteiro
            user="root",
            password="senai@134",
            database="medidor"  # Nome do banco correto
        )

        # Executando a consulta SQL e carregando o resultado em um DataFrame
        dataframe = pd.read_sql_query(query, conn)

        # Fechando a conexão
        conn.close()

        return dataframe
    
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
