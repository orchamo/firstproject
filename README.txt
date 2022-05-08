the projects purpose is to allow adding removing and viewing costumers and books.
in addition to that you should be able to add loan books and return them.

the app is devided to three classes.
books:
id(PK)
Name
Author
Year
Type (1/2/3)

Costumers:
id(PK)
Name
City
Age

Loans:
CostumerID
BookID
LoanDate
ReturnDate

they are based on 3 different classes. each has its own functions to help manage the actions needed.


Each class has:
 __init__  ---   function to start the engine

create_db_table --- to create a table

execute_query --- to allow managing the querys on the sql databases

print_all_data --- to print all the tables data


**books** class has:

addBook --- to add a book

removeBook --- to remove a book


**costumer** class has:

addCostumer --- to add a book

removeCostumer --- to remove a book

