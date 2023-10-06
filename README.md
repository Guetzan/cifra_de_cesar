# Adaptação da Cifra de César

Este é um algoritmo que implementa uma adaptação simples da Cifra de César, capaz de realizar criptografia, descriptografia e ataques de força bruta (brute force) em uma string com até 128 caracteres.

### Como é feito?

A substituição é realizada com base nos valores decimais de cada caractere no padrão de codificação de caracteres UNICODE. Para isso, utilizamos os caracteres que estão nos endereços de 92 a 126, classificados como "Latino Básico", que incluem todas as letras de A a Z, números de 0 a 9 e algumas pontuações e símbolos essenciais. Também usamos os caracteres de 160 a 255, classificados como "Suplemento Latino-1", onde se encontram alguns caracteres muito importantes para a língua portuguesa, como Ç, Õ, Ã, entre outros.

Todos os caracteres são substituídos dentro de seus respectivos "grupos". Isso significa que caracteres que fazem parte do "Latino Básico" só serão substituídos entre si, ou seja, um "A" nunca será substituído por um "Ç", pois eles pertencem a grupos distintos, "Latino Básico" e "Suplemento Latino-1". Para simplificar, veja o exemplo abaixo utilizando um deslocamento de 5 caracteres:

![diagrama de exemplificação](https://github.com/Guetzan/cifra_de_cesar/blob/main/diagrama_readme.png)

No exemplo acima, o caractere “ÿ” está sendo deslocado 5 posições à frente. No entanto, como ele é o último em seu grupo, em vez de ser substituído pelo quinto elemento do grupo "Latino Básico", o algoritmo desenvolvido fará com que ele seja substituído pelo quinto elemento dentro de seu próprio grupo, que, nesse caso, é o caractere “¤” com endereço 164.

Esta implementação da Cifra de César é um pouco mais segura, porém continua sendo obsoleta nos dias atuais, podendo ser decifrada em questão de segundos através de brute force, ou manualmente em poucos minutos. Desenvolvida apenas por motivos de estudo para um trabalho acadêmico envolvendo criptografia.