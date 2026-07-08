import React from 'react';
import { useSelector } from 'react-redux';
import { Search, PlusCircle } from 'lucide-react';

const MaterialsSection = () => {
  const { materialsShared, samplesDistributed } = useSelector(state => state.interaction);

  return (
    <div className="mb-4">
      <label className="block text-sm font-semibold mb-2 text-gray-700">Materials Shared / Samples Distributed</label>
      <div className="border border-gray-200 rounded-md p-4 mb-2">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-gray-600">Materials Shared</span>
          <button className="flex items-center text-sm border border-gray-300 rounded px-2 py-1 hover:bg-gray-50 text-gray-600">
            <Search className="w-3 h-3 mr-1" /> Search/Add
          </button>
        </div>
        {materialsShared ? (
          <p className="text-sm text-gray-800">{materialsShared}</p>
        ) : (
          <p className="text-sm text-gray-400 italic">No materials added.</p>
        )}
      </div>
      <div className="border border-gray-200 rounded-md p-4">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-gray-600">Samples Distributed</span>
          <button className="flex items-center text-sm border border-gray-300 rounded px-2 py-1 hover:bg-gray-50 text-gray-600">
            <PlusCircle className="w-3 h-3 mr-1" /> Add Sample
          </button>
        </div>
        {samplesDistributed ? (
          <p className="text-sm text-gray-800">{samplesDistributed}</p>
        ) : (
          <p className="text-sm text-gray-400 italic">No samples added.</p>
        )}
      </div>
    </div>
  );
};

export default MaterialsSection;
