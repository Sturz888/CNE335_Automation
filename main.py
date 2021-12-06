# This is the template code for the CNA337 Final Project
# Rick Sturza Rlsturza@student.rtc.edu
# based code templete furnished by Zachary Rubin zrubin@rtc.edu
# With tutoring from TJ Dewey
# With cooperation from Sarmad Kubba

# CNA 340 Fall 2020
from server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.11 by RickSturza")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    EC2 = Server("18.118.106.124")
    # TODO - Call Ping method and print the results
    Echo = EC2.ping()
    print(Echo)
