import json
import pymysql

from value_object.user import User


def _our_hash(password):
    d = {
        "pass": "0316253cadc886c3651c89cd8ad7177e6a0b00149df7550f9336342245259ccb"
    }
    return d[password]


class OxwallDB:
    def __init__(self, *args, **kwargs):
        # Connect to the database
        self.__connection = pymysql.connect(*args, **kwargs,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        self.__connection.autocommit(True)

    def close(self):
        self.__connection.close()

    def create_user(self, user):
        with self.__connection.cursor() as cursor:
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`,`emailVerify`, `joinIp`) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.username, user.email, _our_hash(user.password), 0, "2130706433"))
            # connection is not autocommit by default. So you must commit to save your changes
        # self.connection.commit()
        with self.__connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user_id}", "{user.real_name}", "realname")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `intValue`, `questionName`)
                      VALUES("{user_id}", 1, "sex")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `dateValue`, `questionName`)
                      VALUES("{user_id}", "1982-02-10 00:00:00", "birthdate")"""
            cursor.execute(sql)

    def get_users(self):
        with self.__connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, `username`, `password` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchall()
        return [User(**d) for d in result]

    def delete_user(self, user):
        with self.__connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""DELETE FROM `ow_base_question_data`
                      WHERE `ow_base_question_data`.`userId` = {user_id};"""
            cursor.execute(sql)
        with self.__connection.cursor() as cursor:
            sql = f'''DELETE FROM `ow_base_user`
                      WHERE `ow_base_user`.`username` = "{user.username}"'''
            cursor.execute(sql)

    def get_last_text_post(self):
        """ Get post with maximum id that is last added """
        with self.__connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action`
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action` WHERE `entityType`="user-status")
                     AND `entityType`="user-status"
                     """
            cursor.execute(sql)
            response = cursor.fetchone()
            data = json.loads(response["data"])["status"]
        return data


if __name__ == "__main__":
    db = OxwallDB(host='localhost',
                  user='root',
                  password='mysql',
                  db='oxwa767', )
    try:
        user = User(username="dsf", password="secret", email="as@adsd.com")
        # print(db.create_user(user))
        print(db.get_users())
    finally:
        db.close()
