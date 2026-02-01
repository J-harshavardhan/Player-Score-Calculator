# game_score.py

# Step 1: Get player name
player_name = input("Enter the player's name: ")

# Step 2: Get number of games played
games_played = int(input("Enter number of games played: "))

# Step 3: Get total score
total_score = int(input("Enter total score: "))

# Step 4: Calculate average score
average_score = total_score / games_played

# Step 5: Display the results
print("\nPlayer:", player_name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print(f"Average Score:{average_score:.2f}")
