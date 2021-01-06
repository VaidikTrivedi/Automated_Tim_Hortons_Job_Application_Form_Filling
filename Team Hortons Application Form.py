# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:47:52 2020

@author: Vaidik
"""


from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

class FillTeamForm:
    def __init__(self, webLink):
        self.driver = webdriver.Chrome("F:/Software/Setups/chromedriver.exe")
        self.driver.get(webLink)
        sleep(3)
    
    def fillForm(self):
        self.driver.find_element_by_xpath("//input[@name=\"first\"]")\
            .send_keys("Vaidik")
        self.driver.find_element_by_xpath("//input[@name=\"last\"]")\
            .send_keys("Trivedi")
        self.driver.find_element_by_xpath("//input[@name=\"street_address\"]")\
            .send_keys("294 Chandler Drive")
        self.driver.find_element_by_xpath("//input[@name=\"city\"]")\
            .send_keys("Kitchener")
        self.driver.find_element_by_xpath("//input[@name=\"zip_code\"]")\
            .send_keys("N2E2K1")
        selectState = Select(self.driver.find_element_by_id("application_state"))
        selectState.select_by_visible_text("Ontario")
        self.driver.find_element_by_xpath("//input[@name=\"prefer_phone_number\"]")\
            .send_keys("+1 647 857 7422")
        self.driver.find_element_by_xpath("//input[@name=\"email_address\"]")\
            .send_keys("trivedi.vaidik@yahoo.in")
        hereOpportunity = Select(self.driver.find_element_by_id("about_this_opportunity"))
        hereOpportunity.select_by_visible_text("Online at TimHortons.com")
        self.driver.find_element_by_xpath("//input[@name=\"referred_you\"]")\
            .send_keys("Rinkesh Patel")
        eligible =  Select(self.driver.find_element_by_id("work_in_the_us"))
        eligible.select_by_visible_text("Yes")
        workBrfore = Select(self.driver.find_element_by_id("worked_th_before"))
        workBrfore.select_by_visible_text("No")
        levelOfEducation = Select(self.driver.find_element_by_id("education_completed"))
        levelOfEducation.select_by_visible_text("College/University")
        employmentType = Select(self.driver.find_element_by_id("employment_type"))
        employmentType.select_by_visible_text("Part Time")
        
        mondayStart = Select(self.driver.find_element_by_id("edit-start2"))
        mondayStart.select_by_visible_text("05:00 PM")
        mondayEnd = Select(self.driver.find_element_by_id("edit-end2"))
        mondayEnd.select_by_visible_text("11:00 PM")
        tuesdayStart = Select(self.driver.find_element_by_id("edit-start3"))
        tuesdayStart.select_by_visible_text("05:00 PM")
        tuesdatEnd = Select(self.driver.find_element_by_id("edit-end3"))
        tuesdatEnd.select_by_visible_text("11:00 PM")
        wedStart = Select(self.driver.find_element_by_id("edit-start4"))
        wedStart.select_by_visible_text("05:00 PM")
        wedEnd = Select(self.driver.find_element_by_id("edit-end4"))
        wedEnd.select_by_visible_text("11:00 PM")
        
        self.driver.find_element_by_xpath("//input[@name=\"preffered_number\"]")\
            .send_keys("20")
        self.driver.find_element_by_xpath("//input[@name=\"pay_expectations\"]")\
            .send_keys("14")
        self.driver.find_element_by_xpath("//input[@name=\"current_most_recent_com\"]")\
            .send_keys("Starbucks - India")
        self.driver.find_element_by_xpath("//input[@name=\"current_start_date\"]")\
            .send_keys("17-01-2019")
        self.driver.find_element_by_xpath("//input[@name=\"current_end_date\"]")\
            .send_keys("24-08-2019")
        self.driver.find_element_by_xpath("//input[@name=\"position_duties\"]")\
            .send_keys("Customer Handling")
        self.driver.find_element_by_xpath("//input[@name=\"reason_for_leaving\"]")\
            .send_keys("Study Abroad")
        
        
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        
        
fillWholeForm = FillTeamForm("http://jobs.timhortons.com/ca_en/in-restaurant-signup?job_role=1354&restaurant_id=523946&v=ca")
fillWholeForm.fillForm()
