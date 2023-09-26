print("Seja bem vindo a lanchonete do Vinicius Falcão, RU: 4045314\n")
print("================= Cardápio ===================\n")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("|CODIGO|--------- PRODUTO --------------|  VALOR | ")
print("|100|          Dogão                    |  R$9,00|")
print("|101|          Dogão Duplo              | R$11,00|")
print("|102|          X-Egg                    | R$12,00|")
print("|103|          X-Salada                 | R$13,00|")
print("|104|          X-Bacon                  | R$14,00|")
print("|105|          X-Tudo                   | R$17,00|")
print("|200|          Coca Lata 350ml          |  R$5,00|")
print("|201|           Chá Gelado              |  R$4,00|")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
#------------------------------------ definindo as variaveis de total e codigo = a 0. A variavel adicionar vai se repetir sempre no penultimo passo, perguntando se o cliente
                                      #deseja mais alguma coisa, se a resposta for não, a variavel passa a ser falsa e encerra o loop. 
                                                                                                                                   

codigo=0
total = 0
adicionar4045314 = True
#---------------------------------------------------------------------------------------------

#------------------------------- iniciando o loop, e registrando em cada ife else um codigo do menu, o valor do produto sendo adicionado a 
#                                variavel total e a variavel de repetição como false, para não encerrar o loop

while  True:
   while adicionar4045314 == True:
       codigo = input("Digite o código respectivo ao produto desejado:  ")
       if codigo == "100":
           print("Foi adicionado ao pedido um: Dogão - R$9,00")
           total = total + 9      
           adicionar4045314 = False
           print("="*80)

       elif codigo == "101":
           print("Foi adicionado ao pedido um: Dogão Duplo - R$11,00")
           total = total + 11
           adicionar4045314 = False
           print("="*80)

       elif codigo == "102":
           print("Foi adicionado ao pedido um: X-Egg - R$12,00")
           total = total + 12
           adicionar4045314 = False
           print("="*80)

       elif codigo == "103":
           print("Foi adicionado ao pedido um: X-Salada - R$13,00")
           total = total + 13
           adicionar4045314 = False
           print("="*80)

       elif codigo == "104":
           print("Foi adicionado ao pedido um: X-Bacon - R$14,00")
           total = total + 14
           adicionar4045314 = False
           print("="*80)

       elif codigo == "105":
           print("Foi adicionado ao pedido um: X-Tudo - R$17,00")
           total = total + 17
           adicionar4045314 = False
           print("="*80)

       elif codigo == "200":
           print("Foi adicionado ao pedido uma: Coca lata 350ml - R$5,00")
           total = total + 5
           adicionar4045314 = False
           print("="*80)

       elif codigo == "201":
           print("Foi adicionado ao pedido um: Chá Gelado - R$4,00")
           total = total + 4
           adicionar4045314 = False
           print("="*80)

       else:
           print("Desculpe, mas está opção não foi encontrada no cardápio")
           print("="*80)
           continue
 #---------------------------------------------------------------------------------------------

#--------------------------------------------------------------- começo da interface do programa, perguntando para o usuario se gostaria de mais alguma coisa
#                                                                se a resposta for sim, ele vai retornar o "digite o codigo desejado", caso for não, ele encerra o loop com o 
#                                                                break, e apresenta o total do pedido.

   resposta = input("Gostaria de pedir mais alguma coisa? (Por favor, responda com: Sim ou Não):    ")
   if resposta == "sim" or resposta== "Sim":
       adicionar4045314 = True                                      
   else:
       print(f"O Valor total do pedido foi de: R$ {total:.2f}")
       break
