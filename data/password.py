def generate_password(number, name):
    try:
        # Convert number to scientific notation
        scientific_notation = "{:e}".format(float(number))
        
        # Extract the coefficient and exponent
        coefficient, exponent = scientific_notation.split('e')
        coefficient_digits = [int(digit) for digit in coefficient if digit.isdigit()]
        
        # Reduce the coefficient and exponent to single digits
        reduced_coefficient = sum(coefficient_digits) % 10
        reduced_exponent = int(exponent) % 10
        
        # Create S1 by concatenating the first three letters of each digit
        s1 = ''.join([word[:3] for word in map(str, [reduced_coefficient, reduced_exponent])])

        # Create S2 by selecting letters at odd positions if the reduced exponent is odd
        s2 = ''.join([name[i - 1] for i in range(1, len(name) + 1, 2)]) if reduced_exponent % 2 == 1 else ''
        
        # Combine S1 and S2 with '@' symbol
        password = f"{s1}@{s2}"

        return password
    except ValueError:
        # Invalid input
        return "Invalid input"

# Input
t = int(input())
for _ in range(t):
    test_case = input().split()
    number, name = test_case[0], test_case[1]

    # Output
    result = generate_password(number, name)
    print(result)
