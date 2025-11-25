from datetime import datetime
from FitnessCalculator import calculator

class tracker:
    def __init__(self, user):
        self.user = user
        self.bmi = None
        self.bmr = None
        self.history = []


    def update_metrics(self):
      self.bmi = calculator.calculate_bmi(self.user.weight, self.user.height)
      self.bmr = calculator.calculate_bmr(self.user.gender, self.user.weight, self.user.height, self.user.age)
      self._record_progress()  # save to history


    def _record_progress(self):
        """Internal method to store metrics with timestamp."""
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "weight": self.user.weight,
            "bmi": self.bmi,
            "bmr": self.bmr
        }
        self.history.append(record)


    def display_metrics(self):
      if self.bmi is None or self.bmr is None:
        print("Please update metrics first using update_metrics().")
      else:
        print(f"--- {self.user.first_name}'s Fitness Summary ---")
        print(f"BMI: {self.bmi:.2f}")
        print(f"BMR: {self.bmr:.2f} kcal/day")


    def show_progress(self):
      if not self.history:
        print("No progress recorded yet.")
        return

      print(f"\nProgress for {self.user.first_name}:")
      for record in self.history:
        print(f"{record['date']} | Weight: {record['weight']} kg | BMI: {record['bmi']:.2f} | BMR: {record['bmr']:.2f}")