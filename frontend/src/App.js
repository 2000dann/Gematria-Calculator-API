import React, { useState } from 'react';
import './App.css';

function App() {
  const [result, setResult] = useState('');
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

  const calculateGematria = async () => {
    const text = document.getElementById('text').value;
    const method = document.getElementById('method').value;

    if (!text.trim()) {
      setError('Please enter some text.');
      return;
    }
    setError('');

    try {
      const response = await fetch(
        // `${API_URL}/gematria?text=${encodeURIComponent(text)}&system=${method}`
        `http://127.0.0.1:8000/gematria?text=${encodeURIComponent(text)}&system=${method}`
      );
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error('Error calculating Gematria:', error);
      setError('Failed to calculate Gematria. Please try again later.');
    }
  };

  const uploadFile = async () => {
    if (!file) {
      setError('Please select a file first.');
      return;
    }
    setError('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${API_URL}/upload/`, {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error('Error uploading file:', error);
      setError('Failed to upload file. Please try again later.');
    }
  };

  return (
    <div className="App">
      <h1>Gematria Calculator</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <textarea id="text" placeholder="Enter text..." />
      <select id="method">
        <option value="hebrew">Hebrew</option>
        <option value="english">English</option>
      </select>
      <button onClick={calculateGematria}>Calculate</button>
      <br />
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        accept=".txt"
      />
      <button onClick={uploadFile}>Upload File</button>
      <h3>Results:</h3>
      <pre>{result}</pre>
    </div>
  );
}

export default App;
