function chatText(elt) {
  var appendElt = document.createElement("p");
  var appendText = document.createTextNode(elt);
  appendElt.appendChild(appendText);
  $("#chat").append(appendElt);
}

$('#button').on('click', function(){
    $("#chat").append(chatText("Utilisateur : " + $('input[name="search"]').val()));
});

function initMap(lat, lng) {
    var myLatLng = {lat: lat, lng: lng};
    var map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 15
    });
    var marker = new google.maps.Marker({
        map: map,
        position: myLatLng
     });
}

var addressGoogle = "";

$(function(){
    $('#button').on('click', function(event){
        $.getJSON($SCRIPT_ROOT + '/_google_map', {
                user_search : $('input[name="search"]').val()},
            function(data){
                if (data === 'Error'){
                    chatText("GrandPy Bot (perplexe) : Je ne trouve aucun résultat...");
                } else {
                    var lat = Number(data[0]);
                    var lng = Number(data[1]);
                    var address = data[2];
                    addressGoogle = address;
                    chatText("GrandPy Bot : " + address);
                    initMap(lat, lng);
                    wikiContent();
                }
            }
        );
        return false;
    });
});

var wikiContent = function(event){
    $.getJSON($SCRIPT_ROOT + '/_wiki', {
            address : addressGoogle},
        function(data){
            chatText(data);
        });
    return false;
};

