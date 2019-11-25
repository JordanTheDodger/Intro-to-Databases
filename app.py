from user import User

my_usr = User('elonmusk@gmail.com', 'Jordan', 'MuskFan', None)
my_usr.save_to_db()
"""Loading data from the database"""
load_usr = User.load_from_db_by_email('litteJ@gmail.com')
print(load_usr)

my_usr.save_to_db()

""" Inserting data into the database"""
# usr_1 = User('jordan@ggmail.com','Jordan','TheDodger', None)
# usr_2 = User('james@gmail.com', 'James', 'TheArtist', None)
# usr_3 = User('joshua@gmail.com', 'Joshua', 'TheReaper', None)
# usr_4 = User('littleJ@gmail.com', 'Jack', 'Sparrow', None)

# print(usr_1)
# print('\n')
# print(usr_2 + '\n')
# print(usr_3 + '\n')
# print(usr_4)
#
# usr_1.save_to_db()  # >>User.save_to_db(usr_1)
# usr_2.save_to_db()
# usr_3.save_to_db()
# usr_4.save_to_db()
