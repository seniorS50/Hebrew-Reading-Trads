    // var map = L.map('map').setView([35, 34], 4);
    // L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    // maxZoom: 19,
    // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    // }).addTo(map);
    // let cityJSON = fetch('./static/city_locs.json')
    // .then((resp) => resp.json())
    // .then((data) => {
    //     console.log(data);
    //     for (i = 0; i < data.length; i++){
    //         let city_name = data[i]['City'];
    //         let country_name = data[i]['Country']
    //         var marker = L.marker([data[i]['Latitude'], data[i]['Longitude']]).addTo(map)
    //         .bindPopup(country_name +'<br>' + city_name)
    //         // Rather than show popup on click, simply show it on mouseover. This way when we click we can search
    //         .on('mouseover', function (e) {
    //             this.openPopup();
    //         });
    //         // Close popover on mouse out
    //         marker.on('mouseout', function (e) {
    //             this.closePopup();
    //         })
    //         .on("click", function(){
    //             window.location = "search?q=" + city_name
    //         });
    //     }
    // });

    