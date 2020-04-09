from selenium import webdriver

class Function_Library():

    def __init__(self,driver):
        self.driver = driver

    def m_Organizations_SelectOrgBasedOnIndex(self,index):
        print("Am being called")
        selectXpath = f"//a[.='Select' and contains(@id,'OrganizationSearchResultsLV:{str((int(index) - 1))}')]"
        self.driver.find_element_by_xpath(selectXpath).click()
