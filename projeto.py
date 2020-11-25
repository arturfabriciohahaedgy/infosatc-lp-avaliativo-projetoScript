listaPerguntas=["Eu deveria comer fora hoje?","Eu deveria trocar de roupa?","Qual genero de musica deveria ouvir?","Eu deveria ir jogar VideoGame?",
"Quando vai acabar as aulas do curso tecnico?","Será que vai chover hoje?","Eu deveria assistir um filme?","Quando é o dia dos finados?",
"Quantos livros tem a bíblia?","Quanto está o dólar hoje?","Quando foi proclamada a independencia do Brasil?",
"Quantos paises existem no mundo?","Será que a terra é plana?",
"Qual o tempo para cozinhar um ovo?", "Quais são as cores do arco íris?","Me conta uma piada?","Me recomenda uma musica?","Quem é o presidente do Brasil?"]
listaRespostas=["Depende, como está o clima?","Sim, ela não está apropriada com o clima de hoje!","Você deveria ouvir ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCK.","Não!! Você está em aula cara!",
"Dia 4 de Dezembro.","Sim, hoje vai chover.","Sim, assista.","2 de novembro.",
"73 livros.", "Atualmente um dolar esta no valor de 5,31 no Real brasileiro.",
"Dia 7 de setembro de 1822.","Atualmente existem 193 países internacionalmente reconhecidos.","Não, até onde eu saiba.","12 minutos.",
"O arco-íris aparece em sete cores: Violeta, anil, azul, verde, amarelo, laranja e vermelho.","Por que o penguim atirou o relogio pela janela? Porque ele queria ver o tempo voar."
,"Alvin e os Esquilos Caneta Azul","Jair Messias BOLSONAROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"]
print("""Informações sobre a formatação das perguntas:
Perguntas de especulação começam com "Será" (Exemplo: "Será que vai chuver hoje")
Perguntas de decisão começam com "Eu deveria" (Exemplo: "Eu deveria comer fora hoje?")
Perguntas de escolha entre varias começam com "Qual" (Exemplo: "Qual genero de musica deveria ouvir?")
Perguntas de data ou horario começam com "Quando" (Exemplo: "Quando foi proclamada a independencia do Brasil?")
Perguntas de quantidade começam com "Quanto" (Exemplo: "Quanto está o dollar hoje?")
Perguntas de ordem começam com "Me" (Exemplo: "Me conte uma piada?")
""")
try:
    a = input("Faça uma pergunta: ")
except ValueError:
    print("Um erro ocorreu em sua resposta.")
if a.__contains__("?") == False:
    raise Exception("Favor inserir uma pergunta!!")
perguntaConvertida = [g.lower() for g in listaPerguntas] 
for x in perguntaConvertida:
    while a.lower()==x:
        for i in listaRespostas:
            if perguntaConvertida.index(x) == listaRespostas.index(i):
                b = listaRespostas.index(i)
                b1 = perguntaConvertida.index(x)
                if b1 == 0:
                    print("Depende, como está o clima?")
                    aaa = input("")
                    if aaa == "Ensolarado" or "ensolarado" or "ENSOLARADO":
                        print("Então não saia!")
                        break
                    elif aaa == "Chuvoso" or "chuvoso" or "CHUVOSO":
                        print("Saia, mas não esqueça do Guarda-Chuva!!")
                        break
                    else:
                        print("Saia, mas tome cuidado")
                        break
                else:
                    print(listaRespostas[b])
                    break
        break