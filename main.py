from pyscript import display, HTML
import js

def compute_average(event=None):
    # where values are inputted, default is 0
    score1 = float(js.document.getElementById("score1").value or 0)
    score2 = float(js.document.getElementById("score2").value or 0)

    # compute the average
    average = (score1 + score2) / 2

    # pass or fail
    status = "Passed" if average >= 75 else "Failed"

    # display result
    result_div = js.document.getElementById("result")
    result_div.innerHTML = ""  # clear previous result
    display(HTML(f"Average: {average:.2f} - {status}"), target="result")
