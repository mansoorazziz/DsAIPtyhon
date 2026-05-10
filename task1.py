# Program to calculate tax based on salary

# Take salary input from user
salary = float(input("Enter your salary: "))

# Apply conditional statements to determine tax rate
if salary < 30000:
    tax_rate = 0.05
elif 30000 <= salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

# Calculate final tax
final_tax = salary * tax_rate

# Display the result
print(f"Your salary: {salary}")
print(f"Applicable tax rate: {tax_rate * 100}%")
print(f"Final tax amount: {final_tax}")
