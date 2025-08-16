import string
import secrets


class Password:
    def __init__(self, length: int = 20, uppercase: bool = True, symbol: bool = True) -> None:
        self.length = length
        self.useUppercase = uppercase
        self.useSymbol = symbol

        self.basechar: str = string.ascii_lowercase + string.digits

        if uppercase:
            self.basechar += string.ascii_uppercase
        if symbol:
            self.basechar += string.punctuation

    def generate(self) -> str:
        password: list[str] = []
        for _ in range(self.length):
            password.append(secrets.choice(self.basechar))
        return ''.join(password)

    def check(self, password: str) -> bool:
        if len(password) <= 16:
            return False
        # use logical and, not bitwise &
        if any(ch in password for ch in string.punctuation) and any(ch in password for ch in string.ascii_uppercase):
            return True
        return False


def main() -> None:
    password = Password(length=20)
    generated_pass: list[str] = []

    print("\nGenerated Password:")
    for _ in range(5):
        pwd = password.generate()
        is_strong = password.check(pwd)
        print(f"{pwd} ({is_strong})")
        generated_pass.append(pwd)

    # for Checking Password Strength
    # if a password contains a backslash, escape it as \\ or use a raw string r'...'
    checkPass: list[str] = ['j4usnTxNZouDeit5znPV', 'UT)Tl&Z#$>xQiX_X(5E]']
    if checkPass:
        print("\nPassword Strength:")
        for p in checkPass:
            is_strong = password.check(p)
            print(f"{p} ({is_strong})")


if __name__ == "__main__":
    main()

