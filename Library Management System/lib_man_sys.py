import json
import re
# books = {
#     "Python Crash Course": {"author": "Eric Matthes", "copies": 5},
#     "JavaScript: The Good Parts": {"author": "Douglas Crockford", "copies": 3},
#     "Clean Code": {"author": "Robert C. Martin", "copies": 4},
#     "The Pragmatic Programmer": {"author": "Andrew Hunt", "copies": 2},
#     "Design Patterns": {"author": "Erich Gamma", "copies": 1},
#     "Design ": {"author": "Erich Gamma", "copies": 4},
#     "Learning Python": {"author": "Mark Lutz", "copies": 3},
# }


def search_by_title(titl):
    x = 0
    with open("lib_man_sys.json", "r") as f_tit:
        buks = json.load(f_tit)
        for tit, info in buks.items():
            if re.search(f"{titl}", tit, re.IGNORECASE):
                x = 1
                if info["copies"] > 0:
                    print(f"Title: {tit}, Author: {info['author']}, Copies Available: {info['copies']}")
                else:
                    print(f"Title: {tit}, Author: {info['author']}, Status: Not Available")
                
        if x == 0:
            print("This titled book isnt available")
        return x


def search_by_author(auther):
    x = 0
    with open("lib_man_sys.json", "r") as f_au:
        buks = json.load(f_au)
        for tit, info in buks.items():
            if re.search(f"{auther}", info["author"], re.IGNORECASE):
                x = 1
                if info["copies"] > 0:
                    print(f"Title: {tit}, Author: {info['author']}, Copies Available: {info['copies']}")
                else:
                    print(f"Title: {tit}, Author: {info['author']}, Status: Not Available")
        if x == 0:
            print("This Author's book isnt available")


def return_buk(retrn_book):
    with open("lib_man_sys.json", "r") as f_re:
        buk_fi = json.load(f_re)
        for tit, inf in buk_fi.items():
            if tit == retrn_book:
                inf["copies"] = inf["copies"] + 1
    with open("lib_man_sys.json", "w") as f_ret:
        json.dump(buk_fi, f_ret, indent=4)
    print("ThankYou💝,You have succesfully Returned")


def borrow_buk(borow_buk):
    with open("lib_man_sys.json", "r") as f_chus:
        buk_f = json.load(f_chus)
        for titl, info in buk_f.items():
            if titl == borow_buk:
                if info["copies"] > 0:
                    info["copies"] = info["copies"] - 1
                    print("ThankYou💝,You have succesfully Purchased")
                # else:
                #     print("sorry, no copies available.")        
    with open("lib_man_sys.json", "w") as f_choos:
        json.dump(buk_f, f_choos, indent=4)
    


# with open("lib_man_sys.json", "w") as f:
#     json.dump(books, f, indent=4)
while True:
    print("------------------------")
    print("Welcome to the library")
    print("1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit Library")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Value Must be in Number!")
        continue
    if choice == 1:
        search_type = input("Search by (1) Title or (2) Author? ")
        if search_type == "1":
            title = input("Enter book title: ")
            # with open("lib_man_sys.json", "r") as f:
            search_by_title(title)
        if search_type == "2":
            author = input("Enter Book Author name: ")
            search_by_author(author)
    if choice == 2:
        Borrow_book = input("What book do u want to buy?: ")
        x = search_by_title(Borrow_book)
        if x == 1:
            borrow_buk(Borrow_book)
    if choice == 3:
        return_book = input("What book do u want to return?: ")
        return_buk(return_book)

    if choice == 4:
        print("Thank You💝, Visit Again")
        break

    if choice >= 5:
        raise ValueError("Value Must be Less than 5")
