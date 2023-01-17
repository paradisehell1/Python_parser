import socket
import sys
import uuid
import config

code = sys.argv[1]
action_id = int(sys.argv[2])
server_address = ('ovz1.j04522079.m69km.vps.myjino.ru', 49156)

with socket.create_connection(server_address) as CLIENT:
    print('Подключено к:', server_address)

    mac_id = str(hex(uuid.getnode()))
    msg = f"PACKET_ID: {action_id} MAC_ID: {mac_id} CODE: {code}"
    CLIENT.sendall(msg.encode())

    while True:
        data = CLIENT.recv(1024)

        if not data:
            continue

        raw_data = data.decode(encoding="utf-8")
        if raw_data == "1":
            config.IS_ACTIVATED = True
            config.CODE = code
            config.save_code()
            exit(100)
        else:
            if action_id == 1:
                config.reset_code()
                exit(51 + int(raw_data))
            else:
                config.reset_code()
                exit(50)

print('Отключено от:', server_address)