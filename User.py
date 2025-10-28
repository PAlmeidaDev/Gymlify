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

    @property
    def name(self):
        return self.first_name #para o nome de cada perfil