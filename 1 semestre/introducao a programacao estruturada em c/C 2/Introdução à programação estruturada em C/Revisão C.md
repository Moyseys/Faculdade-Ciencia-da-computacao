# Revisão C

DIAGRAMAS:

![Untitled](Revisa%CC%83o%20C%20fffc472b60f941fe88d49e348e21679b/Untitled.png)

![Untitled](Revisa%CC%83o%20C%20fffc472b60f941fe88d49e348e21679b/Untitled%201.png)

IDENTIFICADORES:

São os nomes que podemos utilizar para constantes, variáveis e funções por exemplo;

VARIÁVEL:

Posição de memória que pode ser acessada através de um identificador, temos alguns tipo, como por exemplo:

char → letras e símbolos

int → números inteiros, tanto positivos quanto negativos

float e double

![Untitled](Revisa%CC%83o%20C%20fffc472b60f941fe88d49e348e21679b/Untitled%202.png)

características principais da linguagem C:

1. **Linguagem de Programação de Médio Nível**: C é uma linguagem de programação de nível intermediário, o que significa que ela fornece construções tanto de alto nível (abstratas) quanto de baixo nível (máquina específica), permitindo um controle detalhado sobre o hardware enquanto ainda oferece portabilidade.
2. **Procedimental**: C é uma linguagem de programação procedimental, o que significa que os programas são compostos de funções ou procedimentos que manipulam dados.
3. **Portátil**: Os programas em C podem ser compilados em diferentes sistemas operacionais e arquiteturas de hardware, desde que um compilador adequado esteja disponível para a plataforma de destino.
4. **Estruturada**: C oferece suporte a estruturas de controle de programação estruturada, como loops (while, for) e estruturas condicionais (if-else).
5. **Eficiente**: C é conhecida por sua eficiência e desempenho. Os programas em C têm controle direto sobre a memória e o hardware, o que permite otimizações de código de baixo nível.
6. **Tipagem Estática**: Em C, os tipos de dados são verificados em tempo de compilação, o que significa que você deve declarar o tipo de cada variável antes de usá-la.
7. **Ponto de Entrada Único**: Todo programa em C começa sua execução a partir da função **`main()`**.
8. **Sintaxe Simples e Concisa**: C tem uma sintaxe relativamente simples e concisa, o que a torna uma linguagem popular para sistemas operacionais, compiladores, sistemas embarcados e muitas outras aplicações.
9. **Suporte a Ponteiros**: C fornece suporte a ponteiros, permitindo que os programadores manipulem diretamente a memória, o que é útil para operações de baixo nível e manipulação de estruturas de dados complexas.
10. **Rica Biblioteca Padrão**: C vem com uma rica biblioteca padrão que fornece funções para realizar uma ampla variedade de tarefas, como entrada/saída, manipulação de strings, alocação de memória dinâmica, entre outras.

# C

## Constantes X Varieaveis

**Constantes:**

- Uma constante é um valor que não muda durante a execução do programa.
- Elas são úteis para armazenar valores que não devem ser alterados, como valores matemáticos fixos, configurações importantes, ou qualquer outro valor que seja constante ao longo do tempo.
- Em muitas linguagens de programação, como C, as constantes são declaradas utilizando a palavra-chave **`const`** ou diretivas do pré-processador como **`#define`**.
- Exemplo de declaração de constante em C utilizando **`const`**:
    
    ```c
    const float PI = 3.14159;
    ```
    

**Variáveis:**

- Uma variável é um local na memória do computador onde você pode armazenar e manipular dados durante a execução do programa.
- Ao contrário das constantes, o valor de uma variável pode mudar ao longo do tempo durante a execução do programa.
- As variáveis têm um tipo de dado associado que determina que tipo de valores elas podem armazenar, como inteiros, números de ponto flutuante, caracteres, entre outros.
- Em linguagens como C, as variáveis são declaradas especificando o tipo de dado da variável, seguido pelo seu nome.
- Exemplo de declaração de variável em C:
    
    ```c
    int idade;
    ```
    

## Biblioteca math.h

Uma biblioteca é um conjunto de funções, classes e/ou constantes pré-definidas que podem ser utilizadas por um programa. Elas fornecem funcionalidades adicionais que não estão disponíveis diretamente na linguagem de programação, permitindo que os desenvolvedores realizem tarefas específicas de forma mais eficiente e concisa.

A biblioteca **`math.h`** em C é uma das bibliotecas padrão mais comuns e amplamente utilizadas. Ela fornece uma série de funções matemáticas para realizar operações como cálculos de potência, raiz quadrada, funções trigonométricas, entre outras. Aqui estão algumas das funções matemáticas mais comuns disponíveis na biblioteca **`math.h`**:

- **`pow(x, y)`**: Calcula a potência de **`x`** elevado a **`y`**.
- **`sqrt(x)`**: Calcula a raiz quadrada de **`x`**.
- **`sin(x)`**, **`cos(x)`**, **`tan(x)`**: Calcula os valores das funções trigonométricas seno, cosseno e tangente de um ângulo em radianos, respectivamente.
- **`fabs(x)`**: Retorna o valor absoluto de **`x`**.
- **`ceil(x)`**, **`floor(x)`**: Arredonda **`x`** para o próximo número inteiro superior ou inferior, respectivamente.
- **`log(x)`**, **`log10(x)`**: Calcula o logaritmo natural e o logaritmo na base 10 de **`x`**, respectivamente.

Para usar as funções da biblioteca **`math.h`**, você precisa incluir a linha **`#include <math.h>`** no início do seu programa. Isso permite que o compilador saiba onde encontrar as definições das funções matemáticas ao compilar o seu código. Essas funções são extremamente úteis em uma variedade de aplicações, desde cálculos científicos até jogos e gráficos computacionais.

### Exemplo do uso de POW

```c
#include <stdio.h>
//Importação do "math"
#include <math.h>

int main() {
    double base = 2.0;
    double expoente = 3.0;
    double resultado;

    resultado = pow(base, expoente);

    printf("O resultado de %.1f elevado a %.1f é %.1f\n", base, expoente, resultado);

    return 0;
}
```

## Impressão de tipo de dados

| Código | Tipo |
| --- | --- |
| %c | Char |
| %d ou %i | Int |
| %f | Float |
| %if | Double |
| %e | Float ou Double |
| %s | String |