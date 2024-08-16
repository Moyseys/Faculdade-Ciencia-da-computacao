# Resumo para AV1 - 1° Semestre

# 03/06

# Parâmetros de atraso

Em uma rede de computadores há quatro principais tipos de atrasos, eles estão representados na imagem.

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled.png)

### Processamento nodal

Esse atraso representa o tempo levado para processar o cabeçalho do pacote e determinar para qual saída ele ira ir

### Fila

Esse é o tempo que leva para o pacote ou quadro ser transmitido na camada de enlace. Caso a fila esteja cheia e chega um novo pacote o roteador ira simplesmente descartar o pacote.

> **Camada De Enlace**                                                                                                                                              Nesta camada, leva-se um pacote, denominado ***quadro***, de um nó ao nó seguinte, no caminho entre origem e destino. Em cada nó, a camada de rede passa o datagrama para a camada de enlace, que fica responsável por encaminhar o pacote de dados até o próximo nó, de forma confiável, ou seja, sem erros.
> 

### Transmissão

Tempo que gasto para transmitir, ou também pode ser chamado de “empurrar”, todos os bits para o enlace, esse tempo é uma função com o **tamanho do pacote** e a **velocidade de transmissão** do enlace.

### Propagação

Tempo necessário para propagar o bit desde o início do enlace até o próximo nó. O bit se desloca pelo meio de acordo com a velocidade de propagação do enlace, a qual depende do meio físico, isto é, se o meio utilizado é fibra ótica, fios de cobre e assim por diante. Este atraso é diretamente relacionado à distância entre os roteadores, mas nada tem a ver com o comprimento do pacote ou com a taxa de transmissão do enlace.

# Medida de desempenho

### Atraso fim a fim

Um outro tipo de atraso que vale a pena ser comentado é o atraso fim a fim, esse tipo de atraso se refere ao tempo que um pacote leva para ir de um sistema final até outro, ou seja, é a soma de todos os atrasos que o pacote sofreu em seu caminho

### Vazão fim a fim

A vazão fim a fim de uma rede é determinada pela taxa de transferência de uma rede, que é medida por exemplo em bits/s.

# Arquitetura de camadas

Há dois modelos mais utilizados de arquitetura de camadas, são eles:

### OSI

n sei oq q n sei oq la

### TCP/IP

# Encapsulamento

O encapsulamento é uma uma forma de adicionar informações a mensagem enviada pela camada de aplicação. Em cada camada do pilha de camadas é adicionado um “Header”, cabeçalho, a mensagem, e assim ela vai sendo encapsulada

> **Importante**                                                                                                                                                          A mensagem da camada de aplicação mais o cabeçalho da camada de transporte formam uma unidade de dado de protocolo **PDU**, em cada camada esse PDU tem um nome.
> 
> - **Camada Física**: Bit
> - **Camada de Enlace de Dados**: Quadro (Frame)
> - **Camada de Rede**: Pacote (Packet)
> - **Camada de Transporte**: Segmento (Segment) ou Datagrama
> - **Camada de Sessão, Apresentação e Aplicação**: Mensagem (Message)

         

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%201.png)

# Camada de aplicação

A camada de aplicação é a de mais alto nível, é a camada que o usuário interage, interface, alguns exemplo de softwares de camada de aplicação são navegadores, cliente e-mail, jogos executados em rede.

Dentro da camada de aplicação há dois tipos de arquiteturas, são elas Cliente-Servidor e Peer-To-Peer, na cliente servidor se tem um cliente onde ele somente solicita serviços do servidor e o servidor somente responde, já Peer-To-Peer os computadores podem fazer a mesma coisa, tanto solicitar como prestar serviço

## Exemplos:

### **Arquitetura Cliente-Servidor**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%202.png)

- **Web Browsing**: Navegador (cliente) acessa servidores web.
- **E-mail**: Aplicativos de e-mail (cliente) conectam-se a servidores de e-mail.
- **Banco de Dados**: Aplicativos de banco de dados (cliente) acessam servidores de banco de dados.
- **Aplicações de Negócios**: Softwares de ERP (cliente) utilizam servidores ERP.
    
    ![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%203.png)
    
- **Mensagens Instantâneas**: Aplicativos de mensagens (cliente) se comunicam via servidores centralizados.

### **Arquitetura Peer-to-Peer (P2P)**

- **Compartilhamento de Arquivos**: BitTorrent permite compartilhamento direto de arquivos entre usuários.
- **Mensagens Descentralizadas**: Tox permite comunicação sem servidores centralizados.
    - **Mídia Social Descentralizada**: Mastodon permite comunicação entre diferentes servidores.
- **Criptomoedas**: Bitcoin utiliza uma rede distribuída de nós para verificar transações.
- **CDNs P2P**: Peer5 distribui conteúdo usando tecnologia P2P, compartilhando entre usuários.

# Protocolos de camada de aplicação

Os protocolos da camada de aplicação permitem que duas aplicações que utilizam de linguagem ou sistemas operacionais distintos se comuniquem entre sim, os protocolos estabelecem:

- O tipo da mensagem tocada, podendo ser Requisição ou Resposta
- A sintaxe dos vários tipos de mensagens, tais como os campos da mensagem e como os campos são delineados;
- A semântica dos campos, isto é, o significado da informação nos campos;
- Regras para determinar quando e como um processo envia e responde mensagens.

Enquanto o algoritmo da camada de aplicação determina seu funcionamento no ambiente local, o protocolo dela estipula tudo que é necessário para que aplicações em diferentes hospedeiros possam trocar mensagens de maneira estruturada.

Os protocolos públicos da internet são especificados por **RFCs.** Desse modo, qualquer pessoa é capaz de acessar as especificações de tais protocolos e implementar os próprios softwares.

## **Três serviços importantes da internet e quais protocolos usam**:

### Serviço Web (Protocolo HTTP)

Implementado pelo protocolo HTTP, que muita gente confunde com a própria Internet.

Definido pelas RFCs 1945 e 2616, o HTTP (Hypertext Transfer Protocol) é o protocolo padrão para a transferência de páginas web na internet.

A web foi concebida no CERN em 1991 como uma maneira de permitir que grupos de cientistas de diferentes nacionalidades colaborassem por meio da troca de informações baseadas em hipertextos. Em dezembro daquele ano, uma demonstração pública foi realizada na conferência Hypertext 91.

**Estrutura de uma mensagem HTTP**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%204.png)

**Request**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%205.png)

**Response**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%206.png)

### Serviço de Correio (Protocolos SMTP, IMAP e POP)

A arquitetura do sistema de correio eletrônico é construída com base em **dois agentes**: o a agente de Usuário e o de transferência de mensagem.

- **Agente do usuário:** O **agente do usuário** é o **programa** que faz a interface do usuário com o sistema de correio eletrônico. É por meio dele que o **usuário.**
- **Agentes** de **transferência de mensagens:** Já os **agentes** de **transferência de mensagens** são os responsáveis por fazer com que elas cheguem até o destino. Eles são mais conhecidos como **servidores** de **correio eletrônico**.
    
    ![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%207.png)
    

**SMTP**

O protocolo responsável pela transferência da mensagem até seu destino é o SMTP. Definido pela RFC 5321, ele utiliza o **protocolo de transporte TCP**, obtendo, assim, a **garantia** de que ela será entregue no destino **sem erros**.

O servidor SMTP aguarda por conexões de seus clientes. Quando uma conexão é estabelecida, o servidor inicia a conversação enviando uma linha de texto na qual se identifica e informa se está pronto (ou não) para receber mensagens. Se ele não estiver, o cliente deverá encerrar a conexão e tentar novamente mais tarde.

Caso o servidor esteja acessível, o cliente precisa informar aos usuários a origem e o destino da mensagem. Se o servidor considerar que se trata de uma transferência válida, sinalizará para que ele a envie. Após o envio, o servidor confirma sua recepção e a conexão é encerrada.

**POP3**

A RFC 1939 estipula que o POP3 (*Post Office Protocol version 3*) tem a finalidade de fazer o download das mensagens que se encontram no mailbox do usuário para o sistema local. Caso estejam neste sistema, ele pode utilizá-las em qualquer momento, mesmo sem ter conexão com a internet.

O POP3 é implementado na maioria dos agentes de usuário. Basta configurar os parâmetros de conta e senha do usuário para que o agente faça o download das mensagens. Ele permite o download seletivo delas, assim como apagar as selecionadas no servidor.

I**MAP**

Assim como o POP3, o IMAP (*Internet Message Access Protocol*) permite que um usuário tenha acesso às mensagens armazenadas em sua caixa. Porém, enquanto o POP3 é baseado na transferência delas para o sistema local a fim de serem lidas, o IMAP consegue permitir sua leitura diretamente no servidor, dispensando, portanto, a transferência para o sistema local.

Isso será particularmente útil para usuários que não utilizarem sempre o mesmo computador, pois permite que suas mensagens sejam acessadas a partir de qualquer sistema. Definido pela RFC 3501, o IMAP também fornece mecanismos para criar, excluir e manipular várias caixas de correio no servidor.

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%208.png)

> **Atenção!**
> 
> 
> Um webmail não é um protocolo, mas uma **forma oferecida** por alguns sites da web a fim de que os **usuários** possam **ler suas mensagens** de **correio eletrônico**.
> 
> Para usar o sistema, o usuário abre uma página web, na qual entra com uma identificação e uma senha. A partir desse momento, ele tem acesso imediato às suas mensagens (de forma parecida com a de um cliente IMAP).
> 

### Serviço de Nomes (DNS)

Sistema de resolução de nomes DNS.

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%209.png)

Aqui estão alguns serviços oferecidos por esse protocolo:

- Identificação de servidores de correios eletrônicos;
- Apelidos para hospedeiros;
- Distribuição de carga;
- Descoberta de nomes de hospedeiros (mapeamento reverso).

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%2010.png)

**Genéricos**

- .com = comercial;
- .edu = instituições educacionais;
- .int = algumas organizações internacionais;
- .org = organizações sem fins lucrativos.

**Países**

- .br = Brasil;
- .pt = Portugal;
- .jp = Japão;
- .ar = Argentina.

**Consulta iterativa**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%2011.png)

**Consulta recursiva**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%2012.png)

## TCP persistente X TCP não persistente

**TCP Persistente**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%2013.png)

Em uma conexão TCP persistente, uma vez que a conexão é estabelecida entre o cliente e o servidor, ela permanece aberta e ativa durante múltiplas transações, permitindo a troca contínua de dados sem precisar reestabelecer a conexão.

**TCP Não Persistente**

![Untitled](./Resumo%20para%20AV1%20-%201°%20Semestre/Untitled%2014.png)

Em uma conexão TCP não persistente, a conexão é aberta para cada transação individual e fechada imediatamente após a conclusão da transação, exigindo a reabertura da conexão para cada novo pedido.