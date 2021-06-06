import bot_mod

if __name__ == "__main__":
    try:
        driver = bot_mod.webdriver.Chrome(options=bot_mod.setup_options())

        bot_mod.launch_site(driver)

        bot_mod.enter_details(driver, 1)
        bot_mod.click_continue(driver)

        bot_mod.enter_details(driver, 2)
        bot_mod.click_continue(driver)

        bot_mod.enter_details(driver, 3)
        bot_mod.click_continue(driver)

        bot_mod.enter_details(driver, 4)
        bot_mod.click_continue(driver)

        bot_mod.enter_details(driver, 5)
        bot_mod.click_continue(driver)

        bot_mod.enter_details(driver, 6)
        bot_mod.click_continue(driver)

        bot_mod.display_coffee_bags(driver)
    except Exception as error:
        print(f'{error}')
    finally:
        # time.sleep() is used to keep browser open long
        # enough to see that the code worked properly
        bot_mod.time.sleep(20)
        driver.quit()
