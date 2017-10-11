'''
 # @BeautyParlour.py
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 #
 # Created by @StarmanW
 #
 # Main program driver which is the main class that consists of the main
 # function to run all the classes.
 #
 # @version 1.00 2017/7/28
'''

# Imports
import time, sys, utility as util

# Objects initialisation
customer_list = util.predefined_customer()
beautician_list = util.predefined_beautician()
treatment_list = util.predefined_treatment()
package_list = util.predefined_package(treatment_list)
service_list = util.predefined_service(customer_list, beautician_list, treatment_list, package_list)

# Local variables declaration
login_user = 0
log_out = True

# Display company logo
util.company_logo_header()

# Display the main screen and get input
while log_out:
    choice = util.system_main_screen()
    if choice == '1':

        # login_user = Utility.login()
        login_user = 1
        back_to_main_menu = True

        while back_to_main_menu:
            choice = util.system_main_menu()

            if choice == '1':
                # Make new service
                util.serv.Service.new_service(service_list, treatment_list, package_list, customer_list,
                                              beautician_list)
            elif choice == '2':
                registration_choice = util.registration_menu()

                # Perform registration according to user input choice
                if registration_choice == '1':
                    # register customer
                    util.cust.Customer.register_customer(customer_list)
                elif registration_choice == '2':
                    # register beautician
                    util.beau.Beautician.register_beautician(beautician_list)
                elif registration_choice == '3':
                    # register treatment
                    util.treat.Treatment.register_treatment(treatment_list)
                elif registration_choice == '4':
                    # register package
                    util.packg.Package.register_package(package_list, treatment_list)

                back_to_main_menu = True  # Back to main menu

            elif choice == '3':
                if login_user == 1:
                    record_choice = util.manager_records_menu()

                    # Display the reports according to user input choice
                    if record_choice == '1':
                        # Display customer treatment transaction
                        util.cust_treat_transaction(service_list, customer_list)
                    elif record_choice == '2':
                        # Display appointments records
                        util.display_appoint_records(service_list)
                    elif record_choice == '3':
                        # Display bridal service report
                        util.bridal_report(service_list)
                    elif record_choice == '4':
                        # Check beautician's treatment records
                        util.check_beau_details(service_list, beautician_list)
                    elif record_choice == '5':
                        # Display trial service records
                        util.trials_serv_record(service_list)
                    elif record_choice == '6':
                        # Display treatments list
                        util.display_treatment(treatment_list)
                    elif record_choice == '7':
                        # Display packages list
                        util.display_package(package_list)
                    elif record_choice == '8':
                        # Display customer members list
                        util.display_customer(customer_list)
                    elif record_choice == '9':
                        # Display beauticians list
                        util.display_beautician(beautician_list)
                else:
                    record_choice = util.staff_records_menu()

                    # Display the reports according to user input choice
                    if record_choice == '1':
                        # Display treatments list
                        util.display_treatment(treatment_list)
                    elif record_choice == '2':
                        # Display packages list
                        util.display_package(package_list)
                    elif record_choice == '3':
                        # Display customer members list
                        util.display_customer(customer_list)
                    elif record_choice == '4':
                        # Display beauticians list
                        util.display_beautician(beautician_list)
                    elif record_choice == '5':
                        # Check appointment date
                        util.check_appoint_date(service_list, customer_list)

                back_to_main_menu = True  # Back to main menu

            elif choice == '4':
                back_to_main_menu = False  # Do not go back to main menu, log out
                print()  # Newline for Formatting
    else:
        print('Program is now closing...')
        time.sleep(1)
        sys.exit(0)
