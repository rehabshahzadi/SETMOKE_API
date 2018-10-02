from SETMOK_API.SETMOKE_API import SETMOKE_API
if __name__== "__main__":

    api=SETMOKE_API("PepsiCo", "/home/rehab/PycharmProjects/conf/config.ini")
    list=api.get_data()
    for msg in list:
        print(msg.text)