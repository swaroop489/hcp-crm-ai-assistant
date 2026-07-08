import React, { useState } from 'react';
import { Send } from 'lucide-react';
import Button from '../common/Button';

const ChatInput = ({ onSend, disabled }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSend = () => {
    if (inputValue.trim()) {
      onSend(inputValue.trim());
      setInputValue('');
    }
  };

  return (
    <div className="flex items-center gap-2 w-full">
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        placeholder="Describe interaction..."
        className="flex-1 border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
        disabled={disabled}
      />
      <Button onClick={handleSend} disabled={disabled || !inputValue.trim()} className="bg-blue-600 hover:bg-blue-700 text-white border-none">
        <Send className="w-4 h-4 mr-2" /> Send
      </Button>
    </div>
  );
};

export default ChatInput;
