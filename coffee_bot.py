#!/bin/bash
# Define your functions
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()


def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'Soy latte'
  else:
    print_message()
    return order_latte()


def get_drink_type():
 res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
 if res == 'a':
   return 'brewed coffee'
 elif res == 'b':
  return 'mocha'
 elif res == 'c':
  return order_latte()
 else:
  print_message()
  return get_drink_type()


def hot_or_cold():
  res = input('Would you like that iced? \n[a] No \n[b] Yes \n> ')
  if res == 'a':
    return 'No'
  elif res == 'b':
    return 'Yes'
  else:
    print_message()
    return hot_or_cold()


def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  hot_cold = hot_or_cold()
  if hot_cold == 'Yes':
    print('Alright, that\'s a {} iced {}!'.format(size, drink_type))
  else:
     print('Alright, that\'s a {} {}!'.format(size, drink_type))
  name = input('Can I get your name please? ')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

# Call coffee_bot()!
coffee_bot()
