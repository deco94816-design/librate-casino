from storage import db

def check():
    deposits = db.get_pending_deposits()
    print("Pending Deposits for 7475151989:")
    for d in deposits:
        if str(d.get("user_id")) == "7475151989":
            print(d)
            
    print("Balance:")
    print(db.get_user_balance(7475151989))

if __name__ == "__main__":
    check()
