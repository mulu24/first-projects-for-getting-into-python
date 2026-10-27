import matplotlib.pyplot as plt

def birthday_probability(num_people: int) -> float:
    prob_distinct = 1.0
    for i in range(num_people):
        prob_distinct *= (365 - i) / 365
    return 1 - prob_distinct

def plot_birthday_paradox(max_people: int = 60):
    people_counts = list(range(1, max_people + 1))
    probabilities = [birthday_probability(n) for n in people_counts]
    
    plt.figure(figsize=(10, 5))
    plt.plot(people_counts, probabilities, color="purple", linewidth=2)
    
    # Highlight 23 and 46 people thresholds
    for p_target in [23, 46]:
        prob = birthday_probability(p_target)
        plt.scatter(p_target, prob, color="red", s=50, zorder=5)
        plt.annotate(f"N={p_target}: {prob:.1%}", 
                     (p_target, prob), 
                     textcoords="offset points", 
                     xytext=(-20, 10), 
                     ha='center')
        
    plt.axhline(y=0.5, color="gray", linestyle=":", label="50% Threshold")
    plt.xlabel("Group Size (Number of People)")
    plt.ylabel("Probability of Shared Birthday")
    plt.title("Birthday Paradox Probability Curve")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_birthday_paradox(60)
