Egg Inc - Epic Research Calculator

# What is this?

It is a simple python script / app to determine which epic research upgrade you should take to get the best return for gold eggs spent.

Egg Inc has the 'Soul Food' epic research and the 'Prophecy Bonus' epic research, both of which improve the bonus that 'Mystical Eggs' provide (name Soul Eggs and Prophecy Eggs.)

This script helps to determine which upgrade path should be taken at a given point in time to maximise the bonus improvement obtained per gold egg spent.

# How to use

The script requires several inputs in order to make its determination.

The values are set in the code for the corresponding variables:

```
currentNumberOfSE = 0 #Enter the current number of your soul eggs here
currentNumberOfPE = 0 #Enter current number of your prophecy eggs here
currentSoulEggResearchLevel = 0 #Enter the current level of your soul egg research here
currentProphecyEggResearchLevel = 0 #Enter the current level of your prophecy egg research here
costForNextSoulEggResearchLevel = 0 #The cost (in gold eggs) for the next level of soul egg (aka soul food) research here
costForNextProphecyEggResearchLevel = 0 #The cost (in gold eggs) for the next level of prophecy egg research here
```

After entering all of the required values, run the script. It will perform a set of calculations, output results, with the final line indicating which upgrade should be taken next.

# Limits

1. The script relies on the inputs being correct and accurate in order to determine the best bonus increase per gold egg spent.
1. It currently only makes the determination for the next level (calculates +1 to soul food and +1 to prophecy bonus).
1. It does not yet take into account that increasing prophecy bonus generally cost significantly more per level than soul food and thus for the gold eggs spent increasing prophecy bonus by one, you could get several soul food levels.
