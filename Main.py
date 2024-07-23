import sqlite3
import os


def reset_gophish_password(db_path, username):
    # Hash pré-calculado para a senha "nova_senha"
    hashed_password = "$2a$12$LpndqJOwr9KCArLgTZjGhOc9wLEJ5ASpZHW2/15Naa51Cb6Z1fOJy"

    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Atualizar a senha do usuário
    cursor.execute("UPDATE users SET hash=? WHERE username=?", (hashed_password, username))
    conn.commit()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

    print(f"Senha para o usuário '{username}' foi resetada com sucesso.")


# Configurações
# Substitua pelo caminho absoluto correto para o arquivo gophish.db
db_path = os.path.abspath('C:/Users/WIlllllll/Documents/gophish-v0.12.1-windows-64bit (1)/gophish.db')
username = 'admin'  # Substitua pelo nome de usuário que deseja resetar a senha

# Resetar a senha
reset_gophish_password(db_path, username)
