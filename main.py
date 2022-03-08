import random
from pyrogram import Client, filters

api_id = 7859901
api_hash = '0fb18f748d79a1d68e44e599fdf390cd'
app = Client('test', api_id, api_hash)


@app.on_message(filters.command("magic", prefixes=".") & filters.me)
def mag(_, msg):
    text = input("Введите поздравление")
    buf = ""
    for i in range(9):
        buf += "🤍" * 9 + "\n"
    msg.edit(buf)
    buf = ""
    heart_color = ["❤️", "🧡", "💛", "💚", "💙", "💛", "💜", "💛", "💚", "💙", "💛"]
    for i in heart_color:
        heart = i
        for row in range(9):
            for col in range(9):
                if row == 0:
                    buf += "🤍"
                elif row == 1 and col in [2, 3, 5, 6]:
                    buf += heart
                elif row in [2, 3, 4] and col not in [0, 8]:
                    buf += heart
                elif row == 5 and col in [2, 3, 4, 5, 6]:
                    buf += heart
                elif row == 6 and col in [3, 4, 5]:
                    buf += heart
                elif row == 7 and col == 4:
                    buf += heart
                else:
                    buf += "🤍"
            buf += '\n'
        msg.edit(buf)
        buf = ""

    for i in range(9):
        for row in range(9):
            for col in range(9):
                if row == 0:
                    buf += "🤍"
                elif row == 1 and col in [2, 3, 5, 6]:
                    buf += heart_color[random.randint(0, len(heart_color) - 1)]
                elif row in [2, 3, 4] and col not in [0, 8]:
                    buf += heart_color[random.randint(0, len(heart_color) - 1)]
                elif row == 5 and col in [2, 3, 4, 5, 6]:
                    buf += heart_color[random.randint(0, len(heart_color) - 1)]
                elif row == 6 and col in [3, 4, 5]:
                    buf += heart_color[random.randint(0, len(heart_color) - 1)]
                elif row == 7 and col == 4:
                    buf += heart_color[random.randint(0, len(heart_color) - 1)]
                else:
                    buf += "🤍"
            buf += '\n'
        msg.edit(buf)
        buf = ""

    heart = "❤️"
    for row in range(9):
        for col in range(9):
            if row == 0:
                buf += "🤍"
            elif row == 1 and col in [2, 3, 5, 6]:
                buf += heart
            elif row in [2, 3, 4] and col not in [0, 8]:
                buf += heart
            elif row == 5 and col in [2, 3, 4, 5, 6]:
                buf += heart
            elif row == 6 and col in [3, 4, 5]:
                buf += heart
            elif row == 7 and col == 4:
                buf += heart
            else:
                buf += "🤍"
        buf += '\n'
    msg.edit(buf)
    buf = ""

    row_flag = 0
    col_flag = 0
    for row in range(9):
        for col in range(9):
            if row == row_flag and col == col_flag:
                buf += heart
                col_flag += 1
            elif row == 1 and col in [2, 3, 5, 6]:
                buf += heart
            elif row in [2, 3, 4] and col not in [0, 8]:
                buf += heart
            elif row == 5 and col in [2, 3, 4, 5, 6]:
                buf += heart
            elif row == 6 and col in [3, 4, 5]:
                buf += heart
            elif row == 7 and col == 4:
                buf += heart
            else:
                buf += "🤍"
        buf += '\n'
        col_flag = 0
        row_flag += 1
    msg.edit(buf)
    buf = ""

    for i in range(8, 0, -1):
        for j in range(i):
            buf += "❤️" * i + "\n"
        msg.edit(buf)
        buf = ""

    msg.edit(text)


# app.send_message('me', 'Hello, myself!')

app.run()
