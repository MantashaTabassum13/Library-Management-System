members={}
books={}
books_quantity={}
print("-----------------------------------------------")
print("----- Welcome to ITECH5403 Library System -----")
print("-----------------------------------------------")
while(True):
    print("Main Menu - please select an option: ")
    print("1) Add new member")
    print("2) Add new book")
    print("3) Process borrowing")
    print("4) Process returning")
    print("5) View member status")
    print("6) View book status")
    print("7) Quit")
    #choice given by user
    ch=int(input(""))
    if ch<0 and ch>7:
        print("Value must be between 1 and 7. Please try again:")
    if ch==1:
        while(True):
            print("Adding a new member:")
            member_name=input("Please enter a new member name:")
            member_id=1001
            if len(members)>0:
                member_id=list(members)[-1]+1
            members[member_id] = member_name
            print("Member ",members[member_id], "has been created with member ID: ",member_id)
            btao=input("Would you like to [a]dd a new member or go-[b]ack to the previous menu? ")
            if btao=="b":
                break
    if ch==2:
        while(True):
            print("Adding new book:")
            member_id = 1001

            book_title=input("Please enter a new book title:")
            if book_title in books.values():
                print("Book already exists:")
                print("Book ID: ",book_id)
                print("Book Title",book_title)
                print("Number of copies",books_quantity )
                break
            book_id = 1001
            if (len(books) > 0):
                book_id = list(books)[-1] + 1
            books[book_id] = book_title
            books_quantity = int(input("Enter the number of copies"))
            print("New book added")
            print("Book ID: ", str(book_id))
            print("Book Title ",book_title )
            print("Number of copies ", books_quantity)
            print(books)
            print("book [" + book_title + "] has been added with book ID: " + str(book_id)+" with quanity",books_quantity)
            sub_opt = input("Would you like to [a]dd a new book or go-[b]ack to the previous menu? ")
            if (sub_opt == "b"):
                break

    if ch==3:
        while (True):
            member_id=input("Please enter a valid member ID:")
            while(True):
                if member_id in members:
                    book_id=input("Please enter a valid book ID for borrowing by member ", member_id)
                    while(True):
                        if book_id in books:
                            print("Nothing")
                else:
                    print("Member does not exist.")






