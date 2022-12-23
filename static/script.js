var grayIcon = L.icon({
    iconUrl: 'static/images/gray_marker.png',
    shadowUrl: 'static/images/marker_shadow.png',

    iconSize:     icon_size, // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});


function renderMap(cities) {
    map = L.map('map')
    var featureGroup = new L.featureGroup();
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    for(i = 0; i < cities.length; i++){
        let city_name = cities[i]['city'];
        let country_name = cities[i]['country']
        let marker = L.marker([cities[i]['lat'], cities[i]['long']], {iconUrl: 'static/images/gray_marker.png'}).addTo(map).addTo(featureGroup)
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
        });
        if(cities.length == 1) {
            marker.openPopup;
        }
    }
    map.fitBounds(featureGroup.getBounds());
    if (map.getZoom() > 5) map.setZoom(5)

}

// This functions are all solved by featuregroup

// function calcBounds(cities) {
//     // Instead of calculating the average, calculate the average of the farthest out points
//     let maxX = cities[0].lat
//     let minX = cities[0].lat
//     let maxY = cities[0].long
//     let minY = cities[0].long
//     for (let i = 0; i < cities.length; i++) {
//         let x = cities[i].lat
//         let y = cities[i].long
//         if (x > maxX) maxX = x
//         if (x < minX) maxX = x
//         if (y > maxY) maxY = y
//         if (y < minY) minY = y
//     }
//     return [[minX * 1.1, minY * 1.1], [maxX * 1.1, maxY * 1.1 ]]
// }

// function calcCenter(cities) {
//     // Instead of calculating the average, calculate the average of the farthest out points
//     let maxX = cities[0].lat
//     let minX = cities[0].lat
//     let maxY = cities[0].long
//     let minY = cities[0].long
//     for (let i = 0; i < cities.length; i++) {
//         let x = cities[i].lat
//         let y = cities[i].long
//         if (x > maxX) maxX = x
//         if (x < minX) maxX = x
//         if (y > maxY) maxY = y
//         if (y < minY) minY = y
//     }
//     return [(minX + maxX) / 2, (minY + maxY) / 2]
// }