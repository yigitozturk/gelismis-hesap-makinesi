def hosgeldin():
    print('''
Hesap Makinesine Hoşgeldin!
''')

hosgeldin()

def hesaplama():
    operation = input(""" 
Yapmak istediğin işlemi komut satırına yaz;
Toplama için +
Çıkarma için -
Çarpma için *
Bölme için /
Kuvveti için **

""")

    sayi1 = float(input("İlk sayıyı yazınız: "))
    sayi2 = float(input("İkinci sayıyı yazınız: "))

    if operation == "+":
        print('{} + {} = '.format(sayi1,sayi2))
        print(sayi1 + sayi2)

    elif operation == '-':
        print("{} - {} = ".format(sayi1,sayi2))
        print(sayi1 - sayi2)

    elif operation == '*':
        print("{} * {} = ".format(sayi1,sayi2))
        print(sayi1 * sayi2)

    elif operation == '/':
        print("{} / {} = ".format(sayi1,sayi2))
        print(sayi1 * sayi2)

    elif operation == '**':
        print("{} ** {} = ".format(sayi1,sayi2))
        print(sayi1 ** sayi2)
        
    else:
        print("")
        print("Yanlış bir sembol girdiniz lütfen sembolleri doğru yazın.")
        
    tekrar()

def tekrar():
    tekraret = input(""" 
Tekrar hesaplama yapmak istiyormusun?
Lütfen yapmak istiyor isen E
Yapmamak istiyor isen H yaz.

""")

    if tekraret.upper() == "E":
        hesaplama()
    elif tekraret.upper() == "H":
        print("Daha sonra görüşürüz...")
    else:
        tekrar()
        
hesaplama()
