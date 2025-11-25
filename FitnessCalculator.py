

class calculator:
    @staticmethod


    def calculate_bmi(weight, height_cm):
        height_m = height_cm / 100  # converte cm para metros
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)

    def calculate_bmr(gender,weight,height, age):
        gender = gender.lower()
        if gender == "male" :
            bmr= 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        elif gender == "female":
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
        else:
            raise ValueError("Gender must be 'male' or 'female'.")
        return round(bmr, 2)

    @staticmethod
    def calculate_tdee(bmr, activity_level):
        activity_map = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.9,
        }

        activity_level = activity_level.lower()

        if activity_level not in activity_map:
            raise ValueError(
                "Invalid activity level. Choose one of: sedentary, lightly active, moderately active, very active, extra active."
            )

        tdee = bmr * activity_map[activity_level]
        return round(tdee, 2)


    def calculate_target_calories(self, calculator):
        bmr = calculator.calculate_bmr(self.gender, self.weight, self.height, self.age)
        tdee = calculator.calculate_tdee(bmr, self.activity)
        return tdee + self.daily_calorie_adjustment()