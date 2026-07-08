import api from './api';

export const interactionService = {
  getInteraction: async (id) => {
    const response = await api.get(`/interaction/${id}`);
    return response.data;
  },
  getHcps: async () => {
    const response = await api.get('/hcp/');
    return response.data;
  }
};
