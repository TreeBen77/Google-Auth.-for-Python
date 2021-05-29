### Introduction & Installing
Google Auth for Python can generate a 42002 character long Google Authenticator seed in 1 second, with a 2.2Ghz Processor running Linux. (kinda overkill ngl)
### Quick Setup
idk how to install it with pip install, if you know please tell me.
```python
import googleauth

#returns a securely random 16 digit seed
googleauth.generate(16).token
>>> 'fhDdPqlpiht6jCuE'

#same as above but every 5th digit is a period (.)
googleauth.generate(16, period=5).period
>>> 'LExTT.FBZKH.HlzV'

#returns the code for a time-based seed.
googleauth.get.totp('wa55Ad5Io5xj32ao')
>>> 459745

#returns the code for a HMAC-based seed/
googleauth.get.hotp('1xX1UuJ5iKsJbOH2')
>>> 452806
```
