#Weston Albright
#Summer 2025
#Due on July 8th, 2025
#Instructor: Mark Panger


from collections import Counter

file_name = input("Enter your desired file: ")

try:
    with open(file_name, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        print("\nFile content:")
        print(content)

        #Character Count
        total_characters = len(content)

        #Line Count
        lines = content.splitlines()
        total_lines = len(lines)

        #Word Count
        words = content.split()
        total_words = len(words)
        
        #Unique Words
        unique_words = set(word.lower().strip(".,!?\"'()[]{}") for word in words if word)
        sorted_unique_words = sorted(unique_words)
        total_unique_words = len(sorted_unique_words)

        #2 Word Phrases
        normalized_words = [word.lower().strip(".,!?\"'(){}[]") for word in words if word]
        bigrams = zip(normalized_words, normalized_words[1:])
        bigram_counts = Counter(bigrams)
        repeated_bigrams = {pair: count for pair, count in bigram_counts.items() if count > 1}

        #Word Length (including Unique Words and Normal Words)
        if total_words > 0:
            avg_word_length = sum(len(word) for word in words) / total_words
        else:
            avg_word_length = 0
        if total_unique_words > 0:
            avg_unique_word_length = sum(len(word) for word in unique_words) / total_unique_words
        else:
            avg_unique_word_length = 0

        #File Write Information
        output_filename = "Analysis-" + file_name
        word_counts = Counter(normalized_words)
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(f"Line count: {total_lines}\n")
            outfile.write(f"Word count: {total_words}\n")
            outfile.write(f"Character count: {total_characters}\n\n")
            for word in sorted(word_counts):
                outfile.write(f"{word} ({word_counts[word]})\n")
            outfile.write("\nWord Pairs Appearing More Than Once:\n")
            for pair in sorted(repeated_bigrams):
                outfile.write(f"{pair[0]} {pair[1]} ({repeated_bigrams[pair]})\n")
            outfile.write("\nSummary Statistics:\n")
            outfile.write(f"Total Number Of Words: {total_words}\n")
            outfile.write(f"Average Length of Word: {avg_word_length:.2f}\n")
            outfile.write(f"Number of Unique Words: {total_unique_words}\n")
            outfile.write(f"Average Number of Letters in Unique Words: {avg_unique_word_length:.2f}\n")
            outfile.write(f"Number of Word Pairs That Appear More Than Once: {len(repeated_bigrams)}\n")

         
        #Print statements
        print(f"\nLine count: {total_lines}")
        print(f"Word count: {total_words}")
        print(f"Character count: {total_characters}")
        print("\nWord pairs that appear more than once:")
        for pair, count in sorted(repeated_bigrams.items()):
            print(f"{pair} ({count})")
        print("\nSummary Statistics:")
        print(f"Total number of words: {total_words}")
        print(f"Average length of word: {avg_word_length:.2f}")
        print(f"Number of unique words: {total_unique_words}")
        print(f"Average number of letters in unique words: {avg_unique_word_length:.2f}")
        print(f"Number of words pairs that appear more than once: {len(repeated_bigrams)}")
        
        #Error handling
except FileNotFoundError:
        print(f"Error: File {file_name} was not found or does not exist.")
except Exception as e:
        print(f"An error occured when reading the file: {e}")
