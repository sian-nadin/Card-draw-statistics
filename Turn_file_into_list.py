import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

#30 draws of three cards from a deck of 52 cards

#Read in file and create a list where each element is a set of 3 cards drawn
cards_drawn = []
with open('30_card_draws') as file:
    cards_drawn = [cards_drawn.strip() for cards_drawn in file]

#Get each card as an individual element
cards_list = []
for card_set in cards_drawn:
    cards_list.extend(card_set.split())

#Remove te suits to leave just the card values
cards_list = [ card[:-1] for card in cards_list]

#Change King,Queen and Jack cards to 10 and Ace cards to 1
for card in xrange(len(cards_list)):
    if cards_list[card] =="Q" or cards_list[card]=="K" or cards_list[card]=="J":
        cards_list[card] = "10"
    elif cards_list[card] == "A":
        cards_list[card] = "1"

#Change to a list of integers
cards_list = list(map(int,cards_list))

#Get Nested list of each draw
list_of_draws = [cards_list[i:i+3] for i in range(0, len(cards_list), 3)]

#List of sum for each 3 card draw
sum_of_draw = []
for draw in list_of_draws:
    for value in draw:
        summed_value = sum(int(value) for value in draw)
    sum_of_draw.append(summed_value)

#CALCULATE CENTRAL TENDENCIES - MEAN & MODE:
#Mean sum of 3 card draws
mean = (sum(int(i) for i in sum_of_draw))/30
#For median arrange sum_of_draws from smallest to greatest values
sorted_sum_of_draws = sorted(sum_of_draw)
#Since theres 30 values in order to get median get the mean of 15th & 16th numbers in list
median = (float(sorted_sum_of_draws[14]) + sorted_sum_of_draws[15])/2
#mode
mode = mode(sum_of_draw, axis=None)


#CALCULATE MEASURES OF VARIABILTY - STANDARD DEV & VARIANCE
#standard deviation
numpy_array_of_draws = np.array(sum_of_draw)
standard_dev = np.std(numpy_array_of_draws)
#variance
variance = np.var(numpy_array_of_draws)

#Draw histogram of the card draws
plt.hist(numpy_array_of_draws)
plt.title("Sum of values for three cards drawn")
plt.ylabel("Frequency")
plt.xlabel("Sum of values for 3 cards")
plt.show()


print "The cards drawn were: ", cards_drawn
print "\nThe sum of the 30 draws are: ", sum_of_draw
print "\nMean is %i " % mean
print "\nMedian is %.2f\n" % median
print mode
print "\nStandard deviation is %.2f " % standard_dev
print "\nVariance is %.2f " % variance
