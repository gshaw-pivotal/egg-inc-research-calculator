import decimal
currentNumberOfSE = 0 #Enter the current number of your soul eggs here
currentNumberOfPE = 0 #Enter current number of your prophecy eggs here
currentSoulEggResearchLevel = 0 #Enter the current level of your soul egg research here
currentProphecyEggResearchLevel = 0 #Enter the current level of your prophecy egg research here
costForNextSoulEggResearchLevel = 0 #The cost (in gold eggs) for the next level of soul egg (aka soul food) research here
costForNextProphecyEggResearchLevel = 0 #The cost (in gold eggs) for the next level of prophecy egg research here
message = "Upgrading "

# Calculations for current bonus
decimal.getcontext().prec = 100
currentBonusPerEgg = decimal.Decimal(1 + 0.05 + (0.01 * currentProphecyEggResearchLevel)) ** (decimal.Decimal(currentNumberOfPE)) * decimal.Decimal(10 + currentSoulEggResearchLevel)
currentTotalBonus = currentBonusPerEgg * decimal.Decimal(currentNumberOfSE)

# Calculations for raising soul egg (aka soul food) by one level
bonusPerEggWithNextSoulEggResearchLevel = decimal.Decimal(1 + 0.05 + (0.01 * currentProphecyEggResearchLevel)) ** (decimal.Decimal(currentNumberOfPE)) * decimal.Decimal(10 + (currentSoulEggResearchLevel + 1))
totalBonusWithNextSoulEggResearchLevel = bonusPerEggWithNextSoulEggResearchLevel * decimal.Decimal(currentNumberOfSE)
totalBonusImprovementWithNextSoulEggResearchLevel = decimal.Decimal(totalBonusWithNextSoulEggResearchLevel - currentTotalBonus)
bonusGainedPerGoldEggSpentForNextSoulEggResearchLevel = decimal.Decimal(decimal.Decimal((totalBonusWithNextSoulEggResearchLevel - currentTotalBonus)) / decimal.Decimal(costForNextSoulEggResearchLevel))

# Calculations for raising prophecy egg (aka prophecy bonus) by one level
bonusPerEggWithNextProphecyEggResearchLevel = decimal.Decimal(1 + 0.05 + (0.01 * (currentProphecyEggResearchLevel + 1))) ** (decimal.Decimal(currentNumberOfPE)) * decimal.Decimal(10 + currentSoulEggResearchLevel)
totalBonusWithNextProphecyEggResearchLevel = bonusPerEggWithNextProphecyEggResearchLevel * decimal.Decimal(currentNumberOfSE)
totalBonusImprovementWithNextProphecyEggResearchLevel = decimal.Decimal(totalBonusWithNextProphecyEggResearchLevel - currentTotalBonus)
bonusGainedPerGoldEggSpentForNextProphecyEggResearchLevel = decimal.Decimal(decimal.Decimal((totalBonusWithNextProphecyEggResearchLevel - currentTotalBonus)) / decimal.Decimal(costForNextProphecyEggResearchLevel))

# Determine on the basis of per gold egg spent, which upgrade gives a better bonus improvement
if bonusGainedPerGoldEggSpentForNextProphecyEggResearchLevel > bonusGainedPerGoldEggSpentForNextSoulEggResearchLevel:
  # PB better
  message = message + "Prophecy Bonus gives better value"
else:
  # SF better
  message = message + "Soul Food gives better value"


print("Current number of soul eggs:     " + '{:,.0f}'.format(currentNumberOfSE))
print("Current number of prophecy eggs: " + '{:,.0f}'.format(currentNumberOfPE))
print("Current bonus per soul egg (%):  " + '{:,.0f}'.format(currentBonusPerEgg))
print("Current Total bonus:             " + '{:,.0f}'.format(currentTotalBonus))
print("----------------------------------------------------------------")
print("If upgrade soul egg research by one level:")
print("Bonus per soul egg (with + 1 SERL) (%):   " + '{:,.0f}'.format(bonusPerEggWithNextSoulEggResearchLevel))
print("Total bonus (with + 1 SERL):              " + '{:,.0f}'.format(totalBonusWithNextSoulEggResearchLevel))
print("Bonus improvement:                        " + '{:,.0f}'.format(totalBonusImprovementWithNextSoulEggResearchLevel))
print("Bonus points per gold egg:                " + '{:,.0f}'.format(bonusGainedPerGoldEggSpentForNextSoulEggResearchLevel))
print("----------------------------------------------------------------")
print("If upgrade prophecy egg research by one level:")
print("Bonus per soul egg (with + 1 PERL) (%):   " + '{:,.0f}'.format(bonusPerEggWithNextProphecyEggResearchLevel))
print("Total bonus (with + 1 PERL):              " + '{:,.0f}'.format(totalBonusWithNextProphecyEggResearchLevel))
print("Bonus improvement:                        " + '{:,.0f}'.format(totalBonusImprovementWithNextProphecyEggResearchLevel))
print("Bonus points per gold egg:                " + '{:,.0f}'.format(bonusGainedPerGoldEggSpentForNextProphecyEggResearchLevel))
print("")
print("================================================================")
print(message)
