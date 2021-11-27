import webbrowser

url = input("Coloca ai o endereço do Video: " )

url =url[:12]+'ss'+url[12:]
webbrowser.open(url)
