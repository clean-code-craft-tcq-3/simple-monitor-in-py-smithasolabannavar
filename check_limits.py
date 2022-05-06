
def battery_is_ok(temperature, soc, charge_rate):
  if check_temprature(temperature):
    print_text('Temperature is out of range!')
    return False
  elif check_state_of_charge(soc):
    print_text('State of Charge is out of range!')
    return False
  elif check_charge_rate(charge_rate):
    print_text('Charge rate is out of range!')
    return False
  return True

def print_text(text):
  print(text)

def check_temprature(temperature):
  if temperature < 0 or temperature > 45:
    return True

def check_state_of_charge(soc):
  if soc < 20 or soc > 80:
    return True

def check_charge_rate(charge_rate):
  if charge_rate > 0.8:
    return True
  return False
  
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
