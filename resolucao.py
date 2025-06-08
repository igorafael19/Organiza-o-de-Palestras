from datetime import datetime, timedelta

# Lê o arquivo e carrega as palestras
with open('proposals.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

palestras = []

# Transforma cada linha em (nome, duração)
for linha in linhas:
    linha = linha.strip()
    partes = linha.split()
    tempo = partes[-1]
    nome = ' '.join(partes[:-1])
    if tempo.lower() == 'lightning':
        duracao = 5
    else:
        duracao = int(tempo.replace('min', ''))
    palestras.append((nome, duracao))

track_num = 1

# Continua enquanto houver palestras
while palestras:
    print(f"Track {chr(64 + track_num)}:")  # 65 = A

    # === Manhã ===
    hora = datetime.strptime("09:00", "%H:%M")
    tempo_restante = 180
    palestras_manha = []

    for nome, duracao in palestras[:]:  # cópia para iterar
        if duracao <= tempo_restante:
            print(f"{hora.strftime('%H:%M')} {nome} {duracao}min")
            hora += timedelta(minutes=duracao)
            tempo_restante -= duracao
            palestras_manha.append((nome, duracao))

    # Remove as palestras usadas na manhã
    for p in palestras_manha:
        palestras.remove(p)

    print("12:00 Almoço")

    # === Tarde ===
    hora = datetime.strptime("13:00", "%H:%M")
    tempo_restante = 240
    palestras_tarde = []

    for nome, duracao in palestras[:]:
        if duracao <= tempo_restante:
            print(f"{hora.strftime('%H:%M')} {nome} {duracao}min")
            hora += timedelta(minutes=duracao)
            tempo_restante -= duracao
            palestras_tarde.append((nome, duracao))

    # Remove as palestras usadas na tarde
    for p in palestras_tarde:
        palestras.remove(p)

    # === Networking ===
    if hora < datetime.strptime("16:00", "%H:%M"):
        hora = datetime.strptime("16:00", "%H:%M")
    print(f"{hora.strftime('%H:%M')} Evento de Networking\n")

    track_num += 1

