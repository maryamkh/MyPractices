#!usr/bin/python
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
class CesarCipher:
    def encryptString(self, s, encryptFactor):
        encrypted = "";
        newItem = '';
        for item in s:
            if item.isalpha():
                newItemAscii = ord(item) + encryptFactor;
                #if ord(item) + k > ord('Z') or ord(item) + k > ord('z'):
                if item.isupper() and newItemAscii > ord('Z'):
                    encrypted = encrypted + chr(ord('A') + (newItemAscii - ord('Z'))-1);
                    
                elif item.islower() and newItemAscii > ord('z'):
                    encrypted = encrypted + chr(ord('a') + (newItemAscii - ord('z'))-1);#k-1);
                    
                else:
                    encrypted = encrypted + chr(newItemAscii);
            else:
                encrypted = encrypted + item;
        return encrypted;
        

def main():
    string = raw_input("Please enter the string to encrypt: ")
    rotationVal = int(raw_input("please enter the rotation factor:" ))
    
    encrypter = CesarCipher()
   
    Result = encrypter.encryptString(string, rotationVal)
    
    print 'Main string...', string
    print 'Encypted string...', Result
    

if __name__ == '__main__':
    main()


