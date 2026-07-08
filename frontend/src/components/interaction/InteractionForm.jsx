import React from 'react';
import BasicInfoSection from './BasicInfoSection';
import DiscussionSection from './DiscussionSection';
import MaterialsSection from './MaterialsSection';
import SummarySection from './SummarySection';
import FollowupSection from './FollowupSection';

const InteractionForm = () => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-sm w-full h-full border border-gray-200 overflow-y-auto">
      <h2 className="text-lg font-semibold mb-6">Interaction Details</h2>
      <BasicInfoSection />
      <DiscussionSection />
      <MaterialsSection />
      <SummarySection />
      <FollowupSection />
    </div>
  );
};

export default InteractionForm;
