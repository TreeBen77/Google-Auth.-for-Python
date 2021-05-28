import hmac, base64, struct, hashlib, time, random

system_random = random.SystemRandom()
class Object(object):
  pass

class one():
  def hello():
    return "hi"

def gen_token(length, period=5):
  token = Object()
  period = period + 1
  if period < 2:
    raise Exception("period cannot be 0 or negitive.")
  token.defualt = str()
  token.period = str()
  repeat = 0
  for loop in range(0, length):
      repeat = repeat + 1
      character = system_random.randint(1, 32)
      if not character < 7:
        string = "qwertyuiopasdfghjklzxcvbnm"
        character = str(string[character - 7])
      if random.randint(0,1) == 1: character = str(character).upper()
      if repeat == period:
        token.period = f"{token.period}."
        repeat = 0
      else:
        token.period = f"{token.period}{character}"
      token.defualt = f"{token.defualt}{character}"
  return token

def hotp(secret, intervals_no):
  key = base64.b32decode(secret, True)
  msg = struct.pack(">Q", intervals_no)
  h = hmac.new(key, msg, hashlib.sha1).digest()
  o = h[19] & 15
  h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
  return h

def totp(secret):
  return hotp(secret, intervals_no=int(time.time())//30)
