
function initMap() {
  var myLatLng = {lat: 40.595311, lng: 22.950956};

  var map = new google.maps.Map(document.getElementById('map-container'), {
  zoom: 12,
  center: myLatLng
});

  var marker = new google.maps.Marker({
  position: myLatLng,
  map: map,
  title: 'OK!THESS'
});

}
