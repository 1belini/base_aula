# programa de calculo de media aritmetica

nome = input("Qual é o nome do aluno? ")
nota1 = int(
    input("Qual foi a nota do 1° bimestre? ")
)  # necessario colocar int na frente dos inputs, pois por padrão o input recebe string
nota2 = int(input("Qual foi a nota do 2° bimestre? "))
nota3 = int(input("Qual foi a nota do 3° bimestre? "))
nota4 = int(input("Qual foi a nota do 4° bimestre? "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(
    f"{nome}, Sua media foi de {media}"
)  # o f na frente da string é um padrão para formatar as variaveis dentro de uma string
if media >= 6:
    print(f"Parabens {nome}, voce passou de ano!")
else:
    print(f"{nome}, Voce reprovou!")
