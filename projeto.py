listaPerguntas=["Eu deveria comer fora hoje?","Qual meu horoscopo de hoje?","Eu deveria trocar de roupa?","Qual genero de musica deveria ouvir?","Eu deveria ir jogar VideoGame?",
"Quando vai acabar as aulas do curso tecnico?","Será que vai chover hoje?","Eu deveria assistir um filme?","Quando é o dia dos finados?",
"Quantos livros tem a bíblia?","Quanto está o dólar hoje?","Quando foi proclamada a independencia do Brasil?",
"Quantos paises existem no mundo?","Será que a terra é plana?",
"Qual o tempo para cozinhar um ovo?", "Quais são as cores do arco íris?","Me conta uma piada?","Me recomenda uma musica?","Quem é o presidente do Brasil?"]
listaRespostas=["Depende, como está o clima?","Depende, qual seu signo?","Sim, ela não está apropriada com o clima de hoje!","Você deveria ouvir ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCK.","Não!! Você está em aula cara!",
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
verificacao = 0
pergunta = 1

while pergunta != 0: 
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
                    verificacao = 1
                    b = listaRespostas.index(i)
                    b1 = perguntaConvertida.index(x)
                    if b1 == 0:
                        print("Depende, como está o clima?")
                        aaa = input("")
                        if aaa.lower() == "ensolarado":
                            print("Então não saia!")
                            break
                        if aaa.lower() == "chuvoso" or aaa.lower() == "umido":
                            print("Saia, mas não esqueça do Guarda-Chuva!!")
                            break
                        else:
                            print("Saia, mas tome cuidado")
                            break
                    if b1 == 1:
                        print("Depende, qual seu signo?")
                        aaa = input("")
                        if aaa.lower() == "aries" or aaa.lower() == "áries":
                            print("Agradeça aos antepassados pela sabedoria recebida que será valorosa nestes tempos de mudanças e de provações.")
                            break
                        if aaa.lower() == "touro":
                            print("Mesmo no feriado, negociações de trabalho estarão em andamento. A semana sinaliza mudanças nas parcerias e novas conexões.")
                            break
                        if aaa.lower() == "gêmeos" or aaa.lower() == "gemeos":
                            print("Mercúrio, seu planeta regente, andando para a frente, movimentará a semana com ideias criativas e soluções originais.")
                            break
                        if aaa.lower() == "câncer" or aaa.lower() == "cancer":
                            print("Encontre um ponto de equilíbrio entre o que você deseja e o que será possível realizar neste período de restrições.")
                            break
                        if aaa.lower() == "leão" or aaa.lower() == "leao":
                            print("Semana importante na carreira. Ganhe popularidade e projeção. Mercúrio andando para a frente facilitará divulgações e comunicações de trabalho.")
                            break
                        if aaa.lower() == "virgem":
                            print("Negociações financeiras terão andamento positivo nesta semana, com Mercúrio já em movimento direto.")
                            break
                        if aaa.lower() == "libra":
                            print("Determine objetivos, planeje uma viagem com antecedência e inicie relações num novo padrão.")
                            break
                        if aaa.lower() == "escorpião" or aaa.lower() == "escorpiao":
                            print("Novidades chegarão por todos os lados, nesta semana. Pense positivo e impulsione novo projeto de trabalho.")
                            break
                        if aaa.lower() == "sagitário" or aaa.lower() == "sagitario":
                            print("Entendimento com parceiros, equipe e amizades movimentarão negócios, nesta semana.")
                            break
                        if aaa.lower() == "capricórnio" or aaa.lower() == "capricornio":
                            print("Aprove um projeto, amplie comunicações profissionais e aposte em metas mais altas. Mercúrio em movimento direto impactará diretamente na carreira.")
                            break
                        if aaa.lower() == "aquário" or aaa.lower() == "aquario":
                            print("A semana será decisiva no amor. Renove os sentimentos e aumente a confiança nos projetos da vida íntima. Mercúrio em movimento direto trará mais otimismo.")
                            break
                        if aaa.lower() == "peixes":
                            print("Decisões financeiras envolverão a família e o amor. A semana favorecerá o casamento e associações.")
                            break
                    else:
                        print(listaRespostas[b])
                        break
            break

    if verificacao == 0:
        print("A pergunta não pode ser respondida!! Favor verificar a ortografia ou a estrutura da pergunta.")
        print("Se ainda não funcionou, a pergunta pode não estar no nosso banco de dados.")
    pergunta = int(input("""Você quer fazer mais uma pergunta?
    1- Sim
    0- Não
    """))
    
