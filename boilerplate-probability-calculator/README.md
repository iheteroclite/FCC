# Probability Calculator

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it is possible to calculate this probability mathematically, using distributions, it can be approximated with a high number of trials.

## Usage

Here is how you would call the experiment function based on the example above with 2000 experiments:

    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                      expected_balls={"red":2,"green":1},
                      num_balls_drawn=5,
                      num_experiments=2000)

## Testing

The unit tests for this project are in `test_module.py`
