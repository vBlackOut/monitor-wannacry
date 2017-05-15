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
        text = Tkinter.Text(frame, height=5, width=30)
        text.insert(Tkinter.END, str(output))
        text.pack()

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
