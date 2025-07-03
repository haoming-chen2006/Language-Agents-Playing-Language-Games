const { useState } = React;

function App() {
  const initialAIMessages = [
    "Think of a character, I'll try to guess.",
    "Is your character real?",
    "Is your character from a movie?",
    "Is your character animated?",
    "My final guess is that your character is Mickey Mouse."
  ];
  const [messages, setMessages] = useState([
    { from: 'ai', text: initialAIMessages[0] }
  ]);
  const [aiIndex, setAiIndex] = useState(1);
  const [input, setInput] = useState('');

  function sendMessage(e) {
    if (e.key !== 'Enter') return;
    if (!input.trim()) return;
    const userMsg = { from: 'user', text: input.trim() };
    setMessages(prev => {
      const newMsgs = [...prev, userMsg];
      if (aiIndex < initialAIMessages.length) {
        newMsgs.push({ from: 'ai', text: initialAIMessages[aiIndex] });
      }
      return newMsgs;
    });
    if (aiIndex < initialAIMessages.length) {
      setAiIndex(aiIndex + 1);
    }
    setInput('');
  }

  return (
    React.createElement('div', null,
      React.createElement('h1', null, 'Akinator Chat'),
      React.createElement('div', { id: 'chat' },
        messages.map((m, i) =>
          React.createElement('div', { key: i, className: 'msg ' + m.from }, m.text)
        )
      ),
      React.createElement('input', {
        type: 'text',
        value: input,
        id: 'input',
        onChange: e => setInput(e.target.value),
        onKeyDown: sendMessage,
        placeholder: 'Type here...'
      })
    )
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(React.createElement(App));
