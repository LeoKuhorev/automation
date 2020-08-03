import random

import pytest

from automation.automation import ContactInfo


class TestAutomation:

    def test_proof_of_life(self):
        assert ContactInfo

    @pytest.fixture()
    def c(self):
        return ContactInfo()

    def test_open_file_happy_path(self, c):
        test_file = 'tests/test_files/read.txt'
        assert c.open_file(test_file) == 'test data'

    def test_open_file_err(self, c):
        test_file = 'tests/test_files/not_exists.txt'
        with pytest.raises(FileNotFoundError) as err:
            assert c.open_file(test_file)

    def test_phone_numbers(self, c):
        c.input = """
            (206)111-2222 - parethesis
            206-111-2233 - dashes
            206.111-3333 - mixed dots and dashes
            206.111.3322 - dots
            2061114444 - no delimiters
            111-22-3333 - not a pone number
        """
        phone_numbers = c.get_phone_numbers()
        assert phone_numbers == [
            '206-111-2222', '206-111-2233', '206-111-3322', '206-111-3333', '206-111-4444']

    def test_get_emails(self, c):
        c.input = """
            test@company.com
            test-test@company.com
            test@another-company.com
            not-email.company.com
        """
        emails = c.get_emails()
        assert emails == ['test-test@company.com',
                          'test@another-company.com', 'test@company.com']

    def test_save_file(self, c):
        num = random.randint(1, 10)
        test_data = ''.join('test ' for _ in range(num))
        test_file = 'tests/test_files/write.txt'
        c.save_file(test_file, test_data)

        with open(test_file, 'r') as file:
            assert file.read() == test_data
