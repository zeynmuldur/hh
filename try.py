try:
    a=int(input("bir sayı giriniz:"))
    b=int(input("bir sayı giriniz:"))
    print(a/b)
except ZeroDivisionError:
    print("sayi sifira bolunmez")
    
