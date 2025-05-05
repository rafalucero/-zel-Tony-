import os, uuid, string, random
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import os,sys,time,pyfiglet,py_compile

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m" 

br = pyfiglet.figlet_format("Tony Stark")
print(R+br)

class viking():
    def __init__(self):
        self.target = input("[]  Mail Yada KullanıcıAdı : ")
        if self.target[0] == "@":
            print("[ - ] Enter User Without '@' ", end="")
            input()
            exit()
        if "@" in self.target:
            self.data = {
                "_csrftoken":
                "".join(
                    random.choices(string.ascii_lowercase +
                                   string.ascii_uppercase + string.digits,
                                   k=32)),
                "user_email":
                self.target,
                "guid":
                uuid.uuid4(),
                "device_id":
                uuid.uuid4()
            }
        else:
            self.data = {
                "_csrftoken":
                "".join(
                    random.choices(string.ascii_lowercase +
                                   string.ascii_uppercase + string.digits,
                                   k=32)),
                "username":
                self.target,
                "guid":
                uuid.uuid4(),
                "device_id":
                uuid.uuid4()
            }
        self.send_password_reset()

    def send_password_reset(self):
        head = {
            "user-agent":
            f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
        }
        req = requests.post(
            "https://i.instagram.com/api/v1/accounts/send_password_reset/",
            headers=head,
            data=self.data)
        
        if "obfuscated_email" in req.text:
            print(f"[ + ] {req.text}")
            input()
            exit()
        else:
            print(f"[ - ] {req.text}")
            input()
            exit()


viking()