error = False
try:
    from os import system
    system("title " + "Webhook Deleter,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import requests
    import colorama
except:
    error = True
if error == True:
    while True:
        fix = input("Missing Module, Wanna Try Auto Fix (y/n): ")
        if fix == "y" or fix == "n":
            break
        else:
            print("Enter A Valid Choice")
    if fix == "n":
        exit()
    if fix == "y":
        try:
            import os
            os.system("pip install requests")
            os.system("pip install colorama")
            print("Problem May Be Fixed Now, Restart Prgoram")
            input("")
            exit()
        except:
            print("Error Fixing Error")
            input("")
            exit()
colorama.init(autoreset=True)
while True:
    type = input("""
1. Delete Specific Webhook
2. Delete Webhook(s) In Webhooks.txt
> """)
    if type == "1" or type == "2":
        break
    else:
        print("Enter A Valid Choice")
if type == "2":
    file = open("webhooks.txt", "r")
    webhooks = file.readlines()
    checked = []
    for web in webhooks:
        try:
            if "\n" in web:
                web = web[:-1]
            r = requests.get(web)
            r = str(r)
            if "200" in r:
                print(colorama.Fore.GREEN + "Webhook Valid")
                checked.append(web)
            else:
                print(colorama.Fore.RED + "Webhook Invalid")
        except:
            print(colorama.Fore.RED + "Webhook Invalid")
    print("Checked Webhook(s), Press Enter To Start Deleting Them")
    input("")
    for webi in checked:
        while True:
            print(webi)
            r = requests.delete(webi)
            r = str(r)
            if "204" in r:
                print(colorama.Fore.GREEN + "Webhook Deleted")
                break
            else:
                print(colorama.Fore.RED + "Failed, Retrying")
    print("Done Deleting Webhook(s)")
    input("")
    exit()
if type == "1":
    while True:
        try:
            webhook = input("Enter Webhook: ")
            r1 = requests.get(webhook)
            if "200" in str(r1):
                break
            else:
                print(colorama.Fore.RED + "Webhook Invalid")
        except Exception:
            print(colorama.Fore.RED + "Webhook Invalid")
    while True:
        message = input("Want To Send An Message Before Deleting Webhook (y/n): ")
        if message == "y" or message == "n":
            break
        else:
            print("Enter A Valid Choice")
    if message == "y":
        content = input("Enter Message: ")
        r2 = requests.post(webhook, json={"content": content})
        if "204" in str(r2):
            print(colorama.Fore.GREEN + "Message Sent")
        if "204" not in str(r2):
            print(colorama.Fore.RED + "Error While Sending Message")
    r = requests.delete(webhook)
    if "204" in str(r):
        print(colorama.Fore.GREEN + "Webhook Deleted")
    if "204" not in str(r):
        print(colorama.Fore.RED + "Error While Deleting Webhook")
    print("Done")
    input("")
    exit()


