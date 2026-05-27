def loan(age, income, credit_score, employment):
    if (not isinstance(age, int)):
        return "Invalid Input"
    
    if (not isinstance(income, (int, float))):
        return "Invalid Input"
    
    if (not isinstance(credit_score, int)):
        return "Invalid Input"
    
    if (employment not in ('C', "F")):
        return "Invalid Input"

    if (age < 18 or age > 65):
        return "Invalid Input"

    income = round(income, 1)
    if (income < 5 or income > 500):
        return "Invalid Input"

    if (credit_score < 300 or credit_score > 850):
        return "Invalid Input"
    
    risk = None
    if (credit_score >= 300 and credit_score <= 500):
        risk = "High"
    elif (credit_score >= 501 and credit_score <= 700):
        risk = "Medium"
    else:
        risk = "Low"

    if risk == "High":
        return "REJECT"
    
    if income < 15: 
        if risk == "Medium" or employment == "F":
            return "REJECT"
        if risk == "Low" and employment == "C":
            return "MANUAL REVIEW"
    else:
        if risk in ("Low", "Medium") and employment == "C":
            return "APPROVE"
        elif risk in ("Low", "Medium") and employment == "F":
            return "MANUAL REVIEW"
    
    return "REJECT"