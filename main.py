# coding: utf-8

from misskey import Misskey

import random
import os
import time

misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")

senryu = Misskey(misskey_address)
senryu.token = misskey_token

#使える文字のリスト
hiragana = ['ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん','ー']

#初句.二句.結句をそれぞれ作成
syoku = ''.join(random.choices(hiragana,k=5))
niku = ''.join(random.choices(hiragana,k=7))
kekku = ''.join(random.choices(hiragana,k=5))

#初句の一文字目が"ー"ならそれ以外に
while True:
    if syoku[0] == "ー":
        syoku = ''.join(random.choices(hiragana,k=5))
        print(i)
        i = i+1
    else:
        break

#二句の一文字目が"ー"ならそれ以外に
while True:
    if niku[0] == "ー":
        kekku = ''.join(random.choices(hiragana,k=5))
    else:
        break

#結句の一文字目が"ー"ならそれ以外に
while True:
    if kekku[0] == "ー":
        kekku = ''.join(random.choices(hiragana,k=5))
    else:
        break

#できた川柳
while True:
    try:
        senryu.notes_create(text=syoku+"\n"+niku+"\n"+kekku)
    except:
        time.sleep(300)
    else:
        break
print(syoku+"\n"+niku+"\n"+kekku)
