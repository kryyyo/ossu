try: 
  score = float(input('Enter score: '))
except:
  print('Bad score')
  quit()

def computegrade(score):
  if score >= 10.0:
    return 'Bad score'
  elif score >= 0.9:
    return 'A'
  elif score >= 0.8: 
    return 'B'
  elif score >= 0.7: 
    return 'C'
  elif score >= 0.6: 
    return 'D'
  elif score < 0.6: 
    return 'F'
  else:
    return 'Bad Score'

print(computegrade(score))