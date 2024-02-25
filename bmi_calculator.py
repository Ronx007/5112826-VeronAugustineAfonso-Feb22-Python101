def calculate_bmi(weight, height):

    bmi = (weight / height / height) * 10000

    return bmi

def check_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

bmi = calculate_bmi(weight, height)

category = check_bmi(bmi)
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
