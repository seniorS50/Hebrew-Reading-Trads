// Load the data   
// var cities = []
// fetch('./static/city_locs.json')
//     .then((resp) => resp.json())
//     .then((data) => {
//         for(let i = 0; i < data.length; i++)    {
//             cities.push(data[i]);
//         }
// }).then(console.log(cities));

function buildTable(entries) {
    var table = document.getElementById("myTable")
    for (let i = 0; i < entries.length; i++)    {
        // TODO: add listen functionality
        var row = `<tr>
                <td>${entries[i].country}</td>
                <td>${entries[i].city}</td>
                <td>${entries[i].book}</td>
                <td>${entries[i].ref}</td>
                <td>${entries[i].reader}</td>
                <td>${entries[i].year}</td>
                <td>${entries[i].HULTP}</td>
            </tr>
        `
        table.innerHTML += row
    }

}

function render_map(cities)   {
    map = L.map('map').setView([37.5, 37.5], 3);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    for(i = 0; i < cities.length; i++){
        let city_name = cities[i]['city'];
        let country_name = cities[i]['country']
        let marker = L.marker([cities[i]['lat'], cities[i]['long']]).addTo(map)
        .bindPopup(country_name +'<br>' + city_name)
        // Rather than show popup on click, simply show it on mouseover. This way when we click we can search
        .on('mouseover', function (e) {
            this.openPopup();
        });
        // Close popover on mouse out
        marker.on('mouseout', function (e) {
            this.closePopup();
        })
        .on("click", function(){
            window.location = "search?q=" + city_name
        });
        if(cities.length == 1) {
            marker.openPopup;
        }
    }
    if(cities.length == 1) {
        map.setView([cities[0]['lat'], cities[0]['long']],5);
    }
}
