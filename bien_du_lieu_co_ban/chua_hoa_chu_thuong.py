s = input()

chuHoa = len([x for x in s if x.isupper()])
chuThuong = len(s) - chuHoa

print( s.upper() if chuHoa > chuThuong else s.lower())

