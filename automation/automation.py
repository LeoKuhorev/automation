import re


class ContactInfo:
    def __init__(self):
        """Create new class instance
        """
        # User pre-defined values
        self.POTENTIAL_PATH = 'data/input/potential-contacts.txt'
        self.EXISTING_PATH = 'data/input/existing-contacts.txt'
        self.PHONE_NUMBERS_PATH = 'data/output/phone_numbers.txt'
        self.EMAILS_PATH = 'data/output/emails.txt'

        self.input = ''
        self.existing_contacts = ''
        self.phone_numbers = []
        self.emails = []

    def open_file(self, file_path: str) -> str:
        """Open the given file and return its content

        Args:
            file_path (str): File path to be read

        Returns:
            str: File's content
        """
        with open(file_path, 'r') as file:
            data = file.read()
        return data

    def get_phone_numbers(self) -> list:
        """Read the list of potential phone numbers and existing contacts and return a sorted list of unique numbers

        Returns:
            list: Sorted list of unique numbers
        """
        pattern = r'(?P<phone_number>\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4})(?P<ext>(x\d+)?)'
        phone_numbers = [c[0] + c[1] for c in re.findall(pattern, self.input)]
        existing_numbers = [c[0] + c[1]
                            for c in re.findall(pattern, self.existing_contacts)]

        unique_numbers = []
        for number in phone_numbers:
            if not number in existing_numbers:
                formatted_number = [c for c in number if (
                    c.isnumeric() or c == 'x')]
                formatted_number.insert(3, '-')
                formatted_number.insert(7, '-')

                unique_numbers.append(''.join(formatted_number))

        unique_numbers = sorted(set(unique_numbers))

        return unique_numbers

    def get_emails(self) -> list:
        """Read the list of potential emails and existing contacts and return a sorted list of unique emails

        Returns:
            list: Sorted list of unique emails
        """
        pattern = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(pattern, self.input)
        existing_emails = re.findall(pattern, self.existing_contacts)

        unique_emails = []
        for email in emails:
            if not email in existing_emails:
                unique_emails.append(email)

        unique_emails = sorted(set(unique_emails))

        return unique_emails

    def save_file(self, file_path: str, content: list) -> bool:
        """Save given content into a file by the given path

        Args:
            file_path (str): Path to the file to be saved
            content (list): Content to be saved into the file

        Returns:
            bool: Whether or not the saving went successful
        """
        with open(file_path, 'w+') as file:
            file.write(content)
            return True
        return False

    def run(self) -> None:
        """Read potential and existing contacts, process phone numbers and emails and save them into separate files
        """
        self.input = self.open_file(self.POTENTIAL_PATH)
        self.existing_contacts = self.open_file(self.EXISTING_PATH)
        self.phone_numbers = self.get_phone_numbers()
        self.emails = self.get_emails()
        self.save_file(self.PHONE_NUMBERS_PATH, '\n'.join(self.phone_numbers))
        self.save_file(self.EMAILS_PATH, '\n'.join(self.emails))


if __name__ == "__main__":

    c = ContactInfo()
    c.run()
