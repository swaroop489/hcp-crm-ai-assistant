import React from 'react';

const ChatBubble = ({ message }) => {
  const isUser = message.sender === 'user';
  return (
    <div className={`max-w-[85%] p-3 rounded-lg text-sm ${isUser ? 'bg-blue-600 text-white self-end rounded-br-none' : 'bg-white border border-gray-200 text-gray-800 self-start rounded-bl-none shadow-sm'}`}>
      {message.text}
    </div>
  );
};

export default ChatBubble;
