def replicate_iter(times, data):
  if times <= 0:
    return []
  elif times == [] or data == []:
  	raise ValueError("Times or Data not found")
  else:
    return [data] * times

def replicate_iter(times, data):
  if times <= 0:
    return []
  elif times == [] or data == []:
  	raise ValueError("Times or Data not found")
  else:
    return [data] * times