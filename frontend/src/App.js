import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('Click the button to call the backend!');
  const [loading, setLoading] = useState(false);

  const handleButtonClick = async () => {
    setLoading(true);
    setMessage('Calling backend...');

    try {
      // Get backend URL from environment variable
      const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      console.log('🌐 Calling backend at:', API_URL);

      // Make a POST request to the FastAPI backend
      const response = await fetch(`${API_URL}/open-image`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await response.json();

      if (data.success) {
        setMessage(`✅ Success! ${data.message}`);
      } else {
        setMessage(`❌ Error: ${data.message}`);
      }
    } catch (error) {
      setMessage(`❌ Network Error: ${error.message}`);
      console.error('Error calling backend:', error);
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Client-Server Communication Demo</h1>
        <div className="container">
          <button
            onClick={handleButtonClick}
            disabled={loading}
            className="action-button"
          >
            {loading ? 'Processing...' : 'Open Server Image'}
          </button>
          <div className="message">
            {message}
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;