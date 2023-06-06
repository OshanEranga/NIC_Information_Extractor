#import datetime module
import datetime

# Funtion for validating user input
def validate(nic : str) ->bool:
    if len(nic) != 12:
        return False
    else:
        return nic.isdigit()

# Function for identifying born year
def get_born_year(nic : str) ->int:
    year = int(nic[0:4])
    return year

# Get born date
def get_born_date(nic : str) -> datetime.date:
    born_days = int(nic[4:7])
    if born_days > 500:
        born_days -= 500
    year = get_born_year(nic)
    jan_first = datetime.date(year, 1, 1)
    born_date = jan_first + datetime.timedelta(days = born_days - 1)
    return born_date

#Get Gender of the people
def get_gender(nic :str) ->str:
    born_days = int(nic[4:7])
    if born_days > 500:
        return "Female"
    else:
        return "Male"


# Get the NIC number as a user input
nic_number = input("Please enter your NIC number : ")

# validate user input
if not validate(nic_number):
    print("Invalid NIC! Please check the number again.")
    exit(0)

# Identify the born year
born_year = get_born_year(nic_number)

# Calculate the exact born date
born_date = get_born_date(nic_number)

# Get gender
gender = get_gender(nic_number)

# Print the output 
iso_date = born_date.isoformat()
print("Your birthday :",iso_date)

dayname = born_date.strftime('%A')
print("Born day : ",dayname)

print("Gender :",gender)
