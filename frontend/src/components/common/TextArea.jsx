import React from 'react';

const TextArea = ({ label, className = '', containerClassName = '', ...props }) => {
  return (
    <div className={containerClassName}>
      {label && <label className="block text-sm text-gray-600 mb-1">{label}</label>}
      <textarea
        className={`w-full border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 resize-none ${className}`}
        {...props}
      ></textarea>
    </div>
  );
};

export default TextArea;
