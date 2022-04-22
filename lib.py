from tkinter import *
import io
from PIL import Image, ImageTk
import requests

class ucovid(object):
    def __init__(self):
        self._uciurl = "https://public.tableau.com/static/images/Ex/ExtDashBrd2021_22dv/COVIDdashboard/1.png"
        self._ocurl = "https://occovid19.ochealthinfo.com/coronavirus-in-oc"
        self._caurl = "https://covid19.ca.gov/state-dashboard/"
        self.root = Tk()
        self.getContext()
        self.root.mainloop()
    def getContext(self):
        imgraw = Image.open(io.BytesIO(requests.get(self._uciurl).content))
        box = (0, 0, 800, 800)
        img = ImageTk.PhotoImage(imgraw.crop(box))
        lol = Label(self.root, image=img)
        lol.img = img
        lol.pack()