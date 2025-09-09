import React from 'react';

export default function FooterNav({ active, onChange }) {
  return (
    <footer className="footer-nav">
      <button onClick={() => onChange('report')} className={`footer-nav-btn ${active === 'report' ? 'active' : ''}`}>
        <i className="fas fa-bullhorn icon"></i>
        <span className="label">Report</span>
      </button>
      <button onClick={() => onChange('myreports')} className={`footer-nav-btn ${active === 'myreports' ? 'active' : ''}`}>
        <i className="fas fa-list-alt icon"></i>
        <span className="label">My Reports</span>
      </button>
      <button onClick={() => onChange('profile')} className={`footer-nav-btn ${active === 'profile' ? 'active' : ''}`}>
        <i className="fas fa-user-circle icon"></i>
        <span className="label">Profile</span>
      </button>
    </footer>
  );
}
