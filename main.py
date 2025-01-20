import math

# Attributes
T = float(input("How often do you think about that friend?"))
S = float(input("How often do you see that friend?"))
I = float(input("How often do you interact with that friend?"))
F = int(input("How many friends are involved?"))

# Constants
phi = (1 + math.sqrt(5)) / 2  # Golden ratio

# Summation 1: Sum from n=1 to F of (T + I^2 - S) / (n + 1)
summation_1 = sum((T + I**2 - S) / (n + 1) for n in range(1, F + 1))

# Summation 2: Sum from m=1 to F of 1 / m^2
summation_2 = sum(1 / (m**2) for m in range(1, F + 1))

# Logarithmic damping term: ln(1 + summation_2)
log_term = math.log(1 + summation_2)

# Summation 3: Sum from k=1 to F of k / (F * (T + S + 1))
summation_3 = sum(k / (F * (T + S + 1)) for k in range(1, F + 1))

# Cosine term: cos(pi * summation_3)
cosine_term = math.cos(math.pi * summation_3)

# Numerator
numerator = summation_1 + log_term + cosine_term

# Summation 4: Sum from n=1 to F of (T^3 + I^3 + S^3) / n
summation_4 = sum((T**3 + I**3 + S**3) / n for n in range(1, F + 1))

# Denominator: sqrt(1 + summation_4) + exp(-F / phi) + ln(2)
denominator = math.sqrt(1 + summation_4) + math.exp(-F / phi) + math.log(2)

# Final FR calculation
FR = abs(10 * math.tanh(numerator / denominator));

print(str(FR));
