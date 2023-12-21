def process_calibration_document(filepath):
  sum = 0
  with open (filepath, "r") as f:
    for line in f:
      sum += get_calibration_value(line)
  return sum

def get_calibration_value(line):
  val=""
  first=0
  last=len(line)-1

  while first < len(line)-1:
    try:
      int(line[first])
      break
    except:
      first+=1

  while last > 0:
    try:
      int(line[last])
      break
    except:
      last-=1

  return int(line[first])*10+int(line[last])
