public class Aluno {
  private String nome;
  private int idade;

  public Aluno(String nome, int idade) {
    this.nome = nome;
    this.idade = idade;
  }

  public void mostrarNomeeIdade() {
    System.out.println("Nome: " + this.nome);
    System.out.println("idade: " + this.idade);
  }

  public static void main(String[] args) {
    Aluno a = new Aluno("Toddy", 7);
    a.mostrarNomeeIdade();
  }
}
