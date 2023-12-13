thread_amount = 10
try:
    import os, requests, subprocess, threading, json, time, base64
    from colorama import Fore
except:
    import os
    os.system("title R3CIHook - Installing pacages...")
    for paczka in ["requests", "colorama"]:
        os.system(f"pip install {paczka}")
        input("Done please restart")
        exit()

print("Loading...")
os.system("title R3CIHook - Loading...")

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
res = Fore.RESET
purple = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
black = Fore.LIGHTBLACK_EX

class util: 
    def clear():
        if os.name == "nt": os.system("cls")
        else: os.system("clear")

    def chose_mode(size):
        # I dont know what the fuck is going one here but it works ig
        global wbcount
        global multi
        global wb
        util.clear()
        render.banner(size)
        os.system(f"title R3CIHook - Chose ur mode...")
        render.launch_options(size)
        c = input(f'~@~{os.getlogin()} ~ ')
        if c == "1": multi = False
        elif c == "2": multi = True
        else: input(f"{red}[!]{res} Thats not a choice..."); util.chose_mode(size)
        if multi: 
            os.system("title R3CIHook - Multi enabled")
            path = input(f'~@~{os.getlogin()} {res}path to webhooks file{yellow} ~ ')
            try:
                with open(path, 'r') as wbf:
                    wbcount = sum(1 for _ in wbf)
                with open(path, 'r') as wbf:
                    wb = wbf.read().splitlines()
                os.system(f"title R3CIHook - Multi enabled - {wbcount} webhooks")
            except Exception as e:
                input(f"{red}[!]{res} Failed to read the webhooks {e}")
                exit()
        else:
            os.system("title R3CIHook - Signle enabled")
            wb = input(f'~@~{os.getlogin()} {res}Webhook{yellow} ~ ')
    
    def get_wb_names(wb):
        names = []
        for wb in wb:
            try:
                r = requests.get(wb)
                #print(r.json())
                if r.status_code == 200:
                    names.append(r.json().get('name'))
                    print(f"{green}[*]{res} Fethed names: {names}")
                else:
                    names.append("Unknown")
                    print(f"{red}[!]{res} Failed to fetch name! {black}(code {r.status_code})")
            except Exception as e:
                names.append("Unknown")
                print(f"{red}[!]{res} Failed to fetch name! {black}(code {r.status_code})")
                #print(e)
        return names

class modules:
    def send_message(multi, webhooks, msg):
        if msg == "": pass
        msg = {'content': msg}
        if multi:
            for wb in webhooks:
                r = requests.post(wb, json=msg)
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 204:
                    print(f"{green}[*]{res} Message was sent! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Message failed to send {black}(code {r.status_code}) (response {response})")
        else:
            r = requests.post(webhooks, json=msg)
            try: 
                if r.status_code == None: r.status_code = "Null"
            except : pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            if len(r.text) > 80:
                response = "Too long"
            else:
                response = r.text
            try:
                json_data = json.loads(r.text)
                retry = json_data.get("retry_after")
            except:
                retry = "Null"
            if r.status_code == 204:
                print(f"{green}[*]{res} Message was sent! {black}(code {r.status_code}) (response {response})")
            elif r.status_code == 429:
                print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                try: time.sleep(retry)
                except: pass
            else:
                print(f"{red}[!]{res} Message failed to send {black}(code {r.status_code}) (response {response})")

    def spam_messages(multi, webhooks, msg):
        if msg == "": pass
        msg = {'content': msg}
        if multi:
            while True:
                for wb in webhooks:
                    r = requests.post(wb, json=msg)
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : 
                        pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: 
                        pass
                    if len(r.text) > 80:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 204:
                        print(f"{green}[*]{res} Message was sent! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} Message failed to send {black}(code {r.status_code}) (response {response})")
        else:
            while True:
                r = requests.post(webhooks, json=msg)
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 204:
                    print(f"{green}[*]{res} Message was sent! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Message failed to send {black}(code {r.status_code}) (response {response})")

    def send_file(multi, webhooks, path):
        with open(path, 'rb') as f:
            files = {'file': (f.name, f)}
            if multi:
                for wb in webhooks:
                    r = requests.post(wb, files=files)
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: pass
                    if len(r.text) > 80:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 200:
                        print(f"{green}[*]{res} File was sent! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} File failed to send {black}(code {r.status_code}) (response {response})")
            else:
                r = requests.post(webhooks, files=files)
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 200:
                    print(f"{green}[*]{res} File was sent! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} File failed to send {black}(code {r.status_code}) (response {response})")
    
    def spam_files(multi, webhooks, path):
        with open(path, 'rb') as f:
            files = {'file': (f.name, f)}
            if multi:
                while True:
                    for wb in webhooks:
                        r = requests.post(wb, files=files)
                        try: 
                            if r.status_code == None: r.status_code = "Null"
                        except : pass
                        try: 
                            if r.text == None: r.text = "Null"
                        except: pass

                        if len(r.text) > 80:
                            response = "Too long"
                        else:
                            response = r.text
                        try:
                            json_data = json.loads(r.text)
                            retry = json_data.get("retry_after")
                        except:
                            retry = "Null"
                        if r.status_code == 200:
                            print(f"{green}[*]{res} File was sent! {black}(code {r.status_code}) (response {response})")
                        elif r.status_code == 429:
                            print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                            try: time.sleep(retry)
                            except: pass
                        else:
                            print(f"{red}[!]{res} File failed to send {black}(code {r.status_code}) (response {response})")
            else:
                while True:
                    r = requests.post(webhooks, files=files)
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: pass
                    if len(r.text) > 80:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 200:
                        print(f"{green}[*]{res} File was sent! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} File failed to send {black}(code {r.status_code}) (response {response})")


    def edit_message(multi, webhooks, msg, msgID):
        if msgID == "": pass
        if msg == "": pass
        msg = {'content': msg}
        if multi:
            for wb in webhooks:
                r = requests.patch(f'{wb}/messages/{msgID}', headers = {'Content-Type': 'application/json'}, data=json.dumps(msg))
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 200:
                    print(f"{green}[*]{res} Message was edited! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Message failed to edit {black}(code {r.status_code}) (response {response})")
        else:
            r = requests.patch(f'{wb}/messages/{msgID}', headers = {'Content-Type': 'application/json'}, data=json.dumps(msg))
            try: 
                if r.status_code == None: r.status_code = "Null"
            except : pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            if len(r.text) > 80:
                response = "Too long"
            else:
                response = r.text
            try:
                json_data = json.loads(r.text)
                retry = json_data.get("retry_after")
            except:
                retry = "Null"
            if r.status_code == 200:
                print(f"{green}[*]{res} Message edited! {black}(code {r.status_code}) (response {response})")
            elif r.status_code == 429:
                print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                try: time.sleep(retry)
                except: pass
            else:
                print(f"{red}[!]{res} Message failed to edit {black}(code {r.status_code}) (response {response})")
    
    def deleate_message(multi, webhooks, msgID):
        if msgID == "": pass
        if multi:
            for wb in webhooks:
                r = requests.delete(f'{wb}/messages/{messageID}')
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 204:
                    print(f"{green}[*]{res} Message was deleated! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Message failed to deleate {black}(code {r.status_code}) (response {response})")
        else:
            r = requests.delete(f'{wb}/messages/{messageID}')
            try: 
                if r.status_code == None: r.status_code = "Null"
            except : pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            if len(r.text) > 80:
                response = "Too long"
            else:
                response = r.text
            try:
                json_data = json.loads(r.text)
                retry = json_data.get("retry_after")
            except:
                retry = "Null"
            if r.status_code == 204:
                print(f"{green}[*]{res} Message deleated! {black}(code {r.status_code}) (response {response})")
            elif r.status_code == 429:
                print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                try: time.sleep(retry)
                except: pass
            else:
                print(f"{red}[!]{res} Message failed to deleated {black}(code {r.status_code}) (response {response})")
    
    def change_name(multi, webhooks, name):
        if name == "": pass
        name = {'name': name}
        if multi:
            for wb in webhooks:
                r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 200:
                    print(f"{green}[*]{res} Webhooks name changed! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Failed to change webhooks name {black}(code {r.status_code}) (response {response})")
        else:
            r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
            try: 
                if r.status_code == None: r.status_code = "Null"
            except : pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            if len(r.text) > 80:
                response = "Too long"
            else:
                response = r.text
            try:
                json_data = json.loads(r.text)
                retry = json_data.get("retry_after")
            except:
                retry = "Null"
            if r.status_code == 200:
                print(f"{green}[*]{res} Webhooks name changed! {black}(code {r.status_code}) (response {response})")
            elif r.status_code == 429:
                print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                try: time.sleep(retry)
                except: pass
            else:
                print(f"{red}[!]{res} Failed to change webhooks name {black}(code {r.status_code}) (response {response})")
    
    def spam_change_name(multi, webhooks, name):
        if name == "": pass
        if multi:
            while True:
                for wb in webhooks:
                    r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: pass
                    if len(r.text) > 80:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 200:
                        print(f"{green}[*]{res} Webhooks name changed! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} Failed to change webhooks name {black}(code {r.status_code}) (response {response})")
        else:
            while True:
                r = requests.patch(wb, headers = {'Content-Type': 'application/json'}, data=json.dumps(name))
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 80:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 200:
                    print(f"{green}[*]{res} Webhooks avatar changed! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Failed to change webhooks avatar {black}(code {r.status_code}) (response {response})")
    
    def change_avatar(multi, webhooks, path):
        if path == "": pass
        if multi:
            for wb in webhooks:
                with open(path, 'rb') as f:
                    avatar_data = f.read()
                    avatar_base64 = base64.b64encode(avatar_data).decode('utf-8')
                    avatar = {'avatar': f'data:image/png;base64,{avatar_base64}',}
                    r = requests.patch(wb, headers = {'Content-Type': 'multipart/form-data',}, files=avatar)
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: pass
                    if len(r.text) > 9999999999:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 200:
                        print(f"{green}[*]{res} Webhooks avatar changed! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} Failed to change webhooks avatar {black}(code {r.status_code}) (response {response})")
        else:
            with open(path, 'rb') as f:
                avatar_data = f.read()
                avatar_base64 = base64.b64encode(avatar_data).decode('utf-8')
                avatar = {'avatar': f'data:image/png;base64,{avatar_base64}',}
                r = requests.patch(wb, headers = {'Content-Type': 'multipart/form-data',}, files=avatar)
                try: 
                    if r.status_code == None: r.status_code = "Null"
                except : pass
                try: 
                    if r.text == None: r.text = "Null"
                except: pass
                if len(r.text) > 9999999:
                    response = "Too long"
                else:
                    response = r.text
                try:
                    json_data = json.loads(r.text)
                    retry = json_data.get("retry_after")
                except:
                    retry = "Null"
                if r.status_code == 200:
                    print(f"{green}[*]{res} Webhooks avatar changed! {black}(code {r.status_code}) (response {response})")
                elif r.status_code == 429:
                    print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                    try: time.sleep(retry)
                    except: pass
                else:
                    print(f"{red}[!]{res} Failed to change webhooks avatar {black}(code {r.status_code}) (response {response})")

    def spam_change_avatar(multi, webhooks, path):
        if path == "": pass
        if multi:
            while True:
                for wb in webhooks:
                    with open(path, 'rb') as f:
                        avatar_data = f.read()
                        avatar_base64 = base64.b64encode(avatar_data).decode('utf-8')
                        avatar = {'avatar': f'data:image/png;base64,{avatar_base64}',}
                        r = requests.patch(wb, headers = {'Content-Type': 'multipart/form-data',}, files=avatar)
                        try: 
                            if r.status_code == None: r.status_code = "Null"
                        except : pass
                        try: 
                            if r.text == None: r.text = "Null"
                        except: pass
                        if len(r.text) > 80:
                            response = "Too long"
                        else:
                            response = r.text
                        try:
                            json_data = json.loads(r.text)
                            retry = json_data.get("retry_after")
                        except:
                            retry = "Null"
                        if r.status_code == 200:
                            print(f"{green}[*]{res} Webhooks avatar changed! {black}(code {r.status_code}) (response {response})")
                        elif r.status_code == 429:
                            print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                            try: time.sleep(retry)
                            except: pass
                        else:
                            print(f"{red}[!]{res} Failed to change webhooks avatar {black}(code {r.status_code}) (response {response})")
        else:
            while True:
                with open(path, 'rb') as f:
                    avatar_data = f.read()
                    avatar_base64 = base64.b64encode(avatar_data).decode('utf-8')
                    avatar = {'avatar': f'data:image/png;base64,{avatar_base64}',}
                    r = requests.patch(wb, headers = {'Content-Type': 'multipart/form-data',}, files=avatar)
                    try: 
                        if r.status_code == None: r.status_code = "Null"
                    except : pass
                    try: 
                        if r.text == None: r.text = "Null"
                    except: pass
                    if len(r.text) > 80:
                        response = "Too long"
                    else:
                        response = r.text
                    try:
                        json_data = json.loads(r.text)
                        retry = json_data.get("retry_after")
                    except:
                        retry = "Null"
                    if r.status_code == 200:
                        print(f"{green}[*]{res} Webhooks avatar changed! {black}(code {r.status_code}) (response {response})")
                    elif r.status_code == 429:
                        print(f"{yellow}[#]{res} Ratelimited! {black}(code {r.status_code}) waiting {retry}s (response {response})")
                        try: time.sleep(retry)
                        except: pass
                    else:
                        print(f"{red}[!]{res} Failed to change webhooks avatar {black}(code {r.status_code}) (response {response})")

    def get_info_abt_webhook(multi, webhooks):
        if multi:
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
        else:
            r = requests.get(wb)
            try: 
                if r.status_code == None: r.status_code = "Null"
            except: pass
            try: 
                if r.text == None: r.text = "Null"
            except: pass
            try:
                print(f"{green}[*]{res} {black}(code {r.status_code})")
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
            except:
                print(f"{red}[!]{res} Something went wrong... {black}(code {r.status_code})")     

class render:
    subprocess.check_call('mode con: cols=225 lines=35', shell=True)
    util.clear()
    os.system(f"title R3CIHook - Welcome")
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
        print(banner)
    
    def wb_names(wb):
        names = util.get_wb_names(wb)
        if multi:
            puplet = ', '.join(str(name) for name in names)
            os.system(f"title R3CIHook - Multi enabled - {wbcount} webhooks - Logged as {puplet}")
        else:
            puplet = ', '.join(str(name) for name in names)
            os.system(f"title R3CIHook - Single enabled - Logged as {puplet}")
    
    def options(size):
        opts = f"""
{'01 - Send message              '.center(size)}
{'02 - Spam messages             '.center(size)}
{'03 - Send file                 '.center(size)}
{'04 - Spam files                '.center(size)}
{'05 - Edit message              '.center(size)}
{'06 - Deleate message           '.center(size)}
{'07 - Change name               '.center(size)}
{'08 - Spam change name          '.center(size)}
{'09 - Change avatar             '.center(size)}
{'10 - Spam change avatar        '.center(size)}
{'11 - Get all info about webhook'.center(size)}
"""
        for thong in ["-"]:
            opts = opts.replace(thong, f"{res}{thong}{yellow}")
        print(opts)
    
    def launch_options(size):
        launch_opts = f"""
{'01 - Single webhook    '.center(size)}
{'02 - Multi webhook     '.center(size)}
"""
        for thong in ["-"]:
            launch_opts = launch_opts.replace(thong, f"{res}{thong}{yellow}")
        print(launch_opts)


util.chose_mode(size)
util.clear()
print(f"{yellow}[#] Fething names...")
render.wb_names(wb)
util.clear()
while True:
    util.clear()
    render.banner(size)
    render.options(size)

    c = input(f'~@~{os.getlogin()} ~ ')
    if c == "1": 
        message = input(f'{yellow}~@~{os.getlogin()} {res}message{yellow} ~ ')
        modules.send_message(multi, wb, message)
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "2": 
        message = input(f'{yellow}~@~{os.getlogin()} {res}message{yellow} ~ ')
        threads = []
        for _ in range(thread_amount):
            thread = threading.Thread(target=modules.spam_messages, args=(multi, wb, message))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "3": 
        path = input(f'{yellow}~@~{os.getlogin()} {res}file path{yellow} ~ ')
        modules.send_file(multi, wb, path)
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "4": 
        path = input(f'{yellow}~@~{os.getlogin()} {res}file path{yellow} ~ ')
        threads = []
        for _ in range(thread_amount):
            thread = threading.Thread(target=modules.spam_files, args=(multi, wb, path))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "5": 
        if multi:
            input(f"{yellow}[?]{res} Are u sure u want to run this? It wont be effective with multiple webhooks as u can put only 1 message ID enter to continue...")
        messageID = input(f'{yellow}~@~{os.getlogin()} {res}Message ID{yellow} ~ ')
        edited_message = input(f'{yellow}~@~{os.getlogin()} {res}Edited content{yellow} ~ ')
        modules.edit_message(multi, wb, edited_message, messageID)
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "6": 
        if multi:
            input(f"{yellow}[?]{res} Are u sure u want to run this? It wont be effective with multiple webhooks as u can put only 1 message ID enter to continue...")
        messageID = input(f'{yellow}~@~{os.getlogin()} {res}Message ID{yellow} ~ ')
        modules.deleate_message(multi, wb, messageID)
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "7": 
        name = input(f'{yellow}~@~{os.getlogin()} {res}Name{yellow} ~ ')
        modules.change_name(multi, wb, name)
        input(f"{yellow}[#]{res} Waiting...")
    
    elif c == "8": 
        name = input(f'{yellow}~@~{os.getlogin()} {res}Name{yellow} ~ ')
        modules.spam_change_name(multi, wb, name)
        input(f"{yellow}[#]{res} Waiting...")

    if c == "9": 
        path = input(f'{yellow}~@~{os.getlogin()} {res}Path{yellow} ~ ')
        modules.change_avatar(multi, wb, path)
        input(f"{yellow}[#]{res} Waiting...")

    elif c == "10": 
        path = input(f'{yellow}~@~{os.getlogin()} {res}Path{yellow} ~ ')
        modules.spam_change_avatar(multi, wb, path)
        input(f"{yellow}[#]{res} Waiting...")
    
    elif c == "11": 
        modules.get_info_abt_webhook(multi, wb)
        input(f"{yellow}[#]{res} Waiting...")

    else:
        input(f"{red}[!]{res} This is not an option")