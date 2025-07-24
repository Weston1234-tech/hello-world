from breezypythongui import EasyFrame

class TextFieldDemo(EasyFrame):
    """Converts an input string to uppercase and displays the result."""
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Text Field Demo")
        self.addLabel(text = "Input", row = 0, column = 0)
        self.inputField = self.addTextField(text = "",
                                            row = 0,
                                            column = 1)
        self.addLabel(text = "Output", row = 1, column = 0)
        self.outputField = self.addTextField(text = "",
                                             row = 1,
                                             column = 1,
                                             state = "readonly")
        self.addButton(text = "Convert", row = 2, column = 0,
                       columnspan = 2, command = self.convert)

    def convert(self):
        """Inputs a string, converts to Uppercase, and outputs the result."""
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)

if __name__ == "__main__":
    app = TextFieldDemo()
    app.mainloop()
