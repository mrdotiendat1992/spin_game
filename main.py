from tkinter import *
import random

print(f"Spin game with tkinter library version {TkVersion} !!!")

class Main(Tk):
    '''
    Init window
    '''
    def __init__(self):
        super().__init__()

        #################
        ## Main Window ##
        #################

        self.config(background="white")
        self.title("Spin game")
        self.geometry("300x300")
        self.resizable(0, 0)

        #################
        ## Main Frame ##
        #################

        self.main_frame = Frame(self,background="white")
        self.main_frame.pack()

        ##################
        ## Number Frame ##
        ##################

        self.number_frame = Frame(self.main_frame,background="green")
        self.number_frame.pack()
        self.label1 = Label(self.number_frame, text="0", font=("Arial", 40), fg="red", bg="yellow", relief="sunken", anchor="center", width= 2, height= 1)
        self.label1.grid(row=0, column=1, padx=6, pady=6)
        self.label2 = Label(self.number_frame, text="0", font=("Arial", 40), fg="red", bg="yellow", relief="sunken", anchor="center", width= 2, height= 1)
        self.label2.grid(row=0, column=2, padx=6, pady=6 )
        self.label3 = Label(self.number_frame, text="0", font=("Arial", 40), fg="red", bg="yellow", relief="sunken", anchor="center", width= 2, height= 1)
        self.label3.grid(row=0, column=3, padx=6, pady=6 )
        
        self.label_groups = [self.label1, self.label2, self.label3]
        
        ##################
        ## Button Frame ##
        ##################

        self.button_frame = Frame(self.main_frame,background="white")
        self.button_frame.pack(padx=6, pady=6)
        self.button_start = Button(self.button_frame, text="START" ,command=self.start_spin, width=14, bg='blue', fg="white")
        self.button_start.grid(row=0, column=1,padx=6, pady=6)
        self.button_stop = Button(self.button_frame, text="STOP",  command=self.stop_update, width=14, bg='red', fg="white")
        self.button_stop.grid(row=0, column=2,padx=6, pady=6)

        ######################
        ## PLace coin Frame ##
        ######################
        
        self.coin_frame = Frame(
            self.main_frame, 
            bg="white"
        )
        self.coin_frame.pack(padx=6, pady=6)
        self.input_label = Label(
            self.coin_frame,bg="white",
            text="Place coin "
        )
        self.input_label.grid(row=0, column=0)
        self.input_coin = Entry(
            self.coin_frame, 
            text="0", 
            width=3, 
            font=("Arial", 15), 
            name="input_coin"
        )
        self.input_coin.grid(row=0, column=1)
        self.input_coin.focus()

        ##################
        ## X coin Frame ##
        ##################

        self.x_frame = Frame(self.main_frame)
        self.x_frame.pack(padx=6, pady=6)
        self.label_x = Label(
            self.x_frame, 
            text="x", 
            font=("Arial", 15), 
            bg="white",
            anchor="center",
            width= 1
        )
        self.label_x.grid(row=0, column=0 )

        ##################
        ## Result Frame ##
        ##################

        self.result_frame = Frame(self.main_frame)
        self.result_frame.pack()
        self.result_x = Label(
            self.x_frame, text="", 
            fg="green", 
            font=("Arial", 15), 
            bg="white", 
            relief="raised", 
            anchor="center", 
            width= 3
        )
        self.result_x.grid(row=0, column=1 )

        ##################
        ## Wallet Frame ##
        ##################

        # Get start coin
        self.current_coin = self.get_start_coin()        

        self.wallet_screen = Frame(self.main_frame, background="white")
        self.wallet_screen.pack()
        self.label_wallet = Label(
            self.wallet_screen, 
            text="Wallet ", 
            font=("Arial", 15), 
            relief="flat", 
            anchor="center",
            bg='white',
        )
        
        self.label_wallet.grid(row=0, column=1 )
        self.wallet = Label(
            self.wallet_screen, 
            text=str(self.current_coin), 
            font=("Arial", 20), 
            relief="raised", 
            anchor="center",
            bg='brown',
            fg="white"
        )
        self.wallet.grid(row=0, column=2 )

        ###################
        ## Message Frame ##
        ###################

        self.message_frame = Frame(self.main_frame)
        self.message_frame.pack()
        self.message = Label(self.message_frame, text="", bg="white", fg="red")
        self.message.pack(fill=X)

        # variable check update random number
        self.update_number = False

        # loop for display 
        self.mainloop()

    '''
    Start spin number
    '''
    def start_spin(self):
        # If can update number, start update number in 3 labels if have enough coin
        # else display message "You don't have enough coin"
        if not self.update_number:
            self.update_number = True
            self.result_x.config(text="")
            for label in self.label_groups:
                label.after(100, self.update_label, label)
            try:
                x = int(self.input_coin.get())
            except:
                x = 0
            next_current_coin = self.current_coin - x
            if next_current_coin < 0:
                self.update_number=False
                self.message.config(text="You don't have enough {0} coin !!!".format(x))
                return
            self.wallet.config(text=str(next_current_coin))
            self.current_coin = next_current_coin
        else:
            self.message.config(text="")

    '''
    Choose random integer from 0 to 9 and update to label
    '''
    def update_label(self, label):
        if not self.update_number:
            return
        label.config(text=str(random.randint(0, 9)))
        label.after(100, self.update_label, label)

    '''
    Stop spin number
    '''
    def stop_update(self):
        if self.update_number:
            self.update_number = False

            # get 3 number from label
            number1 = int(self.label1.cget("text"))
            number2 = int(self.label2.cget("text"))
            number3 = int(self.label3.cget("text"))

            # check double number, calculate x_coin win
            if number1 == number2 == number3:
                x_coin = 100
            elif number1 == number2 or number1 == number3 or number2 == number3:
                x_coin = 10
            else:
                x_coin = 0

            self.result_x.config(text=str(x_coin))

            try:
                x = int(self.input_coin.get())
            except:
                x = 0

            # calculate result coin in wallet, set all label text
            if x_coin != 0:
                next_current_coin = self.current_coin + x_coin * x
                self.wallet.config(text=str(next_current_coin))
                self.current_coin = next_current_coin
                self.message.config(text="You won {0} coins!".format(x_coin * x))
                self.result_x.config(bg='green', fg='white')
            else:
                self.message.config(text="You lost {0} coins!".format(x))
                self.result_x.config(bg='red', fg='white')
        else:
            self.message.config(text="")

    '''
    Get random start coin from 100 to 1000
    '''
    def get_start_coin(self):
        return random.randint(100, 1000)
    

if __name__ == "__main__":
    Main()
