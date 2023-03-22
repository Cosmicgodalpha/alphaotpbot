import sqlite3
from dbase import *

def main():
#     adminid = input("2026762108")
#     check = check_admin(adminid)
#     if check == True:
#         print("Admin already exists")
#     else:
#         try:
#             create_admin(adminid)
#             create_user_lifetime(adminid)
#         except:
#             print('something went wrong')
#         else:
#             print('Admin created...')
#            create_admin(2026762108)
    james = fetch_UserData_table()
    print(james)
if __name__ == '__main__':
    main()
