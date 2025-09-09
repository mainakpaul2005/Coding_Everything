import React from 'react';
import { signOut } from 'firebase/auth';

export default function Profile({ user, auth, showToast }) {
  return (
    <div className="container-box" id="profileSection">
      <h2 className="text-xl font-bold mb-4 text-gray-800">My Profile</h2>
      <div id="userInfo" className="flex flex-col items-center text-center p-4 profile-section-bg rounded-lg space-y-4">
        <img id="profileImage" src={user?.photoURL || 'https://placehold.co/100x100/e2e8f0/718096?text=U'} className="w-24 h-24 profile-img-container" alt="profile" />
        <h3 id="profileName" className="text-xl font-semibold text-gray-800">{user?.displayName || 'Not Signed In'}</h3>
        <p id="profileEmail" className="text-sm text-gray-600">{user?.email || 'Sign in to save your reports'}</p>
        <p className="text-xs text-gray-500 break-all">User ID: <span id="profileId" className="font-mono text-gray-700">{user?.uid || 'N/A'}</span></p>
        <button onClick={async () => {
          if (!auth || !auth.currentUser) { showToast('You are not signed in.', 2000); return; }
          try { await signOut(auth); showToast('Signed out successfully!', 3000); } catch (err) { console.error(err); showToast('Sign-out failed. Please try again.', 4000); }
        }} className="w-full flex justify-center py-2 px-4 rounded-lg shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 transition-all duration-200">Sign Out</button>
      </div>
    </div>
  );
}
