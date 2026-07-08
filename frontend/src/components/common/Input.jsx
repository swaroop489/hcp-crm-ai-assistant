import React from 'react';

const Input = ({ label, className = '', ...props }) => {
  return (
    <div className={className}>
      {label && <label className="block text-sm text-gray-600 mb-1">{label}</label>}
      <input
        className="w-full border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
        {...props}
      />
    </div>
  );
};

export default Input;
