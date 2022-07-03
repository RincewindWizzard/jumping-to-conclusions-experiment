# Experiment for measuring peoples tendency to [jumping to conclusion](https://en.wikipedia.org/wiki/Jumping_to_conclusions)
There is an experiment described in [Delusions: Investigations Into The Psychology Of Delusional Reasoning](https://www.amazon.de/Delusions-Investigations-Psychology-Delusional-Reasoning-ebook/dp/B00D1YBN8A)
which persists of two jars with colored marbles (4 White, 6 Black) and vice versa.
The probants are show drawn marbles (which are put back into the jar) and they are asked if they are sure which distribution this jar has or if they want to see more.
With this experiment you can measure how many information a person needs to infer a conclusion.

It was observed, that people with psychosis have a tendency to infer conclusions significantly faster than neurotypical people.

I was interested what would be the mathematical approach to this experiment, and what the confidence intervals were.
So I created a little Python script calculating this table:

![Table of certainties](certainties.png)

This table is diagonal symmetric.
The axis are the number of Black/White marbles drawn.
As you can see, only the differenz between white and black marble count matters.
You loose certainty if the difference gets lower.

In a nutshell for a (0.4/0.6) distribution the confidence by delta is:

| Delta | Certainty |
|-------|-----------|
| 0     | 50.00%    |
| 1     | 60.00%    |
| 2     | 69.23%    |
| 3     | 77.14%    |
| 4     | 83.51%    |
| 5     | 88.36%    |
| 6     | 91.93%    |
| 7     | 94.47%    |
| 8     | 96.24%    |
| 9     | 97.46%    |
| 10    | 98.30%    |
| 11    | 98.86%    |
| 12    | 99.24%    |
| 13    | 99.49%    |
| 14    | 99.66%    |

Please consider, that 50% is full uncertainty because the probability of each distribution is 50%.

Neurotypical people tend to infer a conclusion after delta = 4 (citation needed) a scientific study needs a confidence intervall of at least 95% so delta = 8 is needed there.

