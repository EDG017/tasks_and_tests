HEX_MAP_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

HEX_MAP_TO_STR = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

DIGITS_MAP = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


def conv_num(num_str):
    """Function that takes in a string and returns a number."""

    # create a dictionary to hold the possible values

    final_digit = 0  # hold final result
    multiplier = 1  # multiplier that increases based on which digit we are on
    decimal_counter = 0
    negative = 1

    conv_hex_checker = conv_hex_check(num_str)

    if conv_hex_checker:
        return conv_hex(num_str)

    # function used to determine how large the multiplier should be,
    # also checks if number is negative

    for digit in num_str:
        if digit == '.':
            decimal_counter += 1
        elif multiplier == 1 and digit == '-':
            negative = -1
        elif digit not in DIGITS_MAP:
            return None

    if decimal_counter == 1:
        return conv_decimal(num_str)
    elif decimal_counter > 1:
        return None

    # loop through string, adding each digit to the final digit

    for digit in reversed(num_str):
        if digit in DIGITS_MAP:
            current_digit = DIGITS_MAP[digit] * multiplier
            final_digit += current_digit
            multiplier *= 10

    return final_digit * negative


def conv_hex_check(num_str):
    """Function that checks if a string is a hexadecimal value"""

    if len(num_str) > 1 and num_str[0] == '0' and num_str[1] == 'x':
        return True
    elif num_str[0] == '-' and num_str[1] == '0' and num_str[2] == 'x':
        return True
    else:
        return False


def conv_decimal(num_str):
    """Function that takes in a string and converts it to a decimal value"""

    first_half = 0.0
    second_half = 0.0
    first_multiplier = 1
    second_multiplier = 1
    negative_multiplier = False
    reached_decimal = False

    for digit in reversed(num_str):
        if digit == '.':
            reached_decimal = True
        elif digit == '-':
            negative_multiplier = True
        else:
            if reached_decimal:
                current_digit = DIGITS_MAP[digit] * first_multiplier
                first_half += current_digit
                first_multiplier *= 10
            else:
                current_digit = DIGITS_MAP[digit] * second_multiplier
                second_half += current_digit
                second_multiplier *= 10
    second_half = second_half / second_multiplier
    final_digit = first_half + second_half

    if negative_multiplier:
        final_digit *= -1

    return final_digit


def conv_hex(num_str):
    """Function that takes in a hex string and converts it to an integer"""

    final_digit = 0
    multiplier = 1
    counter = 0

    if num_str[0] == '-':
        negative = True
    else:
        negative = False

    for digit in reversed(num_str):
        if digit in HEX_MAP_TO_INT:
            current_digit = HEX_MAP_TO_INT[digit] * multiplier
            final_digit += current_digit
            multiplier *= 16
        else:
            if digit != 'x' and counter != len(
                    num_str) - 2 and negative is False:
                return None
            elif digit != 'x' and counter != len(
                    num_str) - 3 and negative is False:
                return None

        counter += 1
    if negative:
        final_digit *= -1

    return final_digit


def conv_endian(num, endian='big'):
    """takes in an integer value as num and an optional string as endian type
     and converts the integer to a hexadecimal number"""

    res = ["##"]
    abs_num = abs(num)

    while abs_num > 0:
        remainder = abs_num % 16
        abs_num = abs_num // 16

        if res[0][1] == "#":
            res[0] = "#" + HEX_MAP_TO_STR[remainder]
        elif res[0][0] == "#":
            res[0] = HEX_MAP_TO_STR[remainder] + res[0][1]
        else:
            res.insert(0, "##")
            res[0] = "#" + HEX_MAP_TO_STR[remainder]

    if res[0][0] == "#":
        res[0] = "0" + res[0][1]

    if endian != "big" and endian != "little":
        return None

    if endian == "little":
        res.reverse()

    res = " ".join(res)

    if num < 0:
        res = "-" + res

    if num == 0:
        return "00"

    return res


def my_datetime(num_secs):
    """
    This function returns the date of the timestamp (in seconds)
    passed into it and returns it in an MM-DD-YYYY format
    """
    days, rem = divmod(num_secs, 86400)
    epoch_day = 1
    epoch_month = 1
    epoch_year = 1970
    leap_year = False  # 1970 not a leap year
    calendar_days = calendar_days_helper(leap_year, epoch_month - 1)

    while days > 0:  # This loop uses the days to get the timestamp date
        days -= 1
        epoch_day += 1
        if epoch_day > calendar_days:
            epoch_day = 1
            epoch_month += 1
            if epoch_month <= 12:
                calendar_days = \
                    calendar_days_helper(leap_year, epoch_month - 1)
            if epoch_month > 12:
                epoch_month = 1
                epoch_year += 1
                leap_year = is_leap_year(epoch_year)
    return '%02d-%02d-%04d' % (epoch_month, epoch_day, epoch_year)


def calendar_days_helper(leap_year, month):
    """
    This function is a helper that will return the total days of the month
    passed into it and accounts for leap years
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    calendar_days = month_days[month]
    # Plus 1 due to minus used to get array value
    # Adds 1 day to February for leap year
    if leap_year and month + 1 == 2:
        return 29
    return calendar_days


def is_leap_year(year):
    """Checks if the year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
