import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# gets rid of "Chrome is being controlled by automated test software." infobar
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

try:
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.drinktrade.com/onboarding')

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

    # clicks the continue button
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

    belief_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--sustainability")]//div[contains(@class, "custom-select__tab")]')
    belief_options_field.click()

    belief_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "believe")]')
    belief_option.click()

    # clicks the continue button
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

    cups_consumed_field = driver.find_element_by_xpath('//input[contains(@class, "user-input__text-field") and contains(@type, "number")]')
    cups_consumed_field.send_keys('2')

    brew_method = driver.find_element_by_xpath('//div[contains(@role, "button") and contains(text(), "Pour Over")]')
    brew_method.click()

    add_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--additions")]//div[contains(@class, "custom-select__tab")]')
    add_options_field.click()

    add_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "nothing (I take it black)")]')
    add_option.click()

    # clicks the continue button
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

    roast_level = driver.find_element_by_xpath('//button//span[contains(@class, "progress-level__step-name") and contains(text(), "Medium")]')
    roast_level.click()

    # clicks the continue button
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

    coffee_taste = driver.find_element_by_xpath('//button//span[contains(@class, "progress-level__step-name") and contains(text(), "Hints of something different")]')
    coffee_taste.click()

    # clicks the continue button
    continue_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    continue_button.click()

    brew_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--brand")]//div[contains(@class, "custom-select__tab")]')
    brew_options_field.click()

    brew_option = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "whole bean")]')
    brew_option.click()

    coffee_drinker_options_field = driver.find_element_by_xpath('//div[contains(@class, "question-wrapper--active question-wrapper--caffeine")]//div[contains(@class, "custom-select__tab")]')
    coffee_drinker_options_field.click()

    coffee_drinker_type = driver.find_element_by_xpath('//ul//li[contains(@role, "option") and contains(text(), "regular")]')
    coffee_drinker_type.click()

    get_your_match_button = driver.find_element_by_xpath('//button[contains(@class, "trade__button")]')
    get_your_match_button.click()

    time.sleep(5)

    coffee_bag = driver.find_element_by_xpath('//img[contains(@class, "product-image desktop")]')
    coffee_bags = driver.find_elements_by_xpath('//div[contains(@class, "product-selection-container")]//img[contains(@class, "product-image")]')

    if coffee_bags == []:
        img_url = coffee_bag.get_attribute('src')
        os.system('start ' + img_url)
    else:
        coffee_bags.insert(0, coffee_bag)
        for coffee in coffee_bags:
            img_url = coffee.get_attribute('src')
            uniform_url = img_url.replace('w_200', 'w_2560', 1)
            os.system('start ' + uniform_url)
except Exception as error:
    print(f'{error}')
finally:
    # time.sleep() is used to keep browser open long
    # enough to see that the code worked properly
    time.sleep(20)
    driver.quit()
