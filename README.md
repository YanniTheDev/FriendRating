# Friend Rating Calculation Code

## What is Friend Rating?

Friend Rating (FR) is how much you are of a friend to me. The value of FR is clamped between values of
0 to 10, with 0 meaning "**not a friend**" and 10 meaning "**best friend**".

If you wish to find out your **unrestricted / unclamped** (meaning your FR goes beyond 10) FR, please contact me.

## How do I calculate it?

The FR is related to three significant attributes and one insignificant attribute:

### Significant Attributes

- T (how often I think about you)
- S (how often I see you)
- I (how often I interact with you)

### Insignificant Attributes

- F (total number of friends that I am calculating for a FR during this session)

Altogether, they will combine to form the equation:

$$FR = 10 * [\frac{8T + 4S + I^{2}}{85}]^{\frac{4\sqrt{S + 5}}{F}}$$
