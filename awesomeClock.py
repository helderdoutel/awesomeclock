"""Seloko."""
from os import system, name
from time import sleep, time


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def gerar_indices(letra, display):
    if 'A' == letra:
        linha = [0]
        coluna = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif 'B' == letra:
        linha = [0, 1, 2, 3, 4]
        coluna = [8, 9]
    elif 'C' == letra:
        linha = [4, 5, 6, 7, 8]
        coluna = [8, 9]
    elif 'D' == letra:
        linha = [8]
        coluna = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif 'E' == letra:
        linha = [4, 5, 6, 7, 8]
        coluna = [0, 1]
    elif 'F' == letra:
        linha = [0, 1, 2, 3, 4]
        coluna = [0, 1]
    elif 'G' == letra:
        linha = [4]
        coluna = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    indices = []
    for l in linha:
        for c in coluna:
            indices.append(((90 * l) + c) + (16) * display)
    return indices


def varias_letras(letras, display):
    retorno = []
    for l in letras:
        retorno = retorno + gerar_indices(l, display)
    return retorno


def flip_flop(entrada):
    return (entrada + 1) % 2


def draw(lista):
    clear()
    lista = lista + [208, 209, 240, 241, 298, 299, 330,
                     331, 478, 479, 510, 511, 568, 569, 600, 601]
    y = 0
    string = list(string_display)
    for x in range(len(string)):
        if x in lista:
            string[x] = '1'
        else:
            string[x] = ' '
    saida = ''
    for x in string:
        saida += x
    for x in range(int(len(string) / 90)):
        print(saida[y:y + 90])
        y += 90

string_display = '1111111111      1111111111      1111111111      1111111111      1111111111      111111111111      11      11      11      11      11      11      11      11      11      11      1111      11      11      11  11  11      11      11      11  11  11      11      11      1111      11      11      11  11  11      11      11      11  11  11      11      11      111111111111      1111111111      1111111111      1111111111      1111111111      111111111111      11      11      11  11  11      11      11      11  11  11      11      11      1111      11      11      11  11  11      11      11      11  11  11      11      11      1111      11      11      11      11      11      11      11      11      11      11      111111111111      1111111111      1111111111      1111111111      1111111111      1111111111'
y = 0
# clear()
# for x in range(int(len(string_display) / 90)):
#     print(string_display[y:y + 90])
#     y += 90

u1 = 0
u2 = 0
u3 = 0
u4 = 0

d1 = 0
d2 = 0
d3 = 0

mu1 = 0
mu2 = 0
mu3 = 0
mu4 = 0

md1 = 0
md2 = 0
md3 = 0

hu1 = 0
hu2 = 0
hu3 = 0
hu4 = 0

hd1 = 0
hd2 = 0

flag_4 = False
flag_3 = False
flag_2 = False
flag_1 = False
flag_0 = False
while True:
    lista = []
    start = time()

    u1 = flip_flop(u1)
    if u1 == 0:
        u2 = flip_flop(u2)
        if u2 == 0:
            u3 = flip_flop(u3)
            if u3 == 0:
                u4 = flip_flop(u4)

    if flag_4:
        flag_4 = False
        d1 = flip_flop(d1)
        if d1 == 0:
            d2 = flip_flop(d2)
            if d2 == 0:
                d3 = flip_flop(d3)

    if flag_3:
        flag_3 = False
        mu1 = flip_flop(mu1)
        if mu1 == 0:
            mu2 = flip_flop(mu2)
            if mu2 == 0:
                mu3 = flip_flop(mu3)
                if mu3 == 0:
                    mu4 = flip_flop(mu4)

    if flag_2:
        flag_2 = False
        md1 = flip_flop(md1)
        if md1 == 0:
            md2 = flip_flop(md2)
            if md2 == 0:
                md3 = flip_flop(md3)

    if flag_1:
        flag_1 = False
        hu1 = flip_flop(hu1)
        if hu1 == 0:
            hu2 = flip_flop(hu2)
            if hu2 == 0:
                hu3 = flip_flop(hu3)
                if hu3 == 0:
                    hu4 = flip_flop(hu4)

    if flag_0:
        flag_0 = False
        hd1 = flip_flop(hd1)
        if hd1 == 0:
            hd2 = flip_flop(hd2)

    if not hd1 and not hd2:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 0)
    elif hd1 and not hd2:  # 1
        lista = lista + varias_letras(['B', 'C'], 0)
    elif not hd1 and hd2:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 0)
    elif hd1 and hd2:
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 0)
        hd1 = 0
        hd2 = 0

    if not hu1 and not hu2 and not hu3 and not hu4:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 1)
    elif hu1 and not hu2 and not hu3 and not hu4:  # 1
        lista = lista + varias_letras(['B', 'C'], 1)
    elif not hu1 and hu2 and not hu3 and not hu4:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 1)
    elif hu1 and hu2 and not hu3 and not hu4:  # 3
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'G'], 1)
        if md1 and not md2 and md3:
            if mu1 and not mu2 and not mu3 and mu4:
                if d1 and not d2 and d3:
                    if u1 and not u2 and not u3 and u4:
                        if not hd1 and hd2:
                            flag_0 = True
                            hu1 = 1
                            hu2 = 1
                            hu3 = 1
                            hu4 = 1

    elif not hu1 and not hu2 and hu3 and not hu4:  # 4
        lista = lista + varias_letras(['F', 'G', 'B', 'C'], 1)
    elif hu1 and not hu2 and hu3 and not hu4:  # 5
        lista = lista + varias_letras(['A', 'F', 'G', 'C', 'D'], 1)
    elif not hu1 and hu2 and hu3 and not hu4:  # 6
        lista = lista + varias_letras(['A', 'C', 'D', 'E', 'F', 'G'], 1)
    elif hu1 and hu2 and hu3 and not hu4:  # 7
        lista = lista + varias_letras(['A', 'B', 'C'], 1)
    elif not hu1 and not hu2 and not hu3 and hu4:  # 8
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 1)
    elif hu1 and not hu2 and not hu3 and hu4:  # 9
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'F', 'G'], 1)
        if md1 and not md2 and md3:
            if mu1 and not mu2 and not mu3 and mu4:
                if d1 and not d2 and d3:
                    if u1 and not u2 and not u3 and u4:
                        flag_0 = True
                        hu1 = 1
                        hu2 = 1
                        hu3 = 1
                        hu4 = 1

    if not md1 and not md2 and not md3:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 2)
    elif md1 and not md2 and not md3:  # 1
        lista = lista + varias_letras(['B', 'C'], 2)
    elif not md1 and md2 and not md3:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 2)
    elif md1 and md2 and not md3:  # 3
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'G'], 2)
    elif not md1 and not md2 and md3:  # 4
        lista = lista + varias_letras(['F', 'G', 'B', 'C'], 2)
    elif md1 and not md2 and md3:  # 5
        if mu1 and not mu2 and not mu3 and mu4:
            if d1 and not d2 and d3:
                if u1 and not u2 and not u3 and u4:
                    flag_1 = True
                    md1 = 1
                    md2 = 1
                    md3 = 1
        lista = lista + varias_letras(['A', 'F', 'G', 'C', 'D'], 2)

    if not mu1 and not mu2 and not mu3 and not mu4:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 3)
    elif mu1 and not mu2 and not mu3 and not mu4:  # 1
        lista = lista + varias_letras(['B', 'C'], 3)
    elif not mu1 and mu2 and not mu3 and not mu4:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 3)
    elif mu1 and mu2 and not mu3 and not mu4:  # 3
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'G'], 3)
    elif not mu1 and not mu2 and mu3 and not mu4:  # 4
        lista = lista + varias_letras(['F', 'G', 'B', 'C'], 3)
    elif mu1 and not mu2 and mu3 and not mu4:  # 5
        lista = lista + varias_letras(['A', 'F', 'G', 'C', 'D'], 3)
    elif not mu1 and mu2 and mu3 and not mu4:  # 6
        lista = lista + varias_letras(['A', 'C', 'D', 'E', 'F', 'G'], 3)
    elif mu1 and mu2 and mu3 and not mu4:  # 7
        lista = lista + varias_letras(['A', 'B', 'C'], 3)
    elif not mu1 and not mu2 and not mu3 and mu4:  # 8
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 3)
    elif mu1 and not mu2 and not mu3 and mu4:  # 9
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'F', 'G'], 3)
        if d1 and not d2 and d3:
            if u1 and not u2 and not u3 and u4:
                flag_2 = True
                mu1 = 1
                mu2 = 1
                mu3 = 1
                mu4 = 1

    if not d1 and not d2 and not d3:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 4)
    elif d1 and not d2 and not d3:  # 1
        lista = lista + varias_letras(['B', 'C'], 4)
    elif not d1 and d2 and not d3:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 4)
    elif d1 and d2 and not d3:  # 3
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'G'], 4)
    elif not d1 and not d2 and d3:  # 4
        lista = lista + varias_letras(['F', 'G', 'B', 'C'], 4)
    elif d1 and not d2 and d3:  # 5
        if u1 and not u2 and not u3 and u4:
            flag_3 = True
            d1 = 1
            d2 = 1
            d3 = 1
        lista = lista + varias_letras(['A', 'F', 'G', 'C', 'D'], 4)

    if not u1 and not u2 and not u3 and not u4:  # 0
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F'], 5)
    elif u1 and not u2 and not u3 and not u4:  # 1
        lista = lista + varias_letras(['B', 'C'], 5)
    elif not u1 and u2 and not u3 and not u4:  # 2
        lista = lista + varias_letras(['A', 'B', 'G', 'E', 'D'], 5)
    elif u1 and u2 and not u3 and not u4:  # 3
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'G'], 5)
    elif not u1 and not u2 and u3 and not u4:  # 4
        lista = lista + varias_letras(['F', 'G', 'B', 'C'], 5)
    elif u1 and not u2 and u3 and not u4:  # 5
        lista = lista + varias_letras(['A', 'F', 'G', 'C', 'D'], 5)
    elif not u1 and u2 and u3 and not u4:  # 6
        lista = lista + varias_letras(['A', 'C', 'D', 'E', 'F', 'G'], 5)
    elif u1 and u2 and u3 and not u4:  # 7
        lista = lista + varias_letras(['A', 'B', 'C'], 5)
    elif not u1 and not u2 and not u3 and u4:  # 8
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 5)
    elif u1 and not u2 and not u3 and u4:  # 9
        lista = lista + varias_letras(['A', 'B', 'C', 'D', 'F', 'G'], 5)
        flag_4 = True
        u1 = 1
        u2 = 1
        u3 = 1
        u4 = 1

    draw(lista)
    # print(str(u4) + str(u3) + str(u2) + str(u1))
    # print(str(d3) + str(d2) + str(d1))
    # print(str(mu4) + str(mu3) + str(mu2) + str(mu1))
    # print(str(hd1) + str(hd2))
    end = time()
    tempo = end - start
    # print(end - start)
    sleep(1 - tempo)
