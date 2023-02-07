import webbrowser

list =["1.Google","2.Youtube"]

for li in list:
    print(li)

x =int(input("Podaj liczbę: "))

if x == 1:
    webbrowser.open("https://www.google.com/")
elif x == 2:
    webbrowser.open("https://www.youtube.com/")