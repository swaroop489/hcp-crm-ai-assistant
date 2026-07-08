import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { updateField } from '../../redux/slices/interactionSlice';
import { SENTIMENT_OPTIONS } from '../../utils/constants';

const SummarySection = () => {
  const dispatch = useDispatch();
  const sentiment = useSelector(state => state.interaction.sentiment);

  const handleChange = (e) => {
    dispatch(updateField({ field: e.target.name, value: e.target.value }));
  };

  return (
    <div className="mb-4">
      <label className="block text-sm font-semibold mb-2 text-gray-700">Observed/Inferred HCP Sentiment</label>
      <div className="flex gap-6">
        {SENTIMENT_OPTIONS.map((opt) => (
          <label key={opt.value} className="flex items-center text-sm cursor-pointer text-gray-600">
            <input 
              type="radio" 
              name="sentiment" 
              value={opt.value} 
              checked={sentiment === opt.value} 
              onChange={handleChange} 
              className="mr-2" 
            />
            {opt.emoji} {opt.label}
          </label>
        ))}
      </div>
    </div>
  );
};

export default SummarySection;
