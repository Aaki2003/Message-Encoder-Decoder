alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  enc = ""
  for i in range(0,len(text)):
    if text[i] not in alphabet:
      enc = enc + text[i]
    else:
      for j in range(0,len(alphabet)):
        if text[i] == alphabet[j]:
          if j+shift>=26:
            enc+=alphabet[(j+shift)-26]
          else:
            enc+=alphabet[j+shift]
        
  print(f"Your encoded message is - {enc}")

def decode(text,shift):
  dec = ""
  
  for i in range(0,len(text)):
    if text[i] not in alphabet:
      dec = dec + text[i]
    else:
      for j in range(0,len(alphabet)):
        if text[i] == alphabet[j]:
          if (j-shift)<0:
            dec +=alphabet[26+(j-shift)]
          else:
            dec+=alphabet[j-shift]

  print(f"Your decoded message is - {dec}")

if direction == "encode": 
  encrypt(text,shift)
else:
  decode(text,shift) 
    
