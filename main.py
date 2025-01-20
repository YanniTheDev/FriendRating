import math

def calculate_friend_rating(T, S, I, F):
    """
    Calculate the Friend Rating (FR) based on the given formula.
    
    Parameters:
        T (float): How often you think about the friend (0 to 5).
        S (float): How often you see the friend (0 to 5).
        I (float): How often you interact with the friend (0 to 5).
        F (int): Total number of friends (must be >= 0).
        
    Returns:
        float: The calculated Friend Rating (FR), constrained between 0 and 10.
    """
    if not (0 <= T <= 5 and 0 <= S <= 5 and 0 <= I <= 5):
        raise ValueError("T, S, and I must be between 0 and 5.")
    if F < 0:
        raise ValueError("F (number of friends) must be non-negative.")

    fraction = (8*T + 4*S + I**2)/85
    exponent = 4*math.sqrt(S+5)/F

    FR = 10 * (fraction ** exponent)

    return FR

# Ask user to input values
T = float(input("How often do you think about that friend?"))
S = float(input("How often do you see that friend?"))
I = float(input("How often do you interact with that friend?"))
F = int(input("How many friends are involved?"))

friend_rating = calculate_friend_rating(T, S, I, F)

print(f"Friend Rating (FR): {friend_rating:.2f}")