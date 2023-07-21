lista =[]
while (True):
   escolha = input("O que deseja fazer? \n  1. Adicionar um item à lista \n  2. Remover um item da lista\n  3. Sair\n")  
  
   if escolha =='1':
    item= input("Digite item para adicionar a lista: ") 
    lista.append(item)
    print("Lista atual : ",lista)
  
   elif escolha =='2':
      item= input("Digite item que deseja retirar: ") 
      if item in lista:
         lista.remove(item)
         print(f"item removido com sucesso",{item})
         print ("Lista Atual: ",lista)
      else: 
        print("Item não existe na lista!")
        print("Lista Atual:",lista)
    
    
   elif escolha == '3':
    break    


      