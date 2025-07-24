from breezypythongui import EasyFrame

class CustomColorApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")
        self["background"] = "yellow"
        self.setResizable(False)

if __name__ == "__main__":
    app = CustomColorApp()
    app.mainloop()
