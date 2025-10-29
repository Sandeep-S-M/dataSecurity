List = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

position = 0

def encrypt(msg,a):
  result = ""
  for i in msg.upper():
    if i in List:
      position = List.index(i)
      newposition = (a + position) % 26
      result += List[newposition]
    else:
      result += i
  return result
      
def decrypt(msg,a):
  result = ""
  for i in msg.upper():
    if i in List:
      position = List.index(i)
      newposition = (position - a) % 26
      result += List[newposition]
    else:
      result += i
  return result

def main():
  print("--------------Encrypt/Decrypt---------------")
  data = input("Enter the message: ")
  num = int(input("Enter shift key you want to encrypt/decrypt: [1<val<25]: "))
  what = input()
  if what == "encription":
    print("encrypted info: ",encrypt(data,num))
  elif what == "decription":
    print("decryted info: ",decrypt(data,num))
  else:
    print(" Go to hell and heaven ")
  
if __name__ == "__main__":
  main()


