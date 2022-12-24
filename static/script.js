$(document).ready( function () {
    $('#myTable').DataTable();
} );

// // Let's loop through all of the rows in the document
// $(document).ready( function () {
//     var rows = $('[id=data]')
//     // Print all cities
//     for (let i = 0; i < rows.length; i++) {
//         city = rows[i].querySelector('#city').innerHTML
//         if (city=="Herat") {
//             hideRow(rows[i])
//         }
//     }

// })
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
        .on("click", function(){
            window.location = "search?q=" + city_name
        })

        // Now add to an array for easy access
        markers.push(marker)
    }
    map.fitBounds(featureGroup.getBounds());
    if (map.getZoom() > 5) map.setZoom(5)
    
    // Adding each marker to grayscale filter via css classlist
    markers.forEach(marker => {
        // makeGrayscale(marker)
    })
}

function hideRow(row) {
    if (row.style.display === "none") {
      row.style.display = "block";
    } else {
      row.style.display = "none";
    }
  }