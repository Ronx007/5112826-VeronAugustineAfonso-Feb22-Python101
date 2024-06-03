import unittest
from oop_class_system_extended import System, Server, Client 

class TestSystem(unittest.TestCase):
    def test_system_initialization(self):
        s = System("Apple", "MacBook Pro", "1234567890", 1500)
        self.assertEqual(s.get_brand(), "Apple")
        self.assertEqual(s.get_model(), "MacBook Pro")
        self.assertEqual(s.get_serial_number(), "1234567890")
        self.assertEqual(s.get_price(), 1500)
    
    def test_system_setters(self):
        s = System("Apple", "MacBook Pro", "1234567890", 1500)
        s.set_brand("Asus")
        s.set_model("Zenbook Pro Duo")
        s.set_serial_number("3456789012")
        s.set_price(1600)
        self.assertEqual(s.get_brand(), "Asus")
        self.assertEqual(s.get_model(), "Zenbook Pro Duo")
        self.assertEqual(s.get_serial_number(), "3456789012")
        self.assertEqual(s.get_price(), 1600)

    def test_system_str(self):
        s = System("Apple", "MacBook Pro", "1234567890", 1500)
        expected_output = "\nBrand: Apple\nModel: MacBook Pro\nSerial Number: 1234567890\nPrice: 1500"
        self.assertEqual(str(s), expected_output)

class TestServer(unittest.TestCase):
    def test_server_initialization(self):
        srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        self.assertEqual(srv.get_brand(), "Apple")
        self.assertEqual(srv.get_model(), "MacBook Pro")
        self.assertEqual(srv.get_serial_number(), "1234567890")
        self.assertEqual(srv.get_price(), 1500)
        self.assertEqual(srv.get_administrator_username(), "")
        self.assertEqual(srv.get_administrator_password(), "")
        self.assertEqual(srv.get_ip_address(), "")
    
    def test_server_setters(self):
        srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        srv.set_admin_user("admin")
        srv.set_admin_pass("password")
        srv.set_ip_address("192.168.0.1")
        self.assertEqual(srv.get_administrator_username(), "admin")
        self.assertEqual(srv.get_administrator_password(), "password")
        self.assertEqual(srv.get_ip_address(), "192.168.0.1")

    def test_server_str(self):
        srv = Server("Apple", "MacBook Pro", "1234567890", 1500)
        srv.set_admin_user("admin")
        srv.set_admin_pass("password")
        srv.set_ip_address("192.168.0.1")
        expected_output = ("\nBrand: Apple\nModel: MacBook Pro\nSerial Number: 1234567890\nPrice: 1500"
                           "\nAdministrator Username: admin\nAdministrator Password: password\nIP Address: 192.168.0.1")
        self.assertEqual(str(srv), expected_output)

class TestClient(unittest.TestCase):
    def test_client_initialization(self):
        c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        self.assertEqual(c.get_brand(), "Lenovo")
        self.assertEqual(c.get_model(), "Legion Pro")
        self.assertEqual(c.get_serial_number(), "2345678901")
        self.assertEqual(c.get_price(), 1400)
        self.assertEqual(c.get_office_location(), "")
        self.assertEqual(c.get_assigned_employee(), "")
    
    def test_client_setters(self):
        c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        c.set_office_location("Room 911")
        c.set_assigned_employee("Jake Meister")
        self.assertEqual(c.get_office_location(), "Room 911")
        self.assertEqual(c.get_assigned_employee(), "Jake Meister")

    def test_client_str(self):
        c = Client("Lenovo", "Legion Pro", "2345678901", 1400)
        c.set_office_location("Room 911")
        c.set_assigned_employee("Jake Meister")
        expected_output = ("\nBrand: Lenovo\nModel: Legion Pro\nSerial Number: 2345678901\nPrice: 1400"
                           "\nOffice Location: Room 911\nAssigned Employee: Jake Meister")
        self.assertEqual(str(c), expected_output)

if __name__ == "__main__":
    unittest.main()
