import tkinter as tk
from tkinter import StringVar, Toplevel, ttk
from turtle import title, width

from host_service import get_hosts
from networkdevice_service import add_networkdevice, get_networkdevices
from user_service import add_user, get_users


SERVICE_TICKET = 'NC-19-7661d50f182946278a7e-nbi'


def show_hosts(listBox):
    tempList = get_hosts(SERVICE_TICKET)
    for i, (name, ip, mac, interface) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, ip, mac, interface))


def show_network_devices(listBox):
    tempList = get_networkdevices(SERVICE_TICKET)
    for i, (hostname, platformId, managementIpAddress) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(
            i, hostname, platformId, managementIpAddress))


#UPDATE NOT WORKING
def show_users(listBox):
    tempList = get_users(SERVICE_TICKET)
    for i, (hostname, platformId, managementIpAddress) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(
            i, hostname, platformId, managementIpAddress))


def get_username(username_entry_text):
    return username_entry_text.get()


def get_password(password_entry_text):
    return password_entry_text.get()


def add_new_user():

    new_window = tk.Tk()
    new_window.title("Add new User!")
    new_window.geometry('1200x500')
    new_window.resizable(width=False, height=False)

    username_label = ttk.Label(new_window, text="Username:")
    username_label.pack(fill='none')
    username_entry_text = StringVar()
    username_entry = ttk.Entry(new_window, textvariable=username_entry_text)
    username_entry.pack(fill='none')

    password_label = ttk.Label(new_window, text="Password:")
    password_label.pack(fill='none')
    password_entry_text = StringVar()
    password_entry = ttk.Entry(new_window, textvariable=password_entry_text)
    password_entry.pack(fill='none', pady=5)

    user_button_create = tk.Button(new_window, text="Create", width=15, command=(
        lambda: add_user(SERVICE_TICKET, username_entry.get(), password_entry.get())))
    user_button_create.pack(fill='none')
    new_window.mainloop()


def load_hosts(show_hosts, tab1):
    tk.Label(tab1).grid(row=0, columnspan=5)
    cols = ('Index', 'Hostname', 'IP', 'MAC', 'Interface')
    listBox = ttk.Treeview(tab1, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    tk.Button(tab1, text="Update Hosts", width=15,
              command=show_hosts(listBox)).grid(row=4, column=0)
    tk.Button(tab1, text="Close", width=15, command=exit).grid(row=4, column=1)


def load_network_devies():
    tk.Label(tab2).grid(row=0, columnspan=4)
    cols = ('Index', 'hostname', 'platformId', 'managementIpAddress')
    listBox = ttk.Treeview(tab2, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    tk.Button(tab2, text="Update Devices", width=15,
              command=show_network_devices(listBox)).grid(row=4, column=0)
    tk.Button(tab2, text="Add", width=15,
              command=add_networkdevice).grid(row=4, column=1)
    tk.Button(tab2, text="Close", width=15, command=exit).grid(row=4, column=1)


def load_users():
    tk.Label(tab3).grid(row=0, columnspan=4)
    cols = ('Index', 'role', 'username', 'password')
    listBox = ttk.Treeview(tab3, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    tk.Button(tab3, text="Update Users", width=15,
              command=show_users(listBox)).grid(row=4, column=0)
    tk.Button(tab3, text="Add user", width=15,
              command=add_new_user).grid(row=4, column=1)
    tk.Button(tab3, text="Close", width=15, command=exit).grid(row=4, column=2)


app = tk.Tk()
app.title("API - Cisco")
app.configure(background='DimGray')
app.geometry('1200x500')
app.resizable(width=False, height=False)

note = ttk.Notebook(app)

tab1 = tk.Frame(note)
tab2 = tk.Frame(note)
tab3 = tk.Frame(note)

note.add(tab1, text="Hosts", compound=tk.TOP)
note.add(tab2, text="Networkdevices")
note.add(tab3, text="Users")
note.pack(fill=tk.BOTH, expand=True)

load_hosts(show_hosts, tab1)
load_network_devies()
load_users()


app.mainloop()
