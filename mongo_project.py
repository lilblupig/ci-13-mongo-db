# Import dependencies
import os
import pymongo

# Import sensitive data
if os.path.exists("env.py"):
    import env


# Establish variables for database connection
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    """Connect to MongoDB"""
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    """Show the menu for CRUD operations in the terminal"""
    print("")
    print("1: Add a record")
    print("2: Find a record by name")
    print("3: Edit a record")
    print("4: Delete a record")
    print("5: Exit menu")

    option = input("Enter option: ")
    return option


def get_record():
    """Helper function for Read, Update and Delete functions"""
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error: no results found")

    return doc


def add_record():
    """Function called when option 1 chosen in the menu"""
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower()
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    """Uses result of helper function get_record() to find document"""
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def main_loop():
    """Define what to do when each option pressed"""
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

main_loop()
