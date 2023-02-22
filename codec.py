
# Encrypt 加密


def encrypt(text):
    for i in text:
        print(chr(ord(i) + 11), end='')

# Decrypt 解密


def decrypt(text):
    for i in text:
        print(chr(ord(i)-11), end='')


# 主程式
text = input("Enter the text: ")
while True:
    choose = input("Encrypt or Decrypt ? (E/D)")
    if choose == "E":
        if text:
            encrypt(text)
            break
        else:
            text = input("Enter the text: ")
    elif choose == "D":
        if text:
            decrypt(text)
            break
        else:
            text = input("Enter the text: ")
    else:
        print("選擇錯誤請確認是否為大寫")
