from util.Mysql import MySql
from util.SETMOKE_API import SETMOKE_API

db=MySql('localhost','root','rehab105','SMM_db')
result_set=db.read_mention_from_db()
for row in result_set:
    keyword=str(row[0])
    data_fetch=SETMOKE_API(keyword,"/home/rehab/PycharmProjects/SETMOK_API/conf/config.ini")
    mentionlist=data_fetch.get_data()
    db.add_mention_to_db(mentionlist)


