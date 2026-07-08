import React from 'react';

const Select = ({ label, options, className = '', ...props }) => {
  return (
    <div className={className}>
      {label && <label className="block text-sm text-gray-600 mb-1">{label}</label>}
      <select
        className="w-full border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
        {...props}
      >
        {options.map((opt, idx) => (
          <option key={idx} value={opt.value || opt}>{opt.label || opt}</option>
        ))}
      </select>
    </div>
  );
};

export default Select;
