from PIL import Image
import math
import random

chars = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '>', '<', '?', ';', ':', "'", '[', ']', '{', '}', '-', '_', '=', '+', '(', ')', '*', '&', '^', '%', '$', '#', '@', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'á', 'é', 'í', 'ó', 'à', 'ã', 'õ', 'ç', 'Á', 'É', 'Í', 'Ó', 'À', 'Ã', 'Õ', 'Ç', 'ê', 'Ê', 'â', 'Â', 'ô', 'Ô', 'ú', 'Ú', '"', "'"]

msg = str(input("Digite a mensagem para codificar: "))
msgLen = len(msg)

msgPixels = []

for char in msg:
    msgPixels.append(chars.index(char))

print(msgPixels)

while len(msgPixels) % 3 != 0:
    msgPixels.append(0)

imgData = []

for pixel in range(0, len(msgPixels), 3):
    imgData.append(tuple([msgPixels[pixel], msgPixels[pixel+1], msgPixels[pixel+2]]))

newImg = Image.new("RGB", (480, 480))
newImg.putdata(imgData)
newImg.save("pos.png")
