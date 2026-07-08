import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  hcpName: '',
  interactionType: 'Meeting',
  date: '',
  time: '',
  attendees: '',
  topicsDiscussed: '',
  materialsShared: '',
  samplesDistributed: '',
  sentiment: '',
  outcomes: '',
  followUpActions: '',
};

export const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    updateField: (state, action) => {
      const { field, value } = action.payload;
      if (field in state) {
        state[field] = value;
      }
    },
    resetForm: () => initialState,
    setFormData: (state, action) => {
      return { ...state, ...action.payload };
    },
  },
});

export const { updateField, resetForm, setFormData } = interactionSlice.actions;

export default interactionSlice.reducer;
