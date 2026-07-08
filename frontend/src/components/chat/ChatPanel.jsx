import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { MessageCircle } from 'lucide-react';
import ChatBubble from './ChatBubble';
import ChatInput from './ChatInput';
import TypingIndicator from './TypingIndicator';
import { chatService } from '../../services/chatService';
import { addMessage, setLoading, setError } from '../../redux/slices/chatSlice';

const ChatPanel = () => {
  const dispatch = useDispatch();
  const { messages, isLoading } = useSelector(state => state.chat);
  const { selectedHcp } = useSelector(state => state.hcp);

  const handleSend = async (text) => {
    dispatch(addMessage({ id: Date.now().toString(), sender: 'user', text }));
    dispatch(setLoading(true));
    dispatch(setError(null));

    try {
      const hcpId = selectedHcp ? selectedHcp.id : null;
      const data = await chatService.sendMessage(text, hcpId);
      
      dispatch(addMessage({ id: Date.now().toString(), sender: 'ai', text: data.response }));
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
