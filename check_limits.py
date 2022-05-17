temperatureLowerLimit = 0
temperatureUpperLimit = 45
socLowerLimit = 20
socUpperLimit = 80
chargeRateUpperLimit = 0.8
temperatureOutOfRangeMessage = 'Temperature is out of range!'
socOutOfRangeMessage = 'State of Charge is out of range!'
chargeRateOutOfRangeMessage = 'Charge rate is out of range!'

def battery_is_ok(temperature, soc, charge_rate):
  if is_value_in_range(temperature, temperatureUpperLimit, temperatureLowerLimit) == 0:
    if is_value_in_range(soc, socUpperLimit, socLowerLimit) == 0:
      if is_value_in_range(charge_rate, chargeRateUpperLimit) == 0:
        return_value = True
      else:
        print_text(chargeRateOutOfRangeMessage)
        return_value = False
    else:
      print_text(socOutOfRangeMessage)
      return_value = False
  else:
    print_text(temperatureOutOfRangeMessage)
    return_value = False
  return return_value

def is_value_in_range(value, upper_limit, *args):
  if len(args) == 0:
    if value > upper_limit:
      return_value = -1
    else:
      return_value = 0
  else:
      if value > upper_limit:
        return_value = -1
      elif value < args[0]:
        return_value = 1
      else:
        return_value = 0
  return return_value


def print_text(text):
  print(text)
  
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(40, 60, 1) is False)
  assert(battery_is_ok(40, 90, 0.7) is False)
  assert(battery_is_ok(50, 60, 0.7) is False)
