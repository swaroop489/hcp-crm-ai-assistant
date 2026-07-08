import api from './api';

export const chatService = {
  sendMessage: async (message, hcpId = null) => {
    try {
      const response = await api.post('/chat/', { message, hcp_id: hcpId });
      return response.data;
    } catch (error) {
      console.error('Chat error:', error);
      throw error;
    }
  }
};
