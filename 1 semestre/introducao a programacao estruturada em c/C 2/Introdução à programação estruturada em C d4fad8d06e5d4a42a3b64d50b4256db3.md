# Introdução à programação estruturada em C

[https://www.notion.so](https://www.notion.so)

[https://profturatti.github.io/](https://profturatti.github.io/)

Jogadores:

|  | Vicent  | Lucas  | Pedro  | Roberto |
| --- | --- | --- | --- | --- |
| Cabelo | Castanho | Ruivo | Branco  | Loiro |
| Jogo | Domino  | Dama   | Xadrez  | Poker |

Amigos do Esporte:

| Atleta | Pais  | Esporte  |
| --- | --- | --- |
| Dimitri  | Russia  | Ginastica |
| Paul | EUA | Basquete  |
| Jorge  | Inglaterra  | Atletismo  |
| Luis  | Brasil  | Futebol |

Os Cinco amigos:

| Nome  | Camisa  | Bone |
| --- | --- | --- |
| Antonio  | Guarani  | Verde |
| Robson | Brasil  | Amarelo  |
| Marcos  | Sao Paulo | Vermelho |
| Victor  | Santos  | Preto |
| Andre  | Cruzeiro  | Azul |

Errei fui mlk:

| Ordem | Piloto | Equipe | Cor do Carro |
| --- | --- | --- | --- |
| 1º | Richie | Lotus | Amarelo |
| 2º | Patrese | Minard | Branco |
| 3º | Senna | March | Azul |
| 4º | Eddie | Brabham | Vermelho |
| 5º | Rosset | Lola | Preto |
| 6º | Luyendyk | Tasman | Verde |

ALGORÍTIMO:

código média (nosso código)

[main.c](Introduc%CC%A7a%CC%83o%20a%CC%80%20programac%CC%A7a%CC%83o%20estruturada%20em%20C%20d4fad8d06e5d4a42a3b64d50b4256db3/main.c)

```jsx
#include <stdio.h>
```

```jsx
int main(void) {
float nota1, nota2, media;
```

```jsx
printf("Digite a primeira nota: ");
scanf("%f", &nota1);
```

```jsx
printf("Digite a segunda nota: ");
scanf("%f", &nota2);
```

```jsx
media = (nota1 + nota2) / 2;
printf("A média é: %f\n", media);
```

```jsx
if (media >= 6)
printf("Aprovado");
else {
printf("Reprovado");
}
```

```jsx
return 0;
}
```

#include <stdio.h>

int main(void) {
float nota1, nota2, media = 0;

printf("Digite a primeira nota: \n");
if(nota1 >= 6.5)
printf("Coloque a nota dentro do padrão de duas casas decimais");
else  {
printf("Ok");
}

scanf("%f", &nota1); //ler valor da nota 1

printf("Digite a segunda nota: \n"); // \n pula linha
scanf("%f", &nota2); //ler valor da nota 2

media = (nota1 + nota2) / 2;
printf("A média é: %.2f\n", media); //o %.2f é para mostrar apenas 2 casas decimais

if (media >= 6)
printf("Aprovado");
else {
printf("Reprovado");
}

return 0;
}

```jsx
#include <stdio.h>
```

```jsx
int main(void) {
float nota1, nota2, media = 0;
```

```jsx
printf("Digite a primeira nota: \n");
scanf("%f", &nota1); //ler valor da nota 1
```

```jsx
printf("Digite a segunda nota: \n"); // \n pula linha
scanf("%f", &nota2); //ler valor da nota 2
```

```jsx
media = (nota1 + nota2) / 2;
printf("A média é: %.2f\n", media);
//o %.2f é para mostrar apenas 2 casas decimais
```

```jsx
//if (media >= 6)
// printf("Aprovado");
//else
// printf("Reprovado");
```

```jsx
if(media >= 7)
printf("\nAprovado");
else{
if(media < 5)
printf("\nReprovado");
else{
printf("\nRecuperação");
// se a media estiver entre 5.0 e 6.9 o aluno faz uma prova para recuperação A nova nota será somada com a maior nota e se a nova média for maior ou igual a 7 o aluno será aprovado, senão será reprovado após a recperação
}
}
```

```jsx
// }
```

```jsx
//quando só temos uma linha depois do else, não precisamos acrescentar chaves
```

```jsx
return 0;
}
```

if(nota1 > nota2){
maiornota = nota1;
}else{
maiornota = nota2;

}

#include <stdio.h>

int main(void) {
float nota1, nota2, nota3, media, novamedia, maiornota = 0;

printf("Digite a primeira nota: \n");
scanf("%f", &nota1); //ler valor da nota 1

printf("Digite a segunda nota: \n"); // \n pula linha
scanf("%f", &nota2); //ler valor da nota 2

media = (nota1 + nota2) / 2;
printf("A média é: %.2f\n", media);
//o %.2f é para mostrar apenas 2 casas decimais

//if (media >= 6)
// printf("Aprovado");
//else
// printf("Reprovado");

if(media >= 7)
printf("\nAprovado");
else{
if(media < 5)
printf("\nReprovado");
else{
printf("\nRecuperação");
// se a media estiver entre 5.0 e 6.9 o aluno faz uma prova para recuperação A nova nota será somada com a maior nota e se a nova média for maior ou igual a 7 o aluno será aprovado, senão será reprovado após a recperação

```
  if(nota1 > nota2){
     maiornota = nota1;
   }else{
     maiornota = nota2;
   }

  if(media >= 5 && media < 6.9)
    printf("Faça a recuperação");
  printf("Digite a terceira nota: \\n");
  scanf("%f", &nota3);
  novamedia = (nota3 + maiornota) / 2;
}
}

```

// }

//quando só temos uma linha depois do else, não precisamos acrescentar chaves

return 0;
}

#include <stdio.h>

int main(void) {
float nota1, nota2, media = 0;

printf("Digite a primeira nota: \n");
scanf("%f", &nota1); //ler valor da nota 1

printf("Digite a segunda nota: \n"); // \n pula linha
scanf("%f", &nota2); //ler valor da nota 2

media = (nota1 + nota2) / 2;
printf("A média é: %.2f\n", media);
//o %.2f é para mostrar apenas 2 casas decimais

//if (media >= 6)
// printf("Aprovado");
//else
// printf("Reprovado");

if(media >= 7)
printf("\nAprovado");
else{
if(media < 5)
printf("\nReprovado");
else{
printf("\nRecuperação");
// se a media estiver entre 5.0 e 6.9 o aluno faz uma prova para recuperação A nova nota será somada com a maior nota e se a nova média for maior ou igual a 7 o aluno será aprovado, senão será reprovado após a recperação
}
}

// }

//quando só temos uma linha depois do else, não precisamos acrescentar chaves

return 0;
}

[Revisão C](Introduc%CC%A7a%CC%83o%20a%CC%80%20programac%CC%A7a%CC%83o%20estruturada%20em%20C%20d4fad8d06e5d4a42a3b64d50b4256db3/Revisa%CC%83o%20C%20fffc472b60f941fe88d49e348e21679b.md)

---

17/05

### VETOR (ARRAY) revisar tudo em casa pq não escutei nada do que ele falou

- Vetor é uma variável que tem vários elementos de um mesmo tipo;
- Array por busca binária (Reduz o tempo de interação de elementos); para que a busca binária funcione é necessário que os elementos estejam organizados em ordem crescente;

Exercícios: 

 

```
#include<stdio.h>
int main(){

int numeros1[10], numeros2[10], soma[10];
printf("Digite 10 núemros inteiros para o primeiro vetor:\n ");
for (int i = 0; i<10; i++) {
  printf("Numeros %d: ", i + 1);
  scanf("%d", &numeros1[i]);
}

printf("Digite 10 núemros inteiros para o segundo vetor: \n");
for (int i = 0; i<10; i++) {
  printf("Numeros %d:", i + 1);
  scanf("%d", &numeros2[i]);
}

for (int i = 0; i<10; i++){
  soma[i] = numeros1[i] + numeros2[i];
}

printf("Soma do numero da mesma posicao: \n");
for (int i = 0; i<10; i++){
  printf("Nuemros %d: %d\n", i+1, soma[i]);
}

return 0;
}
```

Exercicio 2:

```c
#include <stdio.h>

int main() {
float vetorA[10], vetorB[10], resultado[10];
char operacao;
int i;

// Entrada de dados para o primeiro vetor
printf("Digite 10 numeros reais para o primeiro vetor:\\n");
for (i = 0; i < 10; i++) {
    printf("Elemento %d: ", i + 1);
    scanf("%f", &vetorA[i]);
}

// Entrada de dados para o segundo vetor
printf("Digite 10 numeros reais para o segundo vetor:\\n");
for (i = 0; i < 10; i++) {
    do {
        printf("Elemento %d (diferente de zero para divisao): ", i + 1);
        scanf("%f", &vetorB[i]);
    } while (vetorB[i] == 0);
}

// Solicita ao usuario a operação a ser realizada
printf("Escolha a operacao (+, -, *, /): ");
scanf(" %c", &operacao);

// Realiza a operação escolhida
switch (operacao) {
    case '+':
        for (i = 0; i < 10; i++) {
            resultado[i] = vetorA[i] + vetorB[i];
        }
        break;
    case '-':
        for (i = 0; i < 10; i++) {
            resultado[i] = vetorA[i] - vetorB[i];
        }
        break;
    case '*':
        for (i = 0; i < 10; i++) {
            resultado[i] = vetorA[i] * vetorB[i];
        }
        break;
    case '/':
        for (i = 0; i < 10; i++) {
            if (vetorB[i] != 0) {
                resultado[i] = vetorA[i] / vetorB[i];
            } else {
                printf("Erro: Divisao por zero no elemento %d\\n", i + 1);
                return 1;
            }
        }
        break;
    default:
        printf("Operacao invalida!\\n");
        return 1;
}

// Exibe os elementos do vetor resultante
printf("Resultado da operacao:\\n");
for (i = 0; i < 10; i++) {
    printf("Elemento %d: %.2f\\n", i + 1, resultado[i]);
}

return 0;

```

exercicio 3:

#include<stdio.h>
int main(){

int numeros[10] = {3, 7, 15, 22, 31, 42, 56, 64, 71, 88};
int numerobusca = 2;
int encontrei = 0;

int i = 0;

while (i < 10){
if (numeros[i] == numerobusca){
encontrei = 1;
break;
}
i++;
}

if(encontrei) printf("encontrei");
else printf("Nao encontrei");

return 0;
}