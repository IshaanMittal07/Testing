import random

class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll_ball(self, pins_left):
        return random.randint(0, pins_left)

    def play_frame(self, frame_number):
        if frame_number < 10:
            first = self.roll_ball(10)
            if first == 10:
                return [10]  # Strike
            second = self.roll_ball(10 - first)
            return [first, second]
        else:  # 10th frame logic
            first = self.roll_ball(10)
            second = self.roll_ball(10 if first == 10 else 10 - first)
            rolls = [first, second]
            if first == 10 or first + second == 10:
                third = self.roll_ball(10)
                rolls.append(third)
            return rolls

    def calculate_score(self):
        total = 0
        roll_index = 0
        rolls = [pin for frame in self.frames for pin in frame]
        
        for frame in range(10):
            if rolls[roll_index] == 10:  # Strike
                total += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
                roll_index += 1
            elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
                total += 10 + rolls[roll_index + 2]
                roll_index += 2
            else:  # Open frame
                total += rolls[roll_index] + rolls[roll_index + 1]
                roll_index += 2
        return total

    def play_game(self):
        for frame in range(1, 11):
            frame_result = self.play_frame(frame)
            self.frames.append(frame_result)
            print(f"Frame {frame}: {frame_result}")

        total_score = self.calculate_score()
        print(f"\nTotal score: {total_score}")

# Run the simulation
game = BowlingGame()
game.play_game()
