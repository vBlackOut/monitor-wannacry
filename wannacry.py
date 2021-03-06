import Tkinter
from subprocess import Popen, PIPE
import time

def Draw(oldframe=None):
    frame = Tkinter.Frame(top,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    frame.pack()
    p = Popen(["python3", "/home/fc_dev/python/maps/crawler.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    status = p.returncode
    print status
    if status:
        text = Tkinter.Text(frame, height=10, width=32)
        text.insert(Tkinter.END, str(output))
        #text.highlight_pattern("word", "red")
        text.pack()
        text.tag_add("start", "1.0", "1.30")
        text.tag_config("start", background="black", foreground="yellow")
        text.tag_add("start-2", "3.0", "3.30")
        text.tag_config("start-2", background="black", foreground="yellow")
        text.tag_add("start-3", "5.0", "5.32")
        text.tag_config("start-3", background="black", foreground="yellow")
        text.tag_add("start-4", "7.0", "7.32")
        text.tag_config("start-4", background="black", foreground="yellow")
        text.tag_add("start-4", "9.0", "9.32")
        text.tag_config("start-4", background="black", foreground="yellow")
        if oldframe is not None:
            oldframe.destroy() # cleanup
        return frame
    else:
        return frame


def Refresher(frame=None):
    #print 'refreshing'
    frame = Draw(frame)
    frame.after(5000, Refresher, frame) # refresh in 10 seconds
    
top = Tkinter.Tk()
Refresher()
Tkinter.mainloop()
