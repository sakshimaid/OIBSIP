#BMI Calculator code

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("BMI Calculator")

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("Your BMI is: ", round(bmi, 2))
    print("Your weight category is: ", category)
    
def classify_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal"
    elif 25.0 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

if __name__ == "__main__":
    main()