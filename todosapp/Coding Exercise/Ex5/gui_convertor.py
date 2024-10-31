import FreeSimpleGUI as sg

sg.theme("LightGrey1")

error_output = sg.Text(key="error_output", text_color="red")
label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter Inches:")
input_inches = sg.Input(key="inches")

button_convert = sg.Button("Convert")
output_label = sg.Text(key="output")

exit_button = sg.Button('Exit')

window = sg.Window('Feet to Meters Convertor', layout=[[error_output], [label_feet, input_feet], [label_inches, input_inches], [button_convert, exit_button, output_label]])

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:  # Close the window if the user exits
        break

    if event == "Exit":
        break

    if event == "Convert":
        try:
            # Get the input values, converting them to floats
            feet = float(values["feet"])
            inches = float(values["inches"])

            # Calculate total inches
            height_in_meters = (feet * 0.3048) + (inches * 0.0254)

            # Display the result in a pop-up message
            window["output"].update(value="Height in meters: " + str(height_in_meters)[:4])

        except ValueError:
            window["error_output"].update(value="Please enter valid numbers for feet and inches.")  # Error handling

# Close the window
window.close()