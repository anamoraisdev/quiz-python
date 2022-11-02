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

print ("Qual criança de A Fantástica Fábrica de Chocolate achou o primeiro Bilhete Dourado?\n(A)Augustos Gloop\n(B)Veruca Salt\n(C)Violet Beauregarde\n(D)Mike Teave)
resposta1 = input ("resposta:")

if resposta1 == "A":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual destes filmes da Disney foi lançado primeiro?\n(A)O rei leão\n(B)Toy story\n(C)Mulan\n(D)Pocahontas")
resposta1 = input ("resposta:")

if resposta1 == "A":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Por qual destes filmes Meryl Streep NÃO ganhou um Oscar?\n(A)A dama de ferro\n(B)Kramer vs Kramer\n(C)A escolha de Sofia\n(D)Duvida")
resposta1 = input ("resposta:")

if resposta1 == "D":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual destes personagens terminou o filme/franquia ainda vivo? \n (A)Dobby-Harry Potter \n (B)Bill Muray-Zumbilândia \n(C)Xerife dewey Riley-Panico \n (D)Jenny-Forrest Gump ")
resposta1 = input ("resposta:")

if resposta1 == "C":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual foi o primeiro filme a mostrar uma descarga em um vaso sanitário?\n(A)Psicose\n(B)Casablanca \n(C)O mágico de Oz\n(D)O que terá acontecido a Baby Jane")
resposta1 = input ("resposta:")

if resposta1 == "A":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")
print ("Qual foi o primeiro filme de animação a ser indicado ao Oscar de Melhor Filme?\n(A)A pequena sereia\n(B)A viagem de Chihiro\n(C)Bambi\n(D)A bela e a Fera")
resposta1 = input ("resposta:")

if resposta1 == "D":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("Qual música Jenna Rink dançou em De Repente 30?\n(A)Ice ice baby\n(B)Jessie's Girl\n(C)Thiller\n(D)I wanna Dance with Somebody")
resposta1 = input ("resposta:")

if resposta1 == "C":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("O que tinha na caixa da cena final do filme Os 7 pecados capitais?\n(A)A caixa estava vazia\n(B)Uma bomba\n(C)Dinheiro de um roubo\n(D)A cabeça de sua esposa")
resposta1 = input ("resposta:")

if resposta1 == "D":
    print ("Correto!")
    score = score + 1 
else:
     print("Incorreto!")

print ("De qual filme é a citação: Eles me chamam de Senhor Tibbs!, de Sidney Poitier?\n(A)No calor da Noite\n(B)Adivinhe quem vem para jantar\n(C)Uma voz nas sombras\n(D)Acorrentados")
resposta1 = input ("resposta:")

if resposta1 == "A":
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




