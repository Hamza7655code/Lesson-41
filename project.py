import tkinter as tk

def convert_inches_to_centimeters():
    try:
        inches_value = float(inches_entry.get())
        centimeters_value = inches_value * 2.54
        output_label.config(text=f"Length in cm: {centimeters_value:.2f}")
    except ValueError:
        output_label.config(text="Please enter a valid number")

main_window = tk.Tk()
main_window.title("Inches to Centimetres Converter")
main_window.geometry("300x200")

inches_label = tk.Label(main_window, text="Enter length in inches:")
inches_label.pack(pady=10)

inches_entry = tk.Entry(main_window)
inches_entry.pack(pady=5)

convert_btn = tk.Button(
    main_window,
    text="Convert",
    command=convert_inches_to_centimeters
)
convert_btn.pack(pady=10)

output_label = tk.Label(main_window, text="")
output_label.pack(pady=10)

main_window.mainloop()
