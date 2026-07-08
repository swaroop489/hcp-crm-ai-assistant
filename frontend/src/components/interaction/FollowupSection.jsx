import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { updateField } from '../../redux/slices/interactionSlice';
import TextArea from '../common/TextArea';

const FollowupSection = () => {
  const dispatch = useDispatch();
  const { outcomes, followUpActions } = useSelector(state => state.interaction);

  const handleChange = (e) => {
    dispatch(updateField({ field: e.target.name, value: e.target.value }));
  };

  return (
    <>
      <TextArea
        label="Outcomes"
        name="outcomes"
        value={outcomes}
        onChange={handleChange}
        placeholder="Key outcomes or agreements..."
        containerClassName="mb-4"
        className="h-20"
      />
      <div className="mb-6">
        <TextArea
          label="Follow-up Actions"
          name="followUpActions"
          value={followUpActions}
          onChange={handleChange}
          placeholder="Enter next steps or tasks..."
          className="h-20"
        />
        {followUpActions && (
          <div className="mt-2">
            <p className="text-xs font-semibold text-blue-700">AI Suggested Follow-ups:</p>
            <ul className="text-xs text-blue-600 list-disc ml-4 mt-1">
              <li>Schedule follow-up meeting in 2 weeks</li>
            </ul>
          </div>
        )}
      </div>
    </>
  );
};

export default FollowupSection;
