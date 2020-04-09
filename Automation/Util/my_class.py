'''from Util.ExcelUtility import ExcelUtility

my_excel = ExcelUtility("C:\\Users\\krishna.teja.taduri\\Desktop\\Automation_WorkPln_V0.1.xlsx","Sheet1")
print(my_excel.column_dictionary)
print(my_excel.get_cell_value("Start Date",3))'''
from Util.BankAccount import BankAccount
from Util.DatabaseUtility import DatabaseUtility
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#DatabaseUtility().execute_statement()

# driver = webdriver.Chrome(executable_path="C:\\Users\\krishna.teja.taduri\\eclipse-workspace\\DB version\\GuidewireGenericFramework\\jars\\chromedriver.exe")
# driver.get(url="")

# def get_player_choice():
#
#     my_list=['X','O']
#     my_dict = {'Player1': input('Player 1 - Please select \'X\' or \'O\'')}
#     if my_dict.get('Player1') is 'X': my_dict['Player2']='O'
#     else: my_dict['Player2']='X'
#     return(my_dict)
#
# get_player_choice()

my_account = BankAccount('John',400)
my_account.deposit(500)
my_account.withdrawal(1000)
my_account.withdrawal(600)

print (my_account)