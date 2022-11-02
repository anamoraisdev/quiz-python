import time 
score = 0

senha = input ("Identificação:")
if senha == "maryfooti":
    print("Bem-vindo ao Quiz Classicos do cinema!")
if senha != "maryfooti":
    quit()

user = input ("Vamos começar? (sim/não):")
if user == "sim":
    print("Começando...")
    print("!!ATENÇÃO!!")
    print("Para melhor funcionamento utilize somente letras maiúsculas")
if user == "não":
    quit()

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('VALENDO!!') 
  
  
t = (5) 
countdown(int(t)) 

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")
print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual o nome do personagem principal do filme Poderoso Chefão 1? \n (A)Michael Corleone \n (B) Vitor Corleone \n(C) Sonny Corleone \n (D) Fredo Corleone ")
resposta1 = input ("resposta:")

if resposta1 == "B":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")


print ("O Quiz acabou!!! \n A sua pontuação é ...")
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
t = (5) 
countdown(int(t)) 


if score == int("10"):
    print(f"{score} de 10 perguntas")
    print("Arrasou!! Você alcançou a pontuação máxima.")
elif score >= int("7"):
    print(f"{score} de 10 perguntas")
    print("Parabéns! Voce se saiu muito bem.")
else:
    print(f"{score} de 10 perguntas")
    print("Você não alcançou pontuação suficiente para o próximo nível. Mas, não fique triste, voce pode tentar de novo reiniciando o programa.")




