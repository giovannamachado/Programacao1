def primo(n_primo, i = 2):
    if (n_primo <= 2):
        return True if(n_primo == 2) else False
    if (n_primo % i ==0):
        return False
    if (i * i > n_primo):
        return True
    return primo(n_primo,i + 1)
    
def soma(n_soma):
    if n_soma == 0:
        return 0
    else:
        return (n_soma % 10) + soma(n_soma // 10)
        
def fatorial(n_fatorial):
    if n_fatorial == 1:
        return 1
    else:
        return n_fatorial * fatorial(n_fatorial-1)

acertos = 0
erros = 0
while acertos < 3 and erros < 3:
    funcao = input()
    if funcao == 'Primo':
        numero_primo = int(input())
        if primo(numero_primo) == True:
            print(f'O número {numero_primo} é primo, continue herói!')
            acertos += 1
            erros = 0
        else:
            print('Por aqui não.')
            erros += 1
            acertos = 0
    elif funcao == 'Somar':
        numero_soma = int(input())
        if soma(numero_soma) % 2 == 0:
            print(f'O número {soma(numero_soma)} é par, siga por aqui Link!')
            acertos += 1
            erros = 0
        else:
            print('Por aqui não.')
            erros += 1
            acertos = 0
    elif funcao == 'Fatorial':
        numero_fat, previsao = input().split(' ')
        nume = int(numero_fat)
        pre = int(previsao)
        if fatorial(nume) == pre:
            print(f'A resposta é mesmo {pre} Link, esse caminho está certo!')
            acertos += 1
            erros = 0
        else:
            print('Por aqui não.')
            erros += 1
            acertos = 0
    else:
        print('Por aqui não.')
        erros += 1
        acertos = 0

if acertos == 3:
    print('Com a sua ajuda o Link finalmente conseguiu sair do labirinto!!!')
elif erros == 3:
    print('Hoje não é um bom dia para o nosso herói...')

