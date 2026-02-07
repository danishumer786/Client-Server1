import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('Ready to test backend connection!');
  const [loading, setLoading] = useState(false);

  const handleButtonClick = async () => {
    setLoading(true);
    setMessage('🔄 Connecting to backend...');

    try {
      // Smart environment detection
      const isLocalhost = window.location.hostname === 'localhost';
      const API_URL = isLocalhost
        ? 'http://localhost:8000'
        : 'https://client-server-backend-gbatq5e8g8g3a9hk.westus2-01.azurewebsites.net';

      console.log('🌐 Environment:', isLocalhost ? 'Development' : 'Production');
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
        setMessage(`🎉 ${data.message}`);
      } else {
        setMessage(`❌ Error: ${data.message}`);
      }
    } catch (error) {
      setMessage(`❌ Network Error: Failed to fetch`);
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
            {loading ? 'Testing Connection...' : 'Test Backend Connection'}
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