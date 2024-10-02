import hashlib
import sys
import argparse
import time
from colorama import Fore, Style

green = Fore.GREEN

hash_to_crack = sys.argv[1]

def hesk_iPass2Hash(plaintext):
    majorsalt = ''
    for char in plaintext:
        majorsalt += hashlib.sha1(char.encode('utf-8')).hexdigest()
    corehash = hashlib.sha1(majorsalt.encode('utf-8')).hexdigest()
    return corehash

def main():
    print('''

   ▄█    █▄       ▄████████    ▄████████    ▄█   ▄█▄                                  
  ███    ███     ███    ███   ███    ███   ███ ▄███▀                                  
  ███    ███     ███    █▀    ███    █▀    ███▐██▀                                    
 ▄███▄▄▄▄███▄▄  ▄███▄▄▄       ███         ▄█████▀                                     
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀███████████ ▀▀█████▄                                     
  ███    ███     ███    █▄           ███   ███▐██▄                                    
  ███    ███     ███    ███    ▄█    ███   ███ ▀███▄                                  
  ███    █▀      ██████████  ▄████████▀    ███   ▀█▀                                  
                                           ▀                                          
 ▄████████    ▄████████    ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
███    ███   ███    ███   ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
███    █▀    ███    ███   ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███ 
███         ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄  ▀███████████   ███    ███ ███    █▄    ███▐██▄     ███    █▄  ▀███████████ 
███    ███   ███    ███   ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
████████▀    ███    ███   ███    █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ 
             ███    ███                           ▀                        ███    ███ 
                                                           
by th3g3ntl3m4n
''')
    time.sleep(2)
    parser = argparse.ArgumentParser(description="Crack a hash from HESK Help Desk Software")
    parser.add_argument('hash', type=str, help="The hash to crack")
    parser.add_argument('wordlist', type=argparse.FileType('r'), help="The wordlist")
    
    args = parser.parse_args()

    with open(sys.argv[2], 'r') as file:
        for line in file:
            plaintext = line.rstrip('\n')
            print(f"[...] Trying: {plaintext} ...")
            hash_value = hesk_iPass2Hash(plaintext)
            time.sleep(0.005)

            if hash_to_crack == hash_value:
                print(f"{green}{Style.BRIGHT}[+] The password is: {plaintext}{Style.RESET_ALL}")
                sys.exit("[+] Bye")

if __name__ == "__main__":
    main()