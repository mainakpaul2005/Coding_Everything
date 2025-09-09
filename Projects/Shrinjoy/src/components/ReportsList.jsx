import React, { useEffect, useState } from 'react';
import { collection, query, onSnapshot } from 'firebase/firestore';

export default function ReportsList({ db, auth, showToast, onSelectReport, appId }) {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    if (!db || !auth || !auth.currentUser) return;
    const reportsRef = collection(db, 'artifacts', appId, 'users', auth.currentUser.uid, 'reports');
    const q = query(reportsRef);
    const unsub = onSnapshot(q, (qs) => {
      if (qs.empty) {
        setReports([]);
        return;
      }
      const arr = [];
      qs.forEach(d => arr.push({ id: d.id, ...d.data() }));
      setReports(arr);
    }, (err) => {
      console.error('reports snapshot error', err);
      showToast('Failed to load reports', 3000);
    });
    return () => unsub();
  }, [db, auth, showToast, appId]);

  function getIcon(issueType) {
    switch (issueType) {
      case 'pothole': return 'fa-road';
      case 'graffiti': return 'fa-paint-roller';
      case 'litter': return 'fa-trash';
      case 'streetlight': return 'fa-lightbulb';
      default: return 'fa-exclamation-circle';
    }
  }

  function getPriorityColor(priority) {
    switch (priority) {
      case 'low': return 'bg-green-500';
      case 'medium': return 'bg-yellow-500';
      case 'high': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  }

  return (
    <div className="container-box" id="myReportsSection">
      <h2 className="text-xl font-bold mb-4 text-gray-800">My Reports</h2>
      <div id="reportsList" className="space-y-4">
        {reports.length === 0 ? (
          <p id="noReportsMessage" className="text-center text-gray-500">You haven't submitted any reports yet.</p>
        ) : reports.map(r => (
          <div key={r.id} className="report-card" onClick={() => onSelectReport(r)}>
            <div className="flex items-center justify-between pb-2 mb-2 border-b border-gray-200">
              <div className="flex items-center space-x-4">
                <i className={`fas ${getIcon(r.issueType)} text-2xl text-purple-600`}></i>
                <div>
                  <h3 className="text-lg font-bold capitalize text-gray-800">{r.issueTitle}</h3>
                  <p className="text-xs text-gray-500">Submitted: {r.timestamp ? new Date(r.timestamp.toDate()).toLocaleDateString() : 'N/A'}</p>
                </div>
              </div>
              <div className={`status-container ${r.status.toLowerCase().replace(/\s/g,'-')}`}>
                <span className="font-semibold">{r.status}</span>
              </div>
            </div>
            <p className="text-sm text-gray-600 mt-1">{r.description}</p>
            {r.location?.address && <p className="text-xs text-gray-500 mt-1">Location: {r.location.address}</p>}
            <div className="flex space-x-2 mt-2">
              <span className={`text-xs font-semibold py-1 px-3 rounded-full text-white ${getPriorityColor(r.priority)}`}>{r.priority} Priority</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
