import pywhatkit as kit
import time

# Defina o número do grupo no formato internacional (com o prefixo do país).
# Por exemplo, se o grupo tiver o nome "Grupo Teste", substitua pelo nome exato.
grupo_nome = "GR-PYTHON-2E24"
mensagem = "Olá, esta é uma mensagem automática!"
intervalo = 10  # Intervalo entre as mensagens em segundos

try:
    while True:
        # Envia a mensagem
        kit.sendwhatmsg_to_group(grupo_nome, mensagem, 21, 38)  # Envia às 15:00, você pode mudar
        time.sleep(intervalo)  # Espera o intervalo definido antes de enviar a próxima mensagem
except KeyboardInterrupt:
    print("Envio de mensagens interrompido.")
