def row_correct(sudoku: list, row_no: int):
  row_size = len(sudoku[row_no]) # Store row size in variable
  checked_numbers = [] # Empty list to store numbers that have already been checked
  number = 1
  while number <= row_size: # Iterate across row
    if number in sudoku[row_no]:
      if checked_numbers.count(number) > 0:
        return False
      else:
        checked_numbers.append(number)
      number += 1
    else:
      return False
  return True
