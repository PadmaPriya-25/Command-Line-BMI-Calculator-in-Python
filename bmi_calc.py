def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))
            return weight, height
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight, height, unit_system):
    if unit_system == 'metric':
        bmi = weight / (height ** 2)
    else: 
        bmi = (weight / (height ** 2)) * 703
    return bmi

def categorize_health(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    unit_system = input("Choose unit system (metric/imperial): ")

    weight, height = get_user_input()

    bmi = calculate_bmi(weight, height, unit_system)
    health_category=categorize_health(bmi)
    
    print(f"You are {health_category} with a BMI of {bmi:.2f}.")
   

if __name__ == "__main__":
    main()
