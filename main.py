from AlmaxGraphics import FrameManager as FM;
import tkinter as TK;

def main():
    window = FM.Window("almax_common");

    window.AddFrame("first", TK.NW);
    window.AddLabelToFrame("prova1", "first", TK.LEFT);
    window.AddCalendarToFrame("first", TK.LEFT);

    window.Mainloop();


if __name__ == "__main__":
    main();