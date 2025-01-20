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

    numerator = math.log(F + math.e) + (2 * T + S + 3 * I)
    denominator = math.sqrt(F*2 + 1)
    FR = (10 / 3) * (numerator / denominator)

    # The uncapped FR (without the 10 max)
    uncapped_FR = FR

    # Ensure FR is within bounds [0, 10]
    FR = max(0, min(10, FR))
    return [FR, uncapped_FR]

# Ask user to input values
T = float(input("How often do you think about that friend?"))
S = float(input("How often do you see that friend?"))
I = float(input("How often do you interact with that friend?"))
F = int(input("How many friends are involved?"))

ratings = calculate_friend_rating(T, S, I, F)

print(f"Friend Rating (FR): {ratings[0]:.2f}")
print(f"Uncapped FR: {ratings[1]:.2f}")