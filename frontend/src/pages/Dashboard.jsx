import React from 'react';
import InteractionForm from '../components/interaction/InteractionForm';
import ChatPanel from '../components/chat/ChatPanel';

const Dashboard = () => {
  return (
    <div className="flex gap-6 h-[calc(100vh-6rem)] w-full">
      <div className="flex-[2] h-full overflow-hidden">
        <InteractionForm />
      </div>
      <div className="flex-[1] h-full overflow-hidden">
        <ChatPanel />
      </div>
    </div>
  );
};

export default Dashboard;
