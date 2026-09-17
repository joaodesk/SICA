# SiCA - Sistema de Compartilhamento de Arquivos

## Descrição

O SiCA é uma aplicação cliente-servidor desenvolvida em Python para compartilhamento de arquivos através de uma rede de computadores.

A comunicação entre cliente e servidor é realizada utilizando sockets TCP.

## Funcionalidades

* Envio de arquivos para o servidor;
* Listagem dos arquivos armazenados no servidor;
* Download de arquivos;
* Comunicação através do protocolo TCP.

## Tecnologias utilizadas

* Python
* Sockets TCP
* Sistema cliente-servidor

## Estrutura do projeto

```text
SICA/
├── servidor.py
├── cliente.py
├── README.md
└── arquivos/
```

## Como executar

Primeiro, execute o servidor:

```bash
python servidor.py
```

Depois, em outro terminal, execute o cliente:

```bash
python cliente.py
```

O cliente apresentará um menu com as opções de enviar, listar e baixar arquivos.

## Funcionamento

O servidor permanece aguardando conexões na porta 5000. Após a conexão, o cliente pode enviar comandos para solicitar as operações disponíveis.

No envio, o arquivo é transmitido pelo socket TCP e armazenado na pasta `arquivos` do servidor.

Na listagem, o servidor retorna os nomes dos arquivos armazenados.

No download, o servidor envia o tamanho e posteriormente os dados do arquivo solicitado para o cliente.

## Execução em computadores diferentes

Quando cliente e servidor estiverem em computadores diferentes, o valor de `HOST` no arquivo `cliente.py` deve ser alterado para o endereço IP do computador que está executando o servidor.

Exemplo:

```python
HOST = "192.168.0.100"
```

O servidor deve estar em execução antes da conexão do cliente.
