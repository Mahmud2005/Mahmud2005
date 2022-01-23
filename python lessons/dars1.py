bugatti = []
for n in range(15):
    new_var = {
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
bugatti.append(new_var)
for bugati in bugatti[:3]:
    bugati["rang"]="qora"
for bugati in bugatti[3:10]:
    bugati["rang"] = "qizil"
for bugati in bugatti[10:]:
    bugati["rang"] = "oq"
    bugati["korobka"] = "avto"
for bugati in bugatti:
    if bugati["korobka"]=="avto":
        bugati["narh"]=2000
    else:
        bugati["narh"]=3000
sonlar = list(range(1,11))
for son in sonlar:
    if son == 10: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
    


p = ("aa","ds")
x,y = p
print(y,x)
data = (16,"Mahmud", "Tursunboyev",178)
yoshi,ismi,familyasi,boyi = data
print(yoshi)
records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]
def do_foo(x, y):
 print('foo', x, y)
def do_bar(s):
 print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
def suma(x,y,*sonlar):
    return x+y+sum(sonlar)
print(suma(2,345,3))    
def multiply(*sonlar):
    kopaytma = 3
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(2,2,2))
def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(1,10))      
son = 1
while son<=(5):
    print(son,end=" ")
    son = son+1
ismlar = []
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print(ismlar)
kitoblar = []
print("yaxshi ko'rgan kitoblarni tuzamiz!")
n=1
while True:
    savol = f"{n}-yaxshi ko'rgan kitobingiz?"
    kitob = input(savol)
    kitoblar.append(kitob)
    javob = input("yana qo'shasizmi?(ha/yo'q)")
    if javob == "ha":
        n+=1
        continue
    else:
        break
print(kitoblar)    
n = 14
i = 1

while i <= 10:
  print(n, 'x', i, '=', n*i)
  i = i+1
  