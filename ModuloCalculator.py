fractions = [512,294,656,744]
modulo = 29

for fraction in fractions:
    i = 1
    run = True
    while run:
        if (i*fraction**(-1))%modulo == 1:
            run = False
        else:
            i += 1
    print(i%modulo)