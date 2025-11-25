class UserProfile:
    def __init__(self, first_name, last_name, gender, weight, height, age, activity, objective):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.gender = gender.lower()
        self.weight = float(weight)
        self.height = float(height)
        self.age = int(age)
        self.activity = activity.lower()
        self.objective = objective.lower()

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, "
                f"{self.height} cm, {self.weight} kg, Activity: {self.activity}, Objective: {self.objective}")



    def change_profile(self):
            print("\nWhich field would you like to update?")
            print("Options: first_name, last_name, gender, weight, height, age, activity, objective")
            field = input("Field to update: ").strip().lower()

            if not hasattr(self, field):
                print("Invalid field name.")
                return

            new_value = input(f"Enter new value for {field}: ")

            # Type conversion depending on the field
            if field in ["weight", "height"]:
                new_value = float(new_value)
            elif field == "age":
                new_value = int(new_value)

            setattr(self, field, new_value)
            print(f"{field} updated successfully!")

    @property
    def name(self):
        return self.first_name #para o nome de cada perfil

    def daily_calorie_adjustment(self):
        """Return calorie adjustment for the user's goal.
        Contract: must return an integer or float.
        Subclasses MUST override this method.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class LoseWeightUser(UserProfile):
    def daily_calorie_adjustment(self):
        return -500

class MaintainUser(UserProfile):
    def daily_calorie_adjustment(self):
        return 0


class GainWeightUser(UserProfile):
    def daily_calorie_adjustment(self):
        return +300