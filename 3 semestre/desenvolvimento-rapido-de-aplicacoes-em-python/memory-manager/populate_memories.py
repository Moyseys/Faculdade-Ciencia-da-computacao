
import sqlite3

def populate_memories():
    conn = sqlite3.connect('memories.db')
    cursor = conn.cursor()
    
    memories = [
        {
            'title': 'O Dia Que Descobri Que Minha WiFi Tem Mais Estabilidade Que Meus Relacionamentos',
            'description': 'Sentado no sofá, olhando para o roteador piscando, percebi que pelo menos ele tenta se reconectar quando algo dá errado. Diferente de certas pessoas que conheci.',
            'image': 'https://images.unsplash.com/photo-1606868306217-dbf5046868d2?w=500',
            'emotion': 'sadness'
        },
        {
            'title': 'Reunião de Família: Um Estudo Antropológico Sobre Disfunção',
            'description': 'Três horas ouvindo tios dando conselhos de vida enquanto bebem cerveja no almoço de domingo. O irônico é que eles acham que EU preciso de terapia.',
            'image': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=500',
            'emotion': 'anger'
        },
        {
            'title': 'Quando Meu Chefe Disse Que Somos Uma "Família"',
            'description': 'Ah sim, aquela família onde você trabalha 60 horas por semana por um salário que mal paga o aluguel. Que família amorosa e funcional.',
            'image': 'https://images.unsplash.com/photo-1497032628192-86f99bcd76bc?w=500',
            'emotion': 'disgust'
        },
        {
            'title': 'A Primeira Vez Que Vi Minha Conta Bancária Depois de Pagar as Contas',
            'description': 'Um momento de pura contemplação existencial. O saldo negativo me olhava de volta como um espelho da minha alma: vazio e decepcionante.',
            'image': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=500',
            'emotion': 'fear'
        },
        {
            'title': 'O Encontro Marcado Pelo Tinder Que Durou 15 Minutos',
            'description': 'Ela chegou, olhou para mim, fingiu receber uma "ligação de emergência" e saiu. Pelo menos foi honesta - a maioria inventa desculpas mais elaboradas.',
            'image': 'https://images.unsplash.com/photo-1516251193007-45ef944ab0c6?w=500',
            'emotion': 'sadness'
        },
        {
            'title': 'Quando Descobri Que Meu "Melhor Amigo" Estava Saindo Com Minha Ex',
            'description': 'Plot twist: eles se merecem. Na verdade, foi um favor. Agora tenho duas pessoas tóxicas longe de mim de uma vez só. Eficiência!',
            'image': 'https://images.unsplash.com/photo-1494178270175-e96de2971df9?w=500',
            'emotion': 'anger'
        },
        {
            'title': 'A Alegria de Ir ao Supermercado Com R$ 50 Para Fazer Compra do Mês',
            'description': 'Uma experiência matemática fascinante. Como transformar macarrão instantâneo e água em um plano alimentar sustentável? Spoiler: não dá.',
            'image': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=500',
            'emotion': 'sadness'
        },
        {
            'title': 'O Dia Que Minha Mãe Perguntou "Quando Vai Me Dar Netos?"',
            'description': 'Mãe, mal consigo cuidar de uma planta. Você realmente quer que eu seja responsável por um ser humano? Aliás, lembra da Violeta que você me deu? Exato.',
            'image': 'https://images.unsplash.com/photo-1476703993599-0035a21b17a9?w=500',
            'emotion': 'surprise'
        },
        {
            'title': 'Assistindo Meus Amigos Casarem Enquanto Eu Não Consigo Nem Manter Uma Conversa No WhatsApp',
            'description': 'Todo mundo postando fotos felizes enquanto eu estou aqui debatendo se devo responder "kkk" ou "hahaha" numa mensagem. A vida adulta é fascinante.',
            'image': 'https://images.unsplash.com/photo-1511285560929-80b456fea0bc?w=500',
            'emotion': 'nostalgia'
        },
        {
            'title': 'A Epifania de Perceber Que Minha Vida Virou Episódio de Sitcom Ruim',
            'description': 'Sabe aqueles episódios que são tão constrangedores que você muda de canal? Pois é, essa é minha vida agora. Só que sem risada de fundo.',
            'image': 'https://images.unsplash.com/photo-1478147427282-58c93bf50e62?w=500',
            'emotion': 'disgust'
        },
        {
            'title': 'Quando Percebi Que Sou o Michael Scott da Minha Própria Vida',
            'description': 'Aquele momento de clareza absoluta: sou simultaneamente o chefe mais incompetente e a pessoa mais confiante do escritório. A diferença é que não tenho uma câmera filmando para transformar isso em comédia.',
            'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500',
            'emotion': 'surprise'
        }
    ]
    
    for memory in memories:
        cursor.execute(
            'INSERT INTO memories (title, description, image, emotion) VALUES (?, ?, ?, ?)',
            (memory['title'], memory['description'], memory['image'], memory['emotion'])
        )
    
    conn.commit()
    conn.close()
    print("10 memórias com humor ácido foram inseridas com sucesso!")

if __name__ == '__main__':
    populate_memories()
