// static/js/trail_tracking.js
var trailPath = L.geoJSON(); // Initialize an empty GeoJSON layer for the trail path
var isRecording = true;

function initializeMap() {
  map.on('locationfound', onLocationFound);
  map.on('locationerror', onLocationError);

  map.locate({ setView: true, maxZoom: 16, watch: true }); // Start watching the user's location

  map.addControl(new L.Control.Button({
    text: 'Pause',
    onClick: toggleRecording,
  }));
}

function onLocationFound(e) {
  if (isRecording) {
    var coords = [e.latitude, e.longitude];
    trailPath.addData({
      type: "Point",
      coordinates: coords
    });

    map.setView(coords);
  }
}

function onLocationError(e) {
  alert("Error getting location: " + e.message);
}

function toggleRecording() {
  isRecording = !isRecording;

  if (isRecording) {
    map.addControl(new L.Control.Button({
      text: 'Pause',
      onClick: toggleRecording,
    }));
  } else {
    map.addControl(new L.Control.Button({
      text: 'Resume',
      onClick: toggleRecording,
    }));
  }
}

// Call the initializeMap function when the document is ready
document.addEventListener('DOMContentLoaded', initializeMap);
