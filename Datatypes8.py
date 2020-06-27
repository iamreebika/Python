def remove_char(str, n):
      first_part = str[:n]
      last_pasrt = str[n+1:]
      return first_part + last_pasrt
print(remove_char('Nepali', 0))
print(remove_char('Nepali', 2))
print(remove_char('Nepali', 4))
