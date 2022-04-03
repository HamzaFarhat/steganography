from encode import encode
from decode import decode


#ROUTER
startUpSelection = int(input("Do you want to encode or decode:\n1: Encode\n2: Decode\n"))

if startUpSelection == 1:
  encode()
if startUpSelection == 2:
  decode()
