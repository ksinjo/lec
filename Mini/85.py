test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5

def paint_calc(height=test_h, width=test_w, cover=coverage):
  cans = int((height* width) / cover) + (height  % width  > 0)
  print(f"You'll need {cans}cans  of patin.")

paint_calc()