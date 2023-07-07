#!/usr/bin/env python3

import requests
import time
import json
import argparse
import datetime

def get_input_data(custom_key=None):
    text_message = input("Message: ")
    if custom_key is None:
        custom_key = input("Key: ")
    return text_message, custom_key

def send_message(phone_number, message, custom_key):
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': message,
        'key': custom_key,
    })
    return resp.json()

def check_status(result):
    list_values = list(result.values())
    print("\nSending Message...")
    time.sleep(2)
    if True in list_values:
        print("\nMessage Successful")
        time.sleep(1)
        print("\nText ID: {}".format(list_values[1]))
        print("Credits Available: {}".format(list_values[2]))
    elif 'Invalid phone number or bad request. If your phone number contains a +, please check that you are URL encoding it properly.' in list_values:
        print("\nMessage Failed")
        print("\nError: Invalid Phone Number")
    elif 'Out of quota' in list_values:
        print("\nMessage Failed")
        print("\nError: Out of Credits")
    else:
        print("\nMessage Failed")
        print("\nThank you for using SMSpoof")

def main(phone_numbers, text_message=None, custom_key=None, delay=None, file=None, schedule=None):
    if phone_numbers == []:  # If no phone numbers provided, ask for one
        phone_number = input("Phone Number: ")
        phone_numbers.append('+' + phone_number)

    if text_message is None and file is not None:
        with open(file, 'r') as f:
            text_message = f.read()
    elif text_message is None and file is None:
        text_message, custom_key = get_input_data(custom_key)
    
    if custom_key is None:
        _, custom_key = get_input_data(custom_key)

    # Schedule the message if a future date and time is provided
    if schedule is not None:
        schedule_dt = datetime.datetime.strptime(schedule, "%Y-%m-%d %H:%M")
        current_dt = datetime.datetime.now()
        time_diff = (schedule_dt - current_dt).total_seconds()

        if time_diff > 0:
            print("\nScheduled message. Will be sent at: {}".format(schedule_dt))
            time.sleep(time_diff)
        else:
            print("\nScheduled time has already passed. Sending immediately.")

    for phone_number in phone_numbers:
        result = send_message(phone_number, text_message, custom_key)
        check_status(result)

        if delay is not None:
            time.sleep(delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a script to send text messages. Use the following flags to provide inputs through the command line:")
    parser.add_argument("-n", "--number", help="The phone number to which the message should be sent. Should be a valid phone number.")
    parser.add_argument("-w", "--wordlist", help="File path to a list of phone numbers. Each number should be on a new line.")
    parser.add_argument("-m", "--message", help="The text message to be sent.")
    parser.add_argument("-k", "--key", help="The custom key for authentication.")
    parser.add_argument("-d", "--delay", type=int, help="Delay in seconds between each message.")
    parser.add_argument("-f", "--file", help="File path to include a text file as the content of the message.")
    parser.add_argument("-s", "--schedule", help="Schedule the message to be sent at a specific date and time (format: 'YYYY-MM-DD HH:MM').")
    args = parser.parse_args()

    phone_numbers = []
    if args.wordlist is not None:
        with open(args.wordlist, 'r') as f:
            phone_numbers = [line.strip() for line in f]
            phone_numbers = ['+' + number for number in phone_numbers]
    elif args.number is not None:
        phone_numbers.append('+' + args.number)

    text_message = args.message

    main(phone_numbers, text_message, args.key, args.delay, args.file, args.schedule)
