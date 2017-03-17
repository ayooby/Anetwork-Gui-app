from Tkinter import *
import requests

root = Tk()

# post data
def post_data():
    data = {
        'email': entry_email.get(),
        'name': entry_name.get(),
        'score': entry_score.get()
    }
    response = requests.post('http://norooz.anetwork.ir/OLDINGstorePHPFILE.php', data=data)
    if response.status_code == 200:
        text = Text(root, width=50, setgrid=0)
        text.grid(row=5, column=1)
        text.insert(INSERT, response.text)


# Labels
score_label = Label(text='Score: ')
score_label.grid(row=0)

name_label = Label(root, text='Name: ')
name_label.grid(row=1)

email_label = Label(root, text='Email: ')
email_label.grid(row=2)


# fields
entry_score = Entry(root)
entry_score.grid(row=0, column=1)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

entry_email = Entry(root)
entry_email.grid(row=2, column=1)


# Button
post_button = Button(root, text='Send Score', command=post_data)
post_button.grid(row=3)

# status bar
status_label = Label(root, text='results: ')
status_label.grid(row=4)

root.geometry('500x300')
root.mainloop()