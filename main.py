##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

PLACEHOLDER = "[NAME]"
birth = {}
letters = []
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
brith_day = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)
if today in brith_day:
    birth = brith_day[today]
    names = birth["name"]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open("letter_templates/letter_1.txt") as file1:
        letter_1 = file1.read()
        new_letter = letter_1.replace(PLACEHOLDER, names)
        letters.append(new_letter)

    with open("letter_templates/letter_2.txt") as file2:
        letter_2 = file2.read()
        new_letter = letter_2.replace(PLACEHOLDER, names)
        letters.append(new_letter)

    with open("letter_templates/letter_2.txt") as file3:
        letter_3 = file3.read()
        new_letter = letter_3.replace(PLACEHOLDER, names)
        letters.append(new_letter)

    rand_letter = random.choice(letters)
    # 4. Send the letter generated in step 3 to that person's email address.
    my_email = "magwebubulelani06@gmail.com"
    password = "yixkrqqcaopxbixs"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="magwebubulelani@yahoo.com",
                            msg=f"Subject:Have a nice day\n\n{rand_letter}."
                            )
