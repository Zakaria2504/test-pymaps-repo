import folium

# Coordinates for the temples (latitude, longitude)
temple_locations = [
    {"name": "Tirumala Venkateswara Temple", "coordinates": [13.6784, 79.3527]},
    {"name": "Meenakshi Temple", "coordinates": [9.9195, 78.1193]},
    {"name": "Golden Temple", "coordinates": [31.6200, 74.8765]},
    {"name": "Kedarnath Temple", "coordinates": [30.7352, 79.0669]},
    {"name": "Somnath Temple", "coordinates": [20.8900, 70.4019]}
]

# Generate the HTML content with a search box, current location, and Leaflet map
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Temple Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        #map { height: 90vh; width: 100%; }
        #search-box { position: absolute; top: 10px; left: 50%; transform: translateX(-50%); z-index: 1000; }
    </style>
</head>
<body>
    <div id="search-box">
        <input type="text" id="temple-search" placeholder="Enter temple name...">
        <button onclick="searchTemple()">Search</button>
    </div>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // Initialize map
        var map = L.map('map').setView([13.6784, 79.3527], 5);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18
        }).addTo(map);

        // Temple markers
        var markers = {
            "Tirumala Venkateswara Temple": [13.6784, 79.3527],
            "Meenakshi Temple": [9.9195, 78.1193],
            "Golden Temple": [31.6200, 74.8765],
            "Kedarnath Temple": [30.7352, 79.0669],
            "Somnath Temple": [20.8900, 70.4019]
        };

        for (var temple in markers) {
            L.marker(markers[temple]).addTo(map).bindPopup(temple);
        }

        // Add current location as a blue dot
        function addCurrentLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    var currentLocation = [position.coords.latitude, position.coords.longitude];
                    L.circleMarker(currentLocation, {
                        radius: 8,
                        color: 'blue',
                        fillColor: 'blue',
                        fillOpacity: 0.8
                    }).addTo(map).bindPopup("You are here").openPopup();
                    map.setView(currentLocation, 12);
                }, function () {
                    alert("Unable to retrieve your location.");
                });
            } else {
                alert("Geolocation is not supported by your browser.");
            }
        }

        addCurrentLocation();

        // Search functionality
        function searchTemple() {
            var templeName = document.getElementById("temple-search").value;
            if (markers[templeName]) {
                map.setView(markers[templeName], 15);
                L.popup().setLatLng(markers[templeName]).setContent(templeName).openOn(map);
            } else {
                alert("Temple not found!");
            }
        }
    </script>
</body>
</html>"""

# Write the HTML to a file
with open("temple_map.html", "w") as file:
    file.write(html_content)

print("Map with temple locations, search functionality, and current location detection as a blue dot has been created and saved as 'temple_map.html'.")