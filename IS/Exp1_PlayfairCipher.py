def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    return text.replace(" ", "")

def generateDigraphs(text):
    digraphs = []
    for i in range(0, len(text), 2):
        if i+1 < len(text):
            digraphs.append(text[i:i+2])
        else:
            digraphs.append(text[i] + 'x')  # Add a bogus letter if the last digraph has only one character
    return digraphs

def addBogusLetter(text):
    if len(text) % 2 != 0:
        text += 'z'  # Adding a bogus letter 'z' at the end
    return text

def removeBogusLetter(text):
    if text[-1] == 'z':
        text = text[:-1]  # Remove the last character if it is 'z'
    return text

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j

def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]

    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]

    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c-1]

    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c-1]

    return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r-1][e1c]

    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r-1][e2c]

    return char1, char2

def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2

def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for i in range(0, len(cipherList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, cipherList[i][0])
        ele2_x, ele2_y = search(Matrix, cipherList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        plain = c1 + c2
        PlainText.append(plain)
    return PlainText

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text_Plain = 'instruments'
print("Plain Text:", text_Plain)

text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = generateDigraphs(addBogusLetter(text_Plain))
text_Plain = addBogusLetter(text_Plain)  # Adding a bogus letter if needed


if len(PlainTextList[-1]) != 2:
	PlainTextList[-1] = PlainTextList[-1]+'z'

key = "monarchy"
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)

CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
	CipherText += i
print("CipherText:", CipherText)


def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1c == 0:
		char1 = matr[e1r][4]
	else:
		char1 = matr[e1r][e1c-1]

	char2 = ''
	if e2c == 0:
		char2 = matr[e2r][4]
	else:
		char2 = matr[e2r][e2c-1]

	return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	if e1r == 0:
		char1 = matr[4][e1c]
	else:
		char1 = matr[e1r-1][e1c]

	char2 = ''
	if e2r == 0:
		char2 = matr[4][e2c]
	else:
		char2 = matr[e2r-1][e2c]

	return char1, char2

def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
	char1 = ''
	char1 = matr[e1r][e2c]

	char2 = ''
	char2 = matr[e2r][e1c]

	return char1, char2

def decryptByPlayfairCipher(Matrix, cipherList):
	PlainText = []
	for i in range(0, len(cipherList)):
		c1 = 0
		c2 = 0
		ele1_x, ele1_y = search(Matrix, cipherList[i][0])
		ele2_x, ele2_y = search(Matrix, cipherList[i][1])

		if ele1_x == ele2_x:
			c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		elif ele1_y == ele2_y:
			c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
		else:
			c1, c2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

		plain = c1 + c2
		PlainText.append(plain)
	return PlainText

def removeBogusLetter(text):
	if text[-1] == 'z':
		text = text[:-1]  # Remove the last character if it is 'z'
	return text

PlainTextList = decryptByPlayfairCipher(Matrix, CipherList)

PlainText = ""
for i in PlainTextList:
	PlainText += i

PlainText = removeBogusLetter(PlainText)  # Removing the bogus letter if present
print("Decrypted Plain Text:", PlainText)