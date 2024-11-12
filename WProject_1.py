import random
import pyautogui 
import hashlib
import string




# function to guess your password
# You have to enter a password 
# and this function try to guess it by brute force.


def PassCrack():

# importation o fall the characters
 chars = string.ascii_letters + string.digits + string.punctuation 

 # make chars in a list
 allchar = list(chars) 

# GU interface to enter the password to guess
 pwd = pyautogui.password("Enter a password: ") 

 sample_pwd = ""

 # loop to find the password by brute force
 while (sample_pwd != pwd ):
     sample_pwd = random.choices(allchar , k=len(pwd))

     print("******** "+str(sample_pwd)+ " ********")

     if (sample_pwd == list(pwd) ):
       return( print ("The Password is: " +"".join(sample_pwd)))
 
        



# function to check if your password exist or not 
# check with defferent types of hashes eg: md5, sha1, sha 256, etc

def HashFind():
    pass_found = False

    # Get the hash type, hash, and filename from the user
    hash_type = input("Enter the hash type you want (e.g., 'md5', 'sha256'): ").strip().lower()
    i_hash = input("Enter the hashed password: ").strip()
    p_doc = input("Enter password filename including path: ").strip()
    
    # To Show the available "hash algorithms" in hashlib library
    #Type this : print(hashlib.algorithms_available)

    # Check if the hash type is available in hashlib
    if not hasattr(hashlib, hash_type):
        print(f"Error: Hash type '{hash_type}' is not supported.")
        return

    # Open the password file
    try:
        with open(p_doc, 'r', encoding='utf-8') as p_file:
            #cheking the existence of the password
            for word in p_file:
                word = word.strip()  # Strip whitespace and newline characters
                enc_word = word.encode('utf-8')

                # Get the hash function dynamically
                hash_func = getattr(hashlib, hash_type)
                hash_word = hash_func(enc_word)
                digest = hash_word.hexdigest()

                # Check if the computed hash matches the input hash
                if digest == i_hash:
                    print("Password found:", word)
                    pass_found = True
                    break
    except FileNotFoundError:
        print(f"Error: File '{p_doc}' not found.")
        return

    if not pass_found:
        print("Password not found.")







    
def main ():
   print("\nHello there! What we have to do today ?\n")
   print("\n 1. Crack a Password\n")
   print("\n 2. Find a Hash\n")
   print("\n 3. Exit \n")
   rep = int(input ("Type a Number Here: "))
   if (rep == 1):
        PassCrack()
   elif(rep == 2 ):
       HashFind()
   elif(rep == 3):
       print ("SEE YOU NEXT TIME!")
       return
   else:
        print ("Service NOT found Type again. ")
        
if __name__ == "__main__":
    main()
