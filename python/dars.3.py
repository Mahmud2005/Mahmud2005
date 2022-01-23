print("sonnik avadratni hisoblovchi dastur!")
savol = "Istalga son kitriting: "
savol += "(to'xtash uchun 'exit'ni bosing!):"
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2,int(qiymat)*2)
print("yoshni hisoblovchi datur!")
savol = "tu'g'ilgan yilni kiriting: "
savol += "(to'xtash uchun  'stop' ni bosing! ):"
qiymat = ''
while qiymat != 'stop':
    qiymat = input(savol)
    if qiymat != 'stop':
        a = (2021-(int(qiymat)))
        print(f"sizni yoshingiz {a} ga teng!")       


sonlar = list(range(1,32))
for son in sonlar:
    if son == 9:
        break 
print(f"{son}ni kvadrati {son**2} ga teng")