from AlmaxGraphics import FrameManager as FM;
from AlmaxUtils import Time as AUT;
from AlmaxClasses import XmlManager as XM;
import tkinter as TK;

window = FM.Window("almax_common")
i = 0;
total = TK.StringVar(value="0")
def AssignCommand(Button: TK.Button, index):
    match(index):
        case 0:
            global i
            # i = i + 1;
            # window.AddFrame(i, TK.NW)
            # window.AddLabelToFrame("prova1", i, TK.LEFT)
            # window.AddTextToFrame(i, TK.LEFT)
            # option = window.AddOptionButtonToFrame(
            #    [str(i) for i in range(0, 101)], i, TK.LEFT
            # )
            # print("Data", calendarDate.get_date())
            total.set(30)
            print("Option", option.get())

def main():
    global option;

    window.AddFrame("first", TK.NW);
    window.AddLabelToFrame(total, "first", TK.LEFT)
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
