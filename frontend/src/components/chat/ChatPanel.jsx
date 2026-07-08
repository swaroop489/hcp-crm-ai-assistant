import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { MessageCircle } from 'lucide-react';
import ChatBubble from './ChatBubble';
import ChatInput from './ChatInput';
import TypingIndicator from './TypingIndicator';
import { chatService } from '../../services/chatService';
import { addMessage, setLoading, setError } from '../../redux/slices/chatSlice';
import { setFormData } from '../../redux/slices/interactionSlice';
import { selectHcp } from '../../redux/slices/hcpSlice';

const ChatPanel = () => {
  const dispatch = useDispatch();
  const { messages, isLoading } = useSelector(state => state.chat);
  const { list: hcps, selectedHcp } = useSelector(state => state.hcp);

  const handleSend = async (text) => {
    dispatch(addMessage({ id: Date.now().toString(), sender: 'user', text }));
    dispatch(setLoading(true));
    dispatch(setError(null));

    try {
      const hcpId = selectedHcp ? selectedHcp.id : null;
      const data = await chatService.sendMessage(text, hcpId);
      
      dispatch(addMessage({ id: Date.now().toString(), sender: 'ai', text: data.response }));
      
      // Map python snake_case to frontend camelCase
      if (data.updated_state && data.updated_state.form_data) {
        const formData = data.updated_state.form_data;
        const mappedData = {};
        
        // Auto-select HCP if AI found one
        if (formData.hcp_id) {
            const foundHcp = hcps.find(h => h.id === formData.hcp_id);
            if (foundHcp) {
                dispatch(selectHcp(foundHcp));
                mappedData.hcpName = foundHcp.name;
            }
        }
        if (formData.interaction_type) mappedData.interactionType = formData.interaction_type;
        if (formData.date) mappedData.date = formData.date;
        if (formData.time) mappedData.time = formData.time;
        if (formData.topics_discussed) mappedData.topicsDiscussed = formData.topics_discussed;
        if (formData.sentiment) mappedData.sentiment = formData.sentiment.charAt(0).toUpperCase() + formData.sentiment.slice(1);
        if (formData.materials_shared) mappedData.materialsShared = formData.materials_shared;
        if (formData.outcomes) mappedData.outcomes = formData.outcomes;
        if (formData.follow_up_actions) mappedData.followUpActions = formData.follow_up_actions;
        
        if (Object.keys(mappedData).length > 0) {
           dispatch(setFormData(mappedData));
        }
      }
    } catch (err) {
      dispatch(setError('Failed to reach AI.'));
      dispatch(addMessage({ id: Date.now().toString(), sender: 'ai', text: 'Error: Could not connect to AI Agent.' }));
    } finally {
      dispatch(setLoading(false));
    }
  };

  return (
    <div className="flex flex-col h-full bg-white rounded-lg shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200 flex items-center">
        <MessageCircle className="w-5 h-5 text-blue-600 mr-2" />
        <div>
          <h2 className="text-sm font-semibold">AI Assistant</h2>
          <p className="text-xs text-gray-500">Log interaction via chat</p>
        </div>
      </div>

      <div className="flex-1 p-4 overflow-y-auto bg-gray-50 flex flex-col gap-3">
        {messages.map((msg) => (
          <ChatBubble key={msg.id} message={msg} />
        ))}
        {isLoading && <TypingIndicator />}
      </div>

      <div className="p-4 border-t border-gray-200 bg-white">
        <ChatInput onSend={handleSend} disabled={isLoading} />
      </div>
    </div>
  );
};

export default ChatPanel;
