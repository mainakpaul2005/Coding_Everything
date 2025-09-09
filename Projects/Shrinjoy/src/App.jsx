import React, { useEffect, useState } from 'react';
import { initFirebase, APP_ID } from './firebase';
import { onAuthStateChanged, signInAnonymously, signInWithCustomToken } from 'firebase/auth';
import { doc, setDoc, serverTimestamp } from 'firebase/firestore';
import ToastProvider, { useToast } from './contexts/ToastContext';
import Header from './components/Header';
import FooterNav from './components/FooterNav';
import ReportForm from './components/ReportForm';
import ReportsList from './components/ReportsList';
import ReportProgress from './components/ReportProgress';
import Profile from './components/Profile';

function InnerApp() {
  const [db, setDb] = useState(null);
  const [auth, setAuth] = useState(null);
  const [user, setUser] = useState(null);
  const [active, setActive] = useState('report');
  const [selectedReport, setSelectedReport] = useState(null);
  const toast = useToast();

  useEffect(() => {
    const { auth: _auth, db: _db } = initFirebase();
    setDb(_db); setAuth(_auth);

    onAuthStateChanged(_auth, async (u) => {
      if (u) {
        setUser(u);
        try {
          const profileDocRef = doc(_db, 'artifacts', APP_ID, 'users', u.uid, 'profile', u.uid);
          await setDoc(profileDocRef, { uid: u.uid, displayName: u.displayName || null, email: u.email || null, photoURL: u.photoURL || null, lastLogin: serverTimestamp() }, { merge: true });
        } catch (err) {
          console.error('profile write failed', err);
        }
      } else {
        setUser(null);
      }
    });

    (async () => {
      if (!_auth.currentUser) {
        const token = process.env.REACT_APP_INITIAL_AUTH_TOKEN;
        try {
          if (token) await signInWithCustomToken(_auth, token);
          else await signInAnonymously(_auth);
        } catch (err) {
          console.error('sign-in failed, falling back to anonymous', err);
          try { await signInAnonymously(_auth); } catch (e) { console.error('anonymous sign-in also failed', e); toast.show('Authentication failed'); }
        }
      }
    })();

  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const showHelp = () => toast.show('Help section is not yet implemented!', 2000);

  return (
    <div className="flex flex-col min-h-screen">
      <Header onHelp={showHelp} />
      <main className="flex-grow">
        <div className="px-4 py-6">
          {active === 'report' && <ReportForm db={db} auth={auth} showToast={toast.show} appId={APP_ID} />}
          {active === 'myreports' && <ReportsList db={db} auth={auth} showToast={toast.show} onSelectReport={(r) => { setSelectedReport(r); setActive('progress'); }} appId={APP_ID} />}
          {active === 'progress' && <ReportProgress report={selectedReport} onBack={() => setActive('myreports')} />}
          {active === 'profile' && <Profile user={user} auth={auth} showToast={toast.show} />}
        </div>
      </main>
      <FooterNav active={active === 'progress' ? 'myreports' : active} onChange={(s) => { setActive(s); if (s !== 'progress') setSelectedReport(null); }} />
    </div>
  );
}

export default function App() {
  return (
    <ToastProvider>
      <InnerApp />
    </ToastProvider>
  );
}
