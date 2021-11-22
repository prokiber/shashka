import telebot
# Manba @API_KOD 
from telebot import types
bot = telebot.TeleBot('2122169336:AAEJKYrH6XZgbvkBGfy6JkT3XQmtvq8_g9s')
first = ""
second = ""
click = 'first'
whereboy = []
l = []
u = 0
boy_damki = {}
trueorfalse = False
trueorfalse1 = False
Trueboy = False
Trueboy1 = False
whiteorblack = 'white'
deletechecers = ''
x = 0
isboy = False
docxod = []
doctypexod = []
y = ''
x1 = 0
y1 = ''
z = 0
z1 = 0
d1 = ('a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8')
d2 = ('a3', 'b2', 'c1')
d3 = ('c1', 'd2', 'e3', 'f4', 'g5', 'h6')
d4 = ('h6', 'g7', 'f8')
d5 = ('a3', 'b4', 'c5', 'd6', 'e7', 'f8')
d6 = ('e1', 'd2', 'c3', 'b4', 'a5')
d7 = ('a5', 'b6', 'c7', 'd8')
d8 = ('h4', 'g5','f6', 'e7','d8')
d9 = ('e1','f2', 'g3','h4')
d10 = ('a7', 'b8')
d11 = ('g1', 'h2')
d12 = ('g1', 'f2', 'e3', 'd4', 'c5', 'b6','a7')
d13 = ('h2', 'g3','f4','e5','d6','c7','b8')
cellsola = ['a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1', 'e3', 'e5',
            'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']
cells = {
    "a1": "•","c1": "•","e1": "•","g1":"•",
    "b2": "•","d2": "•","f2": "•","h2": "•",
    "a3": "•","c3": "•","e3": "•","g3": "•",
    "b4": "•","d4": "•","f4": "⬜","h4": "•",
    "a5": "•","c5": "•","e5": "•","g5": "•",
    "b6": "•","d6": "•","f6": "⚫","h6": "•",
    "a7": "•","c7":"•","e7": "•","g7": "•",
    "b8": "•","d8":"•","f8": "•","h8": "•",
         }
menu = types.InlineKeyboardMarkup(row_width=2)
gamewithfriend = types.InlineKeyboardButton("Играть с другом", url='https://t.me/Onlayn_Shashka', switch_inline_query_current_chat='@OnlaynShashkabot')
turnir = types.InlineKeyboardButton("Турнир", callback_data='turnir')
menu.add(gamewithfriend, turnir)
#Приветствие
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, 'Приветствую тебя', reply_markup=menu)

def started_board():
    board = types.InlineKeyboardMarkup(row_width=8)
    a1 = types.InlineKeyboardButton(cells['a1'], callback_data='a1')
    b1 = types.InlineKeyboardButton(" ", callback_data='b1')
    c1 = types.InlineKeyboardButton(cells['c1'], callback_data='c1')
    d1 = types.InlineKeyboardButton(" ", callback_data='d1')
    e1 = types.InlineKeyboardButton(cells['e1'], callback_data='e1')
    f1 = types.InlineKeyboardButton(" ", callback_data='f1')
    g1 = types.InlineKeyboardButton(cells['g1'], callback_data='g1')
    h1 = types.InlineKeyboardButton(" ", callback_data='h1')
    a2 = types.InlineKeyboardButton(" ", callback_data='a2')
    b2 = types.InlineKeyboardButton(cells['b2'], callback_data='b2')
    c2 = types.InlineKeyboardButton(" ", callback_data='c2')
    d2 = types.InlineKeyboardButton(cells['d2'], callback_data='d2')
    e2 = types.InlineKeyboardButton(" ", callback_data='e2')
    f2 = types.InlineKeyboardButton(cells['f2'], callback_data='f2')
    g2 = types.InlineKeyboardButton(" ", callback_data='g2')
    h2 = types.InlineKeyboardButton(cells['h2'], callback_data='h2')
    a3 = types.InlineKeyboardButton(cells['a3'], callback_data='a3')
    b3 = types.InlineKeyboardButton(" ", callback_data='b3')
    c3 = types.InlineKeyboardButton(cells['c3'], callback_data='c3')
    d3 = types.InlineKeyboardButton(" ", callback_data='d3')
    e3 = types.InlineKeyboardButton(cells['e3'], callback_data='e3')
    f3 = types.InlineKeyboardButton(" ", callback_data='f3')
    g3 = types.InlineKeyboardButton(cells['g3'], callback_data='g3')
    h3 = types.InlineKeyboardButton(" ", callback_data='h3')
    a4 = types.InlineKeyboardButton(" ", callback_data='a4')
    b4 = types.InlineKeyboardButton(cells['b4'], callback_data='b4')
    c4 = types.InlineKeyboardButton(" ", callback_data='c4')
    d4 = types.InlineKeyboardButton(cells['d4'], callback_data='d4')
    e4 = types.InlineKeyboardButton(" ", callback_data='e4')
    f4 = types.InlineKeyboardButton(cells['f4'], callback_data='f4')
    g4 = types.InlineKeyboardButton(" ", callback_data='g4')
    h4 = types.InlineKeyboardButton(cells['h4'], callback_data='h4')
    a5 = types.InlineKeyboardButton(cells['a5'], callback_data='a5')
    b5 = types.InlineKeyboardButton(" ", callback_data='b5')
    c5 = types.InlineKeyboardButton(cells['c5'], callback_data='c5')
    d5 = types.InlineKeyboardButton(" ", callback_data='d5')
    e5 = types.InlineKeyboardButton(cells['e5'], callback_data='e5')
    f5 = types.InlineKeyboardButton(" ", callback_data='f5')
    g5 = types.InlineKeyboardButton(cells['g5'], callback_data='g5')
    h5 = types.InlineKeyboardButton(" ", callback_data='h5')
    a6 = types.InlineKeyboardButton(" ", callback_data='a6')
    b6 = types.InlineKeyboardButton(cells['b6'], callback_data='b6')
    c6 = types.InlineKeyboardButton(" ", callback_data='c6')
    d6 = types.InlineKeyboardButton(cells['d6'], callback_data='d6')
    e6 = types.InlineKeyboardButton(" ", callback_data='e6')
    f6 = types.InlineKeyboardButton(cells['f6'], callback_data='f6')
    g6 = types.InlineKeyboardButton(" ", callback_data='a6')
    h6 = types.InlineKeyboardButton(cells['h6'], callback_data='h6')
    a7 = types.InlineKeyboardButton(cells['a7'], callback_data='a7')
    b7 = types.InlineKeyboardButton(" ", callback_data='b7')
    c7 = types.InlineKeyboardButton(cells['c7'], callback_data='c7')
    d7 = types.InlineKeyboardButton(" ", callback_data='d7')
    e7 = types.InlineKeyboardButton(cells['e7'], callback_data='e7')
    f7 = types.InlineKeyboardButton(" ", callback_data='f7')
    g7 = types.InlineKeyboardButton(cells['g7'], callback_data='g7')
    h7 = types.InlineKeyboardButton(" ", callback_data='h7')
    a8 = types.InlineKeyboardButton(" ", callback_data='a8')
    b8 = types.InlineKeyboardButton(cells['b8'], callback_data='b8')
    c8 = types.InlineKeyboardButton(" ", callback_data='c8')
    d8 = types.InlineKeyboardButton(cells['d8'], callback_data='d8')
    e8 = types.InlineKeyboardButton(" ", callback_data='e8')
    f8 = types.InlineKeyboardButton(cells['f8'], callback_data='f8')
    g8 = types.InlineKeyboardButton(" ", callback_data='g8')
    h8 = types.InlineKeyboardButton(cells['h8'], callback_data='h8')
    unwin = types.InlineKeyboardButton('Сдаться', callback_data='unwin')
    resonas = types.InlineKeyboardButton('Ничья', callback_data='resonas')
    board.add(a8, b8, c8, d8, e8, f8, g8, h8,
                a7, b7, c7, d7, e7, f7, g7, h7,
                a6, b6, c6, d6, e6, f6, g6, h6,
                a5, b5, c5, d5, e5, f5, g5, h5,
                a4, b4, c4, d4, e4, f4, g4, h4,
                a3, b3, c3, d3, e3, f3, g3, h3,
                a2, b2, c2, d2, e2, f2, g2, h2,
                a1, b1, c1, d1, e1, f1, g1, h1)
    board.row(unwin, resonas)
    return board
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global click, x, y, x1, y1, z, z1, l
    global first
    global second, whereboy
    global whiteorblack
    global trueorfalse, isboy1
    global trueorfalse1, deletechecers
    global isboy, Trueboy, Trueboy1, boy_damki, u
    try:
        u = 0
        deletechecers = ''

        if (click == "first") and (cells[call.data] != '•') and (cells[call.data] != " " and call.data in cellsola) and cells[call.data] != "•":
            first = call.data
            click = 'second'
        elif first != '' and call.data in cellsola and cells[call.data] == "•":
            second = call.data
            click = "first"
        def bexod():
            global isboy, doctypexod, deletechecers, whereboy, whereboy1, whereboy2, whereboy3, whereboy4, whereboy5, whereboy6
            white_chekers = []
            boy_damki = {}
            black_chekers = []
            none_chekers = []
            white_damki = []
            black_damki = []
            doctypexod = []
            l = []
            isboy = False
            for i in cells.items():
                if i[1] == "⚫":
                    black_chekers.append(i[0])
                elif i[1] == "⚪" and x == 0:
                    white_chekers.append((i[0]))
                elif i[1] == "⚪" and x == 1:
                    white_chekers.append(y)
                    z = 1
                elif i[1] == "•":
                    none_chekers.append(i[0])
                elif i[1] == "⬛":
                    black_damki.append(i[0])
                elif i[1] == "⬜":
                    white_damki.append(i[0])
            if white_damki != []:
                for white_damka in white_damki:
                    doctypexod = []

                    for i in d1:
                        if white_damka == i:
                            doctypexod.append(d1)
                    for i in d2:
                        if white_damka == i:
                            doctypexod.append(d2)
                    for i in d3:
                        if white_damka == i:
                            doctypexod.append(d3)
                    for i in d4:
                        if white_damka == i:
                            doctypexod.append(d4)
                    for i in d5:
                        if white_damka == i:
                            doctypexod.append(d5)
                    for i in d6:
                        if white_damka == i:
                            doctypexod.append(d6)
                    for i in d7:
                        if white_damka == i:
                            doctypexod.append(d7)
                    for i in d8:
                        if white_damka == i:
                            doctypexod.append(d8)
                    for i in d9:
                        if white_damka == i:
                            doctypexod.append(d9)
                    for i in d10:
                        if white_damka == i:
                            doctypexod.append(d10)
                    for i in d11:
                        if white_damka == i:
                            doctypexod.append(d11)
                    for i in d12:
                        if white_damka == i:
                            doctypexod.append(d12)
                    for i in d13:
                        if white_damka == i:
                            doctypexod.append(d13)

                    a = []
                    whereboy1 = []
                    whereboy2 = []
                    whereboy3 = []
                    whereboy4 = []
                    whereboy5 = []
                    whereboy6 = []
                    if len(doctypexod) == 1:
                        index = doctypexod[0].index(white_damka)

                        if index == 0:
                            a = []
                            for i in doctypexod[0]:

                                if cells[i] == "⬛" or cells[i] == "⚫":
                                    a.append(i)
                                    if len(a) > 1:
                                        a.pop(-1)
                                    deletechecers = ''.join(a)
                                    if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':
                                        u = 0
                                        for j in a:
                                            i = 1
                                            if u == 0:
                                                while 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]):
                                                    if 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1':
                                                        if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                            whereboy1.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                            isboy = True
                                                            i += 1


                                                        elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or cells[
                                                            doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                            u = 1
                                                            break
                                                    else:
                                                        break
                                            else:
                                                break

                        if index == 7:
                            a = []
                            for i in doctypexod[0][::-1]:
                                if cells[i] == "⬛" or cells[i] == "⚫":
                                    a.append(i)
                                    if len(a) > 1:
                                        a.pop(-1)
                                    if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':

                                        deletechecers = ''.join(a)
                                        u = 0
                                        for j in a:
                                            i = 1
                                            if u == 0:
                                                while 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]):
                                                    if 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1':
                                                        if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                            whereboy2.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                            isboy = True
                                                            i += 1


                                                        elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or cells[
                                                            doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                            u = 1
                                                            break
                                                    else:
                                                        break
                                            else:
                                                break
                    elif len(doctypexod) == 2:
                        index = doctypexod[0].index(white_damka)
                        index2 = doctypexod[1].index(white_damka)
                        a = []
                        for i in doctypexod[0][(index + 1)::]:

                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':

                                    deletechecers = ''.join(a)
                                    for j in a:
                                        i = 1
                                        if u == 0:
                                            while 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]) and u == 0:
                                                if 0<=(doctypexod[0].index(j)) + i < len(doctypexod[0]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                    if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                        isboy = True
                                                        whereboy3.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                        i += 1


                                                    elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or cells[
                                                        doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break
                        a = []
                        for i in doctypexod[0][(index - 1)::-1]:
                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':

                                    deletechecers = ''.join(a)
                                    for j in a:
                                        i = 1
                                        if u == 0:
                                            while 0<=(doctypexod[0].index(j)) - i < len(doctypexod[0]) and u == 0 :
                                                if 0<=(doctypexod[0].index(j)) - i < len(doctypexod[0]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                    if cells[doctypexod[0][(doctypexod[0].index(j)) - i]] == "•":
                                                        whereboy4.append(doctypexod[0][(doctypexod[0].index(j)) - i] or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌")
                                                        i += 1
                                                        isboy = True


                                                    elif cells[doctypexod[0][(doctypexod[0].index(j)) - i]] == "⚪" or cells[
                                                        doctypexod[0][(doctypexod[0].index(j)) - i]] == "⬜":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break
                        a = []
                        for i in doctypexod[1][(index2 - 1)::-1]:
                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':

                                    deletechecers = ''.join(a)
                                    for j in a:
                                        i = 1
                                        if u == 0:
                                            while 0 <= (doctypexod[1].index(j)) - i < len(doctypexod[1]) and u == 0:
                                                if 0 <= (doctypexod[1].index(j)) - i < len(doctypexod[1]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                    if cells[doctypexod[1][(doctypexod[1].index(j)) - i]] == "•":
                                                        isboy = True

                                                        whereboy5.append(doctypexod[1][(doctypexod[1].index(j)) - i])
                                                        i += 1


                                                    elif cells[doctypexod[1][(doctypexod[1].index(j)) - i]] == "⚪" or cells[
                                                        doctypexod[1][(doctypexod[1].index(j)) - i]] == "⬜" or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break
                        a = []
                        for k in doctypexod[1][(index2 + 1)::]:
                            if cells[k] == "⬛" or cells[k] == "⚫":
                                a.append(k)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                if deletechecers != 'a1' and deletechecers != 'a3' and deletechecers != 'a5' and deletechecers != 'a7' and deletechecers != 'b8' and deletechecers != 'd8' and deletechecers != 'f8' and deletechecers != 'h8' and deletechecers != 'h6' and deletechecers != 'h4' and deletechecers != 'h2' and deletechecers != 'g1' and deletechecers != 'e1' and deletechecers != 'c1':
                                    deletechecers = ''.join(a)
                                    for j in a:
                                        p = 1
                                        if u == 0:
                                            while 0<=(doctypexod[1].index(j)) + p < len(doctypexod[1]) and u == 0:
                                                if 0<=(doctypexod[1].index(j)) + p < len(doctypexod[1]) and (j != 'a1') and (j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                    if cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "•":
                                                        isboy = True
                                                        whereboy6.append(doctypexod[1][(doctypexod[1].index(j)) + p])
                                                        p += 1

                                                    elif cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "⚪" or cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "⬜" or cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "⬜" or cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break

                    whereboy = []
                    whereboy.extend(whereboy1)
                    whereboy.extend(whereboy2)
                    whereboy.extend(whereboy3)
                    whereboy.extend(whereboy4)
                    whereboy.extend(whereboy5)
                    whereboy.extend(whereboy6)
                    whereboy = set(whereboy)
                    boy_damki[white_damka] = list(whereboy)

            if isboy != True:
            # Проверка есть ли бой для белых
                if ('a1' in white_chekers) and (('b2' in black_chekers) or ('b2' in black_damki)) and ('c3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif (('с1' in white_chekers) and (('b2' in black_chekers) or ('b2' in black_damki)) and (
                        'a3' in none_chekers)) and whiteorblack == 'white':
                    isboy = True
                elif ('c1' in white_chekers) and (('d2' in black_chekers) or('d2' in black_damki)) and ('e3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e1' in white_chekers) and (('d2' in black_chekers) or ('d2' in black_damki)) and ('c3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e1' in white_chekers) and (('f2' in black_chekers) or ('f2' in black_damki)) and ('g3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g1' in white_chekers) and (('f2' in black_chekers) or ('f2' in black_damki)) and ('e3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('b2' in white_chekers) and (('c3' in black_chekers) or ('c3' in black_damki)) and ('d4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d2' in white_chekers) and (('c3' in black_chekers) or ('c3' in black_damki)) and ('b4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d2' in white_chekers) and (('e3' in black_chekers) or ('e3' in black_damki)) and ('f4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f2' in white_chekers) and (('e3' in black_chekers) or ('e3' in black_damki)) and ('d4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f2' in white_chekers) and (('g3' in black_chekers) or ('g3' in black_damki)) and ('h4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('h2' in white_chekers) and (('g3' in black_chekers) or ('g3' in black_damki)) and ('f4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('a3' in white_chekers) and (('b4' in black_chekers) or ('b4' in black_damki)) and ('c5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('a3' in white_chekers) and (('b2' in black_chekers) or ('b2' in black_damki)) and ('c1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c3' in white_chekers) and (('b2' in black_chekers) or ('b2' in black_damki)) and ('a1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c3' in white_chekers) and (('b4' in black_chekers) or ('b4' in black_damki)) and ('a5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c3' in white_chekers) and (('d2' in black_chekers) or ('d2' in black_damki)) and ('e1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c3' in white_chekers) and (('d4' in black_chekers) or ('d4' in black_damki)) and ('e5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e3' in white_chekers) and (('d2' in black_chekers) or ('d2' in black_damki)) and ('c1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e3' in white_chekers) and (('d4' in black_chekers) or ('d4' in black_damki)) and ('c5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e3' in white_chekers) and (('f2' in black_chekers) or ('f2' in black_damki)) and ('g1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e3' in white_chekers) and (('f4' in black_chekers) or ('f4' in black_damki)) and ('g5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g3' in white_chekers) and (('f2' in black_chekers) or ('f2' in black_damki)) and ('e1' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g3' in white_chekers) and (('f4' in black_chekers) or ('f4' in black_damki)) and ('e5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('b4' in white_chekers) and (('c3' in black_chekers) or ('c3' in black_damki)) and ('d2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('b4' in white_chekers) and (('c5' in black_chekers) or ('c5' in black_damki)) and ('d6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d4' in white_chekers) and (('c3' in black_chekers) or ('c3' in black_damki)) and ('b2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d4' in white_chekers) and (('c5' in black_chekers) or ('c5' in black_damki)) and ('b6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d4' in white_chekers) and (('e3' in black_chekers) or ('e3' in black_damki)) and ('f2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d4' in white_chekers) and (('e5' in black_chekers) or ('e5' in black_damki)) and ('f6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f4' in white_chekers) and (('e5' in black_chekers) or ('e5' in black_damki)) and ('d6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f4' in white_chekers) and (('e3' in black_chekers) or ('e3' in black_damki)) and ('d2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f4' in white_chekers) and (('g3' in black_chekers) or ('g3' in black_damki)) and ('h2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f4' in white_chekers) and (('g5' in black_chekers) or ('g5' in black_damki)) and ('h6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('h4' in white_chekers) and (('g5' in black_chekers) or ('g5' in black_damki)) and ('f6' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('h4' in white_chekers) and (('g3' in black_chekers) or ('g3' in black_damki)) and ('f2' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('a5' in white_chekers) and (('b6' in black_chekers) or ('b6' in black_damki)) and ('c7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('a5' in white_chekers) and (('b4' in black_chekers) or ('b4' in black_damki)) and ('c3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c5' in white_chekers) and (('b4' in black_chekers) or ('b4' in black_damki)) and ('a3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c5' in white_chekers) and (('b6' in black_chekers) or ('b6' in black_damki)) and ('a7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c5' in white_chekers) and (('d4' in black_chekers) or ('d4' in black_damki)) and ('e3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c5' in white_chekers) and (('d6' in black_chekers) or ('d6' in black_damki)) and ('e7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e5' in white_chekers) and (('d4' in black_chekers) or ('d4' in black_damki)) and ('c3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e5' in white_chekers) and (('d6' in black_chekers) or ('d6' in black_damki)) and ('c7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e5' in white_chekers) and (('f4' in black_chekers) or ('f4' in black_damki)) and ('g3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e5' in white_chekers) and (('f6' in black_chekers) or ('f6' in black_damki)) and ('g7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g5' in white_chekers) and (('f6' in black_chekers) or ('f6' in black_damki)) and ('e7' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g5' in white_chekers) and (('f4' in black_chekers) or ('f4' in black_damki)) and ('e3' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('b6' in white_chekers) and (('c5' in black_chekers) or ('c5' in black_damki)) and ('d4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('b6' in white_chekers) and (('c7' in black_chekers) or ('c7' in black_damki)) and ('d8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d6' in white_chekers) and (('c5' in black_chekers) or ('c5' in black_damki)) and ('b4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d6' in white_chekers) and (('c7' in black_chekers) or ('c7' in black_damki)) and ('b8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d6' in white_chekers) and (('e7' in black_chekers) or ('e7' in black_damki)) and ('f8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('d6' in white_chekers) and (('e5' in black_chekers) or ('e5' in black_damki)) and ('f4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f6' in white_chekers) and (('g7' in black_chekers) or ('g7' in black_damki)) and ('h8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f6' in white_chekers) and (('g5' in black_chekers) or ('g5' in black_damki)) and ('h4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f6' in white_chekers) and (('e7' in black_chekers) or ('e7' in black_damki)) and ('d8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('f6' in white_chekers) and (('e5' in black_chekers) or ('e5' in black_damki)) and ('d4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('h6' in white_chekers) and (('g7' in black_chekers) or ('g7' in black_damki)) and ('f8' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('h6' in white_chekers) and (('g5' in black_chekers) or ('g5' in black_damki)) and ('f4' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('a7' in white_chekers) and (('b6' in black_chekers) or ('b6' in black_damki)) and ('c5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c7' in white_chekers) and (('b6' in black_chekers) or ('b6' in black_damki)) and ('a5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('c7' in white_chekers) and (('d6' in black_chekers) or ('d6' in black_damki)) and ('e5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e7' in white_chekers) and (('d6' in black_chekers) or ('d6' in black_damki)) and ('c5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('e7' in white_chekers) and (('f6' in black_chekers) or ('f6' in black_damki)) and ('g5' in none_chekers) and whiteorblack == 'white':
                    isboy = True
                elif ('g7' in white_chekers) and (('f6' in black_chekers) or ('f6' in black_damki)) and ('e5' in none_chekers) and whiteorblack == 'white':
                    isboy = True

                else:
                    isboy = False
            return isboy
        def bexod1():
            global isboy1, deletechecers
            isboy1 = False
            boy_damki = {}
            white_chekers1 = []
            black_chekers1 = []
            none_chekers1 = []
            white_damki1 = []
            black_damki1 = []
            for i in cells.items():
                if i[1] == "⚫" and x1 == 0:
                    black_chekers1.append(i[0])
                elif i[1] == "⚫" and x1 == 1:
                    black_chekers1.append(y1)
                    z1 = 1
                elif i[1] == "⚪":
                    white_chekers1.append((i[0]))
                elif i[1] == "•":
                    none_chekers1.append(i[0])
                elif i[1] == "⬛":
                    black_damki1.append(i[0])
                elif i[1] == "⬜":
                    white_damki1.append(i[0])
                for black_damka in black_damki1:
                    doctypexod = []
                    for i in d1:
                        if black_damka == i:
                            doctypexod.append(d1)
                    for i in d2:
                        if black_damka == i:
                            doctypexod.append(d2)
                    for i in d3:
                        if black_damka == i:
                            doctypexod.append(d3)
                    for i in d4:
                        if black_damka == i:
                            doctypexod.append(d4)
                    for i in d5:
                        if black_damka == i:
                            doctypexod.append(d5)
                    for i in d6:
                        if black_damka == i:
                            doctypexod.append(d6)
                    for i in d7:
                        if black_damka == i:
                            doctypexod.append(d7)
                    for i in d8:
                        if black_damka == i:
                            doctypexod.append(d8)
                    for i in d9:
                        if black_damka == i:
                            doctypexod.append(d9)
                    for i in d10:
                        if black_damka == i:
                            doctypexod.append(d10)
                    for i in d11:
                        if black_damka == i:
                            doctypexod.append(d11)
                    for i in d12:
                        if black_damka == i:
                            doctypexod.append(d12)
                    for i in d13:
                        if black_damka == i:
                            doctypexod.append(d13)
                    a = []
                    if len(doctypexod) == 1:
                        index = doctypexod[0].index(black_damka)
                        if index == 0:
                            a = []
                            for i in doctypexod[0]:

                                if cells[i] == "⬛" or cells[i] == "⚫":
                                    a.append(i)
                                    if len(a) > 1:
                                        a.pop(-1)
                                    deletechecers = ''.join(a)
                                    u = 0
                                    for j in a:
                                        i = 1
                                        if u == 0:
                                            while 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]):
                                                if 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]) and (
                                                        j != 'a1') and (
                                                        j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1':
                                                    if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                        whereboy1.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                        isboy = True
                                                        i += 1


                                                    elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or \
                                                            cells[
                                                                doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or \
                                                            cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break

                        if index == 7:
                            a = []
                            for i in doctypexod[0][::-1]:
                                if cells[i] == "⬛" or cells[i] == "⚫":
                                    a.append(i)
                                    if len(a) > 1:
                                        a.pop(-1)
                                    deletechecers = ''.join(a)
                                    u = 0
                                    for j in a:
                                        i = 1
                                        if u == 0:
                                            while 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]):
                                                if 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]) and (
                                                        j != 'a1') and (
                                                        j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1':
                                                    if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                        whereboy2.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                        isboy = True
                                                        i += 1


                                                    elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or \
                                                            cells[
                                                                doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or \
                                                            cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                        u = 1
                                                        break
                                                else:
                                                    break
                                        else:
                                            break
                    elif len(doctypexod) == 2:
                        index = doctypexod[0].index(white_damka)
                        index2 = doctypexod[1].index(white_damka)
                        a = []
                        for i in doctypexod[0][(index + 1)::]:

                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                deletechecers = ''.join(a)
                                for j in a:
                                    i = 1
                                    if u == 0:
                                        while 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]) and u == 0:
                                            if 0 <= (doctypexod[0].index(j)) + i < len(doctypexod[0]) and (
                                                    j != 'a1') and (
                                                    j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                if cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "•":
                                                    isboy = True
                                                    whereboy3.append(doctypexod[0][(doctypexod[0].index(j)) + i])
                                                    i += 1


                                                elif cells[doctypexod[0][(doctypexod[0].index(j)) + i]] == "⚪" or cells[
                                                    doctypexod[0][(doctypexod[0].index(j)) + i]] == "⬜" or cells[
                                                    doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                    u = 1
                                                    break
                                            else:
                                                break
                                    else:
                                        break
                        a = []
                        for i in doctypexod[0][(index - 1)::-1]:
                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                deletechecers = ''.join(a)
                                for j in a:
                                    i = 1
                                    if u == 0:
                                        while 0 <= (doctypexod[0].index(j)) - i < len(doctypexod[0]) and u == 0:
                                            if 0 <= (doctypexod[0].index(j)) - i < len(doctypexod[0]) and (
                                                    j != 'a1') and (
                                                    j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                if cells[doctypexod[0][(doctypexod[0].index(j)) - i]] == "•":
                                                    whereboy4.append(
                                                        doctypexod[0][(doctypexod[0].index(j)) - i] or cells[
                                                            doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌")
                                                    i += 1
                                                    isboy = True


                                                elif cells[doctypexod[0][(doctypexod[0].index(j)) - i]] == "⚪" or cells[
                                                    doctypexod[0][(doctypexod[0].index(j)) - i]] == "⬜":
                                                    u = 1
                                                    break
                                            else:
                                                break
                                    else:
                                        break
                        a = []
                        for i in doctypexod[1][(index2 - 1)::-1]:
                            if cells[i] == "⬛" or cells[i] == "⚫":
                                a.append(i)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                deletechecers = ''.join(a)
                                for j in a:
                                    i = 1
                                    if u == 0:
                                        while 0 <= (doctypexod[1].index(j)) - i < len(doctypexod[1]) and u == 0:
                                            if 0 <= (doctypexod[1].index(j)) - i < len(doctypexod[1]) and (
                                                    j != 'a1') and (
                                                    j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                if cells[doctypexod[1][(doctypexod[1].index(j)) - i]] == "•":
                                                    isboy = True

                                                    whereboy5.append(doctypexod[1][(doctypexod[1].index(j)) - i])
                                                    i += 1


                                                elif cells[doctypexod[1][(doctypexod[1].index(j)) - i]] == "⚪" or cells[
                                                    doctypexod[1][(doctypexod[1].index(j)) - i]] == "⬜" or cells[
                                                    doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                    u = 1
                                                    break
                                            else:
                                                break
                                    else:
                                        break
                        a = []
                        for k in doctypexod[1][(index2 + 1)::]:
                            if cells[k] == "⬛" or cells[k] == "⚫":
                                a.append(k)
                                if len(a) > 1:
                                    a.pop(-1)
                                u = 0
                                deletechecers = ''.join(a)
                                for j in a:
                                    p = 1
                                    if u == 0:
                                        while 0 <= (doctypexod[1].index(j)) + p < len(doctypexod[1]) and u == 0:
                                            if 0 <= (doctypexod[1].index(j)) + p < len(doctypexod[1]) and (
                                                    j != 'a1') and (
                                                    j != 'a3') and j != 'a5' and j != 'a7' and j != 'b8' and j != 'd8' and j != 'f8' and j != 'h8' and j != 'h6' and j != 'h4' and j != 'h2' and j != 'g1' and j != 'e1' and j != 'c1' and u == 0:
                                                if cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "•":
                                                    isboy = True
                                                    whereboy6.append(doctypexod[1][(doctypexod[1].index(j)) + p])
                                                    p += 1

                                                elif cells[doctypexod[1][(doctypexod[1].index(j)) + p]] == "⚪" or cells[
                                                    doctypexod[1][(doctypexod[1].index(j)) + p]] == "⬜" or cells[
                                                    doctypexod[1][(doctypexod[1].index(j)) + p]] == "⬜" or cells[
                                                    doctypexod[0][(doctypexod[0].index(j)) + i]] == "❌":
                                                    u = 1
                                                    break
                                            else:
                                                break
                                    else:
                                        break

                    whereboy = []
                    whereboy.extend(whereboy1)
                    whereboy.extend(whereboy2)
                    whereboy.extend(whereboy3)
                    whereboy.extend(whereboy4)
                    whereboy.extend(whereboy5)
                    whereboy.extend(whereboy6)
                    whereboy = set(whereboy)
                    boy_damki[white_damka] = list(whereboy)


            if isboy1 != True:
                if 'h8' in black_chekers1 and (('g7' in white_chekers1) or ('g7' in white_damki1)) and 'f6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f8' in black_chekers1 and (('g7' in white_chekers1) or ('g7' in white_damki1)) and 'h6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f8' in black_chekers1 and (('e7' in white_chekers1) or ('e7' in white_damki1)) and 'd6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd8' in black_chekers1 and (('e7' in white_chekers1) or ('e7' in white_damki1)) and 'f6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd8' in black_chekers1 and (('c7' in white_chekers1) or ('c7' in white_damki1)) and 'b6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b8' in black_chekers1 and (('c7' in white_chekers1) or ('c7' in white_damki1)) and 'd6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'g7' in black_chekers1 and (('f6' in white_chekers1) or ('f6' in white_damki1)) and 'e5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e7' in black_chekers1 and (('f6' in white_chekers1) or ('f6' in white_damki1)) and 'g5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e7' in black_chekers1 and (('d6' in white_chekers1) or ('d6' in white_damki1)) and 'c5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c7' in black_chekers1 and (('d6' in white_chekers1) or ('d6' in white_damki1)) and 'e5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c7' in black_chekers1 and (('b6' in white_chekers1) or ('b6' in white_damki1)) and 'a5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'a7' in black_chekers1 and (('b6' in white_chekers1) or ('b6' in white_damki1)) and 'c5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'h6' in black_chekers1 and (('g7' in white_chekers1) or ('g7' in white_damki1)) and 'f8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'h6' in black_chekers1 and (('g5' in white_chekers1) or ('g5' in white_damki1)) and 'f4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f6' in black_chekers1 and (('g7' in white_chekers1) or ('g7' in white_damki1)) and 'h8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f6' in black_chekers1 and (('g5' in white_chekers1) or ('g5' in white_damki1)) and 'h4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f6' in black_chekers1 and (('e7' in white_chekers1) or ('e7' in white_damki1)) and 'd8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f6' in black_chekers1 and (('e5' in white_chekers1) or ('e5' in white_damki1)) and 'd4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd6' in black_chekers1 and (('e7' in white_chekers1) or ('e7' in white_damki1)) and 'f8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd6' in black_chekers1 and (('e5' in white_chekers1) or ('e5' in white_damki1)) and 'f4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd6' in black_chekers1 and (('c7' in white_chekers1) or ('c7' in white_damki1)) and 'b8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd6' in black_chekers1 and (('c5' in white_chekers1) or ('c5' in white_damki1)) and 'b4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b6' in black_chekers1 and (('c7' in white_chekers1) or ('c7' in white_damki1)) and 'd8' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b6' in black_chekers1 and (('c5' in white_chekers1) or ('c5' in white_damki1)) and 'd4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'g5' in black_chekers1 and (('f6' in white_chekers1) or ('f6' in white_damki1)) and 'e7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'g5' in black_chekers1 and (('f4' in white_chekers1) or ('f4' in white_damki1)) and 'e3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e5' in black_chekers1 and (('f6' in white_chekers1) or ('f6' in white_damki1)) and 'g7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e5' in black_chekers1 and (('f4' in white_chekers1) or ('f4' in white_damki1)) and 'g3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e5' in black_chekers1 and (('d6' in white_chekers1) or ('d6' in white_damki1)) and 'c7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e5' in black_chekers1 and (('d4' in white_chekers1) or ('d4' in white_damki1)) and 'c3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c5' in black_chekers1 and (('d6' in white_chekers1) or ('d6' in white_damki1)) and 'e7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c5' in black_chekers1 and (('d4' in white_chekers1) or ('d4' in white_damki1)) and 'e3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c5' in black_chekers1 and (('b6' in white_chekers1) or ('b6' in white_damki1)) and 'a7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c5' in black_chekers1 and (('b4' in white_chekers1) or ('b4' in white_damki1)) and 'a3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'a5' in black_chekers1 and (('b6' in white_chekers1) or ('b6' in white_damki1)) and 'c7' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'a5' in black_chekers1 and (('b4' in white_chekers1) or ('b4' in white_damki1)) and 'c3' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'h4' in black_chekers1 and (('g5' in white_chekers1) or ('g5' in white_damki1)) and 'f6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'h4' in black_chekers1 and (('g3' in white_chekers1) or ('g3' in white_damki1)) and 'f2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f4' in black_chekers1 and (('g3' in white_chekers1) or ('g3' in white_damki1)) and 'h2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f4' in black_chekers1 and (('g5' in white_chekers1) or ('g5' in white_damki1)) and 'h6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f4' in black_chekers1 and (('e3' in white_chekers1) or ('e3' in white_damki1)) and 'd2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f4' in black_chekers1 and (('e5' in white_chekers1) or ('e5' in white_damki1)) and 'd6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd4' in black_chekers1 and (('e5' in white_chekers1) or ('e5' in white_damki1)) and 'f6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd4' in black_chekers1 and (('e3' in white_chekers1) or ('e3' in white_damki1)) and 'f2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd4' in black_chekers1 and (('c5' in white_chekers1) or ('c5' in white_damki1)) and 'b6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd4' in black_chekers1 and (('c3' in white_chekers1) or ('c3' in white_damki1)) and 'b2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b4' in black_chekers1 and (('c3' in white_chekers1) or ('c3' in white_damki1)) and 'd2' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b4' in black_chekers1 and (('c5' in white_chekers1) or ('c5' in white_damki1)) and 'd6' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'g3' in black_chekers1 and (('f4' in white_chekers1) or ('f4' in white_damki1)) and 'e5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'g3' in black_chekers1 and (('f2' in white_chekers1) or ('f2' in white_damki1)) and 'e1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e3' in black_chekers1 and (('f4' in white_chekers1) or ('f4' in white_damki1)) and 'g5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e3' in black_chekers1 and (('f2' in white_chekers1) or ('f2' in white_damki1)) and 'g1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e3' in black_chekers1 and (('d4' in white_chekers1) or ('d4' in white_damki1)) and 'c5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'e3' in black_chekers1 and (('d2' in white_chekers1) or ('d2' in white_damki1)) and 'c1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c3' in black_chekers1 and (('d4' in white_chekers1) or ('d4' in white_damki1)) and 'e5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c3' in black_chekers1 and (('d2' in white_chekers1) or ('d2' in white_damki1)) and 'e1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c3' in black_chekers1 and (('b2' in white_chekers1) or ('b2' in white_damki1)) and 'a1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'c3' in black_chekers1 and (('b4' in white_chekers1) or ('b4' in white_damki1)) and 'a5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'a3' in black_chekers1 and (('b4' in white_chekers1) or ('b4' in white_damki1)) and 'c5' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'a3' in black_chekers1 and (('b2' in white_chekers1) or ('b2' in white_damki1)) and 'c1' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'h2' in black_chekers1 and (('g3' in white_chekers1) or ('g3' in white_damki1)) and 'f4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f2' in black_chekers1 and (('g3' in white_chekers1) or ('g3' in white_damki1)) and 'h4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'f2' in black_chekers1 and (('e3' in white_chekers1) or ('e3' in white_damki1)) and 'd4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd2' in black_chekers1 and (('e3' in white_chekers1) or ('e3' in white_damki1)) and 'f4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'd2' in black_chekers1 and (('c3' in white_chekers1) or ('c3' in white_damki1)) and 'b4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                elif 'b2' in black_chekers1 and (('c3' in white_chekers1) or ('c3' in white_damki1)) and 'd4' in none_chekers1 and whiteorblack == 'black':
                    isboy1 = True
                else:
                    isboy1 = False

            return isboy1



        #Проверка правильности боя для белых шашек.
        if z == 1:
            first = y
        if (first == 'a1' and second == 'c3' and bexod() == True and cells[first] == "⚪" and (cells['b2'] == "⚫" or cells['b2'] == '⬛') and cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b2'
        elif (first == 'c1' and second == 'a3' and bexod() == True and cells[first] == "⚪" and (cells['b2'] == "⚫" or cells['b2'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b2'
        elif (first == 'c1' and second == 'e3' and bexod() == True and cells[first] == "⚪" and (cells['d2'] == "⚫" or cells['d2'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd2'
        elif (first == 'e1' and second == 'c3' and bexod() == True and cells[first] == "⚪" and (cells['d2'] == "⚫" or cells['d2'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd2'
        elif (first == 'e1' and second == 'g3' and bexod() == True and cells[first] == "⚪" and (cells['f2'] == "⚫" or cells['f2'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f2'
        elif (first == 'g1' and second == 'e3' and bexod() == True and cells[first] == "⚪" and (cells['f2'] == "⚫" or cells['f2'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f2'
        elif (first == 'b2' and second == 'd4' and bexod() == True and cells[first] == "⚪" and (cells['c3'] == "⚫" or cells['c3'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c3'
        elif (first == 'd2' and second == 'b4' and bexod() == True and cells[first] == "⚪" and (cells['c3'] == "⚫" or cells['c3'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c3'
        elif (first == 'd2' and second == 'f4' and bexod() == True and cells[first] == "⚪" and (cells['e3'] == "⚫" or cells['e3'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e3'
        elif (first == 'f2' and second == 'd4' and bexod() == True and cells[first] == "⚪" and (cells['e3'] == "⚫" or cells['e3'] == '⬛') and cells[second] == '•')and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e3'
        elif (first == 'f2' and second == 'h4' and bexod() == True and cells[first] == "⚪" and (cells['g3'] == "⚫" or cells['g3'] == '⬛') and cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g3'
        elif (first == 'h2' and second == 'f4' and bexod() == True and cells[first] == "⚪" and (cells['g3'] == "⚫" or cells['g3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g3'
        elif (first == 'a3' and second == 'c1' and bexod() == True and cells[first] == "⚪" and (cells['b2'] == "⚫" or cells['b2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b2'
        elif (first == 'a3' and second == 'c5' and bexod() == True and cells[first] == "⚪" and (cells['b4'] == "⚫" or cells['b4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b4'
        elif (first == 'c3' and second == 'a5' and bexod() == True and cells[first] == "⚪" and (cells['b4'] == "⚫" or cells['b4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b4'
        elif (first == 'c3' and second == 'a1' and bexod() == True and cells[first] == "⚪" and (cells['b2'] == "⚫" or cells['b2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b2'
        elif (first == 'c3' and second == 'e1' and bexod() == True and cells[first] == "⚪" and (cells['d2'] == "⚫" or cells['d2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd2'
        elif (first == 'c3' and second == 'e5' and bexod() == True and cells[first] == "⚪" and (cells['d4'] == "⚫" or cells['d4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd4'
        elif (first == 'e3' and second == 'c1' and bexod() == True and cells[first] == "⚪" and (cells['d2'] == "⚫" or cells['d2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd2'
        elif (first == 'e3' and second == 'c5' and bexod() == True and cells[first] == "⚪" and (cells['d4'] == "⚫" or cells['d4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd4'
        elif (first == 'e3' and second == 'g1' and bexod() == True and cells[first] == "⚪" and (cells['f2'] == "⚫" or cells['f2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f2'
        elif (first == 'e3' and second == 'g5' and bexod() == True and cells[first] == "⚪" and (cells['f4'] == "⚫" or cells['f4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f4'
        elif (first == 'g3' and second == 'e1' and bexod() == True and cells[first] == "⚪" and (cells['f2'] == "⚫" or cells['f2'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f2'
        elif (first == 'g3' and second == 'e5' and bexod() == True and cells[first] == "⚪" and (cells['f4'] == "⚫" or cells['f4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f4'
        elif (first == 'b4' and second == 'd2' and bexod() == True and cells[first] == "⚪" and (cells['c3'] == "⚫" or cells['c3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c3'
        elif (first == 'b4' and second == 'd6' and bexod() == True and cells[first] == "⚪" and (cells['c5'] == "⚫" or cells['c5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c5'
        elif (first == 'd4' and second == 'b2' and bexod() == True and cells[first] == "⚪" and (cells['c3'] == "⚫" or cells['c3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c3'
        elif (first == 'd4' and second == 'b6' and bexod() == True and cells[first] == "⚪" and (cells['c5'] == "⚫" or cells['c5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c5'
        elif (first == 'd4' and second == 'f6' and bexod() == True and cells[first] == "⚪" and (cells['e5'] == "⚫" or cells['e5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e5'
        elif (first == 'd4' and second == 'f2' and bexod() == True and cells[first] == "⚪" and (cells['e3'] == "⚫" or cells['e3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e3'
        elif (first == 'f4' and second == 'd2' and bexod() == True and cells[first] == "⚪" and (cells['e3'] == "⚫" or cells['e3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e3'
        elif (first == 'f4' and second == 'd6' and bexod() == True and cells[first] == "⚪" and (cells['e5'] == "⚫" or cells['e5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e5'
        elif (first == 'f4' and second == 'h2' and bexod() == True and cells[first] == "⚪" and (cells['g3'] == "⚫" or cells['g3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g3'
        elif (first == 'f4' and second == 'h6' and bexod() == True and cells[first] == "⚪" and (cells['g5'] == "⚫" or cells['g5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g5'
        elif (first == 'h4' and second == 'f2' and bexod() == True and cells[first] == "⚪" and (cells['g3'] == "⚫" or cells['g3'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g3'
        elif (first == 'h4' and second == 'f6' and bexod() == True and cells[first] == "⚪" and (cells['g5'] == "⚫" or cells['g5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g5'
        elif (first == 'a5' and second == 'c3' and bexod() == True and cells[first] == "⚪" and (cells['b4'] == "⚫" or cells['b4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b4'
        elif (first == 'a5' and second == 'c7' and bexod() == True and cells[first] == "⚪" and (cells['b6'] == "⚫" or cells['b6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b6'
        elif (first == 'c5' and second == 'a3' and bexod() == True and cells[first] == "⚪" and (cells['b4'] == "⚫" or cells['b4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b4'
        elif (first == 'c5' and second == 'a7' and bexod() == True and cells[first] == "⚪" and (cells['b6'] == "⚫" or cells['b6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b6'
        elif (first == 'c5' and second == 'e3' and bexod() == True and cells[first] == "⚪" and (cells['d4'] == "⚫" or cells['d4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd4'
        elif (first == 'c5' and second == 'e7' and bexod() == True and cells[first] == "⚪" and (cells['d6'] == "⚫" or cells['d6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd6'
        elif (first == 'e5' and second == 'c3' and bexod() == True and cells[first] == "⚪" and (cells['d4'] == "⚫" or cells['d4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd4'
        elif (first == 'e5' and second == 'c7' and bexod() == True and cells[first] == "⚪" and (cells['d6'] == "⚫" or cells['d6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd6'
        elif (first == 'e5' and second == 'g3' and bexod() == True and cells[first] == "⚪" and (cells['f4'] == "⚫" or cells['f4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f4'
        elif (first == 'e5' and second == 'g7' and bexod() == True and cells[first] == "⚪" and (cells['f6'] == "⚫" or cells['f6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f6'
        elif (first == 'g5' and second == 'e3' and bexod() == True and cells[first] == "⚪" and (cells['f4'] == "⚫" or cells['f4'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f4'
        elif (first == 'g5' and second == 'e7' and bexod() == True and cells[first] == "⚪" and (cells['f6'] == "⚫" or cells['f6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f6'
        elif (first == 'b6' and second == 'd4' and bexod() == True and cells[first] == "⚪" and (cells['c5'] == "⚫" or cells['c5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c5'
        elif (first == 'b6' and second == 'd8' and bexod() == True and cells[first] == "⚪" and (cells['c7'] == "⚫" or cells['c7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c7'
        elif (first == 'd6' and second == 'b4' and bexod() == True and cells[first] == "⚪" and (cells['c5'] == "⚫" or cells['c5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c5'
        elif (first == 'd6' and second == 'b8' and bexod() == True and cells[first] == "⚪" and (cells['c7'] == "⚫" or cells['c7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'c7'
        elif (first == 'd6' and second == 'f4' and bexod() == True and cells[first] == "⚪" and (cells['e5'] == "⚫" or cells['e5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e5'
        elif (first == 'd6' and second == 'f8' and bexod() == True and cells[first] == "⚪" and (cells['e7'] == "⚫" or cells['e7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e7'
        elif (first == 'f6' and second == 'd8' and bexod() == True and cells[first] == "⚪" and (cells['e7'] == "⚫" or cells['e7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e7'
        elif (first == 'f6' and second == 'd4' and bexod() == True and cells[first] == "⚪" and (cells['e5'] == "⚫" or cells['e5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'e5'
        elif (first == 'f6' and second == 'h4' and bexod() == True and cells[first] == "⚪" and (cells['g5'] == "⚫" or cells['g5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g5'
        elif (first == 'f6' and second == 'h8' and bexod() == True and cells[first] == "⚪" and (cells['g7'] == "⚫" or cells['g7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g7'
        elif (first == 'h6' and second == 'f4' and bexod() == True and cells[first] == "⚪" and (cells['g5'] == "⚫" or cells['g5'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g5'
        elif (first == 'h6' and second == 'f8' and bexod() == True and cells[first] == "⚪" and (cells['g7'] == "⚫" or cells['g7'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'g7'
        elif (first == 'a7' and second == 'c5' and bexod() == True and cells[first] == "⚪" and (cells['b6'] == "⚫" or cells['b6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b6'
        elif (first == 'c7' and second == 'a5' and bexod() == True and cells[first] == "⚪" and (cells['b6'] == "⚫" or cells['b6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'b6'
        elif (first == 'c7' and second == 'e5' and bexod() == True and cells[first] == "⚪" and (cells['d6'] == "⚫" or cells['d6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd6'
        elif (first == 'e7' and second == 'c5' and bexod() == True and cells[first] == "⚪" and (cells['d6'] == "⚫" or cells['d6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'd6'
        elif (first == 'e7' and second == 'g5' and bexod() == True and cells[first] == "⚪" and (cells['f6'] == "⚫" or cells['f6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f6'
        elif (first == 'g7' and second == 'e5' and bexod() == True and cells[first] == "⚪" and (cells['f6'] == "⚫" or cells['f6'] == '⬛') and
              cells[second] == '•') and whiteorblack == 'white':
            Trueboy = True
            deletechecers = 'f6'
        else:
            Trueboy = False


        #Правильный бой за черных
        if z1 == 1:
            first = y1
        if (first == 'h8' and second == 'f6' and bexod1() == True and cells[first] == "⚫" and (cells['g7'] == "⚪" or cells['g7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g7'
        elif (first == 'f8' and second == 'h6' and bexod1() == True and cells[first] == "⚫" and (cells['g7'] == "⚪" or cells['g7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g7'
        elif (first == 'f8' and second == 'd8' and bexod1() == True and cells[first] == "⚫" and (cells['e7'] == "⚪" or cells['e7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e7'
        elif (first == 'd8' and second == 'f6' and bexod1() == True and cells[first] == "⚫" and (cells['e7'] == "⚪" or cells['e7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e7'
        elif (first == 'd8' and second == 'b6' and bexod1() == True and cells[first] == "⚫" and (cells['c7'] == "⚪" or cells['c7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c7'
        elif (first == 'b8' and second == 'd6' and bexod1() == True and cells[first] == "⚫" and (cells['c7'] == "⚪" or cells['c7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c7'
        elif (first == 'g7' and second == 'e5' and bexod1() == True and cells[first] == "⚫" and (cells['f6'] == "⚪" or cells['f6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f6'
        elif (first == 'e7' and second == 'g5' and bexod1() == True and cells[first] == "⚫" and (cells['f6'] == "⚪" or cells['f6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f6'
        elif (first == 'e7' and second == 'c5' and bexod1() == True and cells[first] == "⚫" and (cells['d6'] == "⚪" or cells['d6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd6'
        elif (first == 'c7' and second == 'e5' and bexod1() == True and cells[first] == "⚫" and (cells['d6'] == "⚪" or cells['d6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd6'
        elif (first == 'c7' and second == 'a5' and bexod1() == True and cells[first] == "⚫" and (cells['b6'] == "⚪" or cells['b6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b6'
        elif (first == 'a7' and second == 'c5' and bexod1() == True and cells[first] == "⚫" and (cells['b6'] == "⚪" or cells['b6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b6'
        elif (first == 'h6' and second == 'f8' and bexod1() == True and cells[first] == "⚫" and (cells['g7'] == "⚪" or cells['g7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g7'
        elif (first == 'h6' and second == 'f4' and bexod1() == True and cells[first] == "⚫" and (cells['g5'] == "⚪" or cells['g5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g5'
        elif (first == 'f6' and second == 'h8' and bexod1() == True and cells[first] == "⚫" and (cells['g7'] == "⚪" or cells['g7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g7'
        elif (first == 'f6' and second == 'h4' and bexod1() == True and cells[first] == "⚫" and (cells['g5'] == "⚪" or cells['g5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g5'
        elif (first == 'f6' and second == 'd8' and bexod1() == True and cells[first] == "⚫" and (cells['e7'] == "⚪" or cells['e7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e7'
        elif (first == 'f6' and second == 'd4' and bexod1() == True and cells[first] == "⚫" and (cells['e5'] == "⚪" or cells['e5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e5'
        elif (first == 'd6' and second == 'f8' and bexod1() == True and cells[first] == "⚫" and (cells['e7'] == "⚪" or cells['e7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e7'
        elif (first == 'd6' and second == 'f4' and bexod1() == True and cells[first] == "⚫" and (cells['e5'] == "⚪" or cells['e5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e5'
        elif (first == 'd6' and second == 'b8' and bexod1() == True and cells[first] == "⚫" and (cells['c7'] == "⚪" or cells['c7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c7'
        elif (first == 'd6' and second == 'b4' and bexod1() == True and cells[first] == "⚫" and (cells['c5'] == "⚪" or cells['c5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c5'
        elif (first == 'b6' and second == 'd8' and bexod1() == True and cells[first] == "⚫" and (cells['c7'] == "⚪" or cells['c7'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c7'
        elif (first == 'b6' and second == 'd4' and bexod1() == True and cells[first] == "⚫" and (cells['c5'] == "⚪" or cells['c5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c5'
        elif (first == 'g5' and second == 'e7' and bexod1() == True and cells[first] == "⚫" and (cells['f6'] == "⚪" or cells['f6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f6'
        elif (first == 'g5' and second == 'e3' and bexod1() == True and cells[first] == "⚫" and (cells['f4'] == "⚪" or cells['f4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f4'
        elif (first == 'e5' and second == 'g7' and bexod1() == True and cells[first] == "⚫" and (cells['f6'] == "⚪" or cells['f6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f6'
        elif (first == 'e5' and second == 'g3' and bexod1() == True and cells[first] == "⚫" and (cells['f4'] == "⚪" or cells['f4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f4'
        elif (first == 'e5' and second == 'c7' and bexod1() == True and cells[first] == "⚫" and (cells['d6'] == "⚪" or cells['d6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd6'
        elif (first == 'e5' and second == 'c3' and bexod1() == True and cells[first] == "⚫" and (cells['d4'] == "⚪" or cells['d4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd4'
        elif (first == 'c5' and second == 'e3' and bexod1() == True and cells[first] == "⚫" and (cells['d4'] == "⚪" or cells['d4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd4'
        elif (first == 'c5' and second == 'e7' and bexod1() == True and cells[first] == "⚫" and (cells['d6'] == "⚪" or cells['d6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd6'
        elif (first == 'c5' and second == 'a7' and bexod1() == True and cells[first] == "⚫" and (cells['b6'] == "⚪" or cells['b6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b6'
        elif (first == 'c5' and second == 'a3' and bexod1() == True and cells[first] == "⚫" and (cells['b4'] == "⚪" or cells['b4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b4'
        elif (first == 'a5' and second == 'c7' and bexod1() == True and cells[first] == "⚫" and (cells['b6'] == "⚪" or cells['b6'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b6'
        elif (first == 'a5' and second == 'c3' and bexod1() == True and cells[first] == "⚫" and (cells['b4'] == "⚪" or cells['b4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b4'
        elif (first == 'h4' and second == 'f6' and bexod1() == True and cells[first] == "⚫" and (cells['g5'] == "⚪" or cells['g5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g5'
        elif (first == 'h4' and second == 'f2' and bexod1() == True and cells[first] == "⚫" and (cells['g3'] == "⚪" or cells['g3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g3'
        elif (first == 'f4' and second == 'h2' and bexod1() == True and cells[first] == "⚫" and (cells['g3'] == "⚪" or cells['g3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g3'
        elif (first == 'f4' and second == 'h6' and bexod1() == True and cells[first] == "⚫" and (cells['g5'] == "⚪" or cells['g5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g5'
        elif (first == 'f4' and second == 'd2' and bexod1() == True and cells[first] == "⚫" and (cells['e3'] == "⚪" or cells['e3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e3'
        elif (first == 'f4' and second == 'd6' and bexod1() == True and cells[first] == "⚫" and (cells['e5'] == "⚪" or cells['e5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e5'
        elif (first == 'd4' and second == 'f6' and bexod1() == True and cells[first] == "⚫" and (cells['e5'] == "⚪" or cells['e5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e5'
        elif (first == 'd4' and second == 'f2' and bexod1() == True and cells[first] == "⚫" and (cells['e3'] == "⚪" or cells['e3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e3'
        elif (first == 'd4' and second == 'b6' and bexod1() == True and cells[first] == "⚫" and (cells['c5'] == "⚪" or cells['c5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c5'
        elif (first == 'd4' and second == 'b2' and bexod1() == True and cells[first] == "⚫" and (cells['c5'] == "⚪" or cells['c5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c5'
        elif (first == 'b4' and second == 'd6' and bexod1() == True and cells[first] == "⚫" and (cells['c5'] == "⚪" or cells['c5'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c5'
        elif (first == 'b4' and second == 'd2' and bexod1() == True and cells[first] == "⚫" and (cells['c3'] == "⚪" or cells['c3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c3'
        elif (first == 'g3' and second == 'e1' and bexod1() == True and cells[first] == "⚫" and (cells['f2'] == "⚪" or cells['f2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f2'
        elif (first == 'g3' and second == 'e5' and bexod1() == True and cells[first] == "⚫" and (cells['f4'] == "⚪" or cells['f4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f4'
        elif (first == 'e3' and second == 'g1' and bexod1() == True and cells[first] == "⚫" and (cells['f2'] == "⚪" or cells['f2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f2'
        elif (first == 'e3' and second == 'g5' and bexod1() == True and cells[first] == "⚫" and (cells['f4'] == "⚪" or cells['f4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'f4'
        elif (first == 'e3' and second == 'c1' and bexod1() == True and cells[first] == "⚫" and (cells['d2'] == "⚪" or cells['d2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd2'
        elif (first == 'e3' and second == 'c5' and bexod1() == True and cells[first] == "⚫" and (cells['d4'] == "⚪" or cells['d4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd4'
        elif (first == 'c3' and second == 'e1' and bexod1() == True and cells[first] == "⚫" and (cells['d2'] == "⚪" or cells['d2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd2'
        elif (first == 'c3' and second == 'e5' and bexod1() == True and cells[first] == "⚫" and (cells['d4'] == "⚪" or cells['d4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'd4'
        elif (first == 'c3' and second == 'a1' and bexod1() == True and cells[first] == "⚫" and (cells['b2'] == "⚪" or cells['b2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b2'
        elif (first == 'c3' and second == 'a5' and bexod1() == True and cells[first] == "⚫" and (cells['b4'] == "⚪" or cells['b4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b4'
        elif (first == 'a3' and second == 'c5' and bexod1() == True and cells[first] == "⚫" and (cells['b4'] == "⚪" or cells['b4'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b4'
        elif (first == 'a3' and second == 'c1' and bexod1() == True and cells[first] == "⚫" and (cells['b2'] == "⚪" or cells['b2'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'b2'
        elif (first == 'h2' and second == 'f4' and bexod1() == True and cells[first] == "⚫" and (cells['g3'] == "⚪" or cells['g3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g3'
        elif (first == 'f2' and second == 'h4' and bexod1() == True and cells[first] == "⚫" and (cells['g3'] == "⚪" or cells['g3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'g3'
        elif (first == 'f2' and second == 'd4' and bexod1() == True and cells[first] == "⚫" and (cells['e3'] == "⚪" or cells['e3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e3'
        elif (first == 'd2' and second == 'f4' and bexod1() == True and cells[first] == "⚫" and (cells['e3'] == "⚪" or cells['e3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'e3'
        elif (first == 'd2' and second == 'b4' and bexod1() == True and cells[first] == "⚫" and (cells['c3'] == "⚪" or cells['c3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c3'
        elif (first == 'b2' and second == 'd4' and bexod1() == True and cells[first] == "⚫" and (cells['c3'] == "⚪" or cells['c3'] == "⬜") and
              cells[second] == '•') and whiteorblack == 'black':
            Trueboy1 = True
            deletechecers = 'c3'
        else:
            Trueboy1 = False







        #Правило хода для простых белых шашек
        if first != '' and second != '' and whiteorblack == 'white' and cells[first] == "⚪" and bexod() == False:
            if first == 'a1' and second == 'b2':
                trueorfalse = True
            elif first == 'c1' and (second == 'b2' or second == 'd2'):
                trueorfalse = True
            elif first == 'e1' and (second == 'd2' or second == 'f2'):
                trueorfalse = True
            elif first == 'g1' and (second == 'f2' or second == 'h2'):
                trueorfalse = True
            elif first == 'b2' and (second == 'a3' or second == 'c3'):
                trueorfalse = True
            elif first == 'd2' and (second == 'c3' or second == 'e3'):
                trueorfalse = True
            elif first == 'f2' and (second == 'e3' or second == 'g3'):
                trueorfalse = True
            elif first == 'h2' and second == 'g3':
                trueorfalse = True
            elif first == 'a3' and (second == 'b4'):
                trueorfalse = True
            elif first == 'c3' and (second == 'b4' or second == 'd4'):
                trueorfalse = True
            elif first == 'e3' and (second == 'd4' or second == 'f4'):
                trueorfalse = True
            elif first == 'g3' and (second == 'f4' or second == 'h4'):
                trueorfalse = True
            elif first == 'b4' and (second == 'a5' or second == 'c5'):
                trueorfalse = True
            elif first == 'd4' and (second == 'c5' or second == 'e5'):
                trueorfalse = True
            elif first == 'f4' and (second == 'e5' or second == 'g5'):
                trueorfalse = True
            elif first == 'h4' and second == 'g5':
                trueorfalse = True
            elif first == 'a5' and second == 'b6':
                trueorfalse = True
            elif first == 'c5' and (second == 'b6' or second == 'd6'):
                trueorfalse = True
            elif first == 'e5' and (second == 'd6' or second == 'f6'):
                trueorfalse = True
            elif first == 'g5' and (second == 'f6' or second == 'h6'):
                trueorfalse = True
            elif first == 'b6' and (second == 'a7' or second == 'c7'):
                trueorfalse = True
            elif first == 'd6' and (second == 'c7' or second == 'e7'):
                trueorfalse = True
            elif first == 'f6' and (second == 'e7' or second == 'g7'):
                trueorfalse = True
            elif first == 'h6' and second == 'g7':
                trueorfalse = True
            elif first == 'a7' and second == 'b8':
                trueorfalse = True
            elif first == 'c7' and (second == 'b8' or second == 'd8'):
                trueorfalse = True
            elif first == 'e7' and (second == 'd8' or second == 'f8'):
                trueorfalse = True
            elif first == 'g7' and (second == 'f8' or second == 'h8'):
                trueorfalse = True
            else:
                trueorfalse = False
        #Правило для простых черных шашек.
        elif first != '' and second != '' and whiteorblack == 'black' and cells[first] == "⚫":
            if first == 'h8' and second == 'g7':
                trueorfalse1 = True
            elif first == 'f8' and (second == 'g7' or second == 'e7'):
                trueorfalse1 = True
            elif first == 'd8' and (second == 'e7' or second == 'c7'):
                trueorfalse1 = True
            elif first == 'b8' and (second == 'a7' or second == 'c7'):
                trueorfalse1 = True
            elif first == 'g7' and (second == 'h6' or second == 'f6'):
                trueorfalse1 = True
            elif first == 'e7' and (second == 'f6' or second == 'd6'):
                trueorfalse1 = True
            elif first == 'c7' and (second == 'd6' or second == 'b6'):
                trueorfalse1 = True
            elif first == 'a7' and second == 'b6':
                trueorfalse1 = True
            elif first == 'h6' and second == 'g5':
                trueorfalse1 = True
            elif first == 'f6' and (second == 'g5' or second == 'e5'):
                trueorfalse1 = True
            elif first == 'd6' and (second == 'e5' or second == 'c5'):
                trueorfalse1 = True
            elif first == 'b6' and (second == 'c5' or second == 'a5'):
                trueorfalse1 = True
            elif first == 'g5' and (second == 'h4' or second == 'f4'):
                trueorfalse1 = True
            elif first == 'e5' and (second == 'f4' or second == 'd4'):
                trueorfalse1 = True
            elif first == 'c5' and (second == 'd4' or second == 'b4'):
                trueorfalse1 = True
            elif first == 'a5' and second == 'b4':
                trueorfalse1 = True
            elif first == 'h4' and (second == 'g3'):
                trueorfalse1 = True
            elif first == 'f4' and (second == 'g3' or second == 'e3'):
                trueorfalse1 = True
            elif first == 'd4' and (second == 'e3' or second == 'c3'):
                trueorfalse1 = True
            elif first == 'b4' and (second == 'c3' or second == 'a3'):
                trueorfalse1 = True
            elif first == 'g3' and (second == 'h2' or second == 'f2'):
                trueorfalse1 = True
            elif first == 'e3' and (second == 'f2' or second == 'd2'):
                trueorfalse1 = True
            elif first == 'c3' and (second == 'd2' or second == 'b2'):
                trueorfalse1 = True
            elif first == 'a3' and second == 'b2':
                trueorfalse1 = True
            elif first == 'h2' and second == 'g1':
                trueorfalse1 = True
            elif first == 'f2' and (second == 'g1' or second == 'e1'):
                trueorfalse1 = True
            elif first == 'd2' and (second == 'e1' or second == 'c1'):
                trueorfalse1 = True
            elif first == 'b2' and (second == 'c1' or second == 'a1'):
                trueorfalse1 = True
            else:
                trueorfalse1 = False
        if cells[first] == "⬜" and whiteorblack == 'white':
            doctypexod = []
            white_damka = first
            for i in d1:
                if i == first:
                    doctypexod.append(list(d1))
            for i in d2:
                if i == first:
                    doctypexod.append(list(d2))
            for i in d3:
                if i == first:
                    doctypexod.append(list(d3))
            for i in d4:
                if i == first:
                    doctypexod.append(list(d4))
            for i in d5:
                if i == first:
                    doctypexod.append(list(d5))
            for i in d6:
                if i == first:
                    doctypexod.append(list(d6))
            for i in d7:
                if i == first:
                    doctypexod.append(list(d7))
            for i in d8:
                if i == first:
                    doctypexod.append(list(d8))
            for i in d9:
                if i == first:
                    doctypexod.append(list(d9))
            for i in d10:
                if i == first:
                    doctypexod.append(list(d10))
            for i in d11:
                if i == first:
                    doctypexod.append(list(d11))
            for i in d12:
                if i == first:
                    doctypexod.append(list(d12))
            for i in d13:
                if i == first:
                    doctypexod.append(list(d13))
            if len(doctypexod) == 1:
                index = doctypexod[0].index(first)
                isxod = []
                if index == 0:

                    for i in doctypexod[0][(index+1):]:
                        while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                            if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                                break
                            else:

                                isxod.append(i)
                                break
                    docxod = []
                    for j in isxod:
                        if doctypexod[0][1::].index(j) == isxod.index(j):
                            docxod.append(j)
                    isxod = []
                    if (docxod == []) or (second not in docxod):
                        first = call.data
                        second = ''
                elif index == 7:
                    for i in doctypexod[0][(index-1)::-1]:
                        while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                            if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                                break
                            else:

                                isxod.append(i)
                                break
                    docxod = []
                    for j in isxod:
                        if doctypexod[0][-2::-1].index(j) == isxod.index(j):
                            docxod.append(j)
                    isxod = []
                    if (docxod == []) or (second not in docxod):
                        first = call.data
                        second = ''
            elif len(doctypexod) == 2:
                isxod = []
                index = doctypexod[0].index(first)
                index2 = doctypexod[1].index(first)
                for i in doctypexod[0][(index + 1):]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                            break
                        else:

                            isxod.append(i)
                            break
                docxod = []

                for j in isxod:
                    if doctypexod[0][(index+1)::].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod1 = docxod.copy()
                isxod = []
                for i in doctypexod[0][(index - 1)::-1]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                            break
                        else:

                            isxod.append(i)
                            break

                docxod = []
                for j in isxod:
                    if doctypexod[0][(index-1)::-1].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod2 = docxod.copy()
                isxod = []
                for i in doctypexod[1][(index2 -1)::-1]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                            break
                        else:

                            isxod.append(i)
                            break

                docxod = []
                for j in isxod:
                    if doctypexod[1][(index2 -1)::-1].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod3 = docxod.copy()
                isxod = []
                for i in doctypexod[1][(index2 + 1):]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                            break
                        else:
                            isxod.append(i)
                            break
                docxod = []
                for j in isxod:
                    if doctypexod[1][(index2+1)::].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod4 = docxod.copy()
                isxod = []



                docxod = []
                docxod.extend(docxod1)
                docxod.extend(docxod2)
                docxod.extend(docxod3)
                docxod.extend(docxod4)
                isxod = []
                #int(docxod)
                if (docxod == []) or (second not in docxod):
                    first = call.data
                    second = ''
            else:
                first = call.data
                second = ''
        if cells[first] == "⬛" and whiteorblack == 'black':
            doctypexod = []
            white_damka = first
            for i in d1:
                if i == first:
                    doctypexod.append(list(d1))
            for i in d2:
                if i == first:
                    doctypexod.append(list(d2))
            for i in d3:
                if i == first:
                    doctypexod.append(list(d3))
            for i in d4:
                if i == first:
                    doctypexod.append(list(d4))
            for i in d5:
                if i == first:
                    doctypexod.append(list(d5))
            for i in d6:
                if i == first:
                    doctypexod.append(list(d6))
            for i in d7:
                if i == first:
                    doctypexod.append(list(d7))
            for i in d8:
                if i == first:
                    doctypexod.append(list(d8))
            for i in d9:
                if i == first:
                    doctypexod.append(list(d9))
            for i in d10:
                if i == first:
                    doctypexod.append(list(d10))
            for i in d11:
                if i == first:
                    doctypexod.append(list(d11))
            for i in d12:
                if i == first:
                    doctypexod.append(list(d12))
            for i in d13:
                if i == first:
                    doctypexod.append(list(d13))
            if len(doctypexod) == 1:
                index = doctypexod[0].index(first)
                isxod = []
                if index == 0:

                    for i in doctypexod[0][(index+1):]:
                        while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫"):
                            if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫"):
                                break
                            else:

                                isxod.append(i)
                                break
                    docxod = []
                    for j in isxod:
                        if doctypexod[0][1::].index(j) == isxod.index(j):
                            docxod.append(j)
                    isxod = []
                    if (docxod == []) or (second not in docxod):
                        first = call.data
                        second = ''
                elif index == 7:
                    for i in doctypexod[0][(index-1)::-1]:
                        while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫") or cells[i] != '❌':
                            if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫") or cells[i] == '❌':
                                break
                            else:

                                isxod.append(i)
                                break
                    docxod = []
                    for j in isxod:
                        if doctypexod[0][-2::-1].index(j) == isxod.index(j):
                            docxod.append(j)
                    isxod = []
                    if (docxod == []) or (second not in docxod):
                        first = call.data
                        second = ''
            elif len(doctypexod) == 2:
                isxod = []
                index = doctypexod[0].index(first)
                index2 = doctypexod[1].index(first)
                for i in doctypexod[0][(index + 1):]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫") or cells[i] != '❌':
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫") or cells[i] == '❌':
                            break
                        else:

                            isxod.append(i)
                            break
                docxod = []

                for j in isxod:
                    if doctypexod[0][(index+1)::].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod1 = docxod.copy()
                isxod = []
                for i in doctypexod[0][(index - 1)::-1]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫") or cells[i] != '❌':
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫") or cells[i] == '❌':
                            break
                        else:

                            isxod.append(i)
                            break

                docxod = []
                for j in isxod:
                    if doctypexod[0][(index-1)::-1].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod2 = docxod.copy()
                isxod = []
                for i in doctypexod[1][(index - 1)::-1]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫")  or cells[i] != '❌':
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫") or cells[i] == '❌':
                            break
                        else:

                            isxod.append(i)
                            break

                docxod = []
                for j in isxod:
                    if doctypexod[1][(index-1)::-1].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod3 = docxod.copy()
                isxod = []
                for i in doctypexod[1][(index2 + 1):]:
                    while (cells[i] != "⚪") or (cells[i] != "⬜") or (cells[i] != "⬛") or (cells[i] != "⚫") or cells[i] != '❌':
                        if (cells[i] == "⚪") or (cells[i] == "⬜") or (cells[i] == "⬛") or (cells[i] == "⚫") or cells[i] == '❌':
                            break
                        else:
                            isxod.append(i)
                            break
                docxod = []
                for j in isxod:
                    if doctypexod[1][(index2+1)::].index(j) == isxod.index(j):
                        docxod.append(j)
                docxod4 = docxod.copy()
                isxod = []



                docxod = []
                docxod.extend(docxod1)
                docxod.extend(docxod2)
                docxod.extend(docxod3)
                docxod.extend(docxod4)
                isxod = []
                #int(docxod)
                if (docxod == []) or (second not in docxod):
                    first = call.data
                    second = ''
            else:
                first = call.data
                second = ''
        #Передвижение шашек
        if whiteorblack == 'white' and first != '' and second != '' and cells[first] == "⬜" and second in docxod and bexod() == False:
            cells[first] = '•'
            cells[second] = "⬜"
            whiteorblack = 'black'
        if whiteorblack == 'black' and first != '' and second != '' and cells[first] == "⬛" and second in docxod and bexod1() == False:
            cells[first] = '•'
            cells[second] = "⬛"
            whiteorblack = 'white'
        if whiteorblack == 'white' and first != '' and second != '' and cells[first] == "⬜" and bexod() == True:
            print(second, boy_damki[first])
            cells[first] = '•'
            print(second)
            cells[deletechecers] = '❌'
            cells[second] = "⬜"
            x1 = 1
            y1 = second
            z1 = 1
            if bexod1() == False:
                for i in cells.items():
                    if i[1] == '❌':
                        cells[i[0]] = '•'
                whiteorblack = 'white'
                x1 = 0
                y1 = ""
                z1 = 0
            deletechecers = ''
            first = ''
            second = ''
        if whiteorblack == 'black' and first != '' and second != '' and cells[first] == "⬛" and bexod1() == True:
            pass


        if whiteorblack == 'white' and (first != '') and (second != '') and trueorfalse == True and bexod() == False:
            if 8 == int(second[-1]):
                cells[first] = '•'
                cells[second] = "⬜"
            else:
                cells[first] = '•'
                cells[second] = '⚪'
            trueorfalse = False
            whiteorblack = 'black'
            first = ''
            second = ''


        elif whiteorblack == 'white' and bexod() == True and Trueboy == True and (first != '') and (second != '') and cells[first] == '⚪':
            if 8 == int(second[-1]):
                cells[first] = '•'
                cells[deletechecers] = '❌'
                cells[second] = "⬜"
                x = 1
                y = second
                z = 1

                if bexod() == False:
                    for i in cells.items():
                        if i[1] == '❌':
                            cells[i[0]] = '•'
                    whiteorblack = 'black'
                    x = 0
                    y = ""
                    z = 0
            else:
                cells[first] = '•'
                cells[deletechecers] = '❌'
                cells[second] = '⚪'
                x = 1
                y = second
                z = 1
                print(bexod())
                if bexod() == False:
                    for i in cells.items():
                        if i[1] == '❌':
                            cells[i[0]] = '•'
                    whiteorblack = 'black'
                    x = 0
                    y = ""
                    z = 0
            deletechecers = ''
            first = ''
            second = ''

        elif whiteorblack == 'black' and bexod1() == True and Trueboy1 == True and (first != '') and (second != ''):
            if 1 == int(second[-1]):
                cells[first] = '•'
                cells[deletechecers] = '❌'
                cells[second] = "⬛"
                x1 = 1
                y1 = second
                z1 = 1
                if bexod1() == False:
                    for i in cells.items():
                        if i[1] == '❌':
                            cells[i[0]] = '•'
                    whiteorblack = 'white'
                    x1 = 0
                    y1 = ""
                    z1 = 0
            else:
                cells[first] = '•'
                cells[deletechecers] = '❌'
                cells[second] = "⚫"
                x1 = 1
                y1 = second
                z1 = 1
                if bexod1() == False:
                    for i in cells.items():
                        if i[1] == '❌':
                            cells[i[0]] = '•'
                    whiteorblack = 'white'
                    x1 = 0
                    y1 = ""
                    z1 = 0
            deletechecers = ''
            first = ''
            second = ''


        elif whiteorblack == 'black' and (first != '') and (second != '') and trueorfalse1 == True and bexod1() == False:
            if 1 == int(second[-1]):
                cells[first] = '•'
                cells[second] = "⬛"
            else:
                cells[first] = '•'
                cells[second] = "⚫"
            whiteorblack = 'white'
            trueorfalse1 = False
            first = ''
            second = ''


        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=whiteorblack, reply_markup=started_board())
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    bot.polling(none_stop=True)
