const fileInput = document.getElementById('pdfFiles');
const fileInfo = document.getElementById('fileInfo');
const processBtn = document.getElementById('processBtn');

fileInput.addEventListener('change', function () {
    const count = this.files.length;
    if (count > 0) {
        fileInfo.textContent = `${count} file(s) selected`;
        processBtn.disabled = false;
    } else {
        fileInfo.textContent = 'No files selected';
        processBtn.disabled = true;
    }
});

async function processPDFs() {
    const files = fileInput.files;
    if (files.length === 0) {
        alert('Please select PDF files first');
        return;
    }

    const numClusters = document.getElementById('numClusters').value;
    const summaryLength = document.getElementById('summaryLength').value;

    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    processBtn.disabled = true;

    const formData = new FormData();
    for (let file of files) {
        formData.append('pdfs', file);
    }
    formData.append('num_clusters', numClusters);
    formData.append('summary_length', summaryLength);

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        displayResults(data);
    } catch (error) {
        alert('Error processing PDFs: ' + error.message);
    } finally {
        document.getElementById('loading').style.display = 'none';
        processBtn.disabled = false;
    }
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (data.error) {
        resultsDiv.innerHTML = `<div class="paper-card"><p style="color: red;">Error: ${data.error}</p></div>`;
        resultsDiv.style.display = 'block';
        return;
    }

    // Display stats
    const statsHTML = `
        <div class="stats">
            <span>📄 Total Papers: ${data.total_papers}</span>
            <span>🏷️ Topics: ${data.num_topics}</span>
        </div>
    `;
    resultsDiv.innerHTML = statsHTML;

    // Display clustered papers
    const clusters = data.clusters;
    for (let clusterId in clusters) {
        const papers = clusters[clusterId];
        let clusterHTML = `
            <div class="topic-cluster">
                <h2>📑 Topic ${parseInt(clusterId) + 1} (${papers.length} papers)</h2>
        `;

        papers.forEach(paper => {
            clusterHTML += `
                <div class="paper-card">
                    <div class="paper-title">${paper.filename}</div>
                    <div class="paper-summary">${paper.summary}</div>
                </div>
            `;
        });

        clusterHTML += '</div>';
        resultsDiv.innerHTML += clusterHTML;
    }

    resultsDiv.style.display = 'block';
}