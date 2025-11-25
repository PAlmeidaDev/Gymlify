from User import UserProfile, LoseWeightUser, MaintainUser, GainWeightUser
from FitnessCalculator import calculator
from ProgressTracker import tracker


def get_user_input():
    first_name = get_alpha_input("Enter your first name: ")
    last_name = get_alpha_input("Enter your last name: ")
    gender = get_choice("Enter your gender:", ["male", "female"])
    weight = get_positive_float("Enter your weight in kg: ")
    height = get_positive_float("Enter your height in cm: ")
    age = get_positive_int("Enter your age: ")
    activity = get_choice("Enter your activity level:",["sedentary", "light", "moderate", "active", "very active"])
    objective = get_choice("Enter your fitness goal:",["maintain", "lose", "gain"])

    # Create the UserProfile object
    user = create_user_with_goal(first_name, last_name, gender, weight, height, age, activity, objective)
    return user

def create_user_with_goal(first_name, last_name, gender, weight, height, age, activity, objective):
    if objective == "lose":
        return LoseWeightUser(first_name, last_name, gender, weight, height, age, activity, objective)
    elif objective == "maintain":
        return MaintainUser(first_name, last_name, gender, weight, height, age, activity, objective)
    elif objective == "gain":
        return GainWeightUser(first_name, last_name, gender, weight, height, age, activity, objective)


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Try again.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be a positive whole number. Try again.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")

def get_alpha_input(prompt):
    while True:
        value = input(prompt).strip()  # remove extra spaces
        if value.isalpha():  # checks that all characters are letters
            return value
        else:
            print("Please enter letters only (no numbers or special characters).")

def get_choice(prompt, options):
    options_str = ", ".join(options)
    while True:
        value = input(f"{prompt} ({options_str}): ").lower()
        if value in options:
            return value
        else:
            print(f"Invalid choice. Please choose from: {options_str}")

def main():
    print("Welcome to Gymlify!")
    user= get_user_input()
    print("Here is your Information:")
    print(user)
    #user.change_profile()
    print(user)
    bmi = calculator.calculate_bmi(user.weight, user.height)
    print(f"{user.name}'s BMI is {bmi}")
    bmr = calculator.calculate_bmr(user.gender, user.weight, user.height, user.age)
    print(f"{user.name}'s BMR: {bmr} kcal/day")
    tdee= calculator.calculate_tdee(bmr,user.activity)
    print(f"{user.name}'s TDEE: {tdee} kcal/day")
    progress = tracker(user)
    progress.update_metrics()
    progress.display_metrics()
    progress.show_progress()

if __name__ == "__main__":
    main()

 #test