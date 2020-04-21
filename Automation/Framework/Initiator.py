from Automation.Util import ExcelUtility
from Automation.Framework.TestRunner import TestRunner
import concurrent.futures


class Initiator:

    def __init__(self):
        self.exec_config_dict = {}
        self.test_list = []
        self.test_names = []
        self.current_test_set = []

    def get_run_info(self):
        self.exec_config_dict = ExcelUtility.ExcelUtility(
            path="C:/Users/krishna.teja.taduri/PycharmProjects/Tests/Runner"
                 ".xlsx", sheet_name="Configuration").get_config_info()
        self.test_list = ExcelUtility.ExcelUtility(
            path="C:/Users/krishna.teja.taduri/PycharmProjects/Tests/Runner.xlsx", sheet_name="Runner").get_test_list()
        TestRunner.g_test_set = self.exec_config_dict.get('TestSetName')
        TestRunner.g_environment = self.exec_config_dict.get('Environment')
        TestRunner.g_remote = self.exec_config_dict.get('Remote')
        print(self.exec_config_dict)
        print(self.test_list)

        '''print(ExcelUtility.ExcelUtility(path="C:/Users/krishna.teja.taduri/PycharmProjects/Tests/E2E_Activity_01_PC_AC_01.xlsx",
                                  sheet_name="E2E_Activity_01_PC_AC_01").get_test_steps())'''

    def set_first_execution_order(self):
        # Initializing the test_list with the test case names which are included in the previous test set
        self.set_test_names(self.test_list)

        # Creating the first set of test cases that can be run in parallel (whose parent test is 'NA' or not run as
        # part of the current batch.
        self.current_test_set = []
        num = 0
        while num < len(self.test_list):
            test = self.test_list[num]
            prior_test = test.get('PriorTest')
            if prior_test == 'NA' or prior_test not in self.test_names:
                self.current_test_set.append(test)
                self.test_list.remove(test)
                continue
            num += 1
        print(self.current_test_set)

    def set_test_names(self, test_list):
        self.test_names = []
        for test_detail in test_list:
            self.test_names.append(test_detail.get('TestcaseName'))

    def set_subsequent_execution_order(self):
        # Re-initializing the test_list with the test case names which are included in the previous test set
        self.set_test_names(self.current_test_set)

        # Creating the subsequent set of test cases that can be run in parallel (whose parent test is part of earlier
        # executed test set.
        self.current_test_set = []
        num = 0
        while num < len(self.test_list):
            test = self.test_list[num]
            prior_test = test.get('PriorTest')
            if prior_test in self.test_names:
                self.current_test_set.append(test)
                self.test_list.remove(test)
                continue
            num += 1
        print(self.current_test_set)

    '''def kick_off_tests(self):
        for test in self.current_test_set:
            TestRunner().runner(test)'''


    def kick_off_tests(self):
        '''Method to do Multi process execution'''
        if(__name__=="__main__"):
            with concurrent.futures.ProcessPoolExecutor(max_workers=int(self.exec_config_dict.get('Parallel'))) as executor:
                for test in self.current_test_set:
                    executor.submit(TestRunner().runner,test)


initiator = Initiator()
initiator.get_run_info()
initiator.set_first_execution_order()
initiator.kick_off_tests()
while len(initiator.test_list) > 0:
    initiator.set_subsequent_execution_order()
    initiator.kick_off_tests()

