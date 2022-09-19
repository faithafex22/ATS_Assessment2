#HCF of two numbers
def highest_common_factor(num1 , num2):
    factors1 = []
    factors2 = []
    common_fact = []
    for i in range (1, num1+1):
        if num1%i == 0:
            factors1.append(i)
    for i in range (1, num2+1):
        if num2%i == 0:
            factors2.append(i)
        if i in factors1 and i in factors2:
            common_fact.append(i)
    HCF = max(common_fact)
    return f"The HCF of {num1} and {num2} is {HCF}"

print(highest_common_factor(200, 100))