import string, random

def coding(userinput, key):
    if len(userinput)>=1:
        userinput = userinput[1:]+userinput[0]
        userinput = userinput.split()
        latters = string.ascii_lowercase
        list = []
        for index, i in enumerate(userinput):
            result = "".join(random.sample(latters, int(key)))
            code = result + userinput[index] + result
            list.append(code)
        result = " ".join(list)
        new_result = result[::-1]
        print("Your Code is : ",new_result,"\n")
    else:
        print("Please. Enter Valid Message ❌!")

def dcoding(userinput, key):
    key = int(key)
    userinput= userinput[::-1]
    words = userinput.split(" ")
    if len(words)>=1:
        dcoded_list = []
        for index, word in enumerate(words):
            dcode =  word[key:-key]
            dcoded_list.append(dcode)
        str = " ".join(dcoded_list)
        str1 = str[-1]+str[0:len(str)-1]
        print("Decoded Message : ",str1,"\n")

    else:
        print("Please. Enter Valid Message ❌!")

def main():
    while True:
        user = input("🤗 Welcome, Enter Coding, Dcoding & Quit : ")
        if user.lower().strip() == "coding":
            userinput = input(">> Enter Your Message Here : ")
            key = input("🗝️  Enter Your Passkey 3, 4 or 6 : ").strip()
            if key not in ('3', '4', '6'):
                print("Please Enter Valid Key 🗝️!")
            coding(userinput, key)
        elif user.lower().strip() == "dcoding":
            userinput = input(">> Enter Your Message Here : ")
            key = input("🗝️  Enter Your Passkey 3, 4 or 6 : ")
            dcoding(userinput, key)
        elif user.lower().strip() == "quit":
            print("Thankyou \U0001F607")
            break
        else:
            print('❌ INVALID INPUT ❌!. Please Enter Valid Input')
        
main()