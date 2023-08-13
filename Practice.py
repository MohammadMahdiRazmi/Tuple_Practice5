import time
yesorno = input("print yes or no:")
if yesorno == "yes":    
    while True:
   
        user_tuple = (10, 20, 30, 40, 50 , 60, 70, 80, 90)

        print("Tuple mojod: ", user_tuple) 

        index = int(input("lotfan yek index vared konid: "))
        len_tuple = len(user_tuple)
        if 0 <= index < len(user_tuple):
            selected_item = user_tuple[index]
            print(f"item entekhab shode {selected_item}")
            print(f"index item entekhab shode {index}")
        edame = input("aya edame midahid?")
        if edame == "no":
            print("ended...")
            time.sleep(2)
            exit()
        else:
             print(f"index mojod nist! {len_tuple} <--- tedad index ha  ")
        print("-------------------------------------------------------------")
elif yesorno=="no":
    print("program ended")
    time.sleep(3)
    exit()
else:
    print("error")