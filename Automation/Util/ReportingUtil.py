from html.parser import HTMLParser
import bs4
from datetime import datetime
import os

class ReportingUtil:

    def __init__(self):
        self.test_start_time = datetime.today()
        with open('C:/Users/krishna.teja.taduri/PycharmProjects/Config/TestReportTemplate.html', 'r') as my_file:
            self.soup = bs4.BeautifulSoup(my_file.read(), features="html.parser")
            my_file.close()

    def add_step(self,step_status,step_details):
        cell_color = "#ADFF2F"
        if step_status.upper()=="FAIL":
            cell_color = "#FF6347"
        elif step_status.upper()=="WARNING":
            cell_color = "#A9A9A9"
        #Appending a new empty row to the table
        new_row = self.soup.new_tag("tr")
        #Appending a new entry for status column in the newly added row
        new_status_entry = self.soup.new_tag("td", attrs={"align": "center", "class": f"status {step_status.lower()}", "title": f"{step_status.lower()}", "alt": f"{step_status.lower()}",
                                             "bgcolor": cell_color})
        new_status_entry.append(step_status.capitalize())
        #Appending an new entry in Timestamp column in the newly added row
        new_time_entry = self.soup.new_tag("td", attrs={"align": "center", "class": "timestamp", "title": "timestamp",
                                                          "alt": "timestamp",
                                                          "bgcolor": "#FAFEFE"})
        new_time_entry.append(str(datetime.now().time()).split(".")[0])
        # Appending an new entry in Details column in the newly added row
        # Seperating exception details in case of failure
        exception_details = step_details.split("\n")
        new_details_entry = self.soup.new_tag("td",
                                              attrs={"class": "step-details", "title": "details",
                                                     "alt": "details",
                                                     "bgcolor": "#FAFEFE"})
        if len(exception_details) > 1:
            for detail in exception_details:
                new_details_entry.append(detail)
                new_sub_details_entry = self.soup.new_tag("br")
                new_details_entry.append(new_sub_details_entry)

        else:
            new_details_entry.append(exception_details[0])

        #Appending all the child cell elements to the row
        new_row.append(new_status_entry)
        new_row.append(new_time_entry)
        new_row.append(new_details_entry)

        #Appending the row to the table
        self.soup.find("table").append(new_row)

    def save_report(self,environment,test_set_name,test_name,test_status):
        test_end_time = datetime.today()
        file_path = f"C:/Users/krishna.teja.taduri/PycharmProjects/Reports/{environment}/{test_set_name}"
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(f"{file_path}/{test_name}.html", 'w') as report:
            self.soup.find("h3").append(test_name)
            self.soup.find("span",{"class":"test-status label right outline capitalize fail"}).append(test_status)
            self.soup.find("span",{"title":"Test environment"}).append(environment)
            self.soup.find("span",{"title":"Test started time"}).append(str(self.test_start_time).split(".")[0])
            self.soup.find("span",{"title":"Test ended time"}).append(str(test_end_time).split(".")[0])
            self.soup.find("span",{"title":"Time taken to finish"}).append(str(test_end_time-self.test_start_time).split(".")[0])
            report.write(str(self.soup))
            report.close()


