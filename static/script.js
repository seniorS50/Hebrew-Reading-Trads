$(document).ready(function() {
    // Rather than let DataTables do the ajax, which is annoying, why don't we do it?
    $('#myTable').DataTable({
      "ajax": {
        "url": "/api/all",
        "dataSrc": "data"
      },
      "columns": [
        { "data": "country" },
        { "data": "city" },
        { "data": "ref" },
        { "data": "reader" },
        { "data": "year" },
        { "data": "HULTP" },
      ],
      // Set up the last column as the hyperlink to the listen. TODO: Turn into a button and a GET request
      "columnDefs": [ {
        "targets": 6,
        "data": "HULTP",
        "render": function ( data ) {
            return '<a href="/listen?HULTP='+ data+'">Play</a>';
        }
      },
     ]
    })
    .on( 'search.dt', function () {
        console.log("Search was fired");
    } );
  })
  


function makeGrayscale(marker) {
    marker._icon.classList.add('grayscale')
}


function renderMap(cities) {
    map = L.map('map')
    var featureGroup = new L.featureGroup();
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    // Create an array of all of our markers for easier access
    var markers = []
    for(i = 0; i < cities.length; i++){
        let city_name = cities[i]['city'];
        let country_name = cities[i]['country']
        let marker = L.marker([cities[i]['lat'], cities[i]['long']]).addTo(map).addTo(featureGroup)
        .bindPopup(country_name +'<br>' + city_name)
        // Rather than show popup on click, simply show it on mouseover. This way when we click we can search
        .on('mouseover', function (e) {
            this.openPopup();
        })
        // Close popover on mouse out
        .on('mouseout', function (e) {
            this.closePopup();
        })
        .on("click", function(e){
            // Re-render table with AJAX
            // Clear table using DataTables.js
            let table = $('#myTable').DataTable();
            table
                .search( city_name )
                .draw();
            console.log(table.ajax.json())
            // If we're already centered, zoom in again
            map.setView(marker.getLatLng(), 5)
            // TO DO: continue to zoom in on repeated clicks
            for (let i = 0; i < markers.length; i++) {
                makeGrayscale(markers[i])
            }
            // But not our marker:)
            marker._icon.classList.remove('grayscale')

        })
        // Now add to an array for easy access
        markers.push({cityInfo: cities[i], marker: marker})
    }
    map.fitBounds(featureGroup.getBounds());
    if (map.getZoom() > 5) map.setZoom(5)
    
    // Adding each marker to grayscale filter via css classlist
    markers.forEach(marker => {
        // makeGrayscale(marker)
    })
}
