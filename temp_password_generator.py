#Name of user 
first_name = "Reiko"
last_name = "Matsuki"
## generate temporary password for user ##
## using last 3 characters of their first & last name##
def password_generator(first_name, last_name):
  first_length        = len(first_name)
  last_length         = len(last_name)
  first_name_last_3   = first_name[first_length-3:]
  last_name_last_3    = last_name[last_length-3:]
  temp_pass    = first_name_last_3 + last_name_last_3
  return temp_pass
temp_password = (password_generator(first_name, last_name))