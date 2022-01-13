import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error connecting to the pwned API: HTTP {res.status_code} error')
    return res

    # Example response
    # FE80BD525044312D7684C3C288CC4DFF2DD:10
    # FE85206B862B7C2B5DD00C48A73EA657C93:2
    # FEE1BB02B4C557EAE3F680F9AA73B448DF3:3

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'"{password}" was found {count} times! You should probably change your password.')
        else:
            print(f'Whew! "{password}" was not found. :)')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))