version = 2.1
import os
os.system("title R3CIHook - Loading...")
print("Loading...")
try:
    import requests, subprocess, threading, json, time, base64, threading
    from colorama import Fore
    from datetime import datetime
except:
    os.system("title R3CIHook - Updating pip")
    os.system("python.exe -m pip install --upgrade pip")
    os.system("title R3CIHook - Installing pacages...")
    for paczka in ["requests", "colorama"]:
        os.system(f"title R3CIHook - Installing {paczka}")
        os.system(f"pip install {paczka}")
    input("Done please restart")
    exit()

subprocess.check_call('mode con: cols=225 lines=35', shell=True)

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
res = Fore.RESET
purple = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
black = Fore.LIGHTBLACK_EX

class files:
    path = os.path.join(os.getenv('APPDATA'), "R3CIHook")
    def make_main_folder():
        os.makedirs(files.path, exist_ok=True)
    
    def make_wb_file():
        path = f"{files.path}/wb.txt"
        if os.path.exists(path):
            pass
        else:
            with open(path, 'w') as f:
                f.write("")
    
    def make_cfg():
        path = f"{files.path}/cfg.json"
        if os.path.exists(path):
            pass
        else:
            with open(path, 'w') as f:
                data = {
                    "Threads": 5,
                    "Debug": False
                }
                json.dump(data, f, indent=4)

    def run():
        files.make_main_folder()
        files.make_wb_file()
        files.make_cfg()
files.run()

class cfg:
    path = os.path.join(os.getenv('APPDATA'), "R3CIHook")
    path = f"{path}/cfg.json"
    global thread_numb
    global debug
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            thread_numb = data.get("Threads")
            thread_numb = int(thread_numb)
            debug = data.get("Debug")
    except:
        input(f"{red}[!]{res} Failed to get config values please restart")
        exit()

class log:
    def timee():
        crnt_time = datetime.now().time()
        time = crnt_time.strftime("%H:%M:%S")
        return time
    def succes(message, status, response):
        timee = log.timee()
        try: 
            if status == None: status = "Null"
        except : pass
        try: 
            if response == None: response = "Null"
        except: pass
        if debug:
            response = response
        else:
            if len(response) > 80:
                response = "Too long"
            else:
                response = response

        print(f"{black}{timee} {green}[{lgreen}*{green}]{res} {message} {black}(code: {status}) (response: {response})")

    def ratelimit(message, status, response):
        timee = log.timee()
        try:
            json_data = json.loads(response)
            retry = json_data.get("retry_after")
        except:
            retry = "Null"
        try: 
            if status == None: status = "Null"
        except : pass
        try: 
            if response == None: response = "Null"
        except: pass
        if debug:
            response = response
        else:
            if len(response) > 80:
                response = "Too long"
            else:
                response = response

        print(f"{black}{timee} {yellow}[#]{res} {message} {black}(waiting {retry}s) (code: {status}) (response: {response})")
        try:
            time.sleep(retry)
        except: 
            pass
    
    def fail(message, status, response):
        timee = log.timee()
        try: 
            if status == None: status = "Null"
        except : pass
        try: 
            if response == None: response = "Null"
        except: pass
        if debug:
            response = response
        else:
            if len(response) > 80:
                response = "Too long"
            else:
                response = response

        print(f"{black}{timee} {red}[{lred}!{red}]{res} {message} {black}(code: {status}) (response: {response})")

class util:
    def cls():
        if os.name == "nt": 
            os.system("cls")
        else:
            os.system("clear")
        
    def tit(title):
        os.system(f"title R3CIHook - {title}")
    


    class wb:
        def get_wb():
            global wb
            with open(f"{files.path}/wb.txt", 'r') as wbf:
                wb = wbf.read().splitlines()

        def get_wb_amount():
            global wbcount
            with open(f"{files.path}/wb.txt", 'r') as wbf:
                wbcount = sum(1 for _ in wbf)

        def get_wb_names(wb):
            names = []
            for wb in wb:
                try:
                    r = requests.get(wb)
                    if r.status_code == 200:
                        names.append(r.json().get("name"))
                    else:
                        names.append("Unknown")
                except Exception as e:
                    names.append("Unknown")
            return names

    class auto_update:
        # tbh the downloading process is from chat gpt as i dont really know much abt that all this code is a big fucking mess but it works
        try:
            def get_info():
                os.system("title R3CIHook - Searching for updates")
                print("Searching for updates...")
                r = requests.get(f"https://api.github.com/repos/R3CI/R3CIHook/releases/latest")
                if r.status_code == 200:
                    data = r.json()
                    changelog = data.get('body', '')
                    version = float(data['tag_name'])
                    return version, changelog
                else:
                    input(f"{red}[!]{res} Failed to get info about the version no internet? response: {r.status_code}")
                    return None, None
                
            def check_for_update(local, github, changelog):
                if local == github:
                    pass
                else:
                    if local > github: 
                        os.system("title R3CIHook - New update is released!")
                        if os.name == "nt": 
                            os.system("cls")
                        else:
                            os.system("clear")
                        size = os.get_terminal_size().columns
                        banner = f"""{yellow}
{'      ::::    ::: :::::::::: :::       :::         :::    ::: :::::::::  :::::::::      ::: ::::::::::: :::::::::: ::: '.center(size)}
{'     :+:+:   :+: :+:        :+:       :+:         :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:     :+:        :+:  '.center(size)}
{'    :+:+:+  +:+ +:+        +:+       +:+         +:+    +:+ +:+    +:+ +:+    +:+  +:+   +:+  +:+     +:+        +:+   '.center(size)}
{'   +#+ +:+ +#+ +#++:++#   +#+  +:+  +#+         +#+    +:+ +#++:++#+  +#+    +:+ +#++:++#++: +#+     +#++:++#   +#+    '.center(size)}
{'  +#+  +#+#+# +#+        +#+ +#+#+ +#+         +#+    +#+ +#+        +#+    +#+ +#+     +#+ +#+     +#+        +#+     '.center(size)}
{' #+#   #+#+# #+#         #+#+# #+#+#          #+#    #+# #+#        #+#    #+# #+#     #+# #+#     #+#                 '.center(size)}
{'###    #### ##########   ###   ###            ########  ###        #########  ###     ### ###     ########## ###       '.center(size)}                                                                                                     
"""
                        print(banner)
                        print(f"{yellow}[#]{res} Current version: {yellow}{local}\n{yellow}[#]{res} Newest version: {yellow}{github}\n")
                        print(f"{yellow}[#]{res} New features:\n{res}{changelog}")
                        input(f"{red}[!]{res} If u dont want to update (not reccomended) edit the first line of the code to a higher number {yellow}|{res} Press enter to begin the update")
                        input(f"{red}[!]{res} Do not close or touch any of its files or shut down ur pc as it may breake the process {yellow}|{res} Press enter to begin the update (this time for real)")
                        os.system("title R3CIHook - Starded updating...")

                    def download(local, gh):
                        r = requests.get("https://api.github.com/repos/R3CI/R3CIHook/releases/latest")
                        if r.status_code == 200:
                            os.system("title R3CIHook - Getting version info...")
                            if local <= gh:
                                data = r.json()
                                file = data.get("assets", [])
                                for file in file:
                                    file_url = file.get("browser_download_url")
                                    file_name = file.get("name")
                                    return file_url, file_name
                            else:
                                pass
                        else:
                            print(f"{red}[!]{res} Failed to download the update")

                def download_url(url, save_path):
                    print(f"{green}[*]{res} Downloading started")
                    os.system("title R3CIHook - Downloading update...")
                    response = requests.get(url, stream=True)
                    with open(save_path, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    print(f"{green}[*]{res} Downloaded")
                    os.system("title R3CIHook - Update downloaded")

                file_url, file_name = download(local, github)
                if file_url:
                    download_url(file_url, os.path.join(".", f"{file_name}_UPDATED"))

            def finalize():
                os.system("title R3CIHook - Finalizing")
                scrpt = r"""
                @echo off
                timeout /t 5 /nobreak >nul
                echo Deleting R3CIHook.exe, R3CIHook.py, and data...
                del R3CIHook.exe
                del R3CIHook.py
                del "%APPDATA%\R3CIHook\cfg.json"

                echo Renaming _UPDATED file to R3CIHook.exe...
                for %%I in (*_UPDATED) do (
                    ren "%%I" R3CIHook.exe
                )
                del %0
                """
                
                with open("update.bat", "w") as f:
                    os.system("title R3CIHook - Writing to batch...")
                    f.write(scrpt)
                os.system("title R3CIHook - Running batch")
                subprocess.run("update.bat", shell=True)
                os.system("title R3CIHook - Exiting...")
                exit()

            gh_version, changelog = get_info()
            local_version = version
            if gh_version and changelog:
                check_for_update(local_version, gh_version, changelog)
            finalize()
        except: 
            pass



class modules:
    def send_message(webhooks, msg):
        msg = {'content': msg}
        for wb in webhooks:
            r = requests.post(wb, json=msg)
            status = r.status_code
            response = r.text
            
            if r.status_code == 204:
                log.succes("Sent", status, response)
            elif r.status_code == 429:
                log.ratelimit("Ratelimited", status, response)
            else:
                log.fail("Failed", status, response)

    def spam_messages(webhooks, msg):
        msg = {'content': msg}
        while True:
            for wb in webhooks:
                r = requests.post(wb, json=msg)
                status = r.status_code
                response = r.text
                
                if r.status_code == 204:
                    log.succes("Sent", status, response)
                elif r.status_code == 429:
                    log.ratelimit("Ratelimited", status, response)
                else:
                    log.fail("Failed", status, response)

    def send_file(webhooks, path):
        with open(path, 'rb') as f:
            files = {'file': (f.name, f)}
            for wb in webhooks:
                r = requests.post(wb, files=files)
                status = r.status_code
                response = r.text

                if r.status_code == 200:
                    log.succes("Sent", status, response)
                elif r.status_code == 429:
                    log.ratelimit("Ratelimited", status, response)
                else:
                    log.fail("Failed", status, response)
    
    def spam_files(webhooks, path):
        with open(path, 'rb') as f:
            files = {'file': (f.name, f)}
            while True:
                for wb in webhooks:
                    r = requests.post(wb, files=files)
                    status = r.status_code
                    response = r.text

                    if r.status_code == 200:
                        log.succes("Sent", status, response)
                    elif r.status_code == 429:
                        log.ratelimit("Ratelimited", status, response)
                    else:
                        log.fail("Failed", status, response)


    def edit_message(webhooks, msg, msgID):
        msg = {'content': msg}
        for wb in webhooks:
            r = requests.patch(f'{wb}/messages/{msgID}', headers = {'Content-Type': 'application/json'}, data=json.dumps(msg))
            status = r.status_code
            response = r.text

            if r.status_code == 200:
                log.succes("Edited", status, response)
            elif r.status_code == 429:
                log.ratelimit("Ratelimited", status, response)
            else:
                log.fail("Failed", status, response)
    
    def deleate_message(webhooks, msgID):
        for wb in webhooks:
            r = requests.delete(f'{wb}/messages/{msgID}')
            status = r.status_code
            response = r.text

            if r.status_code == 204:
                log.succes("Deleated", status, response)
            elif r.status_code == 429:
                log.ratelimit("Ratelimited", status, response)
            else:
                log.fail("Failed", status, response)
    
    def change_name(webhooks, name):
        name = {'name': name}
        for wb in webhooks:
            r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
            status = r.status_code
            response = r.text

            if r.status_code == 200:
                log.succes("Changed", status, response)
            elif r.status_code == 429:
                log.ratelimit("Ratelimited", status, response)
            else:
                log.fail("Failed", status, response)
    
    def spam_change_name(webhooks, name):
        name = {'name': name}
        while True:
            for wb in webhooks:
                r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
                status = r.status_code
                response = r.text

                if r.status_code == 200:
                    log.succes("Changed", status, response)
                elif r.status_code == 429:
                    log.ratelimit("Ratelimited", status, response)
                else:
                    log.fail("Failed", status, response)
    
    def change_avatar(webhooks, path):
        with open(path, "rb") as f:
            image = base64.b64encode(f.read()).decode("utf-8")
            headers = {"Content-Type": "application/json",}
            data = {"avatar": f"data:image/png;base64,{image}",}
            for wb in webhooks:
                r = requests.patch(wb, headers=headers, json=data)
                status = r.status_code
                response = r.text
                
                if r.status_code == 200:
                    log.succes("Changed", status, response)
                elif r.status_code == 429:
                    log.ratelimit("Ratelimited", status, response)
                else:
                    log.fail("Failed", status, response)

    def spam_change_avatar(webhooks, path):
        with open(path, "rb") as f:
            image = base64.b64encode(f.read()).decode("utf-8")
            headers = {"Content-Type": "application/json",}
            data = {"avatar": f"data:image/png;base64,{image}",}
            while True:
                for wb in webhooks:
                    r = requests.patch(wb, headers=headers, json=data)
                    status = r.status_code
                    response = r.text
                    
                    if r.status_code == 200:
                        log.succes("Changed", status, response)
                    elif r.status_code == 429:
                        log.ratelimit("Ratelimited", status, response)
                    else:
                        log.fail("Failed", status, response)

    def get_info_abt_webhook(webhooks):
        i = 0
        for wb in webhooks:
            i += 1
            print("\n")
            r = requests.get(wb)
            try: 
                if r.status_code == None: r.status_code = "Null"
            except: pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            try:
                print(f"{res} {i}/{wbcount}")    
                print(f"{red}[!]{res} {black}(code {r.status_code})")
                print(f"{yellow}[#]{res} WEBHOOK INFO")
                print(f"{yellow}[#]{res} Channel id {black}{r.json().get('channel_id')}")
                print(f"{yellow}[#]{res} Guild id {black}{r.json().get('guild_id')}") 
                print(f"{yellow}[#]{res} Bot id {black}{r.json().get('id')}")
                print(f"{yellow}[#]{res} Bot id {black}{r.json().get('name')}")
                print(f"{yellow}[#]{res} Token {black}{r.json().get('token')}")
                print(f"{yellow}[#]{res} Url {black}{r.json().get('url')}")
                print(f"\n{yellow}[#]{res} USER INFO")
                print(f"{yellow}[#]{res} Username {black}{r.json().get('user', {}).get('username')}")
                print(f"{yellow}[#]{res} User ID {black}{r.json().get('user', {}).get('id')}") 
                print(f"{yellow}[#]{res} Global name {black}{r.json().get('user', {}).get('global_name')}") 
                print(f"{yellow}[#]{res} Token {black}{r.json().get('token')}")
                print(f"{yellow}[#]{res} Url {black}{r.json().get('url')}")
                input(f"{green}[*] Webhook {i} done!")
            except:
                print(f"{red}[!]{res} Something went wrong... {black}(code {r.status_code})")  

    def deleate_wb(webhooks):
        for wb in webhooks:
            r = requests.delete(wb)
            status = r.status_code
            response = r.text
            
            if r.status_code == 204:
                log.succes("Deleated", status, response)
            elif r.status_code == 429:
                log.ratelimit("Ratelimited", status, response)
            else:
                log.fail("Failed", status, response) 


class run: 
    def message_sender():
        util.wb.get_wb()
        util.tit("Message sender")
        message = input(f'{yellow}~@~{os.getlogin()}{res} Message ~ ')
        modules.send_message(wb, message)

    def message_spammer():
        util.wb.get_wb()
        util.tit("Message spammer")
        message = input(f'{yellow}~@~{os.getlogin()}{res} Message ~ ')
        threads = []
        for _ in range(thread_numb):
            thread = threading.Thread(target=modules.spam_messages, args=(wb, message))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    
    def file_sender():
        util.wb.get_wb()
        util.tit("File sender")
        path = input(f'{yellow}~@~{os.getlogin()}{res} Path to file ~ ')
        modules.send_file(wb, path)

    def file_spammer():
        util.wb.get_wb()
        util.tit("File spammer")
        path = input(f'{yellow}~@~{os.getlogin()}{res} Path to file ~ ')
        threads = []
        for _ in range(thread_numb):
            thread = threading.Thread(target=modules.spam_files, args=(wb, path))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    
    def message_editor():
        util.wb.get_wb()
        util.tit("Message editor")
        messageID = input(f'{yellow}~@~{os.getlogin()}{res} Message ID ~ ')
        message = input(f'{yellow}~@~{os.getlogin()}{res} Message ~ ')
        modules.edit_message(wb, message, messageID)

    def message_deleater():
        util.wb.get_wb()
        util.tit("Message deleated")
        messageID = input(f'{yellow}~@~{os.getlogin()}{res} Message ID ~ ')
        modules.deleate_message(wb, messageID)

    def name_changer():
        util.wb.get_wb()
        util.tit("Name changer")
        name = input(f'{yellow}~@~{os.getlogin()}{res} Name ~ ')
        modules.change_name(wb, name)

    def spam_name_changer():
        util.wb.get_wb()
        util.tit("Spam name changer")
        name = input(f'{yellow}~@~{os.getlogin()}{res} Name ~ ')
        threads = []
        for _ in range(thread_numb):
            thread = threading.Thread(target=modules.spam_change_name, args=(wb, name))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def avatar_changer():
        util.wb.get_wb()
        util.tit("Avatar changer")
        path = input(f'{yellow}~@~{os.getlogin()}{res} Path to avatar ~ ')
        modules.change_avatar(wb, path)

    def spam_avatar_changer():
        util.wb.get_wb()
        util.tit("Spam avatar changer")
        path = input(f'{yellow}~@~{os.getlogin()}{res} Path to avatar ~ ')
        threads = []
        for _ in range(thread_numb):
            thread = threading.Thread(target=modules.spam_change_avatar, args=(wb, path))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def wb_info_fetcher():
        util.wb.get_wb()
        util.tit("Info fetcher")
        modules.get_info_abt_webhook(wb)

    def webhook_deleater():
        input(f"{red}[!]{res} This will DELEATE all webhooks from wb.txt Are u sure u want to continue?")
        util.wb.get_wb()
        util.tit("Webhook deleater")
        modules.deleate_wb(wb)

class render:
    subprocess.check_call('mode con: cols=225 lines=35', shell=True)
    global size
    size = os.get_terminal_size().columns
    def banner(size):
        banner = f"""{yellow}
{'      :::::::::   ::::::::   :::::::: ::::::::::: :::    :::  ::::::::   ::::::::  :::    ::: '.center(size)}
{'     :+:    :+: :+:    :+: :+:    :+:    :+:     :+:    :+: :+:    :+: :+:    :+: :+:   :+:   '.center(size)}
{'    +:+    +:+        +:+ +:+           +:+     +:+    +:+ +:+    +:+ +:+    +:+ +:+  +:+     '.center(size)}
{'   +#++:++#:      +#++:  +#+           +#+     +#++:++#++ +#+    +:+ +#+    +:+ +#++:++       '.center(size)}
{'  +#+    +#+        +#+ +#+           +#+     +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+       '.center(size)}
{' #+#    #+# #+#    #+# #+#    #+#    #+#     #+#    #+# #+#    #+# #+#    #+# #+#   #+#       '.center(size)}
{'###    ###  ########   ######## ########### ###    ###  ########   ########  ###    ###       '.center(size)}
"""
        return banner
    def options(size):
        opts = f"""
{'# - Settings    $ - Manage webhooks'.center(size)}
{'01 - Send message      '.center(size)}
{'02 - Spam messages     '.center(size)}
{'03 - Send file         '.center(size)}
{'04 - Spam files        '.center(size)}
{'05 - Edit message      '.center(size)}
{'06 - Deleate message   '.center(size)}
{'07 - Change name       '.center(size)}
{'08 - Spam change name  '.center(size)}
{'09 - Change avatar     '.center(size)}
{'10 - Spam change avatar'.center(size)}
{'11 - Info fetcher      '.center(size)}
{'12 - DELEATE WEBHOOK   '.center(size)}
"""
        for thong in ["-"]:
            opts = opts.replace(thong, f"{res}{thong}{yellow}")
        return opts

    os.system("title R3CIHook - Welcome")

while True:
    util.cls()
    print(render.banner(size))
    print(render.options(size))
    util.tit("Chose ur option")
    c = input(f'~@~{os.getlogin()} ~ ')
    if c == "#":
        util.cls()
        print(render.banner(size))
        path = os.path.join(os.getenv('APPDATA'), "R3CIHook")#
        path = f"{path}/cfg.json"
        with open(path, 'r') as f:
            data = json.load(f)
            print(f"{yellow}[#] {res} Current threads: {thread_numb}")
            print(f"{yellow}[#] {res} Debug state: {debug}")
            print(f'{yellow}1 - Edit thread number 2 - Edit debug state 3 - exit'.center(size))
            c = input(f'~@~{os.getlogin()} ~ ')
            if c == "1":
                new_value = input(f'~@~{os.getlogin()} New thread amount ~ ')
                data["Threads"] = new_value
                with open(path, 'w') as f:
                    json.dump(data, f, indent=4)
                    print(f"{green}[*]{res} Set to {new_value}")

            elif c == "2":
                new_value = input(f'~@~{os.getlogin()} New debug state false/true ~ ')
                if new_value != "false" or "true":
                    input(f"{red}[!]{res} Not a valid state")
                    pass
                data["Debug"] = new_value
                with open(path, 'w') as f:
                    json.dump(data, f, indent=4)
                    print(f"{green}[*]{res} Set to {new_value}")
            elif c == "3":
                pass
            else:
                print(f"{red}[!]{res} That not an option my guy")

    elif c == "$": 
        util.cls()
        print(render.banner(size))
        path = os.path.join(os.getenv('APPDATA'), "R3CIHook")
        path = f"{path}/wb.txt"

        with open(path, "r+") as f:
            data = f.read().splitlines()
            print(f"{yellow}[#] Webhooks:")
            for i, webhook in enumerate(data, start=1):
                print(webhook)
            print("\n")
            print(f'{yellow}1 - Edit webhooks 2 - Exit'.center(size))
            c = input(f'~@~{os.getlogin()} ~ ')
            
            if c == "1":
                print(f'{yellow}1 - Copy from file 2 - Input 3 - Clear 4 - Open webhooks file 5 - Exit'.center(size))
                c = input(f'~@~{os.getlogin()} ~ ')

                if c == "1":
                    file_path = input(f'~@~{os.getlogin()} path ~ ')
                    with open(file_path, "r") as file:
                        wbhks = file.read().splitlines()
                        wbhks = '\n'.join(map(str, wbhks))
                        f.write(f"{wbhks}")
                        print(f"{green}[*]{res} Webhooks copied")
                elif c == "2":
                    wbhk = input(f'~@~{os.getlogin()} webhook ~ ')
                    f.write("\n" + wbhk)
                    print(f"{green}[*]{res} Webhook added")
                elif c == "3":
                    with open(path, "w") as f:
                        f.write("")
                        print(f"{green}[*]{res} Webhooks cleared")
                elif c == "4":
                    os.startfile(path) 
                    print(f"{green}[*]{res} File started")   
                elif c == "5":
                    pass
                else:
                    print(f"{red}[!]{res} That's not an option.")
            elif c == "2":
                pass
            else:
                print(f"{red}[!]{res} That's not an option.")
        
    elif c == "1": 
        util.cls()
        print(render.banner(size))
        run.message_sender()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "2": 
        util.cls()
        print(render.banner(size))
        run.message_spammer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "3": 
        util.cls()
        print(render.banner(size))
        run.file_sender()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "4": 
        util.cls()
        print(render.banner(size))
        run.file_spammer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "5": 
        util.cls()
        print(render.banner(size))
        run.message_editor()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "6":
        util.cls()
        print(render.banner(size))
        run.message_deleater()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "7": 
        util.cls()
        print(render.banner(size))
        run.name_changer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "8": 
        util.cls()
        print(render.banner(size))
        run.spam_name_changer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "9": 
        util.cls()
        print(render.banner(size))
        run.avatar_changer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "10": 
        util.cls()
        print(render.banner(size))
        run.spam_avatar_changer()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "11": 
        util.cls()
        print(render.banner(size))
        run.wb_info_fetcher()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "12": 
        util.cls()
        print(render.banner(size))
        run.webhook_deleater()
        input(f"{yellow}[#]{res} Waiting...")

    else:
        input(f"{red}[!]{res} This is not an option")
    
