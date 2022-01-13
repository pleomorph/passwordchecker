# passwordchecker.py

Securely checks if your password appeared in a data leak.  This is done by hashing the user input, then sending a partial hash to the pwnedpasswords API, receiving a list of matching hashes, and comparing the hashes locally.  The password (nor its full hash) is never sent over the Internet.

## Usage

```sh
python3 checkmypass.py myfirstpassword mysecondpassword mythirdpassword
```

```
"myfirstpassword" was found 17 times! You should probably change your password.
"mysecondpassword" was found 7 times! You should probably change your password.
Whew! "mythirdpassword" was not found. :)
done!
```