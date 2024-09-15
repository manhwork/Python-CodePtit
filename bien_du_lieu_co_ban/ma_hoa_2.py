P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

if __name__ == "__main__":
    while True:
        nhap = (input())
        if nhap == "0":
            break
        arr = nhap.split(' ')
        n = int(arr[0])
        s = arr[1]
        result = ""

        for i in range(len(s)):
            index = P.index(s[i])
            result += P[(index + n) % 28]

        print(result[::-1])
