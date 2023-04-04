def cypher(text, shift):
    if text.isalpha():
        index = alphabet.find(text)
        x = index + shift
        y = x % len(alphabet)
        return alphabet[y]
    else:
        return text

alphabet = input("Podaj dowolny klucz-alfabet (w jednej linii), \n np: 'abcdefghijklmnopqrstuvwxyz': ")

#np: abcdefghijklmnopqrstuvwxyz
#pl: aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż

message = input ("Podaj wiadomosc: ")
shift = int(input ("Podaj ilosc przestawien: ")) % len(alphabet) #modulo tu sprawia ze jesli np alfabet ma 26 znakow to przesuniecie o 30 bedzie rownowazne przesunieciu o 4
encrypted_msg = ''

for x in message:
    encrypted_msg += cypher(x, shift)

print("Zaszyfrowana wiadomosc: " + encrypted_msg)

shift = -shift % len(alphabet)
decrypted_msg = ''
for x in encrypted_msg:
    decrypted_msg += cypher(x, shift)

print("Odszyfrowana wiadomosc: " + decrypted_msg)
