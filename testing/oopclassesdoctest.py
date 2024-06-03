class System:
    def __init__(self, brand, model, serial_number, price):
        """
        Initialize a system with brand, model, serial number, and price.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.brand
        'Apple'
        >>> s.model
        'MacBook Pro'
        >>> s.serial_number
        '1234567890'
        >>> s.price
        1500
        """
        self.brand = brand
        self.model = model
        self.serial_number = serial_number
        self.price = price

    def set_brand(self, new_brand):
        """
        Set a new brand for the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.set_brand("Asus")
        >>> s.brand
        'Asus'
        """
        self.brand = new_brand

    def set_model(self, new_model):
        """
        Set a new model for the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.set_model("Zenbook Pro Duo")
        >>> s.model
        'Zenbook Pro Duo'
        """
        self.model = new_model

    def set_serial_number(self, new_serial_number):
        """
        Set a new serial number for the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.set_serial_number("3456789012")
        >>> s.serial_number
        '3456789012'
        """
        self.serial_number = new_serial_number

    def set_price(self, new_price):
        """
        Set a new price for the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.set_price(1600)
        >>> s.price
        1600
        """
        self.price = new_price

    def get_brand(self):
        """
        Get the brand of the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.get_brand()
        'Apple'
        """
        return self.brand

    def get_model(self):
        """
        Get the model of the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.get_model()
        'MacBook Pro'
        """
        return self.model

    def get_serial_number(self):
        """
        Get the serial number of the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.get_serial_number()
        '1234567890'
        """
        return self.serial_number

    def get_price(self):
        """
        Get the price of the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> s.get_price()
        1500
        """
        return self.price

    def __str__(self):
        """
        Get a string representation of the system.

        >>> s = System("Apple", "MacBook Pro", "1234567890", 1500)
        >>> print(s)
        <BLANKLINE>
        Brand: Apple
        Model: MacBook Pro
        Serial Number: 1234567890
        Price: 1500
        """
        return f"\nBrand: {self.brand}\nModel: {self.model}\nSerial Number: {self.serial_number}\nPrice: {self.price}"


class Server(System):
    def __init__(self, brand, model, serial_number, price):
        """
        Initialize a server with brand, model, serial number, price, admin username, admin password, and IP address.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.brand
        'Apple'
        >>> srv.model
        'MacBook Pro'
        >>> srv.admin_username
        ''
        >>> srv.ip_address
        ''
        """
        super().__init__(brand, model, serial_number, price)
        self.admin_username = ""
        self.admin_password = ""
        self.ip_address = ""

    def set_admin_user(self, new_username):
        """
        Set a new admin username for the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.set_admin_user("admin")
        >>> srv.admin_username
        'admin'
        """
        self.admin_username = new_username

    def set_admin_pass(self, new_password):
        """
        Set a new admin password for the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.set_admin_pass("password")
        >>> srv.admin_password
        'password'
        """
        self.admin_password = new_password

    def set_ip_address(self, new_ip_address):
        """
        Set a new IP address for the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.set_ip_address("192.168.0.1")
        >>> srv.ip_address
        '192.168.0.1'
        """
        self.ip_address = new_ip_address

    def get_administrator_username(self):
        """
        Get the admin username of the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.get_administrator_username()
        ''
        """
        return self.admin_username

    def get_administrator_password(self):
        """
        Get the admin password of the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.get_administrator_password()
        ''
        """
        return self.admin_password

    def get_ip_address(self):
        """
        Get the IP address of the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> srv.get_ip_address()
        ''
        """
        return self.ip_address

    def __str__(self):
        """
        Get a string representation of the server.

        >>> srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        >>> print(srv)
        <BLANKLINE>
        Brand: Apple
        Model: MacBook Pro
        Serial Number: 1234567890
        Price: 1500
        Administrator Username: 
        Administrator Password: 
        IP Address: 
        """
        result = super().__str__()
        result += f"\nAdministrator Username: {self.admin_username}\nAdministrator Password: {self.admin_password}\nIP Address: {self.ip_address}"
        return result


class Client(System):
    def __init__(self, brand, model, serial_number, price):
        """
        Initialize a client with brand, model, serial number, price, office location, and assigned employee.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> c.brand
        'Lenovo'
        >>> c.model
        'Legion Pro'
        >>> c.office_location
        ''
        >>> c.assigned_employee
        ''
        """
        super().__init__(brand, model, serial_number, price)
        self.office_location = ""
        self.assigned_employee = ""

    def set_office_location(self, new_office_location):
        """
        Set a new office location for the client.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> c.set_office_location("Room 911")
        >>> c.office_location
        'Room 911'
        """
        self.office_location = new_office_location

    def set_assigned_employee(self, new_assigned_employee):
        """
        Set a new assigned employee for the client.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> c.set_assigned_employee("Jake Meister")
        >>> c.assigned_employee
        'Jake Meister'
        """
        self.assigned_employee = new_assigned_employee

    def get_office_location(self):
        """
        Get the office location of the client.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> c.get_office_location()
        ''
        """
        return self.office_location

    def get_assigned_employee(self):
        """
        Get the assigned employee of the client.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> c.get_assigned_employee()
        ''
        """
        return self.assigned_employee

    def __str__(self):
        """
        Get a string representation of the client.

        >>> c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        >>> print(c)
        <BLANKLINE>
        Brand: Lenovo
        Model: Legion Pro
        Serial Number: 2345678901
        Price: 1400
        Office Location: 
        Assigned Employee: 
        """
        result = super().__str__()
        result += f"\nOffice Location: {self.office_location}\nAssigned Employee: {self.assigned_employee}"
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
