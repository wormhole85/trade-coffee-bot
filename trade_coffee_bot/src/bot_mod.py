import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_options():
    options = Options()

    # gets rid of "Chrome is being controlled by automated test software." infobar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    return options

def launch_site(driver):
    driver.get('https://www.drinktrade.com/onboarding')

def enter_details(driver, details_section):
    if details_section == 1:
        # enters first name
        first_name_field = driver.find_element_by_xpath('//input[contains(@class, "user-input__text-field") and contains(@type, "text")]')
        first_name_field.send_keys('your name')

        # clicks coffee experience field
        coffee_experience_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--boldness")]//div[contains(@class, "custom-select__tab")]')
        coffee_experience_field.click()

        # locates the correct experience level and
        # clicks on it (in this case the level is: intermediate)
        experience_level = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "an intermediate")]')
        time.sleep(0.5)
        experience_level.click()
    elif details_section == 2:
        belief_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--sustainability")]//div[contains(@class, "custom-select__tab")]')
        belief_options_field.click()

        belief_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "believe")]')
        belief_option.click()
    elif details_section == 3:
        cups_consumed_field = driver.find_element_by_xpath('//input[contains(@class, "user-input__text-field") and contains(@type, "number")]')
        cups_consumed_field.send_keys('2')

        brew_method = driver.find_element_by_xpath('//div[contains(@role, "button") and contains(text(), "Pour Over")]')
        brew_method.click()

        add_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--additions")]//div[contains(@class, "custom-select__tab")]')
        add_options_field.click()

        add_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "nothing (I take it black)")]')
        add_option.click()
    elif details_section == 4:
        roast_level = driver.find_element_by_xpath('//button//span[contains(@class, "progress-level__step-name") and contains(text(), "Medium")]')
        roast_level.click()
    elif details_section == 5:
        coffee_taste = driver.find_element_by_xpath('//button//span[contains(@class, "progress-level__step-name") and contains(text(), "Hints of something different")]')
        coffee_taste.click()
    elif details_section == 6:
        brew_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--brand")]//div[contains(@class, "custom-select__tab")]')
        brew_options_field.click()

        brew_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "whole bean")]')
        brew_option.click()

        coffee_drinker_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--caffeine")]//div[contains(@class, "custom-select__tab")]')
        coffee_drinker_options_field.click()

        coffee_drinker_type = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "regular")]')
        coffee_drinker_type.click()

def click_continue(driver):
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

def manipulate_image_urls(coffee):
    img_url = coffee.get_attribute('src')
    uniform_url = img_url.replace('w_200', 'w_2560', 1)

    return uniform_url

def display_coffee_bags(driver):
    time.sleep(5)

    coffee_bag = driver.find_element_by_xpath('//img[contains(@class, "product-image desktop")]')
    coffee_bags = driver.find_elements_by_xpath('//div[contains(@class, "product-selection-container")]//img[contains(@class, "product-image")]')

    if coffee_bags == []:
        img_url = coffee_bag.get_attribute('src')
        os.system('start ' + img_url)
    else:
        coffee_bags.insert(0, coffee_bag)
        for coffee in coffee_bags:
            os.system('start ' + manipulate_image_urls(coffee))
