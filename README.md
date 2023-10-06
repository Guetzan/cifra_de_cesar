# Adaptação da Cifra de César

Um algoritmo que implementa uma simples adaptação da Cifra de César. Capaz de realizar a criptografia, descriptografia e bruteforce em uma string de até 128 caracteres.

### Como é feito?

A transposição é feita com base nos endereços decimais de cada caractere no padrão de codificaçao de caracteres UNICODE. Para isso, está sendo utilizado os caracteres contidos nos endereços de 92 a 126, classificados como "Latino Básico". Onde contém todas letras de A-Z, números de 0-9 e algumas pontuações e símbolos essenciais. Também os caracteres de 160 a 255, classificados como "Suplemento Latino-1", onde se encontram alguns caracteres muito importantes para a língua portuguesa, como o Ç, Õ, Ã, e assim por diante.

Todos os caracteres serão transpostos em seus devidos "grupos", assim caracteres que fazem parte do "Latino Básico" só serão transpostos entre si, ou seja, um "A" nunca será substítuido por um "Ç", pois são classificados em grupos distintos, "Latino Básico" e "Suplemento Latino-1". Para simplificar, segue o exemplo abaixo utilizando um shift (transposição) de 5 caracteres:

![diagrama de exemplificação](https://github.com/Guetzan/cifra_de_cesar/blob/main/diagrama_readme.png)

No exemplo acima o caractere “ÿ” está sendo transposto 5 posições a frente, porém ele é o último em seu grupo, dada a situação, ao invés ser substituido pelo quinto elemento contido no grupo “Latino Básico”, o algoritmo desenvolvido fará com que ele seja substituído pelo quinto elemento dentro de seu próprio grupo, que nesse caso, será o caractere “¤” de endereço 164.