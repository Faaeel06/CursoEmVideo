# Crie um programa que leia as duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
# - Média abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print(f'{"=" * 20:>}', 'SISTEMA DE APRROVAÇAO DE ALUNOS', f'{"=" * 20:>}')

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 5.0:
    print(f'Sua nota final é {media:.2f}. REPROVADO.')
elif 5.0 <= media < 7.0:
    print(f'Sua nota final foi {media:.2f}. RECUPERAÇÃO.')
else:
    print(f'Sua nota final foi {media:.2f}. APROVADO.')
