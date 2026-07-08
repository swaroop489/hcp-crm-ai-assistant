import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { updateField } from '../../redux/slices/interactionSlice';
import { fetchHcps, selectHcp } from '../../redux/slices/hcpSlice';
import Input from '../common/Input';
import Select from '../common/Select';
import { INTERACTION_TYPES } from '../../utils/constants';

const BasicInfoSection = () => {
  const dispatch = useDispatch();
  const formData = useSelector(state => state.interaction);
  const { list: hcps, status } = useSelector(state => state.hcp);

  useEffect(() => {
    if (status === 'idle') {
      dispatch(fetchHcps());
    }
  }, [status, dispatch]);

  const handleChange = (e) => {
    dispatch(updateField({ field: e.target.name, value: e.target.value }));
    if (e.target.name === 'hcpName') {
      const selected = hcps.find(h => h.name === e.target.value);
      if (selected) dispatch(selectHcp(selected));
    }
  };

  return (
    <div className="grid grid-cols-2 gap-4 mb-4">
      <div>
        <label className="block text-sm text-gray-600 mb-1">HCP Name</label>
        <select
          name="hcpName"
          value={formData.hcpName}
          onChange={handleChange}
          className="w-full border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
        >
          <option value="">Select an HCP...</option>
          {hcps.map(hcp => (
            <option key={hcp.id} value={hcp.name}>{hcp.name} - {hcp.specialization}</option>
          ))}
        </select>
      </div>
      <Select
        label="Interaction Type"
        name="interactionType"
        value={formData.interactionType}
        onChange={handleChange}
        options={INTERACTION_TYPES}
      />
      <Input
        type="date"
        label="Date"
        name="date"
        value={formData.date}
        onChange={handleChange}
      />
      <Input
        type="time"
        label="Time"
        name="time"
        value={formData.time}
        onChange={handleChange}
      />
      <Input
        type="text"
        label="Attendees"
        name="attendees"
        value={formData.attendees}
        onChange={handleChange}
        placeholder="Enter names or search..."
        className="col-span-2"
      />
    </div>
  );
};

export default BasicInfoSection;
