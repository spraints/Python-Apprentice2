"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

# Create a window object
window = Tk()

# Hide the window, hint: use the withdraw method
window.withdraw()

# Ask the user for the first number   
nums = [simpledialog.askinteger(p, p) for p in ["first number", "second number", "ONE MORE NOW NOW NOW"]]
a, b, c = nums

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if c % 4 == 0:
    res = a + b
elif c % 4 == 1:
    res = a - b
elif c % 4 == 2:
    res = a * b
else:
    res = a // b

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
messagebox.showinfo("check it", f">>>>>>> {res} <<<<<<<<")

# Keep the window open
window.mainloop()