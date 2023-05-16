import requests
import hashlib
import sys

def demand_api_data(log_in):
    url = 'https://api.pwnedpasswords.com/range/'+ log_in
    req = requests.get(url)
    if req.status_code != 200:
        raise RuntimeError(f'Error fetching: {req.status_code}, check the api and try again!')
    return req

def read_response(response):
    print(response.text)

def let_count_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1_p = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    begin_5, last_5 = sha1_p[:5], sha1_p[5:]
    response = demand_api_data(begin_5)
    print(begin_5, last_5)
    print(response)
    return let_count_leaks(response, last_5)

def run(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} has been identified {count} times. You should change your password!')
        else:
            print(f'{password} has not been found. You can use it!')
    return 'Process has finished!'

run(sys.argv[1:])




