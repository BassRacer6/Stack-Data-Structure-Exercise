class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, item):
        self.itens.append(item)
    
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    
    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def esvaziar(self):
        self.itens.clear()
    
    def mostrar(self):
        print(self.itens)


if __name__ == '__main__':
    pilha = Pilha()
    
    while True:
        print("""O que deseja fazer?
    1- Esvaziar pilha
    2- Checar se pilha está vazia
    3- Inserir item no topo
    4- Remover item no topo
    7- Checar tamanho da pilha
    6- Sair""")
        
        opcao = input("Escolha uma opção: ")

        print("======================================================")
        match opcao:
            case '1':
                pilha.esvaziar()
                print("Pilha esvaziada.")
            case '2':
                if pilha.esta_vazia():
                    print("A pilha está vazia.")
                else:
                    print("A pilha não está vazia.")
            case '3':
                item = input("Digite o item a ser inserido no topo: ")
                print("------------------------------------------------------")
                pilha.empilhar(item)
                print(f"Item '{item}' inserido no topo da pilha.")
            case '4':
                item_removido = pilha.desempilhar()
                if item_removido:
                    print(f"Item '{item_removido}' removido do topo da pilha.")
                else:
                    print("A pilha está vazia, não há item para remover.")
            case '7':
                print(f"O tamanho da pilha é: {pilha.tamanho()}")
            case '6':
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
            
        print("======================================================")
