"""password API"""

import hashlib
import requests


def request_api_data(query_char):
    """request api data"""
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"error fetching: {res.status_code}, check the api and try again!")
    return res


def get_password_leak_count(hashes, hash_to_check):
    """get password leak"""
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for _, count in hashes:
        if _ == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """api check"""
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_char)
    return get_password_leak_count(response, tail)


def main(args):
    """main function"""
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should change your password!!")
        else:
            print(f"{password} was NOT found. carry on!")
    return "done"


if __name__ == "__main__":
    with open("my_password.txt", mode="w", encoding="utf-8") as file:
        txt = file.write("heloooooo")  # -> input password
    with open("my_password.txt", mode="r", encoding="utf-8") as file2:
        txt2 = file2.readlines()
    main(txt2)
