import webbrowser
from colorama import Fore, Back, Style
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

print(Fore.CYAN + "ŞU ANKİ İP ADRESİNİZ : " + IP_addres)

soru = input(Fore.LIGHTYELLOW_EX + "Hız Testi Yapılsın mı (eğer istiyorsanız evet yazın istemiyorsanız hayır yazabilirsiniz) : ")
if soru == "evet":
     print(Fore.GREEN + "Yönlendirme yapılıyor")
     webbrowser.open('https://www.speedtest.net/')
 
elif soru == "hayır":
    print(Fore.RED + "İşlem kullanıcı tarafından iptal edildi")
    print(Fore.LIGHTMAGENTA_EX + "instagram @atillanoxy")
    webbrowser.open('https://www.codenirvana.ml' + "only turkey ip login")
