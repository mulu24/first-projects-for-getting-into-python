import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(sides: int = 6, num_rolls: int = 10_000):
    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    cumulative_means = [sum(rolls[:i+1]) / (i + 1) for i in range(num_rolls)]
    
    theoretical_mean = (sides + 1) / 2
    
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_rolls + 1), cumulative_means, label="Observed Mean", color="blue")
    plt.axhline(y=theoretical_mean, color="red", linestyle="--", label=f"Theoretical Mean ({theoretical_mean})")
    plt.xlabel("Number of Rolls")
    plt.ylabel("Mean Value")
    plt.title(f"Law of Large Numbers: {sides}-Sided Die Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_dice_rolls(sides=6, num_rolls=5_000)
