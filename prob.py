from random import randint
def simulation():
    un = 15
    un_count = 0
    r_count = 0
    leg_count = 0
    rare = 30
    leg = 75
    x = int(input("number of visitors "))
    for i in range(x):
        z = randint(0,10000)
        if z in range(0, 7350):
            un_count += 1
        elif z in range(7360,9565 ):
            r_count += 1
        else:
            leg_count += 1
    xp_count = (un_count*un)+(r_count*rare)+(leg_count*leg)
    print(F"In {x} visitors you can expect {xp_count} garden xp")
    print(F"The average is {xp_count/x}")
    print(F"Uncommon: {un_count}")
    print(F"Rare: {r_count}")
    print(F"Legendary: {leg_count}")
    return xp_count / x
def estimated_time():
    y = simulation()
    w = int(input("How much garden xp do you need? "))
    print(F"It should take {w/y:.2f} visitors to get the needed xp")
    h = (w/y)/15
    h = int(h)
    m = (w/y)%60
    print(F"If you are farming it should take you {h} hours and {m:.0f} minutes")
    htwo = h*3
    mtwo = m*3
    if mtwo > 60:
        htwo += int(mtwo/60)
        print(mtwo)
        mtwo /= 3
    print(F"If you aren't farming it should take you {htwo} hours and {mtwo:.0f} minutes")
estimated_time() 