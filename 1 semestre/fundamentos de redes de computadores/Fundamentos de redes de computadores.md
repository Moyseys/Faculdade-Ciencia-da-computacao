# Fundamentos de redes de computadores

**Instructor:** Eduardo

**Email:** email@email.com

| Assignment | Date | Weight |
| --- | --- | --- |
| ASSIGNMENT 1 | DATE | WEIGHT% |
|  |  |  |
|  |  |  |
|  |  |  |

[https://www.notion.so](https://www.notion.so)

[Estudo](./Fundamentos%20de%20redes%20de%20computadores/Estudo.md)

[Correção](./Fundamentos%20de%20redes%20de%20computadores/Correção.md)

[Resumo para AV1 - 1° Semestre](./Fundamentos%20de%20redes%20de%20computadores/Resumo%20para%20AV1%20-%201°%20Semestre.md)

## 12/03

- computadores são sistemas de processamento digital
- tudo que conectamos as redes (computadores)
- tudo que se conecta e consome ou manda informação é um sistema de processamento digital
- redes (conexão com mais de um elemento)
- sistemas de processamentos digitais conectados entre si
- cliente - servidor
- consome - provê
- fornecimento e consumo (isso é o resumo de redes de computadores)
- a internet é um conjunto de protocolos que padroniza como vamos nos comunicar

### Rede comutado por circuito

### Rede comutada por pacote - comutação por pacote - nativa para trabalhar com pacotes - isso seria uma promessa do 5g.

- compartilha o mesmo meio físico com acesso baseado em regras
- quando maior a demanda mais larga é a banda - podem trafegar mais ao mesmo tempo porém temos que ter mais regras
- maior tráfego - redes oceânicas
- na fibras óticas oceânicas ou estradas temos muitas pessoas conectadas, ou seja um grande peso de utilização logo precisamos de MUITAS regras

COMUTAÇÃO POR PACOTE

- regras para ocupar o mesmo meio físico
- pacote é como se fosse um carro fluindo em uma rodovia
- precisamos de pontos que nos deem uma rota
- cada encruzilhada temos um roteador par guiar esses pacotes
- a rede é desenhada para que cheguemos ao destino seguindo a melhor rota pode ser por velocidade ou ainda por segurança
- os pacotes vão se movimentando ao mesmo tempo e em algum momento vão entrar em fila um com o outro
- um pacote nada mais que um monte de bits (0 e1)
- a rede nada mais é que um conjunto de dados que carregam informações encapsulados em bits (0 e 1)
- rede determinista, quando se estabelece circuito se consegue estabelecer uma comunicação (no caso a outra é isso, essa não é determinista)
- compartilha um mesmo canal assim como uma avenida compartilha passagem para vários carro

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled.png)

- necessidades para o funcionamento

endereçar - origem e destino

esse endereço chama IP(Internet Protocol)

- qualquer pacote tem endereço de origem e endereço de destino

endereço de IP

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%201.png)

- controle de fluxo (estabelecer regras de como trocar dados e remontar informação)

saber como ler 0 e 1 montando uma sequência lógica e reproduzir uma informação

# 5 camadas:

Pilha de protocolos da internet

1. aplicação -significado dos dados, pega os pacotes e atribui um significado para o conjunto de informações (software) Defini os protocolos de troca de informação.
2. transporte - cuida da sequência e da troca de dados (software), tipos de serviços
3. rede - endereçamento propriamente dito, é onde temos o endereço de IP(software), roteamento/encadeamento
4. enlace - interpretar conjuntos de informação, codificação binária (envolve o hardware da placa de rede)
5. física - cuida dos aspectos físicos da rede ex: cabo da internet (envolve o hardware da placa de rede)

## IEEE -  Todas as redes padronizadas

O padrão IEEE 802.11 **define uma arquitetura para as redes sem fio, baseada na divisão da área coberta pela rede em células**

- Todo tipo de aplicação tem um conjunto de regras.

### RFC:  são documentos usados pela comunidade online há mais de 40 anos para definir os padrões da web e compartilhar informações técnicas.

### Aplicação

### Transporte

### Rede

http (Hyper text transfer protocol)

## 1.CAMADA DE APLICAÇÃO:

A Camada de Aplicação é a camada superior da pilha de protocolos da internet e é responsável por lidar com aspectos de alto nível de comunicação, gerenciamento e manipulação de dados. Ela permite que o usuário interaja com a aplicação e a rede. As principais funções da Camada de Aplicação incluem:

1. Definir protocolos de troca de informação: A Camada de Aplicação define o conjunto de regras para a troca de informações entre sistemas, permitindo que os dados sejam enviados e recebidos de maneira eficiente e confiável.
2. Atribuir significado aos dados: A camada de aplicação interpreta os dados recebidos e atribui um significado a eles, permitindo que sejam compreendidos e usados pelo usuário ou pela aplicação.
3. Interagir com o software de aplicação: Esta camada oferece uma interface para que o software de aplicação possa interagir com a rede e fazer uso dos serviços de rede.

Portas de redes: usadas para diferenciar os processos no lado do cliente com alocação dinâmica

![Desenho de rede.png](./Fundamentos%20de%20redes%20de%20computadores/Desenho_de_rede.png)

- P1 - processo 01→ Aba navegador
- P2 - processo 02 →Aba navegador
- P1 e P2 comunicando Ps1

DNS Domain name system: protocolo que faz a tradução de nomes para ips

[www.google.com](http://www.google.com) → ip: 172.217.30.68

→ a seta representa o DNS

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%202.png)

## 26/03

DNS traduz um nome em um IP

porta padrão de http é a 80

SOCKET : conexão virtual entre dois processos (é um canal do qual podemos trocar informações a vontade)

HTTP: muitos processos rodam em cima do http

MÉTODOS: conjuntos de regras de estrutura de cabeçalho referente ao que deve conter a mensagem

get: leitura EX: aceitar o site da unimetrocamp

post: publicação

put: modificar

delete: deletar

## 28/05

# Camada de Rede

## 3 Funções principais

- → Endereçamento(IP)
    - Análogo ao CEP
    - Possui uma relação com a localização real do computador, assim como o CEP
- → Roteamento
    - Rota é uma expectativa.
    - Deve ser maleável.
- → Encaminhamento
    - O encaminhamento é uma tomada de decisão a cada roteador que o pacote passar.
    
    [https://www.notion.so](https://www.notion.so)
    

### IP

Internet Protocolo

**IPv4**

32 bits → 2^32 → ~4,3 bilhões de endereços

**IPv6**

128 bits → 2^128 → ~340 undecilhões 

| Binário | 1 | 0 | 1 |
| --- | --- | --- | --- |
| Potência | 2 | 1 | 0 |
| ——————— |  |  |  |
| ——————— | 2^2 = 4 * 1 | 2^1 = 2 * 0 | 2^0 = 1 * 1 |
| Resultado | 4 | 0 | 1 |

### Gateway

Componente que conecta varias redes geralmente é o `IP` do roteador.

Diz a quantidade de possibilidades de IP’s na sub-rede

### Máscara de Rede

Função é delimitar as possibilidades de IP’s dentro de uma sub-rede

Exemplo: 

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%203.png)

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%204.png)

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%205.png)

![Untitled](./Fundamentos%20de%20redes%20de%20computadores/Untitled%206.png)