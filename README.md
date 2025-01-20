# Friend Rating Calculation Code

## What is Friend Rating?

Friend Rating (FR) is how much you are of a friend to me. The value of FR is clamped between values of
0 to 10, with 0 meaning "**not a friend**" and 10 meaning "**best friend**".

If you wish to find out your **unrestricted / unclamped** (meaning your FR goes beyond 10) FR, please contact me.

## How do I calculate it?

The FR is related to three significant attributes and one insignificant attribute:

### Significant Attributes

- $$T$$ (how often I think about you)
- $$S$$ (how often I see you)
- $$I$$ (how often I interact with you)

Each of these three attributes will score from 0 to 5.

If you wish to know what you scored on each attribute, please contact me.

### Insignificant Attributes

- $$F$$ (total number of friends that I am calculating for a FR during this session)

Note that $$F$$ is usually set to a constant and not physically changeable unless I do so.

Altogether, they will combine to form the equation:

$$FR = 10 * \left(\frac{8T + 4S + I^{2}}{85} \right)^{\frac{4\sqrt{S + 5}}{F}}$$

## How do I maximise my FR?

By looking at the equation, you can see that $$I$$ is being raised to the power of two.

This means that increasing $$I$$ (how often I interact with you) increases your overall FR much faster than other attributes.

## When Will I calculate the FR for you?

I calculate the FR for each and everyone that takes part in the Final Positive Thursday in each year!
