'''
    Exercício 1
    Crie uma lista de tuplas, onde cada tupla contém informações sobre um aluno:
    (Nome do aluno, Idade, Nota média)
    Escreva uma função chamada "alunos_aprovados" que recebe a lista de alunos e retorna
    uma nova lista apenas com os alunos que têm uma nota média maior ou igual a 7.
    Escreva uma função chamada "idade_media" que calcula a idade média de todos os alunos
    na lista.
'''


alunos = []

#listaAprovados = []

quantidadeAlunos = int(input("Informe a quantidade de alunos que deseja inserir: "))

for i in range(quantidadeAlunos):
    listaAlunos = []
    nome = input("Informe o nome do aluno: ")
    listaAlunos.append(nome)
    idade = int(input("Informe a idade do aluno: "))
    listaAlunos.append(idade)
    media = float(input("Informe a nota média do aluno: "))
    listaAlunos.append(media)
    alunos.append(tuple(listaAlunos))

print(f"Todos os alunos: {alunos}")

def alunos_aprovados(alunos):
    alunosAprovados = []
    for item in alunos:
        if item[2] >= 7:
            alunosAprovados.append(item)
    return alunosAprovados

def idade_media(alunos):
    i = 0
    for item in alunos:
        if i == 0:
            i = item[1]
        else:
            i += item[1]
        mediaIdade = i / quantidadeAlunos
    return mediaIdade

print(f"\n Alunos aprovados{alunos_aprovados(alunos)} \n Média das idades: {idade_media(alunos)}")