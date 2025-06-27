from datetime import date, time

# Participantes
participantes = {
    1: {
        'nome': 'Maria Silva',
        'email': 'maria@email.com',
        'pref_tematica': ['Inteligência Artificial', 'Web'],
        'eventos': [1, 2]
    },
    2: {
        'nome': 'João Oliveira',
        'email': 'joao@email.com',
        'pref_tematica': ['Programação'],
        'eventos': [2]
    },
    3: {
        'nome': 'Ana Costa',
        'email': 'ana@email.com',
        'pref_tematica': ['Mobile', 'Segurança'],
        'eventos': []
    },
}

id_participante = 4  # Próximo ID disponível

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
        'nome': 'Workshop Mobile',
        'data_evento': date(2025, 7, 15),
        'hora_evento': time(9, 30),
        'tema': 'Mobile',
        'participantes': []
    },
}

id_evento = 4  # Próximo ID disponível
