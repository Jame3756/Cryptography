
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    message=input("enter you message: ")
    key=int(input("enterkey(1-94)"))
    encryptedtext=""
    for i in range(len(message)):
        temp=(ord(message[i])+key)
        if (temp>126):
            temp=temp-127+32
        encryptedtext+=chr(temp)
    print("encrypted text: "+encryptedtext)
    main()


    


def decryption():
    print("Decryption")
    print("message cna only be in lower or uppercase letters")
    encryptedmessage=input("enter you encrypted message: ")
    decryptedkey=int(input("enterkey(1-94)"))
    decryptedtext=""
    for i in range(len(encryptedmessage)):
        temp=(ord(encryptedmessage[i])-decryptedkey)
        if (temp<32):
            temp=temp+127-32
        decryptedtext+=chr(temp)
    print("decrypted text: "+decryptedtext)
    main()




    
    

        
if __name__ == "__main__":
    main()
