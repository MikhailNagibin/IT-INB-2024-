# import platform
# import os
# import socket
# import psutil
# import uuid
#
#
# def get_system_info():
#     info = {
#         "Имя компьютера": platform.node(),
#         "Операционная система": platform.system(),
#         "Версия ОС": platform.version(),
#         "Архитектура": platform.architecture(),
#         "Процессор": platform.processor(),
#         "Количество ядер": psutil.cpu_count(logical=False),
#         "Логические процессоры": psutil.cpu_count(logical=True),
#         "Объем оперативной памяти (ГБ)": round(psutil.virtual_memory().total / (1024**3), 2),
#         "MAC-адрес": get_mac_address(),
#         "IP-адрес": socket.gethostbyname(socket.gethostname()),
#     }
#     return info
#
#
# def get_mac_address():
#     mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
#     return mac
#
#
# system_info = get_system_info()
# for key, value in system_info.items():
#     print(f"{key}: {value}")
# print(1.9*1.9)


from itertools import permutations
from math import ceil


def f(data, s):
    ans = 0
    a = [el[::] for el in data]
    for el in a:
        el[0] -= 10 * s
        ans += 1
        s = el[1]
        if el[0] > 0:
            ans += ceil(el[0] / (10 * s))
    return ans


n, s = map(int, input().split())
data = []
for i in range(n):
    data.append([int(el) for el in input().split()])
new_data = list(permutations(data))
ans = []
for el in new_data:
    ans.append(f(el, s))
print(min(ans))

'''
1 5
10 1
'''