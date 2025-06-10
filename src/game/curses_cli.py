import time

for score in range(10):
    print(f"\033[FScore: {score}")  # \033[F moves cursor up one line
    time.sleep(0.5)


