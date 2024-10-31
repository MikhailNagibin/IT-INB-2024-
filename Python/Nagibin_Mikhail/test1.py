import platform
import os
import socket
import psutil
import uuid


def get_system_info():
    info = {
        "Имя компьютера": platform.node(),
        "Операционная система": platform.system(),
        "Версия ОС": platform.version(),
        "Архитектура": platform.architecture(),
        "Процессор": platform.processor(),
        "Количество ядер": psutil.cpu_count(logical=False),
        "Логические процессоры": psutil.cpu_count(logical=True),
        "Объем оперативной памяти (ГБ)": round(psutil.virtual_memory().total / (1024**3), 2),
        "MAC-адрес": get_mac_address(),
        "IP-адрес": socket.gethostbyname(socket.gethostname()),
    }
    return info


def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    return mac


system_info = get_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")
