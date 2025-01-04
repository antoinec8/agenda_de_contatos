def adicionar_contato(contatos, nome, telefone, email, favorito):
    contatos.append({"nome" : nome, "telefone" : telefone, "email" : email,
                     "favorito" : favorito})
    print("Contato adicionado!")

def lista_de_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, 1):
        check = "★" if contato["favorito"] == "1" else " "
        print(f"\nContato {indice} {check}")
        print(f"Nome: {contato["nome"]}")
        print(f"Telefone: {contato["telefone"]}")
        print(f"Email: {contato["email"]}")

def editar_contato(contatos, indice, escolha, novo):
    if escolha == 1:
        contatos[indice]["nome"] = novo
    elif escolha == 2:
        contatos[indice]["telefone"] = novo
    elif escolha == 3:
        contatos[indice]["email"] = novo
    else:
        contatos[indice]["favorito"] = novo
    print("Contato atualizado!")

def favoritar_contato(contatos, indice):
    contatos[indice]["favorito"] = "1"
    print("Contato adicionado aos favoritos!")

def contatos_favoritos(favoritos):
    print("Contatos favoritos: ")
    for indice, contato in favoritos:
        print(f"\nContato {indice} ★")
        print(f"Nome: {contato["nome"]}")
        print(f"Telefone: {contato["telefone"]}")
        print(f"Email: {contato["email"]}")

def apagar_contato(contatos, indice):
    del contatos[indice]
    print("Contato deletado!")

contatos = []

while True:

    print("\nAgenda\n")
    print("1 - Adicionar contato")
    print("2 - Lista de contatos")
    print("3 - Editar contato")
    print("4 - Favoritar contato")
    print("5 - Contatos favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")

    opcao = input("\nDigite o número da sua opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        favorito = input("Adicionar contato aos favoritos? 1 - Sim   0 - Não: ")
        while favorito != "1" and favorito != "0":
            print("\nDigite apenas 1 ou 0.")
            favorito = input("Adicionar contato aos favoritos? 1 - Sim   0 - Não: ")
        adicionar_contato(contatos, nome, telefone, email, favorito)
    
    elif opcao == "2":
        if not contatos:
            print("Nenhum contato na agenda.")
        else:
            lista_de_contatos(contatos)
    
    elif opcao == "3":
        if not contatos:
            print("Nenhum contato na agenda.")
        else:
            lista_de_contatos(contatos)
            try:
                indice = int(input("\nQual o número do contato que deseja editar? "))
                indice -= 1
                if indice >= 0 and indice < len(contatos):
                    print("O que deseja alterar? Digite apenas um número de cada vez.")
                    escolha = int(input("1 - Nome, 2 - Telefone, 3 - Email, 4 - Favorito, 5 - Sair: "))
                    try:
                        if escolha >= 1 and escolha < 6:
                            if escolha == 1:
                                novo = input("Digite o novo nome: ")
                                editar_contato(contatos, indice, escolha, novo)
                            elif escolha == 2:
                                novo = input("Digite o novo telefone: ")
                                editar_contato(contatos, indice, escolha, novo)
                            elif escolha == 3:
                                novo = input("Digite o novo email: ")
                                editar_contato(contatos, indice, escolha, novo)
                            elif escolha == 4:
                                print("Deseja adicionar o contato aos seus favoritos?")
                                novo = input("1 - Sim, 0 - Não: ")
                                while novo != "1" and novo != "0":
                                    print("\nDigite apenas 1 ou 0.")
                                    novo = input("Adicionar contato aos favoritos? 1 - Sim   0 - Não: ")
                                editar_contato(contatos, indice, escolha, novo)
                            else:
                                pass
                        else:
                            print("Por favor, digite um número de opção válido.")
                    except Exception as e:
                        print("Por favor, digite um número de opção válido.")
                else:
                   print("Por favor, digite um número de contato válido.") 
            except Exception as e:
                print("Por favor, digite um número de contato válido.")
    
    elif opcao == "4":
        if not contatos:
            print("Nenhum contato na agenda.")
        else:
            lista_de_contatos(contatos)
            try:
                indice = int(input("\nQual o número do contato que deseja favoritar? "))
                indice -= 1
                if indice >= 0 and indice < len(contatos):
                    favoritar_contato(contatos, indice)
                else:
                    print("Por favor, digite um número de contato válido.")
            except Exception as e:
                print("Por favor, digite um número de contato válido.")
    
    elif opcao == "5":
        favoritos = [(indice, contato) for indice, contato in enumerate(contatos, 1) if contato["favorito"] == "1"]
        if favoritos:
            contatos_favoritos(favoritos)
        else:
            print("Não há nenhum contato favorito!")
            
    elif opcao == "6":
        if not contatos:
            print("Nenhum contato na agenda.")
        else:
            lista_de_contatos(contatos)
            try:
                indice = int(input("\nQual o número do contato que deseja apagar? Para sair digite 0. "))
                indice -= 1
                if indice >= 0 and indice < len(contatos):
                    apagar_contato(contatos, indice)
                elif indice == -1:
                    pass
                else:
                    print("Por favor, digite um número de contato válido.")
            except Exception as e:
                print("Por favor, digite um número de contato válido.")

    elif opcao == "7":
        break

print("\nAté mais!")