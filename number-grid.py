from breezypythongui import EasyFrame

class CustomColorApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")
        self["background"] = "yellow"
        self.setResizable(False)
        
class LayoutDemo(EasyFrame):
    """Displays labes in the quadrants."""
    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0,
                      sticky = "NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1,
                      sticky = "NSEW")
        self.addLabel(text = "(1, 0 and 1)", row = 1, column = 0,
                      sticky = "NSEW", columnspan = 2)

if __name__ == "__main__":
    demo = LayoutDemo()
    demo.mainloop()
