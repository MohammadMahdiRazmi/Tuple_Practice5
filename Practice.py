while True:
    user_tuple = (10, 20, 30, 40, 50)  # تاپل موردنظر خود را وارد کنید

    print("Tuple mojod: ", user_tuple) 

    index = int(input("lotfan yek index vared konid: "))
    len_tuple = len(user_tuple)
    if 0 <= index < len(user_tuple):
        selected_item = user_tuple[index]
        print(f"item entekhab shode {selected_item}")
        print(f"index item entekhab shode {index}")
    else:
        print(f"index mojod nist! {len_tuple} <--- tedad index ha  ")
    print("-------------------------------------------------------------")



