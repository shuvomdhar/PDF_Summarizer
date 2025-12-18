# 📚 PDF Research Paper Summarizer

A powerful Flask web application that automatically summarizes research papers and organizes them by topic using machine learning algorithms. Perfect for researchers, students, and anyone dealing with large volumes of academic papers.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📄 **Multiple PDF Upload**: Process multiple research papers simultaneously
- 🤖 **Smart Summarization**: Extractive summarization using advanced word frequency analysis
- 🏷️ **Topic Clustering**: Automatic grouping of papers by topic using TF-IDF embeddings and K-means clustering
- 🎨 **Modern UI**: Beautiful, responsive interface with real-time processing feedback
- 🚀 **No API Keys Required**: Works completely offline using built-in algorithms
- ⚡ **Fast Processing**: Efficient text extraction and analysis

## 🎯 Use Cases

- **Research Literature Review**: Quickly organize and summarize dozens of papers
- **Academic Study**: Get the gist of papers before deep diving
- **Topic Discovery**: Find patterns and themes across multiple documents
- **Time Saving**: Turn hours of reading into minutes of scanning

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone or download the repository:**
   ```bash
   cd PDF_Summarizer
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Start the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Upload and Process:**
   - Click "📄 Choose PDF Files" and select one or more PDF research papers
   - Configure settings:
     - **Topics**: Number of topic clusters (1-10)
     - **Summary Sentences**: Length of each summary (1-10 sentences)
   - Click "🚀 Process Papers"
   - Wait for processing (may take a moment for large files)
   - View your organized, summarized results by topic!

## 📁 Project Structure

```
PDF_Summarizer/
│
├── app.py                      # Main Flask application with routes
│
├── utils/                      # Utility modules
│   ├── __init__.py            # Package initializer
│   ├── pdf_processor.py       # PDF text extraction functions
│   ├── summarizer.py          # Text summarization algorithms
│   ├── embedder.py            # TF-IDF embedding generation
│   └── clusterer.py           # K-means clustering implementation
│
├── templates/                  # HTML templates
│   └── index.html             # Main user interface
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # Application styling
│   └── js/
│       └── main.js            # Frontend JavaScript logic
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this file)
└── .gitignore                 # Git ignore rules
```

## 🔧 Configuration

### Application Settings

Edit `app.py` to modify:

```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max file size (50MB)
app.run(debug=True, port=5000)  # Server port
```

### Processing Parameters

Adjust in the web interface:
- **Number of Topics**: How many clusters to group papers into (default: 5)
- **Summary Length**: Number of sentences per summary (default: 3)

## 🧠 How It Works

### 1. **PDF Text Extraction**
   - Uses PyPDF2 to extract text from uploaded PDF files
   - Handles multiple pages and various PDF formats

### 2. **Text Summarization**
   - Implements extractive summarization
   - Scores sentences based on word frequency
   - Selects most important sentences while maintaining original order

### 3. **TF-IDF Embeddings**
   - Builds vocabulary from all documents
   - Calculates Term Frequency-Inverse Document Frequency vectors
   - Creates semantic representations of each paper

### 4. **K-Means Clustering**
   - Groups papers with similar content together
   - Uses cosine similarity on embeddings
   - Automatically determines optimal clusters

## 📦 Dependencies

```
Flask==3.0.0          # Web framework
PyPDF2==3.0.1         # PDF text extraction
numpy==1.24.3         # Numerical computations
scikit-learn==1.3.0   # Machine learning algorithms
```

## 🎨 Interface Features

- **Drag & Drop Upload**: Easy file selection
- **Real-time Feedback**: Progress indicators during processing
- **Organized Display**: Papers grouped by discovered topics
- **Responsive Design**: Works on desktop and mobile devices
- **Clean Layout**: Easy-to-read summaries with paper titles

## 🔒 Privacy & Security

- All processing happens locally on your machine
- No data is sent to external servers
- No API keys or internet connection required
- Files are processed in memory only

## ⚠️ Limitations

- Maximum file size: 50MB per upload
- Works best with text-based PDFs (not scanned images)
- Summary quality depends on source text quality
- Clustering accuracy improves with more papers

## 🐛 Troubleshooting

### PDFs not processing correctly
- Ensure PDFs contain extractable text (not just images)
- Try reducing file size or number of files
- Check console for error messages

### Port already in use
```bash
# Change port in app.py
app.run(debug=True, port=5001)  # Use different port
```

### Missing dependencies
```bash
pip install --upgrade -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Here are ways you can help:

1. Report bugs and issues
2. Suggest new features
3. Improve documentation
4. Submit pull requests

## 📝 License

This project is for educational purposes only.

## 🙏 Acknowledgments

- Built with Flask web framework
- Uses scikit-learn for machine learning
- PyPDF2 for PDF processing
- Inspired by the need to manage large research paper collections

## 📧 Contact & Support

If you encounter any issues or have questions:
- Open an issue on the repository
- Check existing documentation
- Review troubleshooting section

## 🔮 Future Enhancements

- [ ] Support for more document formats (DOCX, TXT)
- [ ] Advanced NLP models for better summarization
- [ ] Export results to CSV/JSON
- [ ] Save and load previous sessions
- [ ] Batch processing for large collections
- [ ] Custom stopwords and filtering
- [ ] Interactive visualizations of topic relationships

---

**Made with ❤️ for researchers who have too many papers to read**

*Star ⭐ this repository if you find it helpful!*