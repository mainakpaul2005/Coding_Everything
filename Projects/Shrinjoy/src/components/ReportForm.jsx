import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import { collection, addDoc, serverTimestamp } from 'firebase/firestore';

export default function ReportForm({ db, auth, showToast, appId }) {
  const mapRef = useRef(null);
  const mapInstanceRef = useRef(null);
  const markerRef = useRef(null);
  const [currentLat, setCurrentLat] = useState(34.0522);
  const [currentLng, setCurrentLng] = useState(-118.2437);
  const [lastSearchQuery, setLastSearchQuery] = useState('');
  const [photoPreview, setPhotoPreview] = useState(null);

  useEffect(() => {
    // initialize map
    function initializeMap(lat, lng) {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove();
      }
      const map = L.map(mapRef.current).setView([lat, lng], 16);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '© OpenStreetMap contributors' }).addTo(map);
      const marker = L.marker([lat, lng], { draggable: true }).addTo(map);
      marker.on('dragend', async (event) => {
        const latlng = event.target.getLatLng();
        setCurrentLat(latlng.lat);
        setCurrentLng(latlng.lng);
        showToast('Location updated! Finding address...', 2000);
        try {
          const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latlng.lat}&lon=${latlng.lng}`);
          const data = await res.json();
          const input = document.getElementById('locationAddress');
          if (data && data.display_name) {
            input.value = data.display_name;
            showToast('Address auto-filled!', 2000);
          } else {
            input.value = '';
            showToast('No address found for this location.', 2000);
          }
        } catch (err) {
          console.error('Reverse geocode failed', err);
          showToast('Failed to find address. Please enter manually.', 2000);
        }
      });
      mapInstanceRef.current = map;
      markerRef.current = marker;
    }

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        setCurrentLat(position.coords.latitude);
        setCurrentLng(position.coords.longitude);
        initializeMap(position.coords.latitude, position.coords.longitude);
      }, () => {
        initializeMap(currentLat, currentLng);
      });
    } else {
      initializeMap(currentLat, currentLng);
    }

    return () => {
      if (mapInstanceRef.current) mapInstanceRef.current.remove();
    };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Geocode suggestions
  let geocodeTimeout = null;
  const geocode = async (query) => {
    if (!query || query.length < 3) return;
    if (query === lastSearchQuery) return;
    setLastSearchQuery(query);
    try {
      const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&countrycodes=us,ca,in&limit=5`);
      const data = await res.json();
      const datalist = document.getElementById('location-suggestions');
      datalist.innerHTML = '';
      data.forEach(item => {
        const option = document.createElement('option');
        option.value = item.display_name;
        option.dataset.lat = item.lat;
        option.dataset.lon = item.lon;
        datalist.appendChild(option);
      });
    } catch (err) {
      console.error('Geocode failed', err);
    }
  };

  window.updateMapWithLocation = (lat, lng) => {
    if (!mapInstanceRef.current || !markerRef.current) return;
    const latf = parseFloat(lat);
    const lngf = parseFloat(lng);
    setCurrentLat(latf);
    setCurrentLng(lngf);
    mapInstanceRef.current.setView([latf, lngf], 16);
    markerRef.current.setLatLng([latf, lngf]);
  };

  useEffect(() => {
    const input = document.getElementById('locationAddress');
    const onInput = () => {
      clearTimeout(geocodeTimeout);
      geocodeTimeout = setTimeout(() => geocode(input.value), 500);
    };
    const onChange = () => {
      const datalist = document.getElementById('location-suggestions');
      const option = Array.from(datalist.options).find(o => o.value === input.value);
      if (option) {
        window.updateMapWithLocation(option.dataset.lat, option.dataset.lon);
      }
    };
    input.addEventListener('input', onInput);
    input.addEventListener('change', onChange);
    return () => {
      input.removeEventListener('input', onInput);
      input.removeEventListener('change', onChange);
    };
  }, []);

  const handlePhoto = (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (ev) => {
      setPhotoPreview(ev.target.result);
    };
    reader.readAsDataURL(file);
  };

  const handleSubmit = async (ev) => {
    ev.preventDefault();
    if (!db || !auth || !auth.currentUser) {
      showToast('Please wait for authentication to be ready or sign in.', 4000);
      return;
    }

    const form = ev.target;
    const newReport = {
      issueType: form.issueType.value,
      issueTitle: form.issueTitle.value,
      priority: form.priority.value,
      description: form.description.value,
      location: { lat: currentLat, lng: currentLng, address: form.locationAddress.value },
      contact: { name: form.contactName.value, email: form.contactEmail.value },
      status: 'Submitted',
      timestamp: serverTimestamp(),
      userId: auth.currentUser.uid
    };

    try {
      const userReportsRef = collection(db, 'artifacts', appId, 'users', auth.currentUser.uid, 'reports');
      await addDoc(userReportsRef, newReport);
      showToast('Your report has been submitted!', 3000);
      form.reset();
      setPhotoPreview(null);
    } catch (err) {
      console.error('Error adding doc', err);
      showToast('Error submitting report. Please try again.', 4000);
    }
  };

  return (
    <div className="container-box" id="reportSection">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Report an Issue</h2>
      <form id="reportForm" onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="issueType" className="block text-sm font-medium text-gray-700 mb-1">Issue Type</label>
          <select id="issueType" name="issueType" required className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm">
            <option value="">Select an issue type...</option>
            <option value="pothole">Pothole</option>
            <option value="graffiti">Graffiti</option>
            <option value="litter">Litter</option>
            <option value="streetlight">Streetlight Outage</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div>
          <label htmlFor="issueTitle" className="block text-sm font-medium text-gray-700 mb-1">Issue Title</label>
          <input id="issueTitle" name="issueTitle" required placeholder="e.g., Pothole on Main Street" className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm" />
        </div>
        <div>
          <label htmlFor="priority" className="block text-sm font-medium text-gray-700 mb-1">Priority Level</label>
          <select id="priority" name="priority" required className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm">
            <option value="">Select priority...</option>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </div>
        <div>
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">Description</label>
          <textarea id="description" name="description" rows="4" required className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm" placeholder="Describe the issue in detail..."></textarea>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Photo (Optional)</label>
          <div className="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer hover:border-purple-500" onClick={() => document.getElementById('photoInput').click()}>
            <div className="space-y-1 text-center">
              <i className="fas fa-camera text-4xl text-gray-400"></i>
              <div className="flex text-sm text-gray-600">
                <span className="relative font-medium text-purple-600">Upload a photo</span>
                <p className="pl-1">or drag and drop</p>
              </div>
              <p className="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
            </div>
          </div>
          <input id="photoInput" name="photo" type="file" className="hidden" accept="image/*" onChange={handlePhoto} />
          {photoPreview && (
            <div id="photoPreview" className="mt-4">
              <img id="previewImage" src={photoPreview} className="rounded-lg max-h-48 w-auto" alt="preview" />
            </div>
          )}
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Location</label>
          <div id="map" ref={mapRef} className="mt-1 rounded-lg"></div>
          <p className="text-xs text-gray-500 mt-2">Drag the marker to pinpoint the exact location.</p>
          <label htmlFor="locationAddress" className="block text-sm font-medium text-gray-700 mb-1 mt-4">Address or Landmark</label>
          <input id="locationAddress" name="locationAddress" list="location-suggestions" className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm" placeholder="e.g., 123 Main Street" />
          <datalist id="location-suggestions"></datalist>
        </div>
        <div>
          <label htmlFor="contactName" className="block text-sm font-medium text-gray-700 mb-1">Contact Name (Optional)</label>
          <input id="contactName" name="contactName" className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm" placeholder="Your name" />
        </div>
        <div>
          <label htmlFor="contactEmail" className="block text-sm font-medium text-gray-700 mb-1">Contact Email (Optional)</label>
          <input id="contactEmail" name="contactEmail" type="email" className="mt-1 block w-full px-3 py-2 main-input rounded-lg shadow-sm" placeholder="you@example.com" />
        </div>
        <button type="submit" className="w-full flex justify-center py-3 px-4 rounded-lg shadow-lg text-lg font-medium text-white submit-btn">Submit Report</button>
      </form>
    </div>
  );
}
