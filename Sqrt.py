from breezypythongui import EasyFrame
import math

class NumberFieldDemo(EasyFrame):
    """Computes and displays the square root of a number."""
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Number Field Demo")
        self.addLabel(text = "An integer",
                      row = 0, column = 0)
        self.inputField = self.addFloatField(value = 0.0,
                                            row = 0,
                                            column = 1,
                                            width = 10)
        self.addLabel(text = "Square Root",
                      row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0,
                                             row = 1,
                                             column = 1,
                                             width = 8,
                                             precision = 4,
                                             state = "readonly")
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2,
                       command = self.computeSqrt)

    def computeSqrt(self):
        """Inputs the integer and computes the square root."""
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)

if __name__ == "__main__":
    app = NumberFieldDemo()
    app.mainloop()
