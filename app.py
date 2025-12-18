from flask import Flask, render_template, request, jsonify
from utils.pdf_processor import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.embedder import SimpleEmbedder
from utils.clusterer import cluster_papers

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_pdfs():
    try:
        files = request.files.getlist('pdfs')
        num_clusters = int(request.form.get('num_clusters', 5))
        summary_length = int(request.form.get('summary_length', 3))
        
        if not files:
            return jsonify({'error': 'No files uploaded'})
        
        papers_data = []
        all_texts = []
        
        # Extract text from all PDFs
        for file in files:
            if file.filename.endswith('.pdf'):
                text = extract_text_from_pdf(file)
                if text and not text.startswith('Error'):
                    papers_data.append({
                        'filename': file.filename,
                        'text': text
                    })
                    all_texts.append(text)
        
        if not papers_data:
            return jsonify({'error': 'No valid PDF files found'})
        
        # Create embeddings
        embedder = SimpleEmbedder()
        embedder.build_vocab(all_texts)
        
        for paper in papers_data:
            paper['embedding'] = embedder.get_embedding(paper['text'])
            paper['summary'] = summarize_text(paper['text'], summary_length)
        
        # Cluster papers
        clustered_papers = cluster_papers(papers_data, n_clusters=num_clusters)
        
        # Format response
        response = {
            'total_papers': len(papers_data),
            'num_topics': len(clustered_papers),
            'clusters': {}
        }
        
        for cluster_id, papers in clustered_papers.items():
            response['clusters'][cluster_id] = [
                {
                    'filename': p['filename'],
                    'summary': p['summary']
                }
                for p in papers
            ]
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)