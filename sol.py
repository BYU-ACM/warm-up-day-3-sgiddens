def Coin_Combinations(coins, value):
  """
    A Generalized solution to the coins problem provided by project euler #31
    Read it for more specifications
    coins: a list of coins that can be used
    value: the value that the coins should add to
    returns:
     number of possible combinations to make value with givin coins in "coins"
  """
  # Coin sum problem

  two_pound = 200
  one_pound = 100
  fifty_pence = 50
  twenty_pence = 20
  ten_pence = 10
  five_pence = 5
  two_pence = 2
  one_pence = 1

  #L = [two_pound, one_pound, fifty_pence, twenty_pence, ten_pence, five_pence, two_pence, one_pence]
  L = [five_pence, two_pence, one_pence]
  L.reverse()

  coins = [1] + ([0]*8)

  for money in L:
      for i in xrange(len(coins)-1):
          coins[1+i] = 1 + coins[1+i-money]

  return coins
