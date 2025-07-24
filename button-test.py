from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""
    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)
        self.label = self.addLabel(text = "Hello world!",
                                   row = 0, column = 0,
                                   columnspan = 2,
                                   sticky = "NSEW")
        self.clearBtn = self.addButton(text = "Clear",
                                       row = 1, column = 0,
                                       command = self.clear)
        self.restoreBtn = self.addButton(text = "Restore",
                                         row = 1, column = 1,
                                         state = "disabled",
                                         command = self.restore)
    def clear(self):
        """Clears the label and enables the Restore button."""
        self.label["text"] = ""
        self.restoreBtn["state"] = "normal"
        self.clearBtn["state"] = "disabled"

    def restore(self):
        """Restores the label text and disables the Restore button."""
        self.label["text"] = "Hello world!"
        self.restoreBtn["state"] = "disabled"
        self.clearBtn["state"] = "normal"

if __name__ == "__main__":
    app = ButtonDemo()
    app.mainloop()
