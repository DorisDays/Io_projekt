try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk
import datetime
import time
#import sys
#import os

class MAIN_MENU():
    def __init__(self):
        self.m_menu = tk.Tk()   #new window - main menu of "Parkomat"
        self.m_menu.title('Parkomat')

        self.m_menu.withdraw() #hide the window

        self._start = tk.Toplevel(self.m_menu)
        # window dimensions will be set as 600x600

        self.screen_height = self.m_menu.winfo_screenheight()
        self.screen_width = self.m_menu.winfo_screenwidth()
        self.start_coord_x = (self.screen_width / 2) - (600 / 2) #
        self.start_coord_y = (self.screen_height / 2) - (500/ 2)
        self._start.geometry("%dx%d+%d+%d" % (600, 500, self.start_coord_x, self.start_coord_y))

        self._start.resizable(False, False) #to not change window dimensions

        self._start.config(bg="gray75")  # color of main menu window

        self.purchase()   #create frame ticket_buying
        self._purchase.withdraw()   #cancel frame ticket_buying al-l frames below are made in similar way
        self.prices()
        self._prices.withdraw()
        self.keyboard()
        self._keyboard.withdraw()
        self.popup()
        self._popup.withdraw()
        self.ticket()
        self._ticket.withdraw()

        #Labels with type of machine and actual time
        self.start_label_0 = tk.Label(master=self._start, text="PARKOMAT", bg="gray75", font="Arial 40")
        self.start_label_1 = tk.Label(master=self._start, text="DATE:", bg="gray75", font="Arial 25")

        #Placement of labels in m_menu window
        self.start_label_0.place(relx=.5, rely=.20, anchor="center")
        self.start_label_1.place(relx=.5, rely=.75, anchor="center")

        #Buttons for available options
        self.start_button_0 = tk.Button(master=self._start, text="PRICES", command=lambda: self.open_prices(),
                                       width=32, pady=60, height=2, bg="PaleGreen2")
        self.start_button_1 = tk.Button(master=self._start, text="BUY THE TICKET", command=lambda: self.open_purchase(),
                                       width=32, pady=60, height=2, bg="papaya whip")

        #Placement of buttons
        self.start_button_0.place(relx=.3, rely=.50, anchor="center")
        self.start_button_1.place(relx=.7, rely=.50, anchor="center")

        #Placing the actual time function
        self.start_label_2 = tk.Label(master=self._start, text="")
        self.start_label_2.place(relx=.5, rely=.87, anchor="center")
        self.update_clock_start()

        self.m_menu.mainloop()

    def open_purchase(self):
        self._start.withdraw()
        self._purchase.deiconify()

    def close_purchase(self):
        #clean the window
        self.purchase_entry_0.delete(0, 'end')
        self.purchase_entry_1.delete(0, 'end')
        self.purchase_entry_2.delete(0, 'end')
        self._purchase.withdraw()   #hide the ticket buying window
        app0.end()

        self._start.deiconify() #recalling the m_menu window

    def open_prices(self):
        self._prices.grab_set()     #block m_menu window under window prices
        self._prices.deiconify()    #recall the prices window

    def close_prices(self):
        self._prices.withdraw()     #hide the prices window
        self._prices.grab_release() #unlock window under window prices

    def open_popup(self, error):
        self._popup.grab_set() #block window under window prices
        self.text_error = error
        self.popup_label_0.config(text=self.text_error, font='Arial 12', bg="gray75")
        self._popup.deiconify() #recall window under window prices

    def close_popup(self):
        self._popup.withdraw() #hide prices window
        self._popup.grab_release()  #recall window under prices window

    def open_keyboard(self):
        self.purchase_entry_1.delete(0, tk.END)
        self._purchase.withdraw()
        self._keyboard.deiconify()

    def close_keyboard(self):
        self.keyboard_entry_1.delete(0, 'end') #clean the window
        self._keyboard.withdraw()     #hide the keyboard
        self._purchase.deiconify() #recall purchase window

    def update_clock_start(self):
        t=time.strftime('%A %Y-%m-%d\n%H:%M:%S')
        if(t!=''):
            self.start_label_2.config(text=t,font='Arial 25', bg="gray75")
        self._start.after(100,self.update_clock_start)

    def update_clock_window2(self):
        t=time.strftime('%A %Y-%m-%d %H:%M:%S')
        if(t!=''):
            self.purchase_label_1.config(text=t,font='Arial 15', bg="gray75")
        self._purchase.after(100,self.update_clock_window2)

    def open_ticket(self):
        try:
            self.registration_number = self.purchase_entry_1.get()

            if (self.registration_number == ""):
                raise (Wrong_data_error("ERROR: LACK OF REGISTRATION NUMBER"))
            self.paid_price = self.purchase_entry_3.get()

            if (self.paid_price == ""):
                raise (Wrong_data_error("ERROR: PAYMENT IS NOT DONE"))
            self.departure_time = self.purchase_entry_0.get()

            if (self.departure_time == ""):
                raise (Wrong_data_error("ERROR: BAD DEPARTURE TIME"))
            self.teraz = datetime.datetime.now().strftime('%a %Y-%m-%d %H:%M:%S')
            self.ticket_label_1.config(text=self.registration_number, font='Arial 15', bg="gray75")
            self.ticket_label_3.config(text=self.teraz, font='Arial 15', bg="gray75")
            self.ticket_label_5.config(text=self.departure_time, font='Arial 15', bg="gray75")
            self.ticket_label_7.config(text=self.paid_price, font='Arial 15', bg="gray75")
            self._purchase.withdraw() #hide the ticket window
            self._ticket.deiconify()

        except Wrong_data_error as error:
            self.open_popup(error.message)

    def close_ticket(self):
        #clean the window
        self.purchase_entry_0.delete(0, 'end')
        self.purchase_entry_1.delete(0, 'end')
        self.purchase_entry_2.delete(0, 'end')
        self.purchase_entry_3.delete(0, 'end')
        app0.end()
        self._ticket.withdraw() #hide the ticket window
        self._start.deiconify() #recall start window

    def show_departure_time(self):
        self.departure_time = app0.return_departure_time()
        t = self.departure_time.strftime('%a %Y-%m-%d %H:%M:%S')
        self.purchase_entry_0.delete(0, tk.END)
        self.purchase_entry_0.insert(tk.END, t)

    def show_account(self):
        self.account=app0.return_account()
        self.purchase_entry_3.delete(0, tk.END)
        self.account=str(self.account)+"zl"
        self.purchase_entry_3.insert(tk.END,self.account)

    def throw_coin(self):
        self.cash=self.purchase_entry_2.get()
        app0.add_coin(self.cash,self)
        self.show_departure_time()
        self.show_account()
        self.purchase_entry_2.delete(0, tk.END)

    def purchase(self):
        self._purchase = tk.Toplevel(self.m_menu)
        self.purchase_coord_x=(self.screen_width/2)-(600/2)
        self.purchase_coord_y=(self.screen_height/2)-(600/2)
        self._purchase.geometry("%dx%d+%d+%d" % (600,600, self.purchase_coord_x, self.purchase_coord_y))
        self._purchase.config(bg="gray75")
        self._purchase.resizable(False,False)   #to not change window dimensions

        #BACK BUTTON
        self.purchase_button_0 = tk.Button(master = self._purchase, text="BACK", command=lambda: self.close_purchase(),bg="coral", width=14, height=1)
        self.purchase_button_0.place(relx=.85,rely=0.94,anchor="center")

        #TIME
        self.purchase_label_0 = tk.Label(master = self._purchase, text="TIME:", font="Arial 15", bg="gray75")
        self.purchase_label_0.place(relx=0.5, rely=0.05, anchor="center")

        #TICKET TIME VALIDITY
        self.purchase_label_2 = tk.Label(master = self._purchase, text="DEPARTURE TIME:", font="Arial 15", bg="gray75")
        self.purchase_label_2.place(relx=0.5, rely=0.78, anchor="center")
        self.purchase_entry_0 = tk.Entry(master=self._purchase, font="times 15")
        self.purchase_entry_0.place(width=240, height=25, relx=.5, rely=.84, anchor="center")
        self.purchase_entry_0.bind("<Key>", lambda x: "break")

        #REGISTRATION NUMBER
        self.purchase_label_3 = tk.Label(master = self._purchase, text="REGISTRATION NUMBER", font="Arial 15", bg="gray75")
        self.purchase_label_3.place(relx=0.30, rely=0.22, anchor="center")

        self.purchase_entry_1 = tk.Entry(master=self._purchase, font="times 15", justify='center')
        self.purchase_entry_1.place(width=180, height=25, relx=.75, rely=.22, anchor="center")
        self.purchase_entry_1.bind("<Key>", lambda x: "break")

        self.purchase_button_0 = tk.Button(master=self._purchase, text="TYPE YOUR REGISTRATION NUMBER:", command=lambda: self.open_keyboard(), bg="seashell", height=1, width=40)
        self.purchase_button_0.place(relx=.5,rely=.30,anchor="center")

        #THROWING A COIN
        self.purchase_label_4 = tk.Label(master = self._purchase, text="THROW A COIN", font="Arial 15", bg="gray75")
        self.purchase_label_4.place(relx=0.5, rely=0.39, anchor="center")

        self.purchase_entry_2 = tk.Entry(master=self._purchase, font="times 15", justify="center")
        self.purchase_entry_2.place(width = 240, height=25, relx=.4, rely=.52, anchor="center")

        self.purchase_button_1 = tk.Button(master=self._purchase, text="THROW A COIN", command=lambda: self.throw_coin(), bg="seashell", width=14)
        self.purchase_button_1.place(relx=.70,rely=0.52,anchor="center")

        #PRICES
        self.purchase_button_2 = tk.Button(master=self._purchase, text="PRICES", command=lambda: self.open_prices(), bg="PaleGreen2", width=14)
        self.purchase_button_2.place(relx=.5,rely=0.45,anchor="center")

        #PAYMENT
        self.purchase_label_5 = tk.Label(master = self._purchase, text="PAYMENT", font="Arial 15", bg="gray75")
        self.purchase_label_5.place(relx=0.5, rely=0.63, anchor="center")

        self.purchase_entry_3 = tk.Entry(master=self._purchase, font="times 15", justify="center")
        self.purchase_entry_3.place(width=150, height=25, relx=.5, rely=.68, anchor="center")
        self.purchase_entry_3.bind("<Key>", lambda x: "break")

        #CONFIRM PURCHASE
        self.purchase_button_3 = tk.Button(master=self._purchase, text="CONFIRM", command=lambda: self.open_ticket(), bg="Green", width=14, height=1)
        self.purchase_button_3.place(relx=.15, rely=0.94, anchor="center")

        #RETURN MONEY
        self.purchase_button_4 = tk.Button(master=self._purchase, text="RETURN MONEY", bg="seashell", width=18, height=1)
        self.purchase_button_4.place(relx=.5,rely=0.94,anchor="center")

        #SHOW CLOCK
        self.purchase_label_1 = tk.Label(master = self._purchase, text="")
        self.update_clock_window2()
        self.purchase_label_1.place(relx=.5, rely=.12, anchor="center")

        # metoda potrzebna do przycisku zatwierdz w metodzie klawiatura

    def confirm(self):
        try:
            self.zawartosc0 = self.keyboard_entry_1.get()
            if (self.zawartosc0 == ""):
                raise (Wrong_data_error("ERROR: REGISTRATION NUMBER WINDOW IS EMPTY"))
            app0.set_registration_number(self.zawartosc0)
            self.close_keyboard()
            self.purchase_entry_1.insert(tk.END, self.zawartosc0)
        except Wrong_data_error as error:
            self.open_popup(error.message)

    def choose(self,value):
        if value == 'BACK':
            self.zawartosc1 = self.keyboard_entry_1.get()
            k=len(self.zawartosc1)-1
            self.keyboard_entry_1.delete(k, tk.END)
        else:
            self.keyboard_entry_1.insert(tk.END,value)

    # FRAME WITH KEYBOARD
    def keyboard(self):
        self._keyboard = tk.Toplevel(self.m_menu)
        self.keyboard_coord_x = (self.screen_width / 2) - (380 / 2)
        self.keyboard_coord_y = (self.screen_height / 2) - (480 / 2)
        self._keyboard.geometry("%dx%d+%d+%d" % (380, 480, self.purchase_coord_x, self.purchase_coord_y))
        self._keyboard.config(bg="gray75")
        self._keyboard.resizable(False, False)

        #TYPE REGISTRATION NUMBER
        self.keyboard_label_1 = tk.Label(master=self._keyboard, text="TYPE YOUR REGISTRATION NUMBER",
                                          bg="gray75", font="Arial 12")
        self.keyboard_label_1.grid(row=2, column=2, columnspan=3, padx=10)

        #REGISTRATION NUMBER WINDOW
        self.keyboard_entry_1 = tk.Entry(master=self._keyboard, font=("Arial", 15), state="normal")
        self.keyboard_entry_1.bind("<Key>", lambda x: "break")
        self.keyboard_entry_1.grid(row=3, column=2, columnspan=3, pady=10)

        #CONFIRM REGISTRATION NUMBER
        self.keyboard_button_1 = tk.Button(master=self._keyboard, width=9, height=1, text="CONFIRM",
                                            command=lambda: self.confirm(), bg="Green")
        self.keyboard_button_1.grid(row=4, column=2, columnspan=3, pady=15)

        #KEYBOARD
        self._buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'W', 'R', 'S', 'T',
                         'U', 'W', 'V', 'X', 'Y', 'Z', 'DEL', '•', '-']
        self.rowx = 5
        self.columnx = 2

        #CREATING BUTTONS
        for button in self._buttons:
            # self.command = lambda x=button: self.choose(x)
            self.keyboard_button = tk.Button(master=self._keyboard, text=button,
                                                 command=lambda x=button: self.choose(x), bg="seashell",
                                                 width=9, height=1)
            self.keyboard_button.grid(row=self.rowx, column=self.columnx)
            if (self.columnx < 4):
                self.columnx = self.columnx + 1
            else:
                self.rowx = self.rowx + 1
                self.columnx = 2

        # RETURN TO PURCHASE BUTTON
        self.keyboard_button_return = tk.Button(master=self._keyboard, text="BACK",
                                                    command=lambda: self.close_keyboard(), bg="seashell",
                                                    width=9, height=1)
        self.keyboard_button_return.grid(row=self.rowx + 1, column=2, pady=15)

    #PRICES
    def prices(self):
        self._prices = tk.Toplevel(self.m_menu)
        self.prices_coord_x=(self.screen_width/2)-(500/2)
        self.prices_coord_y=(self.screen_height/2)-(300/2)
        self._prices.geometry("%dx%d+%d+%d" % (500,300, self.prices_coord_x, self.prices_coord_y))
        self._prices.config(bg="seashell")
        self._prices.resizable(False,False)

        self.prices_label_0 = tk.Label(master=self._prices, text="PRICES", bg="seashell", font="Arial 25")
        self.prices_label_0.place(relx=.5, rely=.1, anchor="center")

        self.prices_label_5 = tk.Label(master=self._prices, text="Park time is respectively\n scaled based on the amount you payed\n for a certain hour type!", bg="seashell", font="Arial 10")
        self.prices_label_5.place(relx=.5, rely=.35, anchor="center")

        self.prices_label_1 = tk.Label(master=self._prices, text="FIRST HOUR - 2zł", bg="seashell", font="Arial 10")
        self.prices_label_1.place(relx=.5, rely=.55, anchor="center")

        self.prices_label_2 = tk.Label(master=self._prices, text="SECOND HOUR - 4zł:", bg="seashell", font="Arial 10")
        self.prices_label_2.place(relx=.5, rely=.65, anchor="center")

        self.prices_label_3 = tk.Label(master=self._prices, text="THIRD HOUR - 5zł", bg="seashell", font="Arial 10")
        self.prices_label_3.place(relx=.5, rely=.75, anchor="center")

        #BACK
        self.prices_button = tk.Button(master = self._prices, text="BACK", command=lambda: self.close_prices() ,bg="coral", width=40, height=2)
        self.prices_button.place(relx=.5, rely=0.9, anchor="center")

    def popup(self):
        #FAIL FRAME
        self._popup = tk.Toplevel(self.m_menu)
        self.popup_coord_x=(self.screen_width/2)-(200/2)
        self.popup_coord_y=(self.screen_height/2)-(200/2)
        self._popup.geometry("%dx%d+%d+%d" % (600,200, self.popup_coord_x, self.popup_coord_y))
        self._popup.config(bg="gray75")
        self._popup.resizable(False,False)

        #FAIL
        self.popup_label_0 = tk.Label(master=self._popup,text="")
        self.popup_label_0.place(relx=.5, rely=.3, anchor="center")

        #FAIL BUTTON
        self.popup_button_0 = tk.Button(master = self._popup, text="OK!", command=lambda: self.close_popup() ,bg="Green", width=20, height=2)
        self.popup_button_0.place(relx=.5, rely=0.55, anchor="center")

    #TICKET FRAME
    def ticket(self):
        self._ticket = tk.Toplevel(self.m_menu)
        self.ticket_coord_x=(self.screen_width/2)-(600/2)
        self.ticket_coord_y=(self.screen_height/2)-(600/2)
        self._ticket.geometry("%dx%d+%d+%d" % (600,600, self.ticket_coord_x, self.ticket_coord_y))
        self._ticket.config(bg="gray75")
        self._ticket.resizable(False,False)

        #TICKET
        self.ticket_label_0 = tk.Label(master=self._ticket, text="REGISTRATION NUMBER: ", bg="gray75", font="Arial 15 ")
        self.ticket_label_0.place(relx=.5, rely=.1, anchor="center")

        self.ticket_label_1 = tk.Label(master=self._ticket,text="")
        self.ticket_label_1.place(relx=.5, rely=.2, anchor="center")

        self.ticket_label_2 = tk.Label(master=self._ticket, text="TICKET GRT TIME:", bg="gray75", font="Arial 15")
        self.ticket_label_2.place(relx=.5, rely=.3, anchor="center")

        self.ticket_label_3 = tk.Label(master=self._ticket,text="")
        self.ticket_label_3.place(relx=.5, rely=.4, anchor="center")

        self.ticket_label_4 = tk.Label(master=self._ticket, text="DEPARTURE TIME:", bg="gray75", font="Arial 15")
        self.ticket_label_4.place(relx=.5, rely=.5, anchor="center")

        self.ticket_label_5 = tk.Label(master=self._ticket,text="")
        self.ticket_label_5.place(relx=.5, rely=.6, anchor="center")

        self.ticket_label_6 = tk.Label(master=self._ticket, text="PAID SUM:", bg="gray75", font="Arial 15")
        self.ticket_label_6.place(relx=.5, rely=.7, anchor="center")

        self.ticket_label_7 = tk.Label(master=self._ticket,text="")
        self.ticket_label_7.place(relx=.5, rely=.8, anchor="center")

        self.ticket_button_0 = tk.Button(master = self._ticket, text="OK!", command=lambda: self.close_ticket() ,bg="gray75", width=20, height=2)
        self.ticket_button_0.place(relx=.5, rely=0.9, anchor="center")

class Parkomat:

    def __init__(self):
        #CLASS DATA:
        self.gr1 = 0
        self.gr2 = 0
        self.gr5 = 0
        self.gr10 = 0
        self.gr50 = 0
        self.zl1 = 0
        self.zl2 = 0
        self.zl5 = 0
        self.list_last_throwing_coins = []
        self.account = 0
        self.teraz = ""
        self.park_date = ""
        self.departure_time = ""
        self.park_time = ""
        self.registration_number = ""
        self._strefa_poczatek = 8
        self._strefa_koniec = 20
        self.i = 0

    def end(self):
        pass

    #CHECK IF DAY IS NOT WEEKEND DAY
    def it_is_weekend(self):
        self.week_day=self.teraz.weekday()
        if(self.week_day>4):
            self.teraz,=self.teraz+datetime.timedelta(days = (7-self.week_day))

    #CHECK IF DAY IS NOT WEEKEND DAY
    def is_departure_time_weekend(self):
        self.week_day=self.departure_time.weekday()
        if(self.week_day>4):
            self.departure_time=self.departure_time+datetime.timedelta(days = (7-self.week_day))

    #RETURN ACCOUNT STATE
    def return_account(self):
        return self.account

    #RETURN DEPARTURE TIME
    def return_departure_time(self):
        return self.departure_time

    #SET REGISTRATION NUMBER
    def set_registration_number(self, nr):
        self.registration_number = nr

    def end(self):
        self.account = 0
        self.teraz = ""
        self.park_date = ""
        self.departure_time = ""
        self.park_time = ""
        self.registration_number = ""

        #ADD CASH TO ACCOUNT AND TIME
    def add_coin(self, cash, klasa):
        #CHECK IF PARKOMAT IS NOT OVERFLAWED
        try:
            if (cash == "1gr"):
                if (self.gr1 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN"))
                self.account = self.account + 0.01
                self.gr1 = self.gr1 + 1
            elif (cash == "2gr"):
                if (self.gr2 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN" ))
                self.account = self.account + 0.02
                self.gr2 = self.gr2 + 1
            elif (cash == "5gr"):
                if (self.gr5 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN"))
                self.account = self.account + 0.05
                self.gr5 = self.gr5 + 1
            elif (cash == "10gr"):
                if (self.gr10 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN" ))
                self.account = self.account + 0.1
                self.gr10 = self.gr10 + 1
            elif (cash == "50gr"):
                if (self.gr50 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN" ))
                self.account = self.account + 0.5
                self.gr50 = self.gr50 + 1
            elif (cash == "1zl"):
                if (self.zl1 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN"))
                self.account = self.account + 1
                self.zl1 = self.zl1 + 1
            elif (cash == "2zl"):
                if (self.zl2 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN"))
                self.account = self.account + 2
                self.zl2 = self.zl2 + 1
            elif (cash == "5zl"):
                if (self.zl5 == 200):
                    raise (Wrong_data_error("ERROR: PARKOMAT IS OVERFLOVED, PLEASE THROW OTHER COIN"))
                self.account = self.account + 5
                self.zl5 = self.zl5 + 1
            elif (cash == "10zl"):
                self.account = self.account + 10
            elif (cash == "20zl"):
                self.account = self.account + 20
            elif (cash == "50zl"):
                self.account = self.account + 50
            else:
                raise (Wrong_data_error("ERROR: PARKOMAT DOES NOT SUPPORT SUCH NOMINAL "))
        except Wrong_data_error as error: klasa.open_popup(error.message)

        #CLEAR VARIABLES RESPONSIBLE FOR SET UP DEPARTURE DATE
        self.hours=0
        self.minutes=0
        #self.i=0
        self.h=0
        self.m=0
        self.tmp=0
        self.departure_time=""
        self.teraz=datetime.datetime.now()
        self.departure_time=self.teraz


        #CHECK IF ACTUAL DAY IS NOT WEEKEND
        self.it_is_weekend()

        #CHECK IF DAY IS NOT BEFOR STREF IS STARTING
        if(self.teraz.hour<self._strefa_poczatek):
            self.teraz=self.teraz+datetime.timedelta(hours=-(self.teraz.hour))+datetime.timedelta(hours=(self._strefa_poczatek))
            self.teraz=self.teraz+datetime.timedelta(minutes=-(self.teraz.minute))
        if(self.teraz.hour>=self._strefa_koniec):
            self.teraz=self.teraz+datetime.timedelta(hours=-(self._strefa_koniec-self._strefa_poczatek))
            self.teraz=self.teraz+datetime.timedelta(days=1)

        #CHECK IF IT IS 3RD OUR OR MORE
        if(self.account-11<0):
            if(self.account-6<0):
                #IF LESS THAN HOUR
                if(self.account-2<0):
                    self.h=0
                    self.tmp=(self.account % 2)
                    self.m=((self.tmp/2.0)*60.0)
                    self.departure_time=self.teraz+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)
                    self.is_departure_time_weekend()
                    if(self.departure_time.hour>=self._strefa_koniec):
                        self.h=(self.teraz.hour+self.h)-self._strefa_koniec
                        self.m=(self.teraz.minute+self.m)
                        self.departure_time=self.departure_time.replace(hour=self._strefa_poczatek, minute=0)
                        self.departure_time=self.departure_time+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)+datetime.timedelta(days=1)
                        self.is_departure_time_weekend()
                #(1,2)
                else:
                    self.h=1
                    self.tmp=(self.account-2) % 4
                    self.m=((self.tmp/4.0)*60.0)
                    self.departure_time=self.teraz+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)
                    self.is_departure_time_weekend()
                    if(self.departure_time.hour>=self._strefa_koniec):
                        self.h=(self.teraz.hour+self.h)-self._strefa_koniec
                        self.m=(self.teraz.minute+self.m)
                        self.departure_time=self.departure_time.replace(hour=self._strefa_poczatek, minute=0)
                        self.departure_time=self.departure_time+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)+datetime.timedelta(days=1)
                        self.is_departure_time_weekend()
            #(2,3)
            else:
                self.h=2
                self.tmp=(self.account-6) % 5
                self.m=(self.tmp/5.0)*60.0
                self.departure_time=self.teraz+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)
                self.is_departure_time_weekend()
                if(self.departure_time.hour>=self._strefa_koniec):
                    self.h=(self.teraz.hour+self.h)-self._strefa_koniec
                    self.m=(self.teraz.minute+self.m)
                    self.departure_time=self.departure_time.replace(hour=self._strefa_poczatek, minute=0)
                    self.departure_time=self.departure_time+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)+datetime.timedelta(days=1)
                    self.is_departure_time_weekend()
        #(3,inf.)
        else:
            self.h=3+((self.account-11)/5)
            self.tmp=(self.account-11) % 5
            self.m=(self.tmp/5.0)*60.0
            self.departure_time=self.teraz+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)
            self.is_departure_time_weekend()
            if(self.departure_time.hour>=self._strefa_koniec):
                self.h=(self.teraz.hour+self.h)-self._strefa_koniec
                self.m=(self.teraz.minute+self.m)
                self.departure_time=self.departure_time.replace(hour=self._strefa_poczatek, minute=0)
                self.departure_time=self.departure_time+datetime.timedelta(hours=self.h)+datetime.timedelta(minutes=self.m)+datetime.timedelta(days=1)
                self.is_departure_time_weekend()


# CLASS Wrong_data_error INHERITS AFTER CLASS EXCEPTION (WRONG INPUT OF DATA ARE TRECOGNIZED AS ERROR)
class Wrong_data_error(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return (repr(self.message))


#OBJECT OF CLASS PARKOMAT
app0 = Parkomat()
app1 = MAIN_MENU()
app0.set_target(app1)