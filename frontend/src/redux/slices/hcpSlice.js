import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { interactionService } from '../../services/interactionService';

export const fetchHcps = createAsyncThunk('hcp/fetchHcps', async () => {
  const response = await interactionService.getHcps();
  return response;
});

const initialState = {
  list: [],
  selectedHcp: null,
  status: 'idle', // 'idle' | 'loading' | 'succeeded' | 'failed'
};

export const hcpSlice = createSlice({
  name: 'hcp',
  initialState,
  reducers: {
    selectHcp: (state, action) => {
      state.selectedHcp = action.payload;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchHcps.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchHcps.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.list = action.payload;
      })
      .addCase(fetchHcps.rejected, (state) => {
        state.status = 'failed';
      });
  },
});

export const { selectHcp } = hcpSlice.actions;
export default hcpSlice.reducer;
