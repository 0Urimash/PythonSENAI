# ================================
# PROJETO AUTOTECH - SISTEMA CLI
# Desenvolvedores:
# Nome 1 - email@senai.br
# Nome 2 - email@senai.br
# Nome 3 - email@senai.br
# ================================

# ---------- CATÁLOGO ----------
catalogo = {
    "freio": 150.0,
    "oleo": 50.0,
    "filtro": 30.0
}

# ---------- CARRINHO ----------
carrinho = []

# ---------- FUNÇÕES ----------

def calcular_desconto(total):
    """Aplica 10% de desconto para compras acima de 500"""
    if total > 500:
        return total * 0.10
    return 0


def calcular_imposto(total_com_desconto):
    """Aplica 18% de imposto (ICMS)"""
    return total_com_desconto * 0.18


def mostrar_catalogo():
    print("\n--- CATÁLOGO ---")
    for nome, preco in catalogo.items():
        print(f"{nome} - R$ {preco:.2f}")


def adicionar_peca():
    nome = input("Nome da peça: ").lower()
    try:
        preco = float(input("Preço da peça: "))
        catalogo[nome] = preco
        print("Peça adicionada com sucesso!")
    except ValueError:
        print("Preço inválido!")


def atualizar_peca():
    nome = input("Nome da peça a atualizar: ").lower()
    if nome in catalogo:
        try:
            novo_preco = float(input("Novo preço: "))
            catalogo[nome] = novo_preco
            print("Preço atualizado!")
        except ValueError:
            print("Preço inválido!")
    else:
        print("Peça não encontrada.")


def remover_peca():
    nome = input("Nome da peça a remover: ").lower()
    if nome in catalogo:
        del catalogo[nome]
        print("Peça removida!")
    else:
        print("Peça não encontrada.")


def adicionar_ao_carrinho():
    nome = input("Digite o nome da peça: ").lower()

    if nome not in catalogo:
        print("Peça não encontrada. Tente novamente.")
        return

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite apenas números!")
        return

    carrinho.append({"nome": nome, "quantidade": quantidade})
    print("Item adicionado ao carrinho!")


def ver_carrinho():
    print("\n--- CARRINHO ---")
    if not carrinho:
        print("Carrinho vazio.")
        return

    for item in carrinho:
        print(f"{item['nome']} - Quantidade: {item['quantidade']}")


def finalizar_compra():
    if not carrinho:
        print("Carrinho vazio!")
        return

    total = 0

    for item in carrinho:
        nome = item["nome"]
        quantidade = item["quantidade"]
        preco = catalogo[nome]
        total += preco * quantidade

    desconto = calcular_desconto(total)
    total_com_desconto = total - desconto
    imposto = calcular_imposto(total_com_desconto)
    total_final = total_com_desconto + imposto

    print("\n--- RESUMO DA COMPRA ---")
    print(f"Total: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Imposto: R$ {imposto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

    carrinho.clear()
    print("Compra finalizada!\n")


# ---------- MENU PRINCIPAL ----------

while True:
    print("\n===== AUTOTECH =====")
    print("1 - Ver catálogo")
    print("2 - Adicionar peça ao catálogo")
    print("3 - Atualizar peça")
    print("4 - Remover peça")
    print("5 - Adicionar ao carrinho")
    print("6 - Ver carrinho")
    print("7 - Finalizar compra")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_catalogo()

    elif opcao == "2":
        adicionar_peca()

    elif opcao == "3":
        atualizar_peca()

    elif opcao == "4":
        remover_peca()

    elif opcao == "5":
        adicionar_ao_carrinho()

    elif opcao == "6":
        ver_carrinho()

    elif opcao == "7":
        finalizar_compra()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")