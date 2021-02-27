import re

def main():
    phone = '+7 955 12345-67'
    parse_phone(phone)

def parse_phone(number: str):
    result_one = ''.join(re.findall(pattern=r'\d', string=number))
    first_number = re.findall(pattern=r'[78]', string=result_one[0])

    if len(result_one) != 11 or len(first_number) == 0:
        print("Номер не валиден")
        return

    print('+7-{}-{}-{}-{}'.format(result_one[1:4], result_one[4:7], result_one[7:9], result_one[9:11]))

main()
