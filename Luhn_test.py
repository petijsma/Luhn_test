num = 49927398716

def luhn(num):
    '''Luhn test - verification of the existence of credit card number (validation of credit card).
    Returns True if the number is valid, returns False if the number is not valid. '''

    num = str(num)
    obracene_num = num[::-1] #obrácení čísla

    obracene_num = str(obracene_num)

    soucet_lichy = 0
    list_sudy = []
    list_sudy_krat_dva = []
    dvouciferna_suda = []
    soucet_sudy = 0

    # získání součtu lichým a listu sudých
    for i, cislo in enumerate(obracene_num):
        if (i + 1) % 2 != 0:
            soucet_lichy+=int(cislo)
        else:
            list_sudy.append(int(cislo))

    #získání násobku sudých čísel
    for i, cislo in enumerate(list_sudy):
        list_sudy_krat_dva.append(cislo*2)

#získání dvouciferných čísel
    for i, cislo in enumerate(list_sudy_krat_dva):
        if len(str(cislo)) == 1:
            soucet_sudy+= cislo
        else:
            dvouciferna_suda.append(str(cislo))
    # součet dvoucifernych sudych a sectení s souctem sudych celkem        
    for i in dvouciferna_suda:
        for l in i:
            soucet_sudy+= int(l)

    final_soucet =soucet_lichy + soucet_sudy

    if final_soucet % 10 == 0:
        return True
    else:
        return False
        
print(luhn(num))