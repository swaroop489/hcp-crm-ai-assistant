import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  messages: [
    {
      id: 'init-1',
      sender: 'ai',
      text: 'Log interaction details here (e.g., "Met Dr. Smith, discussed Product X efficacy, positive sentiment, shared brochure") or ask for help.'
    }
  ],
  isLoading: false,
  error: null,
};

export const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    addMessage: (state, action) => {
      state.messages.push(action.payload);
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
    clearChat: (state) => {
      state.messages = initialState.messages;
    }
  },
});

export const { addMessage, setLoading, setError, clearChat } = chatSlice.actions;
export default chatSlice.reducer;
