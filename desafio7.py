# Manipulação de Dicionários/Objetos


notas = {"Lucas": 85, "Maria": 92, "Joao": 78}
aluno = input("Digite o nome do aluno: ")
if aluno in notas:
    print(f"A nota de {aluno} é {notas [aluno]}.")
else:
    print("Aluno não encontrado!")