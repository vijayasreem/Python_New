from datetime import datetime

def validate_criteria(sum_assured, age, income, policy_tenure, otp_authentication):
    #Check min and max sum assured
    if sum_assured < 50000 or sum_assured >200000:
        return False

    #Check min and max age limits
    if age >= 18 and age <= 65:
        return True
    else:
        return False
    
    #Check income
    if income < 40000:
        return False
    
    #Check sum assured range
    allowed_sum_assured = [50000, 100000, 150000, 200000]
    if sum_assured not in allowed_sum_assured:
        return False
    
    #Check policy tenure range
    allowed_policy_tenure = [12, 15, 18, 24]
    if policy_tenure not in allowed_policy_tenure:
        return False
    
    #Check OTP authentication
    if not otp_authentication:
        return False
    
    #Check if spouse also ineligible
    if not validate_criteria(sum_assured, age, income, policy_tenure, otp_authentication):
        return False
    
    return True

def main():
    sum_assured = int(input("Enter the Sum Assured: "))
    age = int(input("Enter age: "))
    income = int(input("Enter annual income: "))
    policy_tenure = int(input("Enter policy tenure: "))
    otp_authentication = input("Enter OTP authentication: ")
    
    if validate_criteria(sum_assured, age, income, policy_tenure, otp_authentication):
        print("The criteria is valid")
    else:
        print("The criteria is invalid")

if __name__ == "__main__":
    main()