def sontop(x=20):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar
def son_top(son=5):
    tasodifiy_son = random.randint(0,son)
    print(f"Men 0 dan {son} gacha son o'yladim!,topa olasizmi?",end="") 
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
    if taxmin<tasodifiy_son:
        print("xato.son kattaroq!",end="")
    elif taxmin>tasodifiy_son:
        print("xato.son kichikroq",end="")
    else:
        break
    print(f"men tabriklayman {taxminlar} tataxmin bilan topdingiz!")
    return taxminlar

def sontop_pc(son=10):
    input(f"1 dan {son} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 0
    yuqori = son
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
play()    