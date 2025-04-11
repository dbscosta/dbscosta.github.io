from pyscript import display
from pyscript import document
from datetime import datetime

def show_time(event):
    now = datetime.now()
    div_output = document.querySelector("#output")
    div_output.innerText = now.strftime("%Y/%d/%d, %H:%M:%S"))