import socket
import os

HOST = "127.0.0.1"
PORTA = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))

while True:
    print("\n1 - Enviar arquivo")
    print("2 - Listar arquivos")
    print("3 - Baixar arquivo")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        caminho = input("Arquivo: ")

        if os.path.exists(caminho):
            nome = os.path.basename(caminho)
            tamanho = os.path.getsize(caminho)

            cliente.sendall(f"ENVIAR|{nome}".encode())
            cliente.sendall(str(tamanho).encode())

            with open(caminho, "rb") as arquivo:
                while True:
                    dados = arquivo.read(4096)

                    if not dados:
                        break

                    cliente.sendall(dados)

            print(cliente.recv(1024).decode())

        else:
            print("Arquivo não encontrado.")

    elif opcao == "2":
        cliente.sendall(b"LISTAR")

        arquivos = cliente.recv(4096).decode()

        print("\nArquivos disponíveis:")

        if arquivos:
            print(arquivos)
        else:
            print("Nenhum arquivo disponível.")

    elif opcao == "3":
        nome = input("Nome do arquivo: ")

        cliente.sendall(f"BAIXAR|{nome}".encode())

        resposta = cliente.recv(1024).decode()

        if resposta == "ERRO":
            print("Arquivo não encontrado.")

        else:
            tamanho = int(resposta)

            with open("download_" + nome, "wb") as arquivo:
                recebido = 0

                while recebido < tamanho:
                    dados = cliente.recv(min(4096, tamanho - recebido))

                    if not dados:
                        break

                    arquivo.write(dados)
                    recebido += len(dados)

            print("Download concluído.")

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")

cliente.close()
