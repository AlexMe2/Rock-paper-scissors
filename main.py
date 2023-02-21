from getpass import getpass as input
p1_wins = 0
p2_wins = 0
while True:
  p1 = input("player 1, choose: (r,p,s)")
  p2 = input("player 2, choose: (r,p,s)")
  if p1 == "r":
    if p2 == "r":
      print("Is a tie, you both picked rock")  
    elif p2 == "p":
      print("player 2 won, paper covers rock")
      p2_wins += 1
    elif p2 == "s":
      print("player 1 won, smashed scissors with rock")
      p1_wins += 1
    else:
      print("Invalid choices")
  elif p1 == "p":
    if p2 == "r":
      print("player 2 won, paper covers rock")
      p2_wins += 1
    elif p2 == "p":
      print("Is a tie, you both picked paper")
    elif p2 == "s":
      print("player 2 won, cut the paper with scissors")
      p2_wins += 1
    else:
      print("Invalid choices")
  elif p1 == "s":
    if p2 == "r":
      print("player 2 won, smashed scissors with rock")
    elif p2 == "p":
      print("player 1 won, cut the paper with scissors")
      p1_wins += 1
    elif p2 == "s":
      print("Is a tie, you both picked scissors")
    else:
      print("Invalid choices")
  else:
    print("Invalid choices")
  if p1_wins == 3 or p2_wins == 3:
    print("P1 won ", p1_wins, "times and P2 won ", p2_wins, "times")
    print("Thank you for playing")
    exit()
  else:
    continue
