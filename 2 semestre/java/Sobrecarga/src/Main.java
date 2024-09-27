package src;

public class Main {
	public static void main(String[] args) {
		AlunoPag a1 = new AlunoPag();
		AlunoPag a2 = new AlunoPag("Teste");

		System.out.println(a1.nome);
		System.out.println(a2.nome);

		Pagamento p1 = new Pagamento();

		p1.processarPagemento(1.0);
		p1.processarPagemento(1.0, "Real");
		p1.processarPagemento(1.0, 5);
	}
}
