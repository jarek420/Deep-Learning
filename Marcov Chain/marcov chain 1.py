import random

def read_text_from_file(dir = "tekst.txt"):
    with open("tekst.txt", "r", encoding="utf-8") as file:
        tekst=file.read()
    return tekst

def prepare_data(data):
    data = data.lower()
    allowed = 'abcdefghijklmnopqrstuvwxyz '
    return ''.join(char for char in data if char in allowed)

def build_transition_dict(text, n):
    transitions = {}
    for i in range(len(text) - n):
        current = text[i:i+n]
        next_char = text[i + n]
        if current not in transitions:
            transitions[current] = []
        transitions[current].append(next_char)
    return transitions

def draw_next_letter(transitions, current_ngram):
    if current_ngram not in transitions:
        return random.choice('abcdefghijklmnopqrstuvwxyz ')
    next_chars = transitions[current_ngram]
    freqs = {}
    for c in next_chars:
        freqs[c] = freqs.get(c, 0) + 1
    chars = list(freqs.keys())
    weights = list(freqs.values())
    return random.choices(chars, weights=weights, k=1)[0]


def main():
    n = 5

    # test_text = "In a small village hidden between vast green hills, there lived an old man named Eliot. Every morning, he would walk to the nearby river with a wooden bucket in hand, listening to the wind whispering through the trees. The villagers often wondered what he was doing there so early, yet no one dared to ask. One day, a curious boy followed Eliot and discovered that the old man was releasing tiny paper boats into the water. Each boat had a short message written on it—thoughts, wishes, memories. Eliot believed that the river would carry them to someone who needed those words. Inspired by his kindness, the villagers began writing their own messages, adding hope, love, and courage to the current. Over time, the river became a symbol of unity and healing, connecting strangers across distant lands. What began as a quiet ritual of one man turned into a tradition embraced by many, reminding everyone that even the smallest gesture can ripple through the world in unexpected and beautiful ways."
    test_text = read_text_from_file("tekst.txt")

    clean_text = prepare_data(test_text)

    transitions = build_transition_dict(clean_text, n)

    generated = "the village was a beautyful"

    for _ in range(100000):
        last_char = generated[-n:]
        next_char = draw_next_letter(transitions, last_char)
        generated += next_char

    print(generated)

if __name__ == "__main__":
    main()
