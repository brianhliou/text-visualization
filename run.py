import os
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def gather_texts_from_directory(dir_path):
    """Gather all texts from the specified directory."""
    all_texts = ''
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):  # make sure to process only text files
            with open(os.path.join(dir_path, filename), 'r') as file:
                all_texts += file.read() + '\n'
    return all_texts

def create_word_cloud(text):
    """Generate a word cloud from the specified text."""
    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=set(['the', 'of', 'and', 'to', 'in']), min_font_size=10).generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

def create_frequency_distribution(text):
    """Generate a frequency distribution from the specified text."""
    words = text.split()
    freq_dist = defaultdict(int)
    
    for word in words:
        freq_dist[word.lower()] += 1  # Convert to lowercase to avoid counting same word in different cases
    
    # Sort by frequency
    sorted_freq_dist = sorted(freq_dist.items(), key=lambda item: item[1], reverse=True)
    
    # For better visualization, let's take the top 20 words
    top_words, top_counts = zip(*sorted_freq_dist[:20])
    
    plt.figure(figsize=(15, 10))
    plt.bar(top_words, top_counts, color='blue')
    plt.xticks(rotation=45)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title('Top 20 Most Frequent Words')
    plt.show()

def main():
    directory_path = "./resources/"
    all_texts = gather_texts_from_directory(directory_path)
    
    create_word_cloud(all_texts)
    create_frequency_distribution(all_texts)

if __name__ == '__main__':
    main()
