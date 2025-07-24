from breezypythongui import EasyFrame

class CounterDemo (EasyFrame):
    """Illustrates the use of a counter with an instance variable."""
    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Counter Demo")
        self.setSize(200, 75)
        self.count = 0
        self.label = self.addLabel(text = "0",
                                   row = 0, column = 0,
                                   sticky ="NSEW",
                                   columnspan = 2)
        self.addButton(text = "Next",
                       row = 1, column = 0,
                       command = self.next)
        self.addButton(text = "Reset",
                       row = 1, column = 1,
                       command = self.reset)

    def next(self):
            """Increments teh count and updates display."""
            self.count += 1
            self.label["text"] = str(self.count)

    def reset(self):
        """Resets the count ot 0 and updates the display."""
        self.count = 0
        self.label["text"] = str(self.count)

if __name__ == "__main__":
    app = CounterDemo()
    app.mainloop()
