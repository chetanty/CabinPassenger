"""This application, named Cabin Passenger aims to solve the problem of the inability to imagine the past. Cabin Passenger
uses the recently released DALL-E API, along with a user-friendly text-based program for the best results. The app will
 obtain inputs of a country and a specific year to provide how life was in the era. This can provide a whole new
 perspective on how people see history. Made by Chetan Tyagi."""

import random
import os
import openai
import base64
import time
import argparse


def intro():
    print("Made by Chetan Tyagi.")
    print(
        "-----------------------------------------------------WELCOME TO THE CABIN PASSENGER------------------------------------------------------")
    print("This application outputs a photo of how life looked in any era of a region using DALL-E API.")
    print("The program is made for past images and will work best for the years after 1000 and before 2020.")
    print("Instructions:")
    print("1. " + "\x1B[3m" + "exit" + "\x1B[0m" + ": To exit the Cabin Passenger.")
    print("2. " + "\x1B[3m" + "ride" + "\x1B[0m" + ": To start the Cabin Passenger.")
    print("3. " + "\x1B[3m" + "help" + "\x1B[0m" + ": To know how Cabin Passenger works.")
    print(" ")


def help():
    print("Instructions:")
    print("1. " + "\x1B[3m" + "exit" + "\x1B[0m" + ": To exit the Cabin Passenger.")
    print("2. " + "\x1B[3m" + "ride" + "\x1B[0m" + ": To start the Cabin Passenger.")
    print("3. " + "\x1B[3m" + "help" + "\x1B[0m" + ": To know how Cabin Passenger works.")
    print("The image is saved is saved in the same location as this file.")
    print("For help or suggestions, please mail to ctyagi@ualberta.ca.")

    print(" ")


def program():
    country_list = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                    'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                    'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of',
                    'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil',
                    'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
                    'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic',
                    'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros',
                    'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire",
                    'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
                    'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France',
                    'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia',
                    'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
                    'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                    'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong',
                    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland',
                    'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
                    'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan',
                    "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
                    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar',
                    'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania',
                    'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of',
                    'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
                    'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                    'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
                    'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                    'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania',
                    'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha',
                    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon',
                    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                    'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)',
                    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                    'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                    'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland',
                    'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of',
                    'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                    'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                    'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan',
                    'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British',
                    'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
    lower_country_list = []
    for i in country_list:
        hj = i.lower()
        lower_country_list.append(hj)
    x = []
    y = []
    l = []
    while True:
        try:
            country = str(input("Please enter a Country: "))
            country = country.lower()
            if country in lower_country_list:
                break
            else:
                print("Please enter a valid country.")
                first_letter = (country[0])
                second_letter = (country[1])
                for i in lower_country_list:
                    if i[0] == first_letter:
                        x.append(i)
                if len(x) > 4:
                    for i in lower_country_list:
                        if i[0] == first_letter and i[1] == second_letter:
                            i = i.capitalize()
                            y.append(i)
            for j in range(4):
                h = random.randint(0, len(x) - 1)
                qwe = x[h]
                l.append(qwe.capitalize())
            if len(y) != 0:
                if len(y) > 1:
                    kop = y[-1]
                    y.pop()
                    y_str = ", ".join(y)
                    print(f"The entered country is not found in our database. Did you mean {y_str} or {kop}?")
                    y = []
                    x = []
                    l = []

                else:
                    kop = y[-1]
                    y.pop()
                    print(f"The entered country is not found in our database. Did you mean {kop}?")
                    y = []
                    x = []
                    l = []


            else:
                kopo = l[-1]
                l.pop()
                l_str = ", ".join(l)
                print(f"The entered country is not found in our database. Did you mean {l_str} or {kopo}?")
                l = []
                y = []
                x = []
        except:
            print("The given country is not in our database. Please try again.")

    while True:
        year = str(input("Please select a year: "))
        try:
            if len(year) >= 3 and len(year) <= 4:
                if int(year) < 2023 and int(year) > 100:
                    wer = "Real life in " + country + " in the year " + year
                    parser = argparse.ArgumentParser()
                    parser.add_argument("-p", "--prompt", help="Text to image prompt:", default=wer)
                    parser.add_argument("-n", "--number", help="Number of images generated", default=1)
                    parser.add_argument("-s", "--size", help="Image size: 256, 512 or 1024", default=1024)

                    args = parser.parse_args()

                    openai.api_key = "Your_API_KEY" # DALL-E provides an API Key, which is put here.

                    res = openai.Image.create(
                        prompt=args.prompt,
                        n=int(args.number),
                        size=f'{args.size}x{args.size}',
                        response_format="b64_json"
                    )

                    for i in range(0, len(res['data'])):
                        b64 = res['data'][i]['b64_json']
                        filename = f'image_{int(time.time())}_{i}.png'
                        print('Saving file ' + filename)
                        with open(filename, 'wb') as f:
                            f.write(base64.urlsafe_b64decode(b64))

                    print("The image is saved is saved in the same location as this file.")
                    break
                else:
                    print("The era must be after the year 100 and before the present year.")
            else:
                print("Write a valid value.")
        except:
            print("The year must be a number. For example- 2004.")


def command():
    while True:
        user_inp = input("Please enter a command key: ")
        user_inp = user_inp.lower()
        if user_inp == "exit":
            break
        elif user_inp == "ride":
            program()
        elif user_inp == "help":
            help()


def main():
    """
    The main file for the program.
    """
    intro()
    command()


if __name__ == '__main__':
    main()
