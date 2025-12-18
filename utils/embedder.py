import numpy as np
import re
from collections import defaultdict

class SimpleEmbedder:
    def __init__(self):
        self.vocab = {}
        self.idf = {}
    
    def build_vocab(self, texts):
        """Build vocabulary and calculate IDF scores"""
        doc_freq = defaultdict(int)
        all_words = set()
        
        for text in texts:
            words = set(self.tokenize(text))
            all_words.update(words)
            for word in words:
                doc_freq[word] += 1
        
        self.vocab = {word: idx for idx, word in enumerate(sorted(all_words))}
        n_docs = len(texts)
        self.idf = {word: np.log(n_docs / (freq + 1)) for word, freq in doc_freq.items()}
    
    def tokenize(self, text):
        """Simple tokenization"""
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        words = [w for w in text.split() if len(w) > 3]
        return words
    
    def get_embedding(self, text):
        """Get TF-IDF embedding for text"""
        words = self.tokenize(text)
        vector = np.zeros(len(self.vocab))
        word_count = defaultdict(int)
        
        for word in words:
            word_count[word] += 1
        
        for word, count in word_count.items():
            if word in self.vocab:
                tf = count / len(words) if words else 0
                idx = self.vocab[word]
                vector[idx] = tf * self.idf.get(word, 0)
        
        norm = np.linalg.norm(vector)
        return vector / norm if norm > 0 else vector