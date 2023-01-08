import tkinter as tk


def calculate_bmi():
    # Get the height and weight from the input fields
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    # Convert the height to meters
    height_meters = height / 100

    # Calculate the BMI
    bmi = weight / (height_meters ** 2)

    # BMI ranges
    underweight = 18.5
    normalweight = 24.9
    overweight = 29.9
    obesity = 35
    severobesity = 36

    _underweight = "Underweight"
    _normalweight = "Normal weight"
    _overweight = "Overweight"
    _obesity = "Obesity"
    _severobesity = "Severe obesity"

    verdict = ""

    # Calculate verdict
    if bmi < underweight:
        verdict = _underweight
    elif bmi <= + normalweight:
        verdict = _normalweight
    elif bmi <= overweight:
        verdict = _overweight
    elif bmi <= obesity:
        verdict = _obesity
    else:
        verdict = _severobesity

    # Display the BMI in the result label
    result_label.config(text=f"Your BMI is: {bmi:.2f}")
    verdict_label.config(text=f"You are: {verdict}")


# Create a custom canvas widget that displays a gradient and text
class GradientCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calculate the BMI ranges
        underweight = 18.5
        normalweight = 24.9
        overweight = 29.9
        obesity = 35
        severobesity = 36

        # Calculate the positions of the data points
        self.underweight_pos = underweight / severobesity
        self.normalweight_pos = normalweight / severobesity
        self.overweight_pos = overweight / severobesity
        self.obesity_pos = obesity / severobesity

    def create_image(self):
        # Get the canvas size
        width, height = self.winfo_width(), self.winfo_height()

        # Create a blank image with the canvas size
        image = tk.PhotoImage(width=100, height=100)

        # Draw the gradient on the image
        for x in range(width):
            # Calculate the color based on the position
            pos = x / width
            if pos < self.underweight_pos:
                color = "#0000ff"  # Blue
            elif pos < self.normalweight_pos:
                color = "#00ff00"  # Green
            elif pos < self.overweight_pos:
                color = "#ffff00"  # Yellow
            elif pos < self.obesity_pos:
                color = "#ffa500"  # Orange
            else:
                color = "#ff0000"  # Red

            # Fill the image with the color
            image.put(color, (x, 0, x+1, height))

        # Draw the data on the image
        self.create_text((self.underweight_pos*width, height/2),
                         text="Underweight", anchor="s", fill="#0000ff")
        self.create_text((self.normalweight_pos*width, height/2),
                         text="Normal Weight", anchor="s", fill="#0000ff")
        self.create_text((self.overweight_pos*width, height/2),
                         text="Overweight", anchor="s", fill="#0000ff")
        self.create_text((self.obesity_pos*width, height/2),
                         text="Obesity", anchor="s", fill="#0000ff")

        # Return the image
        return image


# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack()

# Create the height and weight input fields
height_label = tk.Label(main_frame, text="Height (cm):")
height_label.grid(row=0, column=0)
height_entry = tk.Entry(main_frame)
height_entry.grid(row=0, column=1)

weight_label = tk.Label(main_frame, text="Weight (kg):")
weight_label.grid(row=1, column=0)
weight_entry = tk.Entry(main_frame)
weight_entry.grid(row=1, column=1)

# Create the calculate button
calculate_button = tk.Button(
    main_frame, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2)

# Create the result label
result_label = tk.Label(main_frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Create the verdict label
verdict_label = tk.Label(main_frame, text="")
verdict_label.grid(row=4, column=0, columnspan=2)

# Create the canvas widget
canvas = GradientCanvas(root)
canvas.pack()

root.mainloop()
