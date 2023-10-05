def criptografar(texto, shift):
    texto_criptografado = ''

    for caractere in texto:
        caractere_com_shift = ord(caractere) + shift #faz um shift no caractere atual

        #cria a string com o texto criptografado, concatenando o caractere atual na variavel texto_criptografado a cada iteração do for
        if ord(caractere) >= 32 and ord(caractere) <= 126:
            if caractere_com_shift > 126:
                #caso o caractere com shift ultrapasse o limite de 126, ele será subtraido para ser substituido por um caractere dentro dos limites
                #concatenando-o logo em seguida a variável texto_criptografado
                texto_criptografado += chr(caractere_com_shift - 95)
            else:
                #concatena o caractere a variável texto_criptografado, caso ele esteja dentro dos limites
                texto_criptografado += chr(caractere_com_shift)

        #criptografa todos os caracteres com endereço de 160 a 255 na tabela UNICODE
        if ord(caractere) >= 160 and ord(caractere) <= 255:
            if caractere_com_shift > 255:
                texto_criptografado += chr(caractere_com_shift - 96)
            else:
                texto_criptografado += chr(caractere_com_shift)
    
    return texto_criptografado

def descriptografar(texto, shift):
    texto_descriptografado = ''
    
    for caractere in texto:
        caractere_sem_shift = ord(caractere) - shift #faz um shift no caractere atual
        
        #descriptografa todos os caracteres com edereço de 32 a 126 na tabela UNICODE
        if ord(caractere) >= 32 and ord(caractere) <= 126:
            if caractere_sem_shift < 32:
                texto_descriptografado += chr(caractere_sem_shift + 95)
            else:
                texto_descriptografado += chr(caractere_sem_shift)

        #descriptografa todos os caracteres com edereço de 160 a 255 na tabela UNICODE
        if ord(caractere) >= 160 and ord(caractere) <= 255:
            if caractere_sem_shift < 160:
                texto_descriptografado += chr(caractere_sem_shift + 95)
            else:
                texto_descriptografado += chr(caractere_sem_shift)

    return texto_descriptografado

#realiza um bruteforce em uma string, testando shift por shift (de 5 em 5) a cada iteração do for.
def bruteforce(texto, funcao_descriptografar):
    shift_inicial = 1
    quantidades_de_shift = 6 #quantidades de shift a serem realizados no bruteforce, ou seja, inicialmente irá realizar um bruteforce começando de um shift de 1 a 5
    bruteforcing = True

    while bruteforcing:
        for shift_atual in range(shift_inicial, quantidades_de_shift):
            texto_criptografado = descriptografar(texto, shift_atual)
            print(f'Resultado com shift de {shift_atual}:\n{texto_criptografado}\n')

        print('Deseja continuar o bruteforce?')
        print('Digite [1] para sim ou qualquer outro número para não.')
        resposta = int(input('Resposta: '))

        if resposta != 1:
            bruteforcing = False
        else:
            shift_inicial += 5
            quantidades_de_shift += 5 

#função para desenhar o menu e evitar a repetição de código
def desenhar_menu():
    #menu de início
    print('--------------------------------------------')
    print('---------------Cifra de César---------------')
    print(' [1] - Criptografar   [2] - Descriptografar\n')
    print(' [3] - Bruteforce     [4] - Sair            ')
    print('--------------------------------------------')

def testar_tamanho_string(texto):
    #while que impossibiltia o usuário de passar uma string que excede o limite de 128 caracteres
    while len(texto) > 128:
        print(f'O tamanho da string ultrapassou em {len(texto) - 128} caracteres o limite de 128. Tente novamente. ')
        texto = input('Nova string: ')

    return texto

desenhar_menu()
print('Digite o número de acordo com sua escolha:')
escolha_menu = int(input('Sua escolha: '))

#um while para que o usuário possa repetir quantas operações quiser até o mesmo decidir que deseja parar
while escolha_menu != 4:
    if escolha_menu == 1:
        print('\nDigite uma string de até 128 caracteres.')
        texto_original = input('Texto original: ')

        testar_tamanho_string(texto_original)

        valor_shift = int(input('Digite o valor que será utilizado para shift: '))
        texto_criptografado = criptografar(texto_original,valor_shift)

        print('\n--------------------------------------------')
        print (f'Texto descriptografado: {texto_original}')
        print (f'Texto criptografado: {texto_criptografado}')

    if escolha_menu == 2:
        print('\nDigite uma string de até 128 caracteres.')
        texto_criptografado = input('Texto criptografado: ')

        testar_tamanho_string(texto_criptografado)

        valor_shift = int(input('Digite o valor utilizado para shift: '))
        texto_descriptografado = descriptografar(texto_criptografado,valor_shift)

        print('\n--------------------------------------------')
        print (f'Texto criptografado: {texto_criptografado}')
        print (f'Texto descriptografado: {texto_descriptografado}')

    if escolha_menu == 3:
        print('\nDigite uma string de até 128 caracteres.')
        texto_criptografado = input('Texto criptografado: ')

        testar_tamanho_string(texto_criptografado)

        bruteforce(texto_criptografado, descriptografar)

    desenhar_menu()
    print('O que deseja fazer em seguida:')
    escolha_menu = int(input('Sua escolha: '))

print('\nObrigado por utilizar!\n')