alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


import logocaesar
print(logocaesar.logo)



def caesar(word,shift,direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if shift>26:
        shift = shift%26
    if direction == "encode":
        encrypted=[]
        for n in word:
            if alphabet.count(n)==0:
                encrypted.append(n)
            else:
                encrypted.append(alphabet[int(alphabet.index(n))+shift])
        s = ''.join(encrypted)  
    elif direction == "decode":
        decrypted=[]
        for n in word:
            if alphabet.count(n)==0:
                encrypted.append(n)
            if shift<alphabet.index(n):
                decrypted.append(alphabet[int(alphabet.index(n))-shift])
        s = ''.join(decrypted)
        
    print(s)  
req="yes"
while req=="yes":
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    req=input("Type 'yes' if you want to go again. Otherwise type 'no'.")