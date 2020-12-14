from PIL import Image
import math

chars = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '>', '<', '?', ';', ':', "'", '[', ']', '{', '}', '-', '_', '=', '+', '(', ')', '*', '&', '^', '%', '$', '#', '@', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'á', 'é', 'í', 'ó', 'à', 'ã', 'õ', 'ç', 'Á', 'É', 'Í', 'Ó', 'À', 'Ã', 'Õ', 'Ç', 'ê', 'Ê', 'â', 'Â', 'ô', 'Ô', 'ú', 'Ú', '"', "'", '°', 'è', 'È', '^', 'ˆ', '„', '—', '˜', '‚', '‘', '¬', '¨', '²', '¯', '¹', '¦', '¸', '®', '€', '¡', '¿','¢', 'º', '§', '¥', 'Š', '/', '™', '‹', 'œ', 'ž', 'Ÿ', '`', '‰', 'ª', '“', '”', '–', 'ü', '’',  '´', '´', '•','\xad','\n']          

img = Image.open(str(input("Nome do arquivo: ")) + ".png")
img.convert("RGB")
pix = img.load()

pixelsStorage = []

for y in range(0, img.size[1] - 0):
    for x in range(0, img.size[0] - 0):
        pixelsStorage.append(pix[x, y])

msgLen = len(pixelsStorage) * 3
msgPixLen = math.ceil(msgLen/3)
msgChars = ()

for pixel in range(0, msgPixLen):
    if pixelsStorage[pixel:pixel+5] == [(0, 0, 0)]*5:
        break
    else:
        msgChars += pixelsStorage[pixel]

msgChars = list(msgChars)
msgChars = msgChars[:(len(msgChars) - (msgPixLen * 3 - msgLen))]

msg = ""

for char in msgChars:
    if char > len(chars)-1:
        char = len(chars)-1
    msg += chars[char]

if len(pixelsStorage) != img.size[0] * img.size[1]:
    print("Caracteres podem ter sido perdidos")

print("Mensagem oculta: ")
print(msg)