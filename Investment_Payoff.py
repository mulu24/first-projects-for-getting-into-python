import random
import matplotlib.pyplot as plt

def simulate_investment_run(initial: float, target: float, step: float = 1.0, win_prob: float = 0.5) -> bool:
    balance = initial
    while 0 < balance < target:
        if random.random() < win_prob:
            balance += step
        else:
            balance -= step
    return balance >= target

def evaluate_starting_amounts(target: float = 100.0, step: float = 10.0, trials_per_point: int = 10_000):
    starting_balances = [i for i in range(int(step), int(target), int(step))]
    win_probabilities = []

    for s_0 in starting_balances:
        wins = sum(simulate_investment_run(s_0, target, step, win_prob=0.5) for _ in range(trials_per_point))
        win_probabilities.append(wins / trials_per_point)

    plt.figure(figsize=(10, 5))
    plt.plot(starting_balances, win_probabilities, marker='o', color='green', linestyle='-')
    plt.xlabel("Initial Investment ($S_0$)")
    plt.ylabel("Probability of Reaching Target ($T$)")
    plt.title(f"Investment Payoff Probability (Target = {target})")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    evaluate_starting_amounts(target=100.0, step=10.0, trials_per_point=1_000)
