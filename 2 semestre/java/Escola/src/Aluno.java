public class Aluno {
  private String nome;
  private int idade;
  private float nota;

  public void setNota(float nota) {
    this.nota = nota;
  }

  public float getNota() {
    return this.nota;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getNome() {
    return this.nome;
  }

  public void mostrarInformacoes() {
    System.out.println("Nome: " + this.nome);
    System.out.println("idade: " + this.idade);
    System.out.println("Nota: " + this.nota);
  }
}
