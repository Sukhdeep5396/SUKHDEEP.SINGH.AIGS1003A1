#!/usr/bin/env python
# coding: utf-8

# Question 1: To compute P(sunny∣a cone of ice cream) and P(rainy∣a cup of hot coffee) 
#    using the Naive Bayes classifier and the assumption of conditional independence,
# 
# 1. P(sunny∣a cone of ice cream):
# 
# P(sunny|a cone of icecream) = P(a cone of icecream|sunny) * P(sunny) / P(a cone of icecream)
# 
# According to the Naive Bayes assumption, we have:
# P(sunny∣a cone of icecream) = P(sunny) * P(a∣sunny) * P(cone∣sunny) * P(of∣sunny) * P(ice cream∣sunny)
# 
# In this case, you would use the training data to estimate the probabilities 
# P(sunny), P(a|sunny), P(cone|sunny), P(of|sunny), and P(ice cream|sunny) based on the occurrence of these words in the sunny category of your training data.
# 
# 2. P(rainy|a cup of hot coffee):
# 
# P(rainy|a cup of hot coffee) = P(a cup of hot coffee|rainy) * P(rainy) / P(a cup of hot coffee)
# 
# According to the Naive Bayes assumption
# P(rainy|a cup of hot coffee) = P(rainy) * P(a∣rainy) * P(cup|rainy) * P(of|rainy) * P(hot|rainy) * P(coffee|rainy)
# 
# In this case, you would use the training data to estimate the probabilities 
# P(rainy), P(a∣rainy), P(cup∣rainy), P(of∣rainy), P(hot∣rainy), and P(coffee∣rainy) based on the occurrence of these words in the rainy category of your training data.
# 

# In[ ]:




