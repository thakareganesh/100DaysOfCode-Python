import math
def paint_calc(height,width, cover):
  num_of_cans = (height * width) / cover
  round_up_cans = math.ceil(num_of_cans)
                 
  print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input("enter height of wall: ")) # Height of wall (m)
test_w = int(input("enter width of wall: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
