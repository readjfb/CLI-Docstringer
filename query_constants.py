INDENT = "    "

FUNC_EXAMPLE = f'''# Create clear, detailed, high quality docstrings including a detailed summary for the following functions:

def add_binary(a, b):
{INDENT}binary_sum = bin(a+b)[2:]
{INDENT}return binary_sum
"""
{INDENT}Returns the sum of two decimal numbers in binary digits. It can only use
{INDENT}numbers such that a+b >= 0

{INDENT}Parameters:
{INDENT}{INDENT}a (int): A decimal integer
{INDENT}{INDENT}b (int): Another decimal integer

{INDENT}Returns:
{INDENT}{INDENT}binary_sum (str): Binary string of the sum of a and b
"""

def __init__(num1, num2, num3=0):
{INDENT}self.num1 = num1
{INDENT}self.num2 = num2
{INDENT}self.num3 = num3
{INDENT}self.sum_num = num1 + num2 + num3
"""
{INDENT}Creates a new object to hold a collection of numbers.

{INDENT}Parameters:
{INDENT}{INDENT}num1 (float): First decimal float
{INDENT}{INDENT}num2 (float): Second decimal float
{INDENT}{INDENT}num3 (float) (default=0): A decimal float
{INDENT}{INDENT}sum_num (float): Sum of numbers inside the object

{INDENT}Returns:
{INDENT}{INDENT}None
"""

def multiplier(n, m=1):

{INDENT}return m*n
"""
{INDENT}Returns the value of n times m, to be used as a multiplication function

{INDENT}Parameters:
{INDENT}{INDENT}n (int or float): A value to be multiplied
{INDENT}{INDENT}m (int or float) (default=1): A second value to be multiplied

{INDENT}Returns:
{INDENT}{INDENT}(float): m times n
"""

def sum_of_digits(n):
{INDENT}other=12
{INDENT}s = 0
{INDENT}while n > 0:
{INDENT}{INDENT}s, n = s + n%10, n//10
{INDENT}return s
"""
{INDENT}Returns the sum of the digits of an integer number using numerical ops.

{INDENT}Parameters:
{INDENT}{INDENT}n (int): An integer number

{INDENT}Returns:
{INDENT}{INDENT}s (int): The sum of the digits of n
"""
'''


CLASS_EXAMPLE = f'''# Create clear, detailed, high quality docstrings for the following classes:

### CLASS BEGIN ###
@dataclass
class Student:
{INDENT}name: str = None
{INDENT}age: int = None
{INDENT}grade: int = None
{INDENT}teacher: str = None

### DOCSTRING BEGIN ###
"""
A dataclass to represent a student.

Attributes:
{INDENT}name (str):
{INDENT}{INDENT}Name of the student
{INDENT}age (int):
{INDENT}{INDENT}Age of the student
{INDENT}grade (int):
{INDENT}{INDENT}Current grade of the student
{INDENT}teacher (str):
{INDENT}{INDENT}Student's teacher
"""

### CLASS BEGIN ###
class ComplexNumber:
{INDENT}def __init__(self, r=0, i=0):
{INDENT}{INDENT}self.real = r
{INDENT}{INDENT}self.imag = i
{INDENT}{INDENT}self.quadrant = None

{INDENT}def get_data(self):
{INDENT}{INDENT}print(self.real, + '+' + self.imag + 'i')

### DOCSTRING BEGIN ###
"""
A class to hold a single complex number of the form `real` + `imag`i.

Attributes:
{INDENT}real (int or float):
{INDENT}{INDENT}Real component of the number
{INDENT}imag (int or float):
{INDENT}{INDENT}Imaginary compoent coefficient the number
{INDENT}quadrant (int):
{INDENT}{INDENT}The quadrant of the complex number in the imaginary plane

Methods:
{INDENT}__init__(self, r=0, i=0)
{INDENT}{INDENT}Creates a new complex number object

{INDENT}get_data(self)
{INDENT}{INDENT}Returns a well formatted string of the complex number in the
{INDENT}{INDENT}form `real` + `imag`i
"""

### CLASS BEGIN ###
class ImageHolder(pygame.sprite.Sprite):
{INDENT}def __init__(self, file_path):
{INDENT}{INDENT}pygame.sprite.Sprite.__init__(self)
{INDENT}{INDENT}self.file_path = file_path
{INDENT}{INDENT}self.image = pygame.image.load(file_path)
{INDENT}{INDENT}self.rect = self.image.get_rect()

### DOCSTRING BEGIN ###
"""
A class to hold a single pygame image, inheriting from pygame.sprite.Sprite

Attributes:
{INDENT}file_path (str):
{INDENT}{INDENT}Filepath of the image
{INDENT}image (pygame.image)
{INDENT}{INDENT}Pygame image of the file at file_path
{INDENT}rect (int):
{INDENT}{INDENT}The manipulatable object of the image
"""
'''
