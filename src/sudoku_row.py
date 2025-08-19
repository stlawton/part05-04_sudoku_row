def row_correct(sudoku: list, row_no: int):
  row_size = len(sudoku[row_no]) # Store row size in variable
  number = 1
  while number <= row_size: # Iterate across row
    if number in sudoku[row_no]:
      if sudoku[row_no].count(number) > 1:
        return False
    number += 1
  return True

