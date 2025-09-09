import React, { createContext, useContext, useState, useCallback } from 'react';

const ToastContext = createContext(null);

export function useToast() {
  return useContext(ToastContext);
}

export default function ToastProvider({ children }) {
  const [message, setMessage] = useState('');
  const [visible, setVisible] = useState(false);
  const show = useCallback((text, duration = 3000) => {
    setMessage(text);
    setVisible(true);
    setTimeout(() => setVisible(false), duration);
  }, []);

  return (
    <ToastContext.Provider value={{ show }}>
      {children}
      <div className={`message-box ${visible ? 'show' : ''}`} role="status">{message}</div>
    </ToastContext.Provider>
  );
}
