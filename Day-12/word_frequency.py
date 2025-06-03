def clean_text(text):
    punctuations = '.,!?;:"()[]{}-—\n'
    for p in punctuations:
        text = text.replace(p, ' ')
    return text.lower()

def word_frequency(text):
    text = clean_text(text)
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Example usage
if __name__ == "__main__":
    text = "HEllo hello this is me i am writing this to show everyone how much of code i can write"
    
    freq = word_frequency(text)

    for word, count in freq.items():
        print(f"{word}: {count}")
