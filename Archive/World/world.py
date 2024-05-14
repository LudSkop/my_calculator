def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a < 0 < b or b < 0 < a:
      return True
    else:
      return False




if __name__ =="__main__":
  ...