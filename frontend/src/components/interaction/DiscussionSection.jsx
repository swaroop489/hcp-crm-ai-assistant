import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { updateField } from '../../redux/slices/interactionSlice';
import { Mic } from 'lucide-react';
import TextArea from '../common/TextArea';
import Button from '../common/Button';

const DiscussionSection = () => {
  const dispatch = useDispatch();
  const topicsDiscussed = useSelector(state => state.interaction.topicsDiscussed);

  const handleChange = (e) => {
    dispatch(updateField({ field: e.target.name, value: e.target.value }));
  };

  return (
    <div className="mb-4">
      <div className="relative">
        <TextArea
          label="Topics Discussed"
          name="topicsDiscussed"
          value={topicsDiscussed}
          onChange={handleChange}
          placeholder="Enter key discussion points..."
          className="h-24"
        />
        <Mic className="absolute bottom-3 right-3 text-gray-400 w-4 h-4 cursor-pointer hover:text-blue-500" />
      </div>
      <Button variant="secondary" className="mt-2 text-xs py-1.5 px-3">
        <span className="mr-2 text-lg">✨</span> Summarize from Voice Note (Requires Consent)
      </Button>
    </div>
  );
};

export default DiscussionSection;
