'''
 # Utility functions that is used for the main driver
 # and other class that requires a specific display functions.
'''

# Imports
import re, Customer as cust, Beautician as beau, Treatment as treat, Package as packg, Service as serv

'''-------------------------------------------------------------------- PREDEFINED OBJECT LIST SECTION --------------------------------------------------------------------'''
def predefined_beautician():
    beautician_list = [     # These are fake names, phone number, address and don't waste your time searching :^)
        beau.Beautician('BEAU001', 'Natalie', 'Wong', '01-JAN-2017', 'Hair Care', '014-6558315', 'No.42, Taman Bersatu, Putatan', 88200, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU002', 'Cherry', 'Yee', '24-JAN-2017', 'Hair Care', '012-6554892', 'No.55, Taman Walnutwood, Penampang', 88400, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU003', 'Michelle', 'Yeo', '15-FEB-2017', 'Skin Care', '011-2334587', 'No.02, Taman Perkasa, Penampang', 87600, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU004', 'Mary', 'Ann', '18-FEB-2017', 'Skin Care', '010-4557895', 'No.57, Taman Johor, Kepayan', 88500, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU005', 'Sophia', 'Bella', '20-FEB-2017', 'Skin Care', '016-5668794', 'No.20, Taman Johor, Kepayan', 88100, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU006', 'Isabella', 'Skylar', '20-FEB-2017', 'Body Care', '014-6558315', 'No.38, Taman New Lintas, Lintas', 88450, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU007', 'Grace', 'Ella', '22-FEB-2017', 'Body Care', '012-5679826', 'No.17, Taman Jones, Kelombong', 88450, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU008', 'Emily', 'Liang', '25-FEB-2017', 'Bridal makeup specialist', '012-5685465', 'No.34, Taman Margarets, Kelombong', 89250, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU009', 'Elsa', 'Anna', '05-MAR-2017', 'Bridal makeup specialist', '014-6897453', 'No.25, Taman Kurnia Jata, Likas', 89850, 'Kota Kinabalu', 'Sabah'),
        beau.Beautician('BEAU010', 'Charlotte', 'Esther', '08-MAR-2017', 'Bridal makeup specialist', '016-6897456', 'No.75, Taman Marlborough, Kingfisher', 88554, 'Kota Kinabalu', 'Sabah')
    ]

    # Return the beautician_list
    return beautician_list

def predefined_customer():
    customer_list = [       # These are fake names, phone number, address and don't waste your time searching :^)
        cust.Customer('CUST0001', 'Sammy', 'Wong', '02-JAN-2017', '014-6557896', 'No.11, Taman Nanas, Putatan', 88200, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0002', 'Jessy', 'Smith', '02-JAN-2017', '012-8778865', 'No.35, Taman Bunga, Penampang', 88300, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0003', 'Lilly', 'Mayson', '05-JAN-2017', '011-5658974', 'No.64, Taman Iramanis, Kelombong', 88220, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0004', 'Kelly', 'Benderson', '12-JAN-2017', '012-6523496', 'No.23, Taman Kepayan, Penampang', 88500, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0005', 'Sonia', 'Junior', '22-FEB-2017', '016-6234896', 'No.34, Taman Chofu, Jalan Lintas', 88230, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0006', 'Shelly', 'Wong', '15-FEB-2017', '014-0556482', 'No.12, Taman Bunga Raja, Putatan', 86130, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0007', 'Jessie', 'Chen', '22-FEB-2017', '016-2347896', 'No.56, Taman Epal, Putatan', 88240, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0008', 'Bell', 'Ng', '02-MAR-2017', '016-2223568', 'No.90, Taman Air, Penampang', 88300, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0009', 'Lela', 'Tan', '12-MAY-2017', '012-2657896', 'No.56, Taman Choi Sin, Kelombong', 88300, 'Kota Kinabalu', 'Sabah'),
        cust.Customer('CUST0010', 'Fiona', 'Chen', '13-APR-2017', '014-2465879', 'No.54, Taman Nanas, Putatan', 87400, 'Kota Kinabalu', 'Sabah')
    ]

    # Return the customer_list
    return customer_list

def predefined_treatment():
    treatment_list = [
        treat.Treatment('HC001', 'Hair Blow Dry (45 mins)', 50.00, True),
        treat.Treatment('HC002', 'Hair Straightening (60 mins)', 80.00, True),
        treat.Treatment('HC003', 'Loreal Nourishing Hair Spa - Up to Waist (60 Mins)', 120.00, False),
        treat.Treatment('HC004', 'Loreal Nourishing Hair Spa - Below Waist (75 Mins)', 140.00, False),
        treat.Treatment('SC005', 'Express Fruit Clean-Up (45 Mins)', 150.00, False),
        treat.Treatment('SC006', 'Advance (Acne) (60mins)', 100.00, False),
        treat.Treatment('SC007', 'Instant Radiance Facial (60 Mins)', 200.00, False),
        treat.Treatment('SC008', 'Natural De-Tan Face (30 Mins)', 100.00, False),
        treat.Treatment('BC009', 'Full Body Massage (Deep Tissue) - (60 mins)', 180.00, False),
        treat.Treatment('BC010', 'Head, Neck & Shoulder Massage (30 mins)', 60.00, True),
        treat.Treatment('BC011', 'Aroma Manicure (45 mins)', 50.00, True),
        treat.Treatment('BC012', 'Aroma Pedicure (45 mins)', 50.00, True),
        treat.Treatment('BS013', 'Bridal - Hair Upstyle & Make-up (Wedding day & Dinner night)', 2000.00, False),
        treat.Treatment('BS014', 'Flower Girl - Hair Upstyle & Make-up (Wedding day only)', 1500.00, False)
    ]

    # Return the treatment_list
    return treatment_list

def predefined_package(treatment_list):
    package_list = [
        packg.Package('PK001', 'Skin Luxury', 250.00, treatment_list[5], treatment_list[6]),
        packg.Package('PK002', 'Relaxation Indulgence', 200.00, treatment_list[8], treatment_list[10]),
        packg.Package('PK003', 'Hair Essentials (Women)', 80.00, treatment_list[0], treatment_list[1]),
        packg.Package('PK004', 'Woman\'s Big Day', 3200.00, treatment_list[12], treatment_list[13])
    ]

    # Return the package_list
    return package_list

def predefined_service(customer_list, beautician_list, treatment_list, package_list):
    service_list = [
        serv.Service('APT00001', '05-JAN-2017', 1500.00, customer_list[0], beautician_list[9], treatment_list[13], False),
        serv.Service('APT00002', '08-JAN-2017', 80.00, customer_list[5], beautician_list[1], package_list[2], False),
        serv.Service('APT00003', '10-FEB-2017', 100.00, customer_list[1], beautician_list[4], treatment_list[5], False),
        serv.Service('APT00004', '20-FEB-2017', 250.00, customer_list[1], beautician_list[4], package_list[1], False),
        serv.Service('APT00005', '13-MAR-2017', 140.00, customer_list[0], beautician_list[1], treatment_list[3], False),
        serv.Service('APT00006', '15-APR-2017', 250.00, customer_list[0], beautician_list[3], package_list[0], False),
        serv.Service('APT00007', '20-JUN-2017', 120.00, customer_list[2], beautician_list[0], treatment_list[2], False),
        serv.Service('APT00008', '25-JUN-2017', 0.00, customer_list[5], beautician_list[0], treatment_list[0], True),
        serv.Service('APT00009', '25-JUN-2017', 0.00, customer_list[3], beautician_list[1], treatment_list[1], True),
        serv.Service('APT00010', '25-JUN-2017', 0.00, customer_list[4], beautician_list[6], treatment_list[9], True),
        serv.Service('APT00011', '22-JUL-2017', 100.00, customer_list[4], beautician_list[4], treatment_list[7], False),
        serv.Service('APT00012', '22-JUL-2017', 3200.00, customer_list[3], beautician_list[9], package_list[3], False)
    ]

    # Return the service_list
    return service_list

'''-------------------------------------------------------------------- LOGIN/MENU SECTION --------------------------------------------------------------------'''
# Company logo header
def company_logo_header():
    print('=' * 60)
    print('|' + ('~' * 58) + '|')
    print('|' + (' ' * 11) + 'Everlove Home Service Beauty Parlour' + (' ' * 11) + '|')
    print('|' + ('~' * 58) + '|')
    print('=' * 60)
    print()

# System main screen display
def system_main_screen():
    print('~' * 30)
    print(('=' * 6) + ' Main Menu Screen ' + ('=' * 6))
    print('~' * 30)
    print('1. Login\n' +
          '2. Exit program\n' +
          ('~' * 30))
    choice = input('Enter choice: ')

    while not (re.match('^[12]$', choice)):
        print('Invalid input choice, please try again with only 1 or 2 as input choice.\n')
        choice = input('Enter choice: ')

    return choice

# Login modules
def login():
    #Initialization
    login_success = False

    #Print login headers
    print()
    print('~' * 27)
    print(('=' * 10) + ' LOGIN ' + ('=' * 10))
    print('~' * 27)

    #Begin login
    while not login_success:
        login_id = input('Login ID: ')
        password = input('Password: ')

        if (not login_id == 'manager123' or not password == 'manager123456789') and (not login_id == 'staff123' or not password == 'staff123456789'):
            print('Invalid login ID or password, please try again or contact the system support staff.\n')
            login_success = False
        else: login_success = True

    #Return statement
    return 1 if (login_id == 'manager123' and password == 'manager123456789') else 0

# System main menu display
def system_main_menu():
    print()
    print('~' * 31)
    print(('=' * 10) + ' Main Menu ' + ('=' * 10))
    print('~' * 31)
    print('1. New Service\n' +
          '2. Registration\n' +
          '3. Display Records\n' +
          '4. Log out\n' +
          ('~' * 31))
    choice = input('Enter choice: ')

    while not (re.match('^[1234]$', choice)):
        print('Invalid input, please try again with only range from 1 to 4 as input.\n')
        choice = input('Enter choice: ')

    return choice

# Registration menu
def registration_menu():
    print()
    print('~' * 39)
    print(('=' * 10) + ' Registration Menu ' + ('=' * 10))
    print('~' * 39)
    print('1. Register new Cusotmer\n' +
          '2. Register new Beautician\n' +
          '3. Register new Treatment\n' +
          '4. Register new Package\n' +
          '5. Back to main menu\n' +
          ('~' * 39))
    choice = input('Enter choice: ')

    while not (re.match('^[12345]$', choice)):
        print('Invalid input choice, please try again with only range from 1 to 5 as input\n')
        choice = input('Enter choice: ')

    return choice

# Staff records menu
def staff_records_menu():
    print()
    print('~' * 38)
    print(('=' * 8) + ' Records Menu (Staff) ' + ('=' * 8))
    print('~' * 38)
    print('1. Display treatment list\n' +
          '2. Display package list\n' +
          '3. Display customer member list\n' +
          '4. Display beautician list\n' +
          '5. Check appointment date\n' +
          '6. Return to main menu\n' +
          ('~' * 38))
    choice = input('Enter choice: ')

    while not (re.match('^[123456]$', choice)):
        print('Invalid input choice, please try again with only range from 1 to 6 as input\n')
        choice = input('Enter choice: ')

    return choice

# Manager records menu
def manager_records_menu():
    print()
    print('~' * 48)
    print(('=' * 12) + ' Records Menu (Manager) ' + ('=' * 12))
    print('~' * 48)
    print('1. Display customer treatment transaction\n' +
          '2. Display appointments records\n' +
          '3. Display bridal service report\n' +
          '4. Check beautician\'s treatment records\n' +
          '5. Display trial service records\n' +
          '6. Display treatment list\n' +
          '7. Display package list\n' +
          '8. Display customer member list\n' +
          '9. Display beautician list\n' +
          '10. Return to main menu\n' +
          ('~' * 48))
    choice = input('Enter choice: ')

    while not (re.match('^([123456789]|[1][0])$', choice)):
        print('Invalid input choice, please try again with only range from 1 to 10 as input\n')
        choice = input('Enter choice: ')

    return choice

'''-------------------------------------------------------------------- OUTPUT/REPORT SECTION --------------------------------------------------------------------'''
# Service notes
def new_service_notes():
    print('\n\n============================ NOTES =============================\n' +
          '1. If a customer bring along extra member and registers for any\n' +
          'ervices enjoys additional discount as shown in the table below\n\n' +
          'he FIRST customer to register for a service must be the referer\n' +
          '(The customer that brought extra members)\n\n' +
          '--------------------------------------------\n' +
          '|      No. of members      | Discount Rate |\n' +
          '|--------------------------|---------------|\n' +
          '| More than or equals 5    |      15%      |\n' +
          '| More than or equals to 10|      30%      |\n' +
          '| More than  10            |      50%      |\n' +
          '--------------------------------------------\n\n' +
          '2. Free trials are only available during the Chinese New Year,\n' +
          'Deepavali, Christmas and Hari Raya dates. Thus, the treatment\n' +
          'date should match the specified holidays\n' +
          '=================================================================\n\n')

# Header and footer for treatment
def treatment_header_footer(header_footer):
    if header_footer == 'header':
        print('-' * 141)
        print('%60s \t TREATMENT LIST' % ' ')
        print('-' * 141)
        print('%-15s \t %-55s \t %-8s     %-10s' % (('-' * 14), ('-' * 60), ('-' * 15), ('-' * 36)))
        print('%-40s \t %-35s \t %-10s     %-20s' % ('Treatment code', 'Treatment description', 'Treatment price', 'Free trials'))
        print('%-15s \t %-55s \t %-8s     %-10s' % (('-' * 14), ('-' * 60), ('-' * 15), ('-' * 36)))
    elif header_footer == 'footer':
        print('%-15s \t %-55s \t %-8s     %-10s' % (('-' * 14), ('-' * 60), ('-' * 15), ('-' * 36)))
        print('-' * 141)
    elif header_footer == 'header1':
        print('-' * 100)
        print('%40s \t TREATMENT LIST' % ' ')
        print('-' * 100)
        print('%-15s \t %-55s \t %-8s' % (('-' * 14), ('-' * 60), ('-' * 15)))
        print('%-35s \t %-40s \t %-10s' % ('Treatment Code', 'Treatment Description', 'Treatment Price'))
        print('%-15s \t %-55s \t %-8s' % (('-' * 14), ('-' * 60), ('-' * 15)))
    elif header_footer == 'footer1':
        print('%-15s \t %-55s \t %-8s' % (('-' * 14), ('-' * 60), ('-' * 15)))
        print('-' * 100)

# Display the full listing of treatments
def display_treatment(treatment_list):
    treatment_header_footer('header')
    for i in range(len(treatment_list)):
        print(treatment_list[i].__str__())
    treatment_header_footer('footer')

    print('\n' + str(len(treatment_list)) +  ' treatment(s) are shown.\n')

# Display the list of treatments according to a specific choice -- Used by newService(params) methods in Service.java (Service class)
def display_specific_treatment(serv_choice, treatment_list, package_list):
    if serv_choice == '1':
        treatment_header_footer("header")
        for i in range(len(treatment_list)):
            if re.match("^HC\\d{3}$", treatment_list[i].treatment_code):
                print(treatment_list[i].__str__())
        treatment_header_footer("footer")
        prefix_code = "HC"
    elif serv_choice == '2':
        treatment_header_footer("header")
        for i in range(len(treatment_list)):
            if re.match("^SC\\d{3}$", treatment_list[i].treatment_code):
                print(treatment_list[i].__str__())
        treatment_header_footer("footer")
        prefix_code = "SC"
    elif serv_choice == '3':
        treatment_header_footer("header")
        for i in range(len(treatment_list)):
            if re.match("^BC\\d{3}$", treatment_list[i].treatment_code):
                print(treatment_list[i].__str__())
        treatment_header_footer("footer")
        prefix_code = "BC"
    elif serv_choice == '4':
        treatment_header_footer("header")
        for i in range(len(treatment_list)):
            if re.match("^BS\\d{3}$", treatment_list[i].treatment_code):
                print(treatment_list[i].__str__())
        treatment_header_footer("footer")
        prefix_code = "BS"
    else:
        display_package(package_list)
        prefix_code = "PK"

    return prefix_code

# Display the list of free trials
def display_free_trials(treatment_list):
    free_trials_count = 0

    treatment_header_footer('header1')
    for i in range(len(treatment_list)):
        if treatment_list[i].free_trials == "Yes":
            print('%-15s \t %-60s \t RM %10.2f' % (treatment_list[i].treatment_code, treatment_list[i].treatment_desc, treatment_list[i].treatment_price))
            free_trials_count += 1
    treatment_header_footer('footer1')

    print('\n' + str(free_trials_count) + ' free trials are shown.\n')

# Display the full listing of packages
def display_package(package_list):
    print('-' * 193)
    print('%-96s PACKAGE LIST' % ' ')
    print('-' * 193)
    print('%-12s \t %-15s \t %-10s \t %10s \t %-10s' % (('-' * 12), ('-' * 25), ('-' * 60), ('-' * 60), ('-' * 20)))
    print('%-20s \t%-40s \t %-65s \t %-35s \t %10s' % ('Package Code', 'Package name', 'Treatment 1', 'Treatment 2', 'Package price'))
    print('%-12s \t %-15s \t %-10s \t %10s \t %-10s' % (('-' * 12), ('-' * 25), ('-' * 60), ('-' * 60), ('-' * 20)))
    for i in range(len(package_list)):
        print(package_list[i].__str__())
    print('-' * 193)
    print('\n' + str(len(package_list)) + ' package(s) are shown.\n')

# Display the full listing of customer members
def display_customer(customer_list):
    print('-' * 158)
    print('%70s CUSTOMER MEMBERS LIST' % ' ')
    print('-' * 158)
    print('%-7s \t %-20s \t %-11s \t %-13s \t %s' % (('-' * 11), ('-' * 20), ('-' * 11),('-' * 80), ('-' * 17)))
    print('%-7s \t %-20s \t %-45s \t\t %-40s \t\t %s' % ('Customer ID', 'Customer Name', 'Contact No.', 'Home Address', 'Date member since'))
    print('%-7s \t %-20s \t %-11s \t %-13s \t %s' % (('-' * 11), ('-' * 20), ('-' * 11),('-' * 80), ('-' * 17)))
    for i in range(len(customer_list)):
        print(customer_list[i].__str__())
    print('%-7s \t %-20s \t %-11s \t %-13s \t %s' % (('-' * 11), ('-' * 20), ('-' * 11),('-' * 80), ('-' * 17)))
    print('-' * 158)
    print('\n' + str(len(customer_list)) + ' customer member(s) are shown.\n')

# Display the full listing of beauticians
def display_beautician(beautician_list):
    print('-' * 171)
    print('%75s BEAUTICIAN LIST' % ' ')
    print('-' * 171)
    print('%-7s \t %-20s \t %-11s \t %-10s \t %-13s \t %s' % (('-' * 13), ('-' * 20), ('-' * 11), ('-' * 25),('-' * 11), ('-' * 70)))
    print('%-7s \t %-20s \t %-10s \t %-25s \t %-30s \t\t %s' % ('Beautician ID', 'Beautician Name', 'Date joined', 'Specialization', 'Contact No.', 'Home Address'))
    print('%-7s \t %-20s \t %-11s \t %-10s \t %-13s \t %s' % (('-' * 13), ('-' * 20), ('-' * 11), ('-' * 25),('-' * 11), ('-' * 70)))
    for i in range(len(beautician_list)):
        print(beautician_list[i].__str__())
    print('%-7s \t %-20s \t %-11s \t %-10s \t %-13s \t %s' % (('-' * 13), ('-' * 20), ('-' * 11), ('-' * 25),('-' * 11), ('-' * 70)))
    print('-' * 171)
    print('\n' + str(len(beautician_list)) + ' beautician(s) are shown.\n')

# Display the beautician list - Used in Service.py
def display_beautician_serv(beautician_list):
    print('-' * 80)
    print('%30s BEAUTICIAN LIST' % ' ')
    print('-' * 80)
    print('%-7s \t %-20s \t %-10s \t %-13s' % (('-' * 13), ('-' * 20), ('-' * 25),('-' * 11)))
    print('%-7s \t %-20s \t %-25s \t %-30s' % ('Beautician ID', 'Beautician Name', 'Specialization', 'Contact No.'))
    print('%-7s \t %-20s \t %-10s \t %-13s' % (('-' * 13), ('-' * 20), ('-' * 25),('-' * 11)))
    for i in range(len(beautician_list)):
        print("%-12s \t %-20s \t %-25s \t %-10s" %
        (beautician_list[i].beautician_id, beautician_list[i]._name.get_full_name(), beautician_list[i].specialization,
         beautician_list[i]._contact_number))
    print('%-7s \t %-20s \t %-10s \t %-13s' % (('-' * 13), ('-' * 20), ('-' * 25),('-' * 11)))
    print('-' * 80)
    print('\n' + str(len(beautician_list)) + ' beautician(s) are shown.\n')

# Check customer appointment date
def check_appoint_date(service_list, customer_list):
    cust_found, cust_count = False, 0

    while not cust_found:
        cust_id = input('Enter customer ID to show appointment list: CUST')
        while not re.match("^\\d{4}$", cust_id):
            print("Invalid customer ID, please try again and ensure the correct customer ID.\n")
            cust_id = input('Enter customer ID to show appointment list: CUST')
        for i in range(len(customer_list)):
            if customer_list[i].member_id == ("CUST" + cust_id):
                cust_found = True
                break
            else:
                cust_found = False

            if not cust_found:
                print("Customer not found in the system, please try again and ensure the customer member ID is an existing member.\n")

    service_header_footer("header")
    for x in range(len(service_list)):
        if ("CUST" + cust_id) == service_list[x].customer.member_id:
            print(service_list[x].__str__())
            cust_count += 1
    service_header_footer("footer")
    print('\n' + str(cust_count) + " record(s) are shown.\n")

# Bridal service report
def bridal_report(service_list):
    bridal_count = 0
    service_header_footer("bridalService")
    service_header_footer("header")
    for i in range(len(service_list)):
        if service_list[i].total_price > 1000:
            print(service_list[i].__str__())
            bridal_count += 1
    service_header_footer("footer")
    print('\n' + str(bridal_count) + " record(s) are shown.\n")

# Display the trials service records
def trials_serv_record(service_list):
    serv_count = 0

    service_header_footer("header2")
    for i in range(len(service_list)):
        if service_list[i].free_trials == "Yes":
            print("%-12s \t %-15s \t %-25s \t %-25s \t %-15s \t\t\t %-60s" %
                  (service_list[i].service_id, service_list[i].service_date,
                  service_list[i].customer._name.get_full_name(), service_list[i].beautician._name.get_full_name(),
                  service_list[i].treatment_or_package.treatment_code, service_list[i].treatment_or_package.treatment_desc))
            serv_count += 1
    service_header_footer("footer2")
    print('\n' + str(serv_count) + " record(s) are shown.\n")

# Display the full appointment records
def display_appoint_records(service_list):
    service_header_footer("appRecords")
    service_header_footer("header")
    for i in range(len(service_list)):
        print(service_list[i].__str__())
    service_header_footer("footer")
    print("\n" + str(len(service_list)) + " record(s) are shown.\n")

# Check beauticians record
def check_beau_details(service_list, beautician_list):
    beau_found, beau_count = False, 0

    while not beau_found:
        beau_id = input("Enter beautician ID to show details: BEAU")
        while not re.match("^\\d{3}$", beau_id):
            print("Invalid beautician ID, please try again and ensure the correct beautician ID.\n")
            beau_id = input("Enter beautician ID to show details: BEAU")

        for i in range(len(beautician_list)):
            if beautician_list[i].beautician_id == ("BEAU" + beau_id):
                beau_found = True
                break
            else:
                beau_found = False

        if not beau_found:
            print("Beautician not found in the system, please try again and ensure the beautician ID exist.\n")

    print(('-' * 215) + '\n' +
          ('\t' * 22) + "Beautician Appointment Details for BEAU" + beau_id + '\n' +
          ('-' * 215))
    service_header_footer("beauticianDetailsHead")
    for x in range(len(service_list)):
        if ("BEAU" + beau_id) == service_list[x].beautician.beautician_id:
            if type(service_list[x].treatment_or_package) == treat.Treatment:
                print("%s \t\t %-15s \t RM %8.2f \t %-10s \t %-20s \t %-20s \t %-20s \t %-60s \t %6s" % (service_list[x].service_id,
                      service_list[x].service_date, service_list[i].total_price, service_list[x].customer.member_id,
                      service_list[x].customer._name.get_full_name(), service_list[x].beautician._name.get_full_name(),
                      service_list[x].treatment_or_package.treatment_code, service_list[x].treatment_or_package.treatment_desc,
                      service_list[x].free_trials))
            else:
                print("%s \t\t %-15s \t RM %8.2f \t %-10s \t %-20s \t %-20s \t %-20s \t %-60s \t %6s" % (service_list[x].service_id,
                      service_list[x].service_date, service_list[i].total_price, service_list[x].customer.member_id,
                      service_list[x].customer._name.get_full_name(), service_list[x].beautician._name.get_full_name(),
                      service_list[x].treatment_or_package.package_id, service_list[x].treatment_or_package.package_name,
                      service_list[x].free_trials))
            beau_count += 1

    service_header_footer("beauticianDetailsFoot")
    print('\n' + str(beau_count) + " record(s) are shown.\n")

# Check the treatment list for a specific customer
def cust_treat_transaction(service_list, customer_list):
    cust_found, treat_count = False, 0
    while not cust_found:
        cust_id = input("Enter customer ID to show appointment list: CUST")
        while not re.match("^\\d{4}$", cust_id):
            print("Invalid customer ID, please try again and ensure the correct customer ID.\n")
            cust_id = input("Enter customer ID to show appointment list: CUST")


        for i in range(len(customer_list)):
            if customer_list[i].member_id == ("CUST" + cust_id):
                cust_found = True
                break
            else:
                cust_found = False

        if not cust_found:
            print("Customer not found in the system, please try again and ensure the customer member ID is an existing member.\n")

    print(('-' * 172) + '\n' +
          ('\t' * 16) + "Customer Treatment Transaction for CUST" + cust_id + '\n' +
          ('-' * 172))
    service_header_footer("header1")
    for x in range(len(service_list)):
        if ("CUST" + cust_id) == service_list[x].customer.member_id and type(service_list[x].treatment_or_package) == treat.Treatment:
            print("%-12s \t %-15s \t %-28s \t %-15s \t\t\t %-60s \t RM %8.2f" % (service_list[x].service_id, service_list[x].service_date,
                  service_list[x].customer._name.get_full_name(), service_list[x].treatment_or_package.treatment_code,
                  service_list[x].treatment_or_package.treatment_desc, service_list[x].total_price))
            treat_count += 1
    service_header_footer("footer1")
    print('\n' + str(treat_count) + " record(s) are shown.\n")

# Header/Footer for displaying the Service
def service_header_footer(head_foot):
    if head_foot == "beauticianDetailsHead":
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-15s \t%-5s \t %-55s \t%-5s" %
              (("-" * 14), "-" * 16, "-" * 11, "-" * 11, "-" * 21, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
        print("%s \t %-12s \t %7s \t %-10s \t %-20s \t %-20s \t%-40s \t %-40s \t%-5s" %
              ("Appointment ID", "Appointment Date", "Total Price", "Customer ID", "Customer Name", "Beautician Name",
               "Treatment/Package Code", "Treatment/Package", "Free Trials"))
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-15s \t%-5s \t %-55s \t%-5s" %
              (("-" * 14), "-" * 16, "-" * 11, "-" * 11, "-" * 21, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
    elif head_foot == "beauticianDetailsFoot":
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-15s \t%-5s \t %-55s \t%-5s" %
              (("-" * 14), "-" * 16, "-" * 11, "-" * 11, "-" * 21, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
    elif head_foot == "bridalService":
        print(('-' * 235) + '\n' +
              ('\t' * 25) + "Bridal Service Report\n" +
              ('-' * 235))
    elif head_foot == "appRecords":
        print(('-' * 235) + '\n' +
              ('\t' * 25) + "Appointment Records\n" +
              ('-' * 235))
    elif head_foot == "header":
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-10s \t %-15s \t%-5s \t %-55s \t%-5s" %
              ("-" * 14, "-" * 18, "-" * 11, "-" * 11, "-" * 21, "-" * 13, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
        print("%s \t %-15s \t\t %7s \t %-12s \t %-18s \t %-13s \t %-18s \t%-40s \t\t %-35s \t%-5s" %
              ("Appointment ID", "Appointment Date", "Total Price", "Customer ID", "Customer Name", "Beautician ID",
               "Beautician Name", "Treatment/Package Code", "Treatment/Package", "Free Trials"))
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-10s \t %-15s \t%-5s \t %-55s \t%-5s" %
              ("-" * 14, "-" * 18, "-" * 11, "-" * 11, "-" * 21, "-" * 13, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
    elif head_foot == "footer":
        print("%s \t %-10s \t %7s \t %-10s \t %-15s \t %-10s \t %-15s \t%-5s \t %-55s \t%-5s" %
              ("-" * 14, "-" * 18, "-" * 11, "-" * 11, "-" * 21, "-" * 13, "-" * 21, "-" * 22, "-" * 58, "-" * 11))
    elif head_foot == "header1":
        print("%s \t %-10s \t %-25s \t %-10s \t %-60s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 26, "-" * 22, "-" * 57, "-" * 11))
        print("%s \t %-12s \t %-28s \t %-48s \t %-35s \t %-10s" %
              ("Appointment ID", "Appointment Date", "Customer Name", "Treatment Code", "Treatment", "Total Price"))
        print("%s \t %-10s \t %-25s \t %-10s \t %-60s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 26, "-" * 22, "-" * 57, "-" * 11))
    elif head_foot == "footer1":
        print("%s \t %-10s \t %-25s \t %-10s \t %-60s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 26, "-" * 22, "-" * 57, "-" * 11))
    elif head_foot == "header2":
        print(('-' * 178) + '\n' +
              ('\t' * 20) + "Trial Service Records\n" +
              ('-' * 178))
        print("%s \t %-10s \t %-25s \t %-10s \t %-8s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 21, "-" * 22, "-" * 22, "-" * 57))
        print("%s \t %-12s \t %-25s \t %-25s \t %-30s \t\t    %-10s" %
              ("Appointment ID", "Appointment Date", "Customer Name", "Beautician Name", "Treatment/Package Code", "Treatment/Package"))
        print("%s \t %-10s \t %-25s \t %-10s \t %-8s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 21, "-" * 22, "-" * 22, "-" * 57))
    elif head_foot == "footer2":
        print("%s \t %-10s \t %-25s \t %-10s \t %-8s \t %-15s" %
              ("-" * 14, "-" * 16, "-" * 21, "-" * 22, "-" * 22, "-" * 57))
