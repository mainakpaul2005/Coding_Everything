import React from 'react';

export default function ReportProgress({ report, onBack }) {
  if (!report) return null;
  return (
    <div className="container-box" id="reportProgressSection">
      <button onClick={onBack} className="flex items-center text-sm font-medium text-gray-500 mb-4 transition-colors duration-200 hover:text-gray-900">
        <i className="fas fa-arrow-left mr-2"></i> Back to My Reports
      </button>
      <div id="progressContent">
        <h2 className="text-2xl font-bold mb-4 text-gray-800">{report.issueTitle}</h2>
        <p className="text-sm font-medium text-gray-700 mb-4">{report.description}</p>
        <h3 className="text-xl font-bold mb-4 text-gray-800">Progress Timeline</h3>
        <div className="timeline-container">
          <div className={`timeline-item ${['Submitted','In Progress','Resolved'].includes(report.status) ? 'active' : ''}`}>
            <div className="timeline-icon"><i className="fas fa-paper-plane"></i></div>
            <span className="timeline-text">Report Submitted</span>
          </div>
          <div className={`timeline-item ${['In Progress','Resolved'].includes(report.status) ? 'active' : ''}`}>
            <div className="timeline-icon"><i className="fas fa-cogs"></i></div>
            <span className="timeline-text">In Progress</span>
          </div>
          <div className={`timeline-item ${report.status === 'Resolved' ? 'active' : ''}`}>
            <div className="timeline-icon"><i className="fas fa-check-circle"></i></div>
            <span className="timeline-text">Issue Resolved</span>
          </div>
        </div>
      </div>
    </div>
  );
}
