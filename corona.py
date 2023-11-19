import math

def neon_corona(TM, FLAG):
    # Table for G, for Neon, pre-calculated from Corona Model
    if TM > 10 ** 8:
        g = 1.66667
    elif TM > 2 * 10 ** 7:
        g = 1.6 + 0.83 * (10 ** -9) * (TM - 2 * 10 ** 7)
    elif TM > 4.5 * 10 ** 6:
        g = 1.47 + 0.84 * (10 ** -8) * (TM - 4.5 * 10 ** 6)
    elif TM > 2.3 * 10 ** 6:
        g = 1.485
    elif TM > 3.4 * 10 ** 5:
        g = 1.23 + 1.2 * (10 ** -7) * (TM - 3.4 * 10 ** 5)
    elif TM > 2.4 * 10 ** 4:
        g = 1.15 + 2.22 * 10 ** -7 * (TM - 2.4 * 10 ** 4)
    elif TM > 1.7 * 10 ** 4:
        g = 1.66667 - 7.67E-05 * (TM - 10000)
    elif TM > 10 ** 4:
        g = 1.66667
    else:
        g = 1.66667

    # Table for Z for Neon, pre-calculated from Corona Model
    if TM > 7 * 10 ** 6:
        Z = 10
    elif TM > 2.3 * 10 ** 6:
        Z = 8 + 0.4255 * (10 ** -6) * (TM - 2.3 * 10 ** 6)
    elif TM > 4.5 * 10 ** 5:
        Z = 8
    elif TM > 4.5 * 10 ** 4:
        Z = 1.9 + 1.5 * (10 ** -5) * (TM - 4.5 * 10 ** 4)
    elif TM > 15000:
        Z = 6.3E-05 * (TM - 15000)
    else:
        Z = 0

    if FLAG == 10:
        # Code for when FLAG is 10
        pass
    elif FLAG == 11:
        # Code for when FLAG is 11
        pass
    else:
        # Code for when ZN is 10 and none of the FLAG conditions are met
        pass

    return g, Z

def argon_corona(TM, FLAG):
    # Table for G, for Argon, pre-calculated from Corona Model
    if TM > 1.5 * 10 ** 8:
        g = 1.66667
    elif TM > 1.2 * 10 ** 7:
        g = 1.54 + 9 * (10 ** -10) * (TM - 1.2 * 10 ** 7)
    elif TM > 1.9 * 10 ** 6:
        g = 1.31 + 2.6 * (10 ** -8) * (TM - 1.9 * 10 ** 6)
    elif TM > 9.3 * 10 ** 5:
        g = 1.3
    elif TM > 5.7 * 10 ** 5:
        g = 1.34 - 1.6 * (10 ** -7) * (TM - 5.7 * 10 ** 5)
    elif TM > 10 ** 5:
        g = 1.17 + 3.8 * (10 ** -7) * (TM - 10 ** 5)
    elif TM > 1.3 * 10 ** 4:
        g = 1.15 + 2.3 * (10 ** -7) * (TM - 1.3 * 10 ** 4)
    elif TM > 9000:
        g = 1.66667 - 1.29 * (10 ** -4) * (TM - 9000)
    else:
        g = 1.66667

    # Table for Z for Argon, pre-calculated from Corona Model
    if TM > 1.3 * 10 ** 8:
        Z = 18
    elif TM > 1.3 * 10 ** 7:
        Z = 16 + 1.8 * (10 ** -8) * (TM - 1.3 * 10 ** 7)
    elif TM > 3.5 * 10 ** 6:
        Z = 16
    elif TM > 4.7 * 10 ** 5:
        Z = 8 + 2.9 * (10 ** -6) * (TM - 4.7 * 10 ** 5)
    elif TM > 2 * 10 ** 5:
        Z = 8
    elif TM > 1.9 * 10 ** 4:
        Z = 1 + 3.7 * (10 ** -5) * (TM - 1.9 * 10 ** 4)
    elif TM > 1.4 * 10 ** 4:
        Z = 1
    elif TM > 9000:
        Z = 0.0002 * (TM - 9000)
    else:
        Z = 0

    G1 = 2 / (g + 1)
    G2 = (g - 1) / g

    if FLAG == 10:
        # Code for when FLAG is 10
        pass
    elif FLAG == 11:
        # Code for when FLAG is 11
        pass
    else:
        # Code for when ZN is 18 and none of the FLAG conditions are met
        pass

    return g, Z, G1, G2

def xenon_corona(TM, FLAG):
    # Table for G, for Xenon, pre-calculated from Corona Model
    if TM > 9 * 10 ** 10:
        g = 1.66667
    elif TM > 1.16 * 10 ** 9:
        g = 0.0053 * math.log(TM) / math.log(10) + 1.631
    elif TM > 1.01 * 10 ** 8:
        g = 0.063 * math.log(TM) / math.log(10) + 1.342
    elif TM > 2.02 * 10 ** 7:
        g = 0.166 * math.log(TM) / math.log(10) + 0.936
    elif TM > 6.23 * 10 ** 6:
        g = 0.096 * math.log(TM) / math.log(10) + 1.163
    elif TM > 9.4 * 10 ** 5:
        g = 0.1775 * math.log(TM) / math.log(10) + 0.9404
    elif TM > 3.3 * 10 ** 5:
        g = 1.27
    elif TM > 6 * 10 ** 4:
        g = 0.122 * math.log(TM) / math.log(10) + 1.093
    elif TM > 1.2 * 10 ** 4:
        g = 1.17
    elif TM > 8 * 10 ** 3:
        g = -2.624 * math.log(TM) / math.log(10) + 1.229
    else:
        g = 1.66667

    # Table for Z for Xenon, pre-calculated from Corona Model
    if TM > 9 * 10 ** 10:
        Z = 54
    elif TM > 2.85 * 10 ** 8:
        Z = 1.06 * math.log(TM) / math.log(10) + 46.4
    elif TM > 8.8 * 10 ** 7:
        Z = 10.72 * math.log(TM) / math.log(10) + 3.99
    elif TM > 2.11 * 10 ** 7:
        Z = 5.266 * math.log(TM) / math.log(10) + 25.3
    elif TM > 5.68 * 10 ** 6:
        Z = 25.23 * math.log(TM) / math.log(10) - 40
    elif TM > 3.35 * 10 ** 6:
        Z = 9.53 * math.log(TM) / math.log(10) + 2.326
    elif TM > 2.37 * 10 ** 5:
        Z = 15.39 * math.log(TM) / math.log(10) - 12.1
    elif TM > 10000:
        Z = 5.8 * math.log(TM) / math.log(10) + 0.466
    else:
        Z = 0
    G1 = 2 / (g + 1)
    G2 = (g - 1) / g

    if FLAG == 10:
        # Code for when FLAG is 10
        pass
    elif FLAG == 11:
        # Code for when FLAG is 11
        pass
    else:
        # Code for when ZN is 54 and none of the FLAG conditions are met
        pass

    return g, Z, G1, G2

def nitrogen_corona(TeV, zFLAG, gFLAG, FLAG):
    # For N2 compute specific heat ratio g and effective charge z using polynomials fitted from Corona model
    if zFLAG == 1:
        Z = 7
    else:
        Z = -0.5681 * ((math.log(TeV) / math.log(10)) ** 6) + 4.2149 * ((math.log(TeV) / math.log(10)) ** 5) - 10.771 * ((math.log(TeV) / math.log(10)) ** 4) + 10.307 * ((math.log(TeV) / math.log(10)) ** 3) - 1.9463 * ((math.log(TeV) / math.log(10)) ** 2) + 2.2765 * (math.log(TeV) / math.log(10)) + 0.2025
        if Z > 7:
            Z = 7
            zFLAG = 1

    if gFLAG == 1:
        g = 1.6667
    else:
        g = 0.0869 * ((math.log(TeV) / math.log(10)) ** 6) - 0.7726 * ((math.log(TeV) / math.log(10)) ** 5) + 2.6889 * ((math.log(TeV) / math.log(10)) ** 4) - 4.6815 * ((math.log(TeV) / math.log(10)) ** 3) + 4.3215 * ((math.log(TeV) / math.log(10)) ** 2) - 1.8471 * ((math.log(TeV) / math.log(10))) + 1.4399
        if g > 1.6667:
            g = 1.6667
            gFLAG = 1

    G1 = 2 / (g + 1)
    G2 = (g - 1) / g

    if FLAG == 10:
        # Code for when FLAG is 10
        pass
    elif FLAG == 11:
        # Code for when FLAG is 11
        pass
    else:
        # Code for when ZN is 7 and none of the FLAG conditions are met
        pass

    return g, Z, G1, G2, zFLAG, gFLAG

def krypton_corona(TeV, zFLAG, gFLAG, FLAG):
    # For Krypton compute specific heat ratio g and effective charge z using polynomials fitted from Corona model
    if zFLAG == 1:
        Z = 36
    else:
        Z = -0.0347 * ((math.log(TeV) / math.log(10)) ** 6) + 0.6605 * ((math.log(TeV) / math.log(10)) ** 5) - 4.5854 * ((math.log(TeV) / math.log(10)) ** 4) + 13.565 * ((math.log(TeV) / math.log(10)) ** 3) - 14.619 * ((math.log(TeV) / math.log(10)) ** 2) + 9.9659 * (math.log(TeV) / math.log(10)) - 0.2588
        if Z > 36:
            Z = 36
            zFLAG = 1

    if gFLAG == 1:
        g = 1.6667
    else:
        g = 0.0014 * ((math.log(TeV) / math.log(10)) ** 6) - 0.0249 * ((math.log(TeV) / math.log(10)) ** 5) + 0.1751 * ((math.log(TeV) / math.log(10)) ** 4) - 0.6051 * ((math.log(TeV) / math.log(10)) ** 3) + 1.0754 * ((math.log(TeV) / math.log(10)) ** 2) - 0.7905 * ((math.log(TeV) / math.log(10))) + 1.3541
        if g > 1.6667:
            g = 1.6667
            gFLAG = 1

    G1 = 2 / (g + 1)
    G2 = (g - 1) / g

    if FLAG == 10:
        # Code for when FLAG is 10
        pass
    elif FLAG == 11:
        # Code for when FLAG is 11
        pass
    else:
        # Code for when ZN is 36 and none of the FLAG conditions are met
        pass

    return g, Z, G1, G2, zFLAG, gFLAG


