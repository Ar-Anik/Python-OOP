# Static Method Example : Date Validation
class DateValidator:
    @staticmethod
    def is_valid_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return True
        else:
            return False

print(DateValidator.is_valid_date(31, 12, 2023))
print(DateValidator.is_valid_date(32, 12, 2023))