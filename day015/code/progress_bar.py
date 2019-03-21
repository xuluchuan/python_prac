import time
import progressbar

number_of_entry = 177
with progressbar.ProgressBar(max_value=number_of_entry) as bar:
    for i in range(number_of_entry):
        time.sleep(0.1)
        bar.update(i)
