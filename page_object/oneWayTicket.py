import time

from selenium.webdriver.common.by import By

from Dataset import test_data
from page_object.basePage import BasePage


class Ticket(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    oneWayTab = (By.XPATH,"//a[@class='blur_class type-active']")
    DepartFrom = (By.XPATH,"//input[@id='BE_flight_origin_city']")
    DropdownfirstList = (By.XPATH, "//div[@class='viewport']/div/div/li/div[1]")
    arrivalCity = (By.XPATH,"//input[@id='BE_flight_arrival_city']")
    departure = (By.XPATH,"//input[@class='custom-date-input BE_flight_origin_date']")
    calender = (By.XPATH,"//td[@id='05/01/2024']")
    arrow = (By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']")
    radioButton = (By.XPATH,"(//li[@class='enabled _msddli_'])[2]")
    checkBox = (By.XPATH,"(//i[@class='ico ico-checkbox'])[2]")
    Search = (By.XPATH,"//input[@id='BE_flight_flsearch_btn']")

    def ticketBook(self):
        self.wait_for(self.oneWayTab)
        self.click(self.oneWayTab)
        self.click(self.DepartFrom)
        self.send_keys(self.DepartFrom,test_data.departFrom)
        self.click(self.DropdownfirstList)
        self.click(self.arrivalCity)
        self.send_keys(self.arrivalCity,test_data.arrivalTo)
        self.click(self.DropdownfirstList)
        time.sleep(2)
        self.click(self.departure)
        self.wait_for(self.calender)
        self.click(self.calender)
        self.wait_for(self.arrow)
        self.click(self.arrow)
        self.click(self.radioButton)
        self.click(self.checkBox)
        self.click(self.Search)
