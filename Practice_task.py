import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

class App:
    def __init__(self, root):
        self.root=root
        self.root.title("Library App")
        self.root.geometry("500x500")

        self.library_csv=pd.read_csv("library.csv")

        self.name_label=tk.Label(text="Name: ")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry()
        self.name_entry.grid(row=0, column=1)

        self.author_label = tk.Label(text="Author: ")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry()
        self.author_entry.grid(row=1, column=1)

        self.ganre_label = tk.Label(text="Ganre: ")
        self.ganre_label.grid(row=2, column=0)
        self.ganre_entry = tk.Entry()
        self.ganre_entry.grid(row=2, column=1)

        self.year_label = tk.Label(text="Year: ")
        self.year_label.grid(row=3, column=0)
        self.year_entry = tk.Entry()
        self.year_entry.grid(row=3, column=1)

        self.amount_label = tk.Label(text="Amount: ")
        self.amount_label.grid(row=4, column=0)
        self.amount_entry = tk.Entry()
        self.amount_entry.grid(row=4, column=1)

        self.button_add=tk.Button(text="Add", command=self.add_book)
        self.button_add.grid(row=5, column=0)

        self.button_pie = tk.Button(text="Pie Chart", command=self.pie_chart)
        self.button_pie.grid(row=6, column=0)

        self.to_change = tk.Label(text="Find book to change: ")
        self.to_change.grid(row=7, column=0)
        self.to_cha_entry=tk.Entry()
        self.to_cha_entry.grid(row=7, column=1)

        self.change_book = tk.Button(text="Change book", command=self.change_book)
        self.change_book.grid(row=8, column=0)

        self.hist = tk.Button(text="Histogram", command=self.graph_chart)
        self.hist.grid(row=9, column=0)

        self.show_table = tk.Button(text="Show_table", command=self.show_table)
        self.show_table.grid(row=10, column=0)

        self.button_remove = tk.Button(text="remove", command=self.remove_book)
        self.button_remove.grid(row=11, column=0)

    def add_book(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        name = self.name_entry.get()
        a = self.author_entry.get()
        g = self.ganre_entry.get()
        y = self.year_entry.get()
        am = self.amount_entry.get()

        values = [name, a, g, y, am]
        new_row = ",".join(values) + "\n"

        with open("library.csv", "a") as file:
            file.write(new_row)


    def change_book(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        change_name = self.to_cha_entry.get()
        name = self.name_entry.get()
        a = self.author_entry.get()
        g = self.ganre_entry.get()
        y = self.year_entry.get()
        am = self.amount_entry.get()
        for i in range(len(self.library_csv)):
            if self.library_csv["name"] == change_name:
                self.library_csv["name"] = name
                self.library_csv["author"] = a
                self.library_csv["year"] = y
                self.library_csv["ganre"] = g
                self.library_csv["amount"] = am

        self.library_csv.to_csv("library.csv")

    def remove_book(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        name = self.name_entry.get()

        self.library_csv=self.library_csv[self.library_csv["name"]!=name]
        self.library_csv.to_csv("library.csv")

    def show_table(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        print(self.library_csv.to_str())
        tk.messagebox.showinfo("table in the console")

    def total_amount(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")

        total_amount=self.library_csv["amount"].sum()
        tk.messagebox.showindex(total_amount)

    def popular_ganre(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")

        ganre_amount = self.library_csv.groupby("ganre")["amount"].sum()
        popular=ganre_amount["amount"].idxmax()
        tk.messagebox.showindex(self.library_csv.loc[popular])

    def find_by_author(self):
        a = self.author_entry.get()
        y = self.year_entry.get()
        book_a=self.library_csv["name"==a]
        if book_a != None:
            tk.messagbox.showinfo(book_a)

        book_y = self.library_csv["year" == y]
        if book_y != None:
            tk.messagbox.showinfo(book_y)

    def pie_chart(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        ganre_amount = self.library_csv.groupby("ganre")["amount"].sum()
        plt.pie(ganre_amount)
        plt.title("Pie Chart")
        plt.show()

    def graph_chart(self):
        self.library_csv = pd.read_csv("library.csv", on_bad_lines="skip")
        year_amount = self.library_csv.groupby("year")["amount"].sum()
        plt.bar(year_amount[0], year_amount[1])
        plt.title("Pie Chart")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.show()



if __name__=="__main__":
    root=tk.Tk()
    app=App(root)
    root.mainloop()

