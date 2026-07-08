import React from 'react';

const TypingIndicator = () => {
  return (
    <div className="bg-white border border-gray-200 text-gray-500 self-start rounded-lg p-3 text-sm rounded-bl-none shadow-sm animate-pulse flex items-center space-x-1">
      <div className="w-1.5 h-1.5 bg-gray-400 rounded-full"></div>
      <div className="w-1.5 h-1.5 bg-gray-400 rounded-full"></div>
      <div className="w-1.5 h-1.5 bg-gray-400 rounded-full"></div>
    </div>
  );
};

export default TypingIndicator;
