import React from 'react';

const SuggestedPrompts = ({ onSelect }) => {
  const prompts = [
    "I met with Dr. Smith today.",
    "Edit sentiment to negative.",
    "Recommend a follow-up action."
  ];

  return (
    <div className="flex flex-wrap gap-2 mb-3">
      {prompts.map((p, idx) => (
        <button 
          key={idx} 
          onClick={() => onSelect(p)}
          className="text-[10px] bg-blue-50 text-blue-600 border border-blue-200 px-2 py-1 rounded-full hover:bg-blue-100 transition-colors"
        >
          {p}
        </button>
      ))}
    </div>
  );
};

export default SuggestedPrompts;
