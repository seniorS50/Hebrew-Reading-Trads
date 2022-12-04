//const json = open('/city_locs.json')
//const cities = JSON.parse(json);
//console.log(cities[1]['Latitude'])

import code from './city_locs.json' assert {type: 'json'};
console.log(code[1]['Latitude'])