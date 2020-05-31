import time
from credentials import *
from constants import *
from drivers import driver
from message import *


def login():
    driver.get(SIGN_IN_URL)
    driver.find_element_by_id(USERNAME_ID).send_keys(username)
    driver.find_element_by_id(PASSWORD_ID).send_keys(password)
    driver.find_element_by_xpath(SUBMIT_XPATH).click()


def navigate_to_profile(profile_url):
    driver.get(profile_url)


def send_message(message, name):
    try:
        # change button xpath in case of non-friends
        time.sleep(1)
        driver.find_element_by_xpath(MESSAGE_BTN_XPATH).click()
        time.sleep(2)
        message_input = driver.switch_to.active_element
        message_input.send_keys(message.format(name))
        message_input.submit()
        print("Sent message to " + name + "...")
        return True
    except Exception:
        print("Could not send message to " + name + " :-(")
        return False


def main():
    print("Welcome to ColdLink v1! The script is starting...")
    sent_messages = 0
    total_messages = 0

    login()

    with open('leads.txt') as leads:
        lead = leads.readline()
        time.sleep(3)
        while lead:
            navigate_to_profile(lead)
            name = driver.find_element_by_xpath(FULL_NAME_XPATH).text
            was_sent = send_message(MESSAGE, name)
            if was_sent:
                sent_messages += 1
            total_messages += 1
            time.sleep(3)
            lead = leads.readline()

    time.sleep(3)
    print("Done! Sent {} messages out of {}".format(
        sent_messages, total_messages))
    driver.close()


if __name__ == "__main__":
    main()
