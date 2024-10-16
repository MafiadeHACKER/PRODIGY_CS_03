import re

def check_length(password):
    """Check if password has at least 8 characters."""  
    return len(password) >= 8

def check_uppercase(password):
    """Check if password contains at least one uppercase letter."""
    return re.search(r"[A-Z]", password)

def check_lowercase(password):
    """Check if password contains at least one lowercase letter."""
    return re.search(r"[a-z]", password)

def check_digit(password):
    """Check if password contains at least one digit."""
    return re.search(r"\d", password)

def check_special_char(password):
    """Check if password contains at least one special character."""
    return re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

def calculate_strength(password):
    """Calculate password strength score and provide detailed feedback."""
    strength_criteria = [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digit(password),
        check_special_char(password)
    ]
    
    # Count how many criteria are satisfied
    score = sum(bool(criteria) for criteria in strength_criteria)
    
    feedback = []
    
    if not check_length(password):
        feedback.append("Password should be at least 8 characters long.")
    if not check_uppercase(password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not check_lowercase(password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not check_digit(password):
        feedback.append("Password should contain at least one number.")
    if not check_special_char(password):
        feedback.append("Password should contain at least one special character.")
    
    return score, feedback

def password_strength(password):
    """Assess the overall strength of the password and provide a rating and feedback."""
    score, feedback = calculate_strength(password)
    
    # Provide strength ratings
    if score == 5:
        rating = "Strong (10/10)" 
    elif score == 4:
        rating = "Moderate (8/10)"      
    elif score == 3:
        rating = "Weak (5/10)"
    else:
        rating = f"Very Weak ({score}/10)"

    # Generate a final report
    if not feedback:
        feedback_message = "Your password is excellent!"
    else:
        feedback_message = "Improve your password by addressing the following:\n" + "\n".join(feedback)
    
    return f"Password Strength: {rating}\n{feedback_message}"

# Example Usage
password = input("Enter your password: ")
print(password_strength(password))

