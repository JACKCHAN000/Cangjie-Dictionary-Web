import sqlite3

conn = sqlite3.connect('dict.db')
c = conn.cursor()

radical = {
    "a": "日",
    "b": "月",
    "c": "金",
    "d": "木",
    "e": "水",
    "f": "火",
    "g": "土",
    "h": "竹",
    "i": "戈",
    "j": "十",
    "k": "大",
    "l": "中",
    "m": "一",
    "n": "弓",
    "o": "人",
    "p": "心",
    "q": "手",
    "r": "口",
    "s": "尸",
    "t": "廿",
    "u": "山",
    "v": "女",
    "w": "田",
    "x": "難",
    "y": "卜",
    "z": "Z",
}


def single_word(word):
    temp = []
    for output in c.execute(
            'SELECT * FROM DICT WHERE WORD=="{}"'.format(word)):
        temp.append(output[1])
        break
    if len(temp) == 0:
        return ""
    else:
        return temp[0]


def cangjie(words, Quick=False, English=False):
    output = []
    for word in words:
        code = single_word(word)
        if code == "":
            code = word
        else:
            if Quick == True:
                num = len(code)
                if num >= 2:
                    code = code[0] + code[-1]
                else:
                    code = code
            if English == False:
                out = ""
                for i in range(len(code)):
                    out += radical[code[i]]
                code = out
            else:
                code = code.upper()
        print(word, code)
        output.append(code)
    return output
