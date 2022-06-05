"""
SEGUNDA ATIVIDADE TRABALHO
LUAN MICHAEL SANTOS COUTINHO
RU: 3960563
"""

print('Bem Vindo A Lanchonete do Luan Michael Santos Coutinho - 3960563')

print('''  ********CARDAPIO********
[100] Cachorro Quente - R$9,00 1 
[101] Cachorro-Quente Duplo - R$11,00'2 
[102] X-EGG - R$12,00'3 
[103] X-SALADA - R$13,00'4 
[104] X-Bacon - R$14,00'5 
[105] X-Tudo - R$17,00'6 
[200] Refrigerante Lata - R$5,00 7 
[201] Chá Gelado - R$4,00'8 
''')


food =["100","101","102","103","104","105","200","201"]
prices =[9,11,12,13,14,17,5,4]

myorderFood=[]
myorderCost=[]
counter=0
total=0


order = input("Gostaria de fazer seu pedido? Y/N ")
if order =="N":
	exit()
else:
	print ("Ok, prossiga")

nextOrder = True

while nextOrder==True:
	foodOrder = input("Favor, coloque o codigo do seu pedido:")
	if foodOrder =="100":
		myorderFood.append(food[0])
		myorderCost.append(prices[0])
		counter=counter+1
		total=total+(prices[0])

	elif foodOrder=="101":
		myorderFood.append(food[1])
		myorderCost.append(prices[1])
		counter=counter+1
		total=total+(prices[1])

	elif foodOrder=="102":
		myorderFood.append(food[2])
		myorderCost.append(prices[2])
		counter=counter+1
		total=total+(prices[2])

	elif foodOrder=="103":
		myorderFood.append(food[3])
		myorderCost.append(prices[3])
		counter=counter+1
		total=total+(prices[3])


	elif foodOrder=="104":
		myorderFood.append(food[4])
		myorderCost.append(prices[4])
		counter=counter+1
		total=total+(prices[4])

	elif foodOrder=="105":
		myorderFood.append(food[5])
		myorderCost.append(prices[5])
		counter=counter+1
		total=total+(prices[5])

	elif foodOrder=="200":
		myorderFood.append(food[6])
		myorderCost.append(prices[6])
		counter=counter+1
		total=total+(prices[6])

	elif foodOrder=="201":
		myorderFood.append(food[7])
		myorderCost.append(prices[7])
		counter=counter+1
		total=total+(prices[7])

	else:
		print ("Não está no Menu.")
	finished = input("Já acabou de pedir? S/N")
	if finished =="N":
		nextOrder=True
	else:
		nextOrder = False

y=0

print ("Aqui está seu pedido")
print ("     ")
print ("********")
while y <counter:

	print ("Item: "+ (myorderFood[y]))
	print ("Valor: R$"+str(myorderCost[y]))
	y=y+1
print ("Você pagará: R$"+str(total))
