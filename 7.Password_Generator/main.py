import string
import secrets
from tabnanny import check

class Password:
    def __init__(self,length:int = 20,uppercase:bool = True,symbol:bool = True) -> None:
        self.length = length
        self.useUppercase = uppercase
        self.useSymbol = symbol
        
        self.basechar: str = string.ascii_lowercase + string.digits

        if (uppercase):
            self.basechar += string.ascii_uppercase
        if(symbol):
            self.basechar += string.punctuation

    def genrate(self)-> str:
        password: list[str] =  []
        for i in range(self.length):
            password.append(secrets.choice(self.basechar))
        return ''.join(password)
    
    def check(self,password:str)-> bool:
        if(len(password) <= 16):
            return False
        elif any(c in password for c in string.punctuation):
            return True
        else:
            return False


def main()->None:
    password:Password = Password(length=20)
    genratedPass:list[str] = []

    print(f"\nGenrated Password: ")
    for i in range(5):
        passw:str = password.genrate()
        isStrong = password.check(passw)
        print(f"{passw} ({isStrong})")
        genratedPass.append(passw)

    
    # for Checking Password Strength
    checkPass:list[str] = ['j4usnTxNZouDeit5znPV','UT)Tl&Z#$>xQiX_X(5E]']
    if checkPass:
        print("\nPassword Strength: ")
        for i in range(len(checkPass)):
            isStrong = password.check(checkPass[i])
            print(f"{checkPass[i]} ({isStrong})")



if __name__ == "__main__": 
    main()

