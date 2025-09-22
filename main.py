from pyscript import document

def compute_average(event=None):
    # gets the values from input fields (if empty then 0)
    score1 = float(document.getElementById("score1").value or 0)
    score2 = float(document.getElementById("score2").value or 0)

    # computes the average of the two scores
    average = (score1 + score2) / 2

    # pass or fail 
    passed = "Yes" if average >= 75 else "No"

    # displays result
    result_div = document.getElementById("result")
    result_div.innerText = f"Average: {average:.2f}\nPassed?: {passed}"
