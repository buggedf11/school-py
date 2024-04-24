myfile = ("/workspaces/school-py/highscores.txt""r")
highscores = myfile.read()
for line in highscores:
    myhighscorer = line.split(",")
    highscorename = myhighscorer[0].strip()
    highscore = myhighscorer[1].strip()
    highscore = int(highscore)
    if highscore > 30000:
        print(highscorename)
myfile