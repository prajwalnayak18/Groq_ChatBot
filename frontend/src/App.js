import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleAsk = async () => {
    try {
      const response = await axios.post('http://localhost:8000/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching answer:', error);
      setAnswer('Failed to get answer');
    }
  };

  return (
    <div className="App">
      <h1>Q&A Interface</h1>
      <div>
        <input
          type="text"
          placeholder="Enter your question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button onClick={handleAsk}>Ask</button>
      </div>
      {answer && (
        <div className="answer">
          <p><strong>Answer:</strong> {answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;

