import numpy as np
from sklearn.cluster import KMeans
from collections import defaultdict

def cluster_papers(papers_data, n_clusters=5):
    """Cluster papers by topic using embeddings"""
    if len(papers_data) < n_clusters:
        n_clusters = len(papers_data)
    
    embeddings = [paper['embedding'] for paper in papers_data]
    embeddings_array = np.array(embeddings)
    
    if n_clusters > 1:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(embeddings_array)
    else:
        clusters = np.zeros(len(papers_data), dtype=int)
    
    # Group papers by cluster
    clustered_papers = defaultdict(list)
    for idx, cluster_id in enumerate(clusters):
        papers_data[idx]['cluster'] = int(cluster_id)
        clustered_papers[int(cluster_id)].append(papers_data[idx])
    
    return clustered_papers