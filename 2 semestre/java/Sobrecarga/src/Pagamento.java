package src;
public class Pagamento {
    public void processarPagemento(double valor){
        System.out.println("O valor do pagamento é: " + valor);
    }
    
    public void processarPagemento(double valor, String moeda){
        System.out.println("O valor do pagamento é: " + valor + " em: " + moeda);
    }
    
    public void processarPagemento(double valor, int parcelas){
        System.out.println("O valor do pagamento é: " + valor + " parcela: " + parcelas);
    }
}
