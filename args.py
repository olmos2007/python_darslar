def shifoxona(bemor, kasalligi, yoshi, manzili, holati):
    bemor_1 = {'bemor':bemor,
        'kasalligi':kasalligi,
        'yoshi':yoshi,
        'manzili':manzili,
        'holati':holati,
        }
    return bemor_1
bemorlar = []
while True:
    bemor = input('Isim va familiyasi: ')
    kasalligi = input('Kasalligi: ')
    yoshi = input('Yoshi: ')
    manzili = input('Manzili: ')
    holati = input('Holati: ')
    bemorlar.append(shifoxona(bemor, kasalligi, yoshi, manzili, holati))
    javob = input('Yana iformatsiya bo`lsa kiriting yes/no: ')
    if javob == 'no':
        break
print(f"Bemorning isn va familiyasi:   {bemor} \n"
      f"Bemorning kasalligi: {kasalligi} \n"
      f"Bemorning yoshi: {yoshi} \n"
      f"Bemorning manzili:  {manzili} \n"
      f"Bemorning holati:  {holati} \n"
      )