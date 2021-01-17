def hosgeldin():
    print('''
Hesap Makinesine Hoşgeldin!
''')

hosgeldin()

def hesaplama():
    operation = input(""" 
Yapmak istediğin işlemi komut satırına yazınız;
Toplama için +
Çıkarma için -
Çarpma için *
Bölme için /
Kuvveti için **
Bölümünden kalanı için %
Karekökden çıkarmak için V

""")

    if operation == "+":
        sayi1 = float(input("Toplanan ilk sayıyı yazınız: "))
        sayi2 = float(input("Toplanan ikinci sayıyı yazınız: "))
        print('{} + {} = '.format(sayi1,sayi2))
        print(sayi1 + sayi2)

    elif operation == '-':
        sayi1 = float(input("Eksilen sayıyı yazınız: "))
        sayi2 = float(input("Çıkan sayıyı yazınız: "))
        print("{} - {} = ".format(sayi1,sayi2))
        print(sayi1 - sayi2)

    elif operation == '*':
        sayi1 = float(input("Çarpan ilk sayıyı yazınız: "))
        sayi2 = float(input("Çarpan ikinci sayıyı yazınız: "))
        print("{} * {} = ".format(sayi1,sayi2))
        print(sayi1 * sayi2)

    elif operation == '/':
        sayi1 = float(input("Bölünen sayıyı yazınız: "))
        sayi2 = float(input("Bölen sayıyı yazınız: "))
        print("{} / {} = ".format(sayi1,sayi2))
        print(sayi1 * sayi2)

    elif operation == '**':
        sayi1 = float(input("İlk sayıyı yazınız: "))
        sayi2 = float(input("Kuvvetini yazınız: "))
        print("{} ** {} = ".format(sayi1,sayi2))
        print(sayi1 ** sayi2)
        
    elif operation == '%':
        sayi1 = float(input("İlk sayıyı yazınız: "))
        sayi2 = float(input("Bölen sayıyı yazınız: "))
        print("{} % {} = ".format(sayi1,sayi2))
        print(sayi1 % sayi2)
        
    elif operation == 'V':
        import math
        sayi1 = float(input("Karekökden çıkarıcağınız sayıyı yazınız: "))
        print("√¯{}".format(sayi1))
        print(math.sqrt(sayi1))
        
    else:
        print("")
        print("Yanlış bir sembol girdiniz lütfen sembolleri doğru yazınız.")
        hesaplama()
        
    tekrar()

def tekrar():
    tekraret = input(""" 
Tekrar hesaplama yapmak istiyormusun?
Lütfen yapmak istiyor isen E
Yapmamak istiyor isen H yazınız.

""")

    if tekraret.upper() == "E":
        hesaplama()
    elif tekraret.upper() == "H":
        print("Daha sonra görüşürüz...")
    else:
        tekrar()
        
hesaplama()
