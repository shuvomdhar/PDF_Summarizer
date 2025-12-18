import re
from collections import defaultdict

def summarize_text(text, num_sentences=3):
    """Create extractive summary by selecting important sentences"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    if len(sentences) <= num_sentences:
        return ' '.join(sentences)
    
    # Score sentences by word frequency
    word_freq = defaultdict(int)
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence.lower())
        for word in words:
            if len(word) > 3:
                word_freq[word] += 1
    
    sentence_scores = []
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence.lower())
        score = sum(word_freq.get(word, 0) for word in words if len(word) > 3)
        sentence_scores.append((score, sentence))
    
    sentence_scores.sort(reverse=True)
    top_sentences = [sent for _, sent in sentence_scores[:num_sentences]]
    
    # Return in original order
    result = []
    for sentence in sentences:
        if sentence in top_sentences:
            result.append(sentence)
            if len(result) == num_sentences:
                break
    
    return '. '.join(result) + '.'