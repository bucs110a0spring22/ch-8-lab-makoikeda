class StringUtility:
  def __init__(self, string):
    self.string = string
  
  def __str__(self):
    obj_str = str(self.string)
    return obj_str

  #Part B
    
  def vowels(self):
    count = 0
    vowels = "aeiou"
    for char in self.string:
      if char in vowels:
        count += 1
    if count >= 5:
      return "many"
    return str(count)
    
  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
      new_string = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    return new_string
    
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    else:
      first_char = self.string[0]
      rest_char = self.string[1:]
      new_string = first_char
      for char in rest_char:
        if char == first_char:
          new_string += '*'
        else:
          new_string += char
      return new_string
    
  def asciiSum(self):
    sum = 0
    for char in self.string:
      sum += ord(char)
    return sum
    
  
    
  def cipher(self):
  
    new_string = ''
    shift_value = len(self.string)
    shift_value = shift_value % 26 
    for char in self.string:
      if char >= 'a' and char <= 'z': 
        if ord(char) + shift_value > ord(
                          'z'): 
          shifting_from_beginning = (shift_value -
                                                 (ord('z') - ord(char) + 1))
          new_char_ascii_value = ord('a') + shifting_from_beginning
          new_char = chr(new_char_ascii_value)
          new_string += new_char
        else:
          new_char_ascii_value = ord(char) + shift_value
          new_char = chr(new_char_ascii_value)
          new_string += new_char
      elif char >= 'A' and char <= 'Z':  
        if ord(char) + shift_value > ord(
                          'Z'):  
          shifting_from_beginning = (shift_value -
                                                 (ord('Z') - ord(char) + 1))
          new_char_ascii_value = ord('A') + shifting_from_beginning
          new_char = chr(new_char_ascii_value)
          new_string += new_char
        else:
          new_char_ascii_value = ord(char) + shift_value
          new_char = chr(new_char_ascii_value)
          new_string += new_char
      else: 
          new_string += char
    return new_string
