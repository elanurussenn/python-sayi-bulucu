#GUCLU VE KUVVETLI SAYI BULMA
# with open("guclusayilar.txt","r+") as dosya:
#     sinirlar=dosya.read().split(",")
#     alt_sinir=int(sinirlar[0])
#     ust_sinir=int(sinirlar[1])
# def guclu_bul(alt_sinir,ust_sinir):
#     def faktoriyel(sayi):
#         carpim=1
#         for i in range(1,sayi+1):
#             carpim*=i
#         return carpim
#     def guclu_mu(sayi):
#         basamaklar=[]
#         temp=sayi
#         while sayi>0:
#             kalan=sayi%10
#             sayi-=kalan
#             sayi=sayi//10
#             basamaklar.append(kalan)
#         toplam=0
#         for i in basamaklar:
#             toplam+=faktoriyel(i)
#         if toplam==temp:
#             return True
#         else:
#             return False
#     sayac=0
#     while alt_sinir<ust_sinir:
#         if sayac==0:
#             if guclu_mu(alt_sinir):
#                 with open("guclusayilar.txt","w+") as dosya:
#                      dosya.write(str(alt_sinir)+"\n")
#                      sayac+=1
#         else:
#             if guclu_mu(alt_sinir):
#                 with open("guclusayilar.txt","a+") as dosya:
#                      dosya.write(str(alt_sinir)+"\n")
#         alt_sinir+=1
# guclu_bul(alt_sinir,ust_sinir)

with open("kuvvetlisayilar.txt","r+") as dosya:
    sinirlar=dosya.read().split(",")
    alt_sinir=int(sinirlar[0])
    ust_sinir=int(sinirlar[1])
liste=[]
def kuvvetli_bul(alt_sinir,ust_sinir):
    def asal_mi(sayi):
        for i in range(1,sayi):
            if sayi%i==0:
                for f in range(1,i//2+1):
                    if i%f==0:
                        break
                else:
                    liste.append(i)
    def kuvvetli_mi(sayi):
        asal_mi(sayi)
        for i in liste:
            if i**2==sayi:
                return True
            else:
                return False

    sayac = 0
    while alt_sinir < ust_sinir:
        if sayac == 0:
            if kuvvetli_mi(alt_sinir):
                with open("kuvvetlisayilar.txt", "w+") as dosya:
                    dosya.write(str(alt_sinir) + "\n")
                    sayac += 1
        else:
            if kuvvetli_mi(alt_sinir):
                with open("kuvvetlisayilar.txt", "a+") as dosya:
                    dosya.write(str(alt_sinir) + "\n")
        alt_sinir += 1
kuvvetli_bul(alt_sinir, ust_sinir)