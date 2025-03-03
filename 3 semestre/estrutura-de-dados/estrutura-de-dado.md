# Aula dia 25/02/2024 de estruturas de dados

maloc -> Função utilizada em C para realizar alocação dinamica de memoria

> Sempre que for utilizada deve ser liberada a memoria no final do program, isso pode ser feito utilizando a função `free`

realloc -> redimensiona a area alocada pelo maloc

calloc -> Acessa a memoria por meio de indice

Tipo Float:

|-------|-------|----------|
| sinal | power | mantissa |
|-------|-------|----------|

Quando:

50 -> 0.5 X 10^1
500 -> 0.5 X 10^2

> Então o float salva o valor em notação cientifica

## Variaveis na memoria

São alocadas em formato de pilha

int A;
int B

|---|
| B |
|---|
| A |
|---|


## Pointers

int *ip
double *dp 

*Cada declaração de um ponteiro aloca um espaço na memoria com o tamnho do tipo dela

## Indirição

## Indireção multipla

int **prt;

> Um pointer para um outro pointer

## Alocação na memoria de variaveis

```C

int A;
char X;
int B;

```

|----|----|----|----|
|    |    |    |B39 | B
|----|----|----|----|
|B40 |B41 |B42 |C43 | X
|----|----|----|----|
|A44 |A45 |A46 |A47 | A
|----|----|----|----|


## Caminhando pela memoria por ponteiros


Ao somar ints ao ponteiro ele caminha pela memoria, somando no endereço de memoria. Então caso some 1 a um pointer int ele ira caminhar um 4 byte na memoria





