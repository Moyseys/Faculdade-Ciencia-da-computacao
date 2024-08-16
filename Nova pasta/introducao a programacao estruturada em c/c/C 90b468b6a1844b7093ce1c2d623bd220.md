# C

# Operadores ternários

```c
//condição1 ? (Caso a condição for verdade execute) : (Caso não seja xecute isso);
(5 == 5) ? printf("É\n") : printf("não é\n");
```

# Recursão

```c
int conta(int inicio, int fim){
    if(inicio == fim){
        return fim;
    }
    
    printf("%d\n", inicio);
    inicio = inicio + 1;
    return conta(inicio, fim);
}
```

### Exercício 1: Números Pares

Escreva um programa que imprime todos os números pares de 1 a 100.

### Exercício 2: Soma de Números

Escreva um programa que lê 10 números do usuário e calcula a soma desses números.

```c
int main() {
    int a, b, r = 0;
    
    printf("a = ");
    scanf("%d", &a);

    printf("b = ");
    scanf("%d", &b);
    
    r = a + b;
    printf("%d", r);
    return 0;
}
```

### Exercício 4: Verificação de Palíndromo

Escreva um programa que verifica se uma string fornecida pelo usuário é um palíndromo.

```c
char nome[100] = {};

printf("Digite um nome para testar: ");
scanf("%s", &nome);

char nomeInverso[100] = {};
int tamanhoDoNome = strlen(nome);

for(int i = 0; i <= tamanhoDoNome - 1; i++){
    int iInverso = (tamanhoDoNome - 1) - i;
    //printf("%d\n", iInverso);
    nomeInverso[i] = nome[iInverso];
}

printf("Nome: %s\n", nome);
printf("Nome inverso: %s\n\n", nomeInverso);

if(strcmp(nome, nomeInverso) == 0){
    printf("✨ %s' é um palíndromo! ✨\t🎉🎉", nome);
}else{
    printf("'%s' NÃO é um palíndromo!", nome);
}

```

### Exercício 5: Ordenação de Vetor

Escreva um programa que lê 5 números do usuário e os ordena em ordem crescente.

### Exercício 6: Maior e Menor Valor

Escreva um programa que lê 10 números do usuário e encontra o maior e o menor valor entre eles.

### Exercício 7: Média de Notas

Escreva um programa que lê as notas de 5 alunos e calcula a média das notas.

### Exercício 8: Tabuada

Escreva um programa que imprime a tabuada de um número fornecido pelo usuário.

### Exercício 9: Número Primo

Escreva um programa que verifica se um número fornecido pelo usuário é primo.

### Exercício 10: Inversão de String

Escreva um programa que inverte uma string fornecida pelo usuário.