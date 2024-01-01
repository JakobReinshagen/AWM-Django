// static/js/trail_tracking.js
var trailPath = L.geoJSON(); // Initialize an empty GeoJSON layer for the trail path
var isRecording = true;

function initializeMap() {
    map.on('locationfound', onLocationFound);
    map.on('locationerror', onLocationError);

    // Check if there is a trail ID in the URL (assuming the trail ID is in the URL, modify accordingly)
    var trailId = getTrailIdFromUrl();

    if (trailId) {
        // Fetch trail data from the server
        fetchTrailPath(trailId);
    } else {
        // Start watching the user's location
        map.locate({ setView: true, maxZoom: 16, watch: true });
    }

    // Add the trailPath layer to the map
    trailPath.addTo(map);
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

function getTrailIdFromUrl() {
   var currentUrl = window.location.href;
    var regexPattern = /\/trail\/(\d+)\/?/;
    var matches = currentUrl.match(regexPattern);
    if (matches && matches.length > 1) {
        return matches[1];
    }

    return null;
}

function fetchTrailPath(trailId) {
    // Make an AJAX request to fetch trail data from the server
    fetch(`/trail_tracking//api/trail/${trailId}/path/`)
        .then(response => response.json())
        .then(data => {
            trailPath.addData(data);
            map.fitBounds(trailPath.getBounds());
        })
        .catch(error => {
            console.error('Error fetching trail path:', error);
        });
}

// Call the initializeMap function when the document is ready
document.addEventListener('DOMContentLoaded', initializeMap);

document.getElementById('stop-link').addEventListener('click', toggleRecording);
