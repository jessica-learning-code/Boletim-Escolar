print('-'*30)
print(f'{"Boletim Escolar":^30}')
print('-'*30)

ficha = []

while True:
    nome = str(input('Digite o nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])#adicionados na lista em formato de nome=string; nota 1 e 2=lista; media=string
    
    continuar = str(input('Deseja adicionar mais(s/n): '))
    if continuar in 'Nn':
        break

print('-'*30)
print(f'{"No.":<4}{"Nome":^15}{"Média":>6}' )
print('-'*30)

for loc, valor in enumerate(ficha):#o (loc) serve de localização entre os (No.) no boletim e o (valor) armazena os valores da (ficha) 
    print(f'{loc:<4} {valor[0]:^13} {valor[2]:>6.1f}')

print('-'*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno?(90 interrompe): '))

    if aluno == 90:
        print('------Programa encerrado------')
        break
    

    if aluno < 0 or aluno >= len(ficha):# aqui possibilita o usuário digitar apenas os números respectivos a cada aluno cadastrado
        print('Número inválido, tente novamente.')
        continue

    print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
    print('-'*30)

    
