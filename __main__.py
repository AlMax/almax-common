from AlmaxGraphics import FrameManager as FM;
from AlmaxUtils import Time as AUT;
from AlmaxClasses import XmlManager as XM;
import tkinter as TK;

def AssignCommand(Button: TK.Button, index):
    match(index):
        case 0:
            #print("Data", calendarDate.get_date())
            print("Option", option.get())

def main():

    window = FM.Window("almax_common");

    global option;

    window.AddFrame("first", TK.NW);
    window.AddLabelToFrame("prova1", "first", TK.LEFT)
    window.AddTextToFrame("first", TK.LEFT)
    option = window.AddOptionButtonToFrame(
        [str(i) for i in range(0, 101)],
        "first", 
        TK.LEFT
    );

    global calendarDate;
    # calendarDate = window.AddCalendarToFrame(
    #    "first",
    #    TK.LEFT,
    #    showLabel=True,
    #    defaultDate=AUT.LastDayNameOccurence("friday")
    # );

    window.AddFrame("buttons", TK.S);
    window.AddButtonToFrame("Stampa", 0, AssignCommand, "buttons", TK.LEFT);

    window.Mainloop();

if __name__ == "__main__":
    main();
