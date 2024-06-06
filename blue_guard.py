"""
    O LINK DO VIDEO ESTÁ NO README! :)
"""

dados = [
    {"local": "Atlântico Norte", "temperatura": 22.4, "salinidade": 35.0, "poluicao": "Baixa", "id": 1},
    {"local": "Pacífico Sul", "temperatura": 18.7, "salinidade": 34.5, "poluicao": "Moderada", "id": 2},
    {"local": "Índico", "temperatura": 25.6, "salinidade": 36.1, "poluicao": "Alta", "id": 3}
]


def coletar_dados():
    print()
    for dado in dados:
        print(f"Local: {dado['local']} / Id: {dado['id']}\n")
        
        print(f"    Temperatura: {dado['temperatura']}°C\n    Salinidade: {dado['salinidade']}‰, \n    Poluição: {dado['poluicao']}\n".upper())

        
         
    return "--- Coleta de dados realizada com sucesso! ---"


def adicionar_dado(dado):

    # Verifica se o nosso objeto dict foi preenchido corretamente
    if(not dado['local'] or not dado['temperatura'] or not dado['salinidade'] or not dado['poluicao']):
        return "--- Solicitação Inválida ---"
    
    for dadoArmazenado in dados:
        if dadoArmazenado['local'] == dado['local']:
            return "Este local já foi adicionado."
    
    # Obtendo o ultimo ID dos dados já exitentes
    if len(dados) > 0:
        ultimoId = dados[-1]['id']
    else:
        ultimoId = 0

    # Incrementando um ao ultimo ID
    dado['id'] = ultimoId + 1

    # Adicionando o novo dado a lista
    dados.append(dado)

    return "--- Novo dado adicionado com sucesso! ---"



def alterar_dado(alteracoes: dict, id=None, local=None):

    # Verifica se o usuario enviou ao menos um parametro para realizar a busca
    if not id and not local:
        return "--- Solicitação Inválida ---"
    
    # Remove o id e o local caso sejam enviados no dict de alteracao
    alteracoes.pop('id', None)
    alteracoes.pop('local', None)

    # Obtem todas as chaves do dict
    keysAlteracao = alteracoes.keys()

    # Verificando qual dado foi solicitado a alteração
    for dado in dados:
        
        # Verifica se o dado atual e igual aos parametros solicitados
        if dado['id'] == id or dado['local'] == local:

            # Verificando cada chave de alteracao enviada e atualizando os valores do dado
            for key in keysAlteracao:
                dado[key] = alteracoes[key]

            # Para a repeticao apos a alteracao
            break

    return "--- Alteração realizada com sucesso! --- "


def remover_dado(id=None, local=None):
    
    # Tratando o nao envio de parametros para busca e remocao
    if not id and not local:
        return "--- Solicitação Inválida. ---"
    else:
        # Busca o dado
        for dado in dados:

            # Deleta o dado
            if dado["local"] == local or dado['id'] == id:
                dados.remove(dado)
                
                return "--- Dado removido com sucesso! ---"


def menu():
    while True:
        print("\nMenu:")
        print("1. Exibir dados")
        print("2. Adicionar dado")
        print("3. Remover dado")
        print("4. Atualizar dado")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print()
            print(coletar_dados())

        elif escolha == "2":
            local = input("Local: ")
            temperatura = float(input("Temperatura: "))
            salinidade = float(input("Salinidade: "))
            poluicao = input("Poluição: ")

            novoDado = {"local": local, "temperatura": temperatura, "salinidade": salinidade, "poluicao": poluicao}
            
            print()
            print(adicionar_dado(novoDado))

        elif escolha == "3":
            local = None
            id = None

            print("\nDeletar por:")
            
            print("1. Local")
            print("2. ID")

            escolha = input("Escolha um opção: ")

            if escolha == "1":
                local = input("Local a deletar: ")
            elif escolha == "2":
                id = int(input("ID a deletar: "))
            else:
                print()
                print(" --- Escolha uma opção válida. --- ")

                continue

            print()
            print(remover_dado(id, local))

        elif escolha == "4":
            local = None
            id = None

            print("\nAlterar por:")
            
            print("1. Local")
            print("2. ID")

            escolha = input("Escolha um opção: ")

            if escolha == "1":
                local = input("Local a atualizar: ")
            elif escolha == "2":
                id = int(input("ID a atualizar: "))
            else:
                print()
                print(" --- Escolha uma opção válida. --- ")

                continue
            
            temperatura = input("Nova temperatura (deixe em branco se não quiser mudar): ")
            salinidade = input("Nova salinidade (deixe em branco se não quiser mudar): ")
            poluicao = input("Nova poluição (deixe em branco se não quiser mudar): ")

            dadoAlterado = {"temperatura": temperatura if temperatura else None, "salinidade": salinidade if salinidade else None, "poluicao": poluicao if poluicao else None}

            print()
            print(alterar_dado(dadoAlterado, id, local))
        elif escolha == "5":
            break
        else:
            print()
            print(" --- Escolha uma opção válida. --- ")

menu()