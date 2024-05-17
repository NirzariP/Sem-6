def enc_playfair(plaintext,matrix):
    plaintext += "0"
    plaintext = plaintext.replace('j', 'i')
    encrypted_text = ""
    counter = 0
    while(True):
        if plaintext[counter] == "0":
            break
        if plaintext[counter] == plaintext[counter+1] or plaintext[counter+1] == "0":
            if plaintext[counter] == "x" and plaintext[counter+1] == "x":
                plaintext = plaintext[:counter+1] + "a" + plaintext[counter+1:]
            elif plaintext[counter] == 'x' and plaintext[counter+1] == '0':
                plaintext = plaintext[:counter+1] + "a" + plaintext[counter+1:]
            else:
                plaintext = plaintext[:counter+1] + "x" + plaintext[counter+1:]
        temp_state = ""
        pos = [0,0]
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == plaintext[counter]:
                    pos[0] = [i,j]
                elif matrix[i][j] == plaintext[counter+1]:
                    pos[1] = [i,j]
                else:
                    continue
        if pos[0][0] == pos[1][0]:
            if pos[0][1] == 4:
                pos[0][1] = -1
            if pos[1][1] == 4:
                pos[1][1] = -1
            temp_state +=  matrix[pos[0][0]][pos[0][1]+1]
            temp_state +=  matrix[pos[1][0]][pos[1][1]+1]
        elif pos[0][1] == pos[1][1]:
            if pos[0][0] == 4:
                pos[0][0] = -1
            if pos[1][0] == 4:
                pos[1][0] = -1
            temp_state +=  matrix[pos[0][0]+1][pos[0][1]]
            temp_state +=  matrix[pos[1][0]+1][pos[1][1]]
        else:
            temp_state +=  matrix[pos[0][0]][pos[1][1]]
            temp_state +=  matrix[pos[1][0]][pos[0][1]]
        encrypted_text += temp_state
        counter += 2
    return encrypted_text
 
def dec_playfair(plaintext,matrix,n):
    encrypted_text = ""
    plaintext += "0"
    counter = 0
    while(True):
        if plaintext[counter] == "0":
            break
        temp_state = ""
        pos = [0,0]
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == plaintext[counter]:
                    pos[0] = [i,j]
                elif matrix[i][j] == plaintext[counter+1]:
                    pos[1] = [i,j]
                else:
                    continue
        if pos[0][0] == pos[1][0]:
            if pos[0][1] == 0:
                pos[0][1] = 5
            if pos[1][1] == 0:
                pos[1][1] = 5
            temp_state +=  matrix[pos[0][0]][pos[0][1]-1]
            temp_state +=  matrix[pos[1][0]][pos[1][1]-1]
        elif pos[0][1] == pos[1][1]:
            if pos[0][0] == 0:
                pos[0][0] = 5
            if pos[1][0] == 0:
                pos[1][0] = 5
            temp_state +=  matrix[pos[0][0]-1][pos[0][1]]
            temp_state +=  matrix[pos[1][0]-1][pos[1][1]]
        else:
            temp_state +=  matrix[pos[0][0]][pos[1][1]]
            temp_state +=  matrix[pos[1][0]][pos[0][1]]
        encrypted_text += temp_state
        counter += 2
    index = len(encrypted_text) - 1
    while(len(encrypted_text) > n):
        if encrypted_text[index] == "x":
            if index == len(encrypted_text)-1:
                encrypted_text = encrypted_text[:index]
            elif encrypted_text[index-1] == encrypted_text[index+1]:
                encrypted_text = encrypted_text[:index]+encrypted_text[index+1:]
        elif encrypted_text[index] == "a":
            if index == len(encrypted_text)-1:
                encrypted_text = encrypted_text[:index]
            elif encrypted_text[index-1] == 'x' and encrypted_text[index+1]=='x':
                encrypted_text = encrypted_text[:index]+encrypted_text[index+1:]
        index -= 1
    return encrypted_text
 
def create_matrix(key):
    key = key.replace('j', 'i')
    mat = []
    count,num = 0,0
    done,arr = [], []
    for i in range(97,97+26):
        if chr(i) == 'j':
            continue
        arr.append(chr(i))
 
    for i in range(5):
        row = []
        temp = 0
        while(temp < 5):
            if count < len(key):
                if key[count] not in done:
                    row.append(key[count])
                    done.append(key[count])
                    temp += 1
                count += 1
            else:
                if arr[num] not in done:
                    row.append(arr[num])
                    done.append(arr[num])
                    temp += 1
                num += 1
        mat.append(row)
    return mat
 
plaintext = input("Enter the plaintext text: ").lower()
key = input("Enter the key: ").lower()
matrix = create_matrix(key)
print(matrix)
encrypted_text = enc_playfair(plaintext, matrix)
print("The Ciper text is ", encrypted_text)
dec = dec_playfair(encrypted_text, matrix, len(plaintext))
print("The Decrypted text is ", dec)
if "i" in dec:
    dec = dec.replace("i","j")
    print("The Decrypted text is ", dec)
elif "j" in dec:
    dec = dec.replace("j","i")
    print("The Decrypted text is ", dec)
else:
    pass