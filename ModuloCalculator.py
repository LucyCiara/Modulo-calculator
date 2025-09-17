fraction = (3/11)
modulo = 26

i = 1
run = True
while run:
    if (i*fraction**(-1))%modulo == 1:
        run = False
    else:
        i += 1
print(i%modulo)