#include <stdio.h>

int main(void) {
  float nota1, nota2, media;

  printf("Digite a primeira nota: ");
  scanf("%f", &nota1);

  printf("Digite a segunda nota: ");
  scanf("%f", &nota2);

  media = (nota1 + nota2) / 2;
  printf("A média é: %f\n", media);

  if (media >= 6)
    printf("Aprovado");
  else {
    printf("Reprovado");
  }

  return 0;
}