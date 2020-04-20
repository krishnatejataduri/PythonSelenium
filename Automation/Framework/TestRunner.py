from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import importlib.util
import sys
from Automation.Util.JsonUtil import JsonUtil
from Automation.Util.ExcelUtility import ExcelUtility
from Automation.Util.ReportingUtil import ReportingUtil
from Automation.Util import DebugUtil


def external_loader(file_name, file_path):
    spec = importlib.util.spec_from_file_location(file_name, file_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


class TestRunner:
    g_test_set = None
    g_environment = None
    g_remote = None

    def __init__(self):
        self.g_driver = None
        self.g_action = None
        self.g_browser = None
        self.g_user_input = None
        self.g_object_name = None
        self.g_screen_name = None
        self.g_object_type = None
        self.g_locator_type = None
        self.g_locator_value = None
        self.g_function_name = None
        self.g_func_lib_path = "C:/Users/krishna.teja.taduri/Desktop/Functions"
        self.g_func_lib_instance = None
        self.g_test_name = None
        self.g_prior_test = None
        self.g_debug_mode = None
        self.g_current_object = None
        self.g_test_steps_list = []
        self.g_step_environment = None
        self.g_runtime_object_repo = {}
        # Initializing Report
        self.g_report = ReportingUtil()
        self.g_test_status = "Pass"

    def open_browser_instance(self):
        if self.g_browser.upper() == 'CHROME':
            self.g_driver = webdriver.Chrome(
                executable_path="C:\\Users\\krishna.teja.taduri\\eclipse-workspace\\"
                                "DB version\\GuidewireGenericFramework\\Driver Executables\\chromedriver.exe")
        elif self.g_browser.upper() == 'IE':
            pass
            # Add code for opening IE browser
        self.g_driver.implicitly_wait(time_to_wait=30)

    def object_builder(self):
        if self.g_locator_type.upper() == 'XPATH':
            self.g_current_object = self.g_driver.find_element_by_xpath(self.g_locator_value)
        elif self.g_locator_type.upper() == 'ID':
            self.g_current_object = self.g_driver.find_element_by_id(self.g_locator_value)
        elif self.g_locator_type.upper() == 'NAME':
            self.g_current_object = self.g_driver.find_element_by_name(self.g_locator_value)
        elif self.g_locator_type.upper() == 'CLASSNAME':
            self.g_current_object = self.g_driver.find_element_by_class_name(self.g_locator_value)
        elif self.g_locator_type.upper() == 'LINKTEXT':
            self.g_current_object = self.g_driver.find_element_by_link_text(self.g_locator_value)
        elif self.g_locator_type.upper() == 'PARTIALLINKTEXT':
            self.g_current_object = self.g_driver.find_element_by_partial_link_text(self.g_locator_value)
        elif self.g_locator_type.upper() == 'CSSSELECTOR':
            self.g_current_object = self.g_driver.find_element_by_css_selector(self.g_locator_value)
        elif self.g_locator_type.upper() == 'TAGNAME':
            self.g_current_object = self.g_driver.find_element_by_tag_name(self.g_locator_value)

    def perform_action(self):
        if self.g_action.upper() == 'LAUNCHBROWSER':
            if self.g_driver is None:
                self.open_browser_instance()
            self.g_driver.get(
                JsonUtil("C:/Users/krishna.teja.taduri/PycharmProjects/Config/Metadata.txt").load_json()['url'][
                    self.g_user_input][TestRunner.g_environment])
        elif self.g_action.upper() == 'CLOSEBROWSER':
            self.g_driver.close()
        elif self.g_action.upper() == 'ENTERTEXT':
            # sync()
            self.object_builder()
            self.g_current_object.send_keys(self.g_user_input)
            self.g_current_object.send_keys(Keys.TAB)
            self.g_report.add_step("Pass", f"Entered \"{self.g_user_input}\" as {self.g_object_name}.")
        elif self.g_action.upper() == 'CLICK':
            # sync()
            self.object_builder()
            self.g_current_object.click()
            self.g_report.add_step("Pass", f"Clicked on {self.g_object_name}.")
        elif self.g_action.upper() == 'SELECT':
            # sync()
            self.object_builder()
            self.g_current_object.click()
            if self.g_object_type.upper() == 'DROPDOWN':
                Select(self.g_current_object).deselect_by_visible_text(self.g_user_input)
                self.g_report.add_step("Pass",
                                       f"Selected the value \"{self.g_user_input}\" from {self.g_object_name} dropdown list.")
            elif self.g_object_type.upper() == 'RADIOGROUP':
                self.g_locator_value += f"[@value='{self.g_user_input}']"
                self.object_builder()
                self.g_current_object.click()
                self.g_report.add_step("Pass",
                                       f"Selected the radio option \"{self.g_user_input}\" for {self.g_object_name}.")
            elif self.g_object_type.upper() == 'CHECKBOX':
                if (self.g_user_input.upper() == 'OFF' and self.g_current_object.is_selected()) or (
                        self.g_user_input.upper() == 'ON' and not self.g_current_object.is_selected()):
                    self.g_current_object.click()
                    self.g_report.add_step("Pass", f"Checked {self.g_object_name}.")
        elif self.g_action.upper() == 'WAIT':
            sleep(self.g_user_input)
            self.g_report.add_step("Pass", f"Waited for \"{self.g_user_input}\" seconds.")
        elif self.g_action.upper() == 'TAKESCREENSHOT':
            self.g_driver.save_screenshot(self.g_user_input + ".png")
        elif self.g_action.upper() == 'ACCEPTALERT':
            # sync()
            alert_text = self.g_driver.switch_to.alert.text
            self.g_driver.switch_to.alert.accept()
            self.g_report.add_step("Pass", f"Accepted the alert \"{alert_text}\".")
        elif self.g_action.upper() == 'HIGHLIGHT':
            # sync()
            self.object_builder()
            original_style = self.g_current_object.get_attribute("style")
            self.g_driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",
                                         self.g_current_object, "style", "border:2px solid red; border-style:dashed;")
            sleep(2)
            self.g_driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",
                                         self.g_current_object, "style", original_style)
            self.g_report.add_step("Pass", f"Highlighted the element \"{self.g_object_name}\".")
        elif self.g_action.upper() == "FUNCTION":
            if self.g_func_lib_instance == None:
                # Loading function library
                module = external_loader("Functions.Function_Library", "C:\\Users\\krishna.teja.taduri\\PycharmProjects"
                                                                       "\\Functions\\Function_Library.py")
                func_lib_class_name = 'Function_Library'
                exec(f'self.g_func_lib_instance = module.{func_lib_class_name}(self.g_driver)')
            # Method call
            self.g_report.add_step("Pass", f"Calling the function \"{self.g_function_name}\".")
            exec(f'self.g_func_lib_instance.{self.g_function_name}({self.g_user_input})')

    def runner(self, test):
        try:
            self.g_test_name = test.get('TestcaseName')
            self.g_browser = test.get('Browser')
            self.g_prior_test = test.get('PriorTest')
            self.g_debug_mode = test.get('DebugMode')
            prior_step_screen_name = 'NA'
            print(self.g_test_name)
            self.g_test_steps_list = ExcelUtility(path="C:/Users/krishna.teja.taduri/PycharmProjects/Tests"
                                                       f"/{self.g_test_name}.xlsx",
                                                  sheet_name=f"{self.g_test_name}").get_test_steps(
                execution_environment=TestRunner.g_environment)
            step_num = 0
            print(self.g_test_steps_list)
            while step_num < len(self.g_test_steps_list):
                try:
                    self.g_object_name = self.g_test_steps_list[step_num].get('ObjectName')
                    self.g_screen_name = self.g_test_steps_list[step_num].get('ScreenName')
                    self.g_action = self.g_test_steps_list[step_num].get('Action')
                    self.g_function_name = self.g_test_steps_list[step_num].get('Function')
                    self.g_user_input = self.g_test_steps_list[step_num].get('UserInput')
                    self.g_step_environment = self.g_test_steps_list[step_num].get('Environment')
                    # Loading the object repository of the current screen if its not loaded already
                    if (
                            prior_step_screen_name == 'NA' or prior_step_screen_name != self.g_screen_name) and self.g_screen_name != 'NA':
                        prior_step_screen_name = self.g_screen_name
                        self.g_runtime_object_repo = ExcelUtility(path="C:/Users/krishna.teja.taduri/eclipse-workspace"
                                                                       "/GuidewireGenericFramework/config"
                                                                       "/ObjectRepository.xlsx",
                                                                  sheet_name=self.g_screen_name).load_object_repo()
                        print(self.g_runtime_object_repo)

                    if self.g_object_name != 'NA':
                        self.g_object_type = self.g_runtime_object_repo.get(self.g_object_name).get('ObjectType')
                        self.g_locator_type = self.g_runtime_object_repo.get(self.g_object_name).get('LocatorType')
                        self.g_locator_value = self.g_runtime_object_repo.get(self.g_object_name).get('LocatorValue')

                    # Building the object
                    if self.g_object_name.upper() != 'NA':
                        self.object_builder()

                    # Performing the action
                    self.perform_action()

                    step_num += 1
                except Exception as loop_exception:
                    user_choice = DebugUtil.show_message(test_name=self.g_test_name,screen_name=self.g_screen_name,object_or_func_name=self.g_object_name,action=self.g_action,error_details=(str(loop_exception).split("\n")[0])[:300])
                    if (user_choice == 'Retry'):
                        self.g_report.add_step("Warning",
                                               f"Screen: {self.g_screen_name}\nObject: {self.g_object_name}\nAction: {self.g_action}\nError Info: \n"+(str(loop_exception).split("\n")[0])[:300])
                        continue
                    elif (user_choice == 'Ignore'):
                        step_num += 1
                        self.g_report.add_step("Fail",
                                               f"Screen: {self.g_screen_name}\nObject: {self.g_object_name}\nAction: {self.g_action}\nError Info: \n"+
                                               (str(loop_exception).split("\n")[0])[:300])
                        self.g_test_status = "Fail"
                    else:
                        self.g_report.add_step("Fail",
                                               f"Screen: {self.g_screen_name}\nObject: {self.g_object_name}\nAction: {self.g_action}\nError Info: \n"+
                                               (str(loop_exception).split("\n")[0])[:300])
                        self.g_test_status = "Fail"
                        break
                    #break

        except Exception as exception:
            print(exception)
            self.g_test_status = "Fail"

        finally:
            if self.g_driver is not None:
                self.g_driver.close()
            self.g_report.save_report(TestRunner.g_environment, TestRunner.g_test_set, self.g_test_name,self.g_test_status)
