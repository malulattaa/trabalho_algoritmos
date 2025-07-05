from datetime import date, time

# Participantes
participantes = {
    1: {
        'nome': 'Maria Latta',
        'email': 'maria@gmail.com',
        'pref_tematica': ['Inteligência Artificial', 'Web', 'Programação'],
        'eventos': [1, 2]
    },
    2: {
        'nome': 'Matheus Camarotto',
        'email': 'matheus@gmail.com',
        'pref_tematica': ['Programação', 'Segurança'],
        'eventos': [2]
    },
    3: {
        'nome': 'Ana Clara',
        'email': 'ana@gmail.com',
        'pref_tematica': ['Mobile', 'Segurança'],
        'eventos': []
    },
    4: {
        'nome': 'Vinicius Lima',
        'email': 'vini@gmail.com',
        'pref_tematica': ['Web', 'Robótica'],
        'eventos': [3]
    },
    5: {
        'nome': 'Gabriela Santos',
        'email': 'gabibibi@gmail.com',
        'pref_tematica': ['Banco de Dados', 'Programação'],
        'eventos': []
    },
}

id_participante = 6
#próximo id de participante disponível para cadastro

# Eventos
eventos = {
    1: {
        'nome': 'Semana da IA',
        'data_evento': date(2025, 7, 10),
        'hora_evento': time(10, 0),
        'tema': 'Inteligência Artificial',
        'participantes': [1]
    },
    2: {
        'nome': 'Maratona de Programação',
        'data_evento': date(2025, 7, 12),
        'hora_evento': time(14, 0),
        'tema': 'Programação',
        'participantes': [1, 2]
    },
    3: {
        'nome': 'Workshop IA',
        'data_evento': date(2025, 7, 15),
        'hora_evento': time(9, 30),
        'tema': 'Inteligência Artificial',
        'participantes': []
    },
    4: {
        'nome': 'Palestra Cybersecurity',
        'data_evento': date(2025, 6, 12),
        'hora_evento': time(14, 30),
        'tema': 'Segurança',
        'participantes': [4]
    },
}

id_evento = 5
#próximo id de evento disponível para cadastro