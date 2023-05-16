import requests
import hashlib                                                                   # this library for hushing your passwords
import sys

#url = 'https://api.pwnedpasswords.com/range/'+'c291b'
#response = requests.get(url)
#print(response)

def reques_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f'Error fetching: {resp.status_code}, check the api and try again!')
    return resp

def read_resp(response):                                                         # this function prints responses with showing how many times matching passwords were hacked
    print(response.text)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]                             # for grabbing only first 5 and last 5 characters of sha-code we use this synthaxis  var_name[:5] - for grabbing the first 5 and  var_name[5:] - for the last 5
    response = reques_api_data(first5_char)
    print(first5_char, tail)
    print(response)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You had better change your password!')
        else:
            print(f'{password} was NOT found. Keep on working!')
    return 'The process executed!'

main(sys.argv[1:])

