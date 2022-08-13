from tkinter import *
from tkinter import messagebox
import ben_crist
import Calculator


class GUI:
    """
    A class representing functions for a gui
    """

    def __init__(self, window, notebook) -> None:
        """
        Method to set up the gui window
        :param window: Default parameter for the window
        :param notebook: Default parameter for the notebook
        """
        # Code to set up the window, notebook, and all the tabs
        self.window = window
        self.notebook = notebook
        self.circle_tab = Frame(self.notebook)
        self.rectangle_tab = Frame(self.notebook)
        self.square_tab = Frame(self.notebook)
        self.triangle_tab = Frame(self.notebook)
        self.trapezoid_tab = Frame(self.notebook)
        self.ellipse_tab = Frame(self.notebook)
        self.power_tab = Frame(self.notebook)
        self.factorial_tab = Frame(self.notebook)
        self.sqrt_tab = Frame(self.notebook)
        self.notebook.add(self.circle_tab, text='Circle')
        self.notebook.add(self.rectangle_tab, text='Rectangle')
        self.notebook.add(self.square_tab, text='Square')
        self.notebook.add(self.triangle_tab, text='Triangle')
        self.notebook.add(self.trapezoid_tab, text='Trapezoid')
        self.notebook.add(self.ellipse_tab, text='Ellipse')
        self.notebook.add(self.power_tab, text='Power')
        self.notebook.add(self.factorial_tab, text='Factorial')
        self.notebook.add(self.sqrt_tab, text='Square Root')
        self.notebook.pack()

        # Code for the Circle Tab
        self.label_main_circle = Label(self.circle_tab, text='Calculate the Area of a Circle',
                                       font=('Arial', 15, 'bold'))
        self.label_circle = Label(self.circle_tab, text='Enter the Radius', font=('Arial', 20))
        self.entry_circle = Entry(self.circle_tab)
        self.label_circle_result_title = Label(self.circle_tab, text='The result is', font=50)
        self.label_circle_result = Label(self.circle_tab, text='', font=100)
        self.circle_button = Button(self.circle_tab, text='CALCULATE', font=50, command=self.circle)
        self.label_main_circle.pack(padx=75, pady=50)
        self.label_circle.pack()
        self.entry_circle.pack()
        self.circle_button.pack()
        self.label_circle_result_title.pack()
        self.label_circle_result.pack()

        # Code for the Rectangle Tab
        self.label_main_rectangle = Label(self.rectangle_tab, text='Calculate the Area of a Rectangle', font=('Arial',
                                                                                                              15,
                                                                                                              'bold'))
        self.label_rectangle_length = Label(self.rectangle_tab, text='Enter the Length', font=('Arial', 20))
        self.entry_rectangle_length = Entry(self.rectangle_tab)
        self.label_rectangle_width = Label(self.rectangle_tab, text='Enter the Width', font=('Arial', 20))
        self.entry_rectangle_width = Entry(self.rectangle_tab)
        self.rectangle_button = Button(self.rectangle_tab, text='CALCULATE', font=50, command=self.rectangle)
        self.label_rectangle_result_title = Label(self.rectangle_tab, text='The result is', font=50)
        self.label_rectangle_result = Label(self.rectangle_tab, text='', font=100)
        self.label_main_rectangle.pack(padx=75, pady=50)
        self.label_rectangle_length.pack()
        self.entry_rectangle_length.pack()
        self.label_rectangle_width.pack()
        self.entry_rectangle_width.pack()
        self.rectangle_button.pack()
        self.label_rectangle_result_title.pack()
        self.label_rectangle_result.pack()

        # Code for the Square Tab
        self.label_main_square = Label(self.square_tab, text='Calculate the Area of a Square',
                                       font=('Arial', 15, 'bold'))
        self.label_square = Label(self.square_tab, text='Enter the Length', font=('Arial', 20))
        self.entry_square = Entry(self.square_tab)
        self.label_square_result_title = Label(self.square_tab, text='The result is', font=50)
        self.label_square_result = Label(self.square_tab, text='', font=100)
        self.square_button = Button(self.square_tab, text='CALCULATE', font=50, command=self.square)
        self.label_main_square.pack(padx=75, pady=50)
        self.label_square.pack()
        self.entry_square.pack()
        self.square_button.pack()
        self.label_square_result_title.pack()
        self.label_square_result.pack()

        # Code for the Triangle Tab
        self.label_main_triangle = Label(self.triangle_tab, text='Calculate the Area of a Triangle', font=('Arial',
                                                                                                           15,
                                                                                                           'bold'))
        self.label_triangle_base = Label(self.triangle_tab, text='Enter the Base', font=('Arial', 20))
        self.entry_triangle_base = Entry(self.triangle_tab)
        self.label_triangle_height = Label(self.triangle_tab, text='Enter the Height', font=('Arial', 20))
        self.entry_triangle_height = Entry(self.triangle_tab)
        self.triangle_button = Button(self.triangle_tab, text='CALCULATE', font=50, command=self.triangle)
        self.label_triangle_result_title = Label(self.triangle_tab, text='The result is', font=50)
        self.label_triangle_result = Label(self.triangle_tab, text='', font=100)
        self.label_main_triangle.pack(padx=75, pady=50)
        self.label_triangle_base.pack()
        self.entry_triangle_base.pack()
        self.label_triangle_height.pack()
        self.entry_triangle_height.pack()
        self.triangle_button.pack()
        self.label_triangle_result_title.pack()
        self.label_triangle_result.pack()

        # Code for the Trapezoid Tab
        self.label_main_trapezoid = Label(self.trapezoid_tab, text='Calculate the Area of a Trapezoid', font=('Arial',
                                                                                                              15,
                                                                                                              'bold'))
        self.label_trapezoid_base1 = Label(self.trapezoid_tab, text='Enter the First Base', font=('Arial', 20))
        self.entry_trapezoid_base1 = Entry(self.trapezoid_tab)
        self.label_trapezoid_base2 = Label(self.trapezoid_tab, text='Enter the Second Base', font=('Arial', 20))
        self.entry_trapezoid_base2 = Entry(self.trapezoid_tab)
        self.label_trapezoid_height = Label(self.trapezoid_tab, text='Enter the Height', font=('Arial', 20))
        self.entry_trapezoid_height = Entry(self.trapezoid_tab)
        self.trapezoid_button = Button(self.trapezoid_tab, text='CALCULATE', font=50, command=self.trapezoid)
        self.label_trapezoid_result_title = Label(self.trapezoid_tab, text='The result is', font=50)
        self.label_trapezoid_result = Label(self.trapezoid_tab, text='', font=100)
        self.label_main_trapezoid.pack(padx=75, pady=50)
        self.label_trapezoid_base1.pack()
        self.entry_trapezoid_base1.pack()
        self.label_trapezoid_base2.pack()
        self.entry_trapezoid_base2.pack()
        self.label_trapezoid_height.pack()
        self.entry_trapezoid_height.pack()
        self.trapezoid_button.pack()
        self.label_trapezoid_result_title.pack()
        self.label_trapezoid_result.pack()

        # Code for the Ellipse Tab
        self.label_main_ellipse = Label(self.ellipse_tab, text='Calculate the Area of an Ellipse', font=('Arial',
                                                                                                         15,
                                                                                                         'bold'))
        self.label_ellipse_radius1 = Label(self.ellipse_tab, text='Enter the Horizontal Radius', font=('Arial', 20))
        self.entry_ellipse_radius1 = Entry(self.ellipse_tab)
        self.label_ellipse_radius2 = Label(self.ellipse_tab, text='Enter the Vertical Radius', font=('Arial', 20))
        self.entry_ellipse_radius2 = Entry(self.ellipse_tab)
        self.ellipse_button = Button(self.ellipse_tab, text='CALCULATE', font=50, command=self.ellipse)
        self.label_ellipse_result_title = Label(self.ellipse_tab, text='The result is', font=50)
        self.label_ellipse_result = Label(self.ellipse_tab, text='', font=100)
        self.label_main_ellipse.pack(padx=75, pady=50)
        self.label_ellipse_radius1.pack()
        self.entry_ellipse_radius1.pack()
        self.label_ellipse_radius2.pack()
        self.entry_ellipse_radius2.pack()
        self.ellipse_button.pack()
        self.label_ellipse_result_title.pack()
        self.label_ellipse_result.pack()

        # Code for the Power Tab
        self.label_main_power = Label(self.power_tab, text='Calculate the Power of a Number', font=('Arial',
                                                                                                    15,
                                                                                                    'bold'))
        self.label_power_num = Label(self.power_tab, text='Enter the Base Number', font=('Arial', 20))
        self.entry_power_num = Entry(self.power_tab)
        self.label_power_pow = Label(self.power_tab, text='Enter the Power the Base is Being Raised to',
                                     font=('Arial', 15))
        self.entry_power_pow = Entry(self.power_tab)
        self.power_button = Button(self.power_tab, text='CALCULATE', font=50, command=self.power)
        self.label_power_result_title = Label(self.power_tab, text='The result is', font=50)
        self.label_power_result = Label(self.power_tab, text='', font=100)
        self.label_main_power.pack(padx=75, pady=50)
        self.label_power_num.pack()
        self.entry_power_num.pack()
        self.label_power_pow.pack()
        self.entry_power_pow.pack()
        self.power_button.pack()
        self.label_power_result_title.pack()
        self.label_power_result.pack()

        # Code for the Factorial Tab
        self.label_main_factorial = Label(self.factorial_tab, text='Calculate the Factorial of a Number',
                                          font=('Arial', 15, 'bold'))
        self.label_factorial = Label(self.factorial_tab, text='Enter a Number', font=('Arial', 20))
        self.entry_factorial = Entry(self.factorial_tab)
        self.label_factorial_result_title = Label(self.factorial_tab, text='The resulting factorial is', font=50)
        self.label_factorial_result = Label(self.factorial_tab, text='', font=100)
        self.factorial_button = Button(self.factorial_tab, text='CALCULATE', font=50, command=self.factorial)
        self.label_main_factorial.pack(padx=75, pady=50)
        self.label_factorial.pack()
        self.entry_factorial.pack()
        self.factorial_button.pack()
        self.label_factorial_result_title.pack()
        self.label_factorial_result.pack()

        # Code for the Square Root tab
        self.label_main_sqrt = Label(self.sqrt_tab, text='Calculate the Square Root of a Number',
                                     font=('Arial', 15, 'bold'))
        self.label_sqrt = Label(self.sqrt_tab, text='Enter a Number', font=('Arial', 20))
        self.entry_sqrt = Entry(self.sqrt_tab)
        self.label_sqrt_result_title = Label(self.sqrt_tab, text='The resulting square root is', font=50)
        self.label_sqrt_result = Label(self.sqrt_tab, text='', font=100)
        self.sqrt_button = Button(self.sqrt_tab, text='CALCULATE', font=50, command=self.square_root)
        self.label_main_sqrt.pack(padx=75, pady=50)
        self.label_sqrt.pack()
        self.entry_sqrt.pack()
        self.sqrt_button.pack()
        self.label_sqrt_result_title.pack()
        self.label_sqrt_result.pack()

    def circle(self) -> None:
        """
        Method when the circle button is clicked
        """
        try:
            radius = int(self.entry_circle.get())
            self.entry_circle.delete(0, END)
            self.label_circle_result['text'] = ben_crist.circle(radius)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_circle_result['text'] = ''
            self.entry_circle.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_circle_result['text'] = ''
            self.entry_circle.delete(0, END)

    def rectangle(self) -> None:
        """
        Method when the rectangle button is clicked
        """
        try:
            length = int(self.entry_rectangle_length.get())
            width = int(self.entry_rectangle_width.get())
            self.entry_rectangle_length.delete(0, END)
            self.entry_rectangle_width.delete(0, END)
            self.label_rectangle_result['text'] = ben_crist.rectangle(length, width)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_rectangle_result['text'] = ''
            self.entry_rectangle_width.delete(0, END)
            self.entry_rectangle_length.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_rectangle_result['text'] = ''
            self.entry_rectangle_width.delete(0, END)
            self.entry_rectangle_length.delete(0, END)

    def square(self) -> None:
        """
        Method when the square button is clicked
        """
        try:
            length = int(self.entry_square.get())
            self.entry_square.delete(0, END)
            self.label_square_result['text'] = ben_crist.square(length)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_circle_result['text'] = ''
            self.entry_circle.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_circle_result['text'] = ''
            self.entry_circle.delete(0, END)

    def triangle(self) -> None:
        """
        Method when the triangle button is clicked
        """
        try:
            base = int(self.entry_triangle_base.get())
            height = int(self.entry_triangle_height.get())
            self.entry_triangle_base.delete(0, END)
            self.entry_triangle_height.delete(0, END)
            self.label_triangle_result['text'] = ben_crist.triangle(base, height)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_triangle_result['text'] = ''
            self.entry_triangle_height.delete(0, END)
            self.entry_triangle_base.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_triangle_result['text'] = ''
            self.entry_triangle_height.delete(0, END)
            self.entry_triangle_base.delete(0, END)

    def trapezoid(self) -> None:
        """
        Method when the trapezoid button is clicked
        """
        try:
            base1 = int(self.entry_trapezoid_base1.get())
            base2 = int(self.entry_trapezoid_base2.get())
            height = int(self.entry_trapezoid_height.get())
            self.entry_trapezoid_base1.delete(0, END)
            self.entry_trapezoid_base2.delete(0, END)
            self.entry_trapezoid_height.delete(0, END)
            self.label_trapezoid_result['text'] = ben_crist.trapezoid(base1, base2, height)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_trapezoid_result['text'] = ''
            self.entry_trapezoid_height.delete(0, END)
            self.entry_trapezoid_base1.delete(0, END)
            self.entry_trapezoid_base2.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_trapezoid_result['text'] = ''
            self.entry_trapezoid_height.delete(0, END)
            self.entry_trapezoid_base1.delete(0, END)
            self.entry_trapezoid_base2.delete(0, END)

    def ellipse(self) -> None:
        """
        Method when the ellipse button is clicked
        """
        try:
            radius1 = int(self.entry_ellipse_radius1.get())
            radius2 = int(self.entry_ellipse_radius2.get())
            self.entry_ellipse_radius1.delete(0, END)
            self.entry_ellipse_radius2.delete(0, END)
            self.label_ellipse_result['text'] = ben_crist.ellipse(radius1, radius2)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a numeric input')
            self.label_ellipse_result['text'] = ''
            self.entry_ellipse_radius1.delete(0, END)
            self.entry_ellipse_radius2.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a positive integer')
            self.label_ellipse_result['text'] = ''
            self.entry_ellipse_radius1.delete(0, END)
            self.entry_ellipse_radius2.delete(0, END)

    def power(self) -> None:
        """
        Method when the power button is clicked
        """
        try:
            num = int(self.entry_power_num.get())
            exponent = int(self.entry_power_pow.get())
            self.entry_power_num.delete(0, END)
            self.entry_power_pow.delete(0, END)
            self.label_power_result['text'] = Calculator.power(num, exponent)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a whole numeric input')
            self.label_power_result['text'] = ''
            self.entry_power_pow.delete(0, END)
            self.entry_power_num.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a whole positive integer')
            self.label_power_result['text'] = ''
            self.entry_power_pow.delete(0, END)
            self.entry_power_num.delete(0, END)

    def factorial(self) -> None:
        """
        Method when the factorial button is clicked
        """
        try:
            num = int(self.entry_factorial.get())
            self.entry_factorial.delete(0, END)
            self.label_factorial_result['text'] = Calculator.factorial(num)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a whole numeric input')
            self.label_factorial_result['text'] = ''
            self.entry_factorial.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a whole positive integer')
            self.label_factorial_result['text'] = ''
            self.entry_factorial.delete(0, END)

    def square_root(self) -> None:
        """
        Method when the sqrt button is clicked
        """
        try:
            num = int(self.entry_sqrt.get())
            self.entry_sqrt.delete(0, END)
            self.label_sqrt_result['text'] = Calculator.square_root(num)

        except TypeError:
            messagebox.showerror('ERROR!', 'Must enter a whole numeric input')
            self.label_sqrt_result['text'] = ''
            self.entry_sqrt.delete(0, END)
        except ValueError:
            messagebox.showerror('ERROR!', 'Must enter a whole positive integer')
            self.label_sqrt_result['text'] = ''
            self.entry_sqrt.delete(0, END)
