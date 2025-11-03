

class calculator:
    @staticmethod
    def calculate_bmi(weight, height_cm):
        height_m = height_cm / 100  # convert cm to meters
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)