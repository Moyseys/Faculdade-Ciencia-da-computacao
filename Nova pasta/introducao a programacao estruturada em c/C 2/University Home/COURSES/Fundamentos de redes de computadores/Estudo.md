# Estudo

Internet: rede global de computadores que usam o protocolo de comunicação TCP/IP para se comunicar, permitindo a troca de informações e dados.

Rede: conjunto de dispositivos eletrônicos interconectados para compartilhar recursos e trocar informações. As redes podem ser: locais (LANs), metropolitanas (MANs) e globais (Wans).

Os dispositivos que usamos e que estão conectados à internet são chamados de sistemas finais, ou hosts (hospedeiros) pois se encontram no entorno ou periferia da internet e são nesses dispositivos que executamos as aplicações de rede.

Em termos de redes de computadores, um "host" é qualquer dispositivo que esteja conectado a uma rede e que possua um endereço IP atribuído a ele. O host pode ser um computador, servidor, impressora, roteador, smartphone, tablet ou qualquer outro dispositivo que possa se comunicar em uma rede. O termo "host" é comumente usado em contextos de rede para se referir a qualquer dispositivo que participe de uma comunicação de rede.

Temos redes com meios físicos guiados e não guiados, podendo ser cabos, ou rede wireless por exemplo.

Podemos também descrever a internet como uma infraestrutura provedora de serviços a aplicações.

Em resumo, uma API de socket é uma maneira de os programas se comunicarem por meio de uma rede, permitindo a troca de dados entre diferentes dispositivos conectados à rede.

Atraso em redes de comutação de pacotes:

- Atraso de processamento: Tempo gasto no dispositivo para examinar o cabeçalho do pacote e determinar por qual saída deve encaminhá-lo.
- Atraso de fila: Tempo que o pacote espera para ser transmitido no enlace caso exista fila (buffer).
- Atraso de transmissão: Tempo para transmitir todos os bits do pacote par o enlace
- Atraso de propagação: Tempo necessário para propagar o bit desde o início do enlace até o próximo nó.

O texto fornece informações sobre três parâmetros importantes em redes de computadores: perda, atraso fim a fim e vazão. 

1. **Perda de Pacotes**:
    - A perda de pacotes pode ocorrer quando a intensidade de tráfego excede a capacidade de transmissão da rede, levando a fila de pacotes a ficar cheia e pacotes subsequentes a serem descartados.
    - Alguns aplicativos, como transferência de arquivos, podem ser impactados negativamente pela perda de pacotes, enquanto outros, como streaming de vídeo, podem tolerá-la.
    - A infraestrutura de rede pode corrigir a perda de pacotes automaticamente, permitindo que os desenvolvedores de aplicativos se concentrem na lógica da aplicação.
2. **Atraso Fim a Fim**:
    - O atraso fim a fim é o tempo total que um pacote leva para viajar do remetente ao destinatário, incluindo todos os atrasos ao longo do caminho, como atrasos de fila e de processamento nos roteadores intermediários.
    - O atraso fim a fim pode impactar aplicativos sensíveis ao tempo, como chamadas de voz pela internet (VoIP) e jogos online.
    - Ferramentas como o Traceroute podem ser usadas para medir e diagnosticar atrasos de rede.
3. **Vazão**:
    - A vazão é a taxa de transferência de dados entre dois pontos na rede, medida em bits por segundo.
    - A vazão pode ser influenciada por vários fatores, incluindo a capacidade dos enlaces de rede e o congestionamento da rede.
    - Aplicações diferentes têm diferentes requisitos de vazão, sendo importante manter uma vazão adequada para garantir o desempenho da aplicação.

Esses parâmetros são essenciais para entender o desempenho e o comportamento de redes de computadores e são fundamentais para projetar e otimizar sistemas de rede.