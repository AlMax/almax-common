from AlmaxUtils import Time as AUT;
import tkinter as TK;
import almax_graphics.managers.FrameManager as AMG;

def AssignCommand(Button: TK.Button, index):
    match(index):
        case 0:
            print("Data", calendarDate.get_date());

def main():
    window = AMG.Window("almax_common");

    window.AddFrame("first", TK.NW);
    window.AddLabelToFrame("prova1", "first", TK.LEFT);
    global calendarDate;
    calendarDate = window.AddCalendarToFrame(
        "first", 
        TK.LEFT, 
        showLabel=True,
        defaultDate=AUT.LastDayNameOccurence("friday")
    );

    window.AddFrame("buttons", TK.S);
    window.AddButtonToFrame("Stampa", 0, AssignCommand, "buttons", TK.LEFT);

    window.Mainloop();

if __name__ == "__main__":
    main();