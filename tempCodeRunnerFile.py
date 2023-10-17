    for index, caractere in enumerate(text):
        if caractere.islower():
            caractere = caractere.upper()

        shift = calcular_shift(index, caractere, chave)
        caractere_com_shift = ord(caractere) + shift

        if caractere_com_shift > 90:    
            texto_cifrado += chr(caractere_com_shift - 26)
        else:
            texto_cifrado += chr(caractere_com_shift)