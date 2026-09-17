import socket
import os

HOST = "0.0.0.0"
PORTA = 5000
PASTA = "arquivos"

os.makedirs(PASTA, exist_ok=True)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen()

print(f"Servidor iniciado na porta {PORTA}")

while True:
    conexao, endereco = servidor.accept()
    print(f"Cliente conectado: {endereco}")

    while True:
        comando = conexao.recv(1024).decode()

        if not comando:
            break

        if comando == "LISTAR":
            arquivos = os.listdir(PASTA)
            conexao.sendall("\n".join(arquivos).encode())

        elif comando.startswith("ENVIAR|"):
            nome = comando.split("|", 1)[1]
            tamanho = int(conexao.recv(1024).decode())

            caminho = os.path.join(PASTA, nome)

            with open(caminho, "wb") as arquivo:
                recebido = 0

                while recebido < tamanho:
                    dados = conexao.recv(min(4096, tamanho - recebido))

                    if not dados:
                        break

                    arquivo.write(dados)
                    recebido += len(dados)

            conexao.sendall(b"OK")

        elif comando.startswith("BAIXAR|"):
            nome = comando.split("|", 1)[1]
            caminho = os.path.join(PASTA, nome)

            if os.path.exists(caminho):
                tamanho = os.path.getsize(caminho)

                conexao.sendall(str(tamanho).encode())

                with open(caminho, "rb") as arquivo:
                    while True:
                        dados = arquivo.read(4096)

                        if not dados:
                            break

                        conexao.sendall(dados)
            else:
                conexao.sendall(b"ERRO")

    conexao.close()
    print("Cliente desconectado.")
