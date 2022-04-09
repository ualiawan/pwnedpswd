pwnedpswd is a useful Python  command line utility that lets you check if a passphrase has been pwned. It uses the [Pwned Passwords v2 API](https://haveibeenpwned.com/API/v2#PwnedPasswords). All provided password data is [k-anonymized](https://en.wikipedia.org/wiki/K-anonymity) before sending to the API, so plaintext passwords never leaves your computer. Additionlaly, the program also accepts [SHA-1](https://en.wikipedia.org/wiki/SHA-1) as input instead of plaintext passphrase for one more layer of conviction.

## From [PwnedPasswords](https://haveibeenpwned.com/API/v2#PwnedPasswords):
> Pwned Passwords are more than half a billion passwords which have previously been exposed in data breaches. The service is detailed in the launch blog post then further expanded on with the release of version 2. The entire data set is both downloadable and searchable online via the Pwned Passwords page.

Each password is stored as a SHA-1 hash of a UTF-8 encoded password. The downloadable source data delimits the full SHA-1 hash and the password count with a colon (:) and each line with a CRLF.

## Usage

Clone this repository:

```
git clone git@github.com:ualiawan/pwnedpswd.git
```

Alternatively, you can also download directly from [here](https://github.com/ualiawan/pwnedpswd/archive/refs/heads/master.zip).

Run followowing command from `pwnedpswd` directory:

```
python pwned.py --pass-phrase 'enter-your-plaintext-password-here'
```

You may also enter SHA-1 hash of your passphrase instead of plaintext as follows:
```
python pwned.py --pass-phrase AE9030C665364EB2651D450E8321AE62DD51A726 --is-sha1
```

The CLI will log whether your passphrase has been pwned in a previous data breach, along with the number of times it has been pwned. If it has been pwned, the best course of action will be to change your passphrase as soon as possible.
