import json
import pymysql

from value_object.user import User


def _our_hash(password):
    d = {
        "pass": "bf6116af8e4b3e83a7646640590b9d5f5c95b06bf7eebf6c424487ff39293833",
        "test": "62fc22c0da68a727562013a405e45ad29fe67725db24870d8dff48a39b37f5ae",
        "secret": "94d1297b55907d7158b27cd91f0d0b0d212abc0ccd4a3e861b1f4e1f404c67e0"
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
                  db='oxwa166', )
    try:
        user = User(username="dsf", password="secret", email="as@adsd.com")
        # print(db.create_user(user))
        print(db.get_users())
    finally:
        db.close()
