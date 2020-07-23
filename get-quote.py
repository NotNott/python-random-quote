import random

def primary():
  print("Keep it logically awesome.")
  file = open("quotes.txt")
  quotes = file.readlines()
  file.close()
  last = 15
  middle = 7
  rnd = random.randint(0, last)
  early = random.randint(0, middle)
  print(quotes[rnd].rstrip() + ". " + quotes[early].rstrip())
if __name__== "__main__":
  primary()
