$(document).ready(function(){
var url = window.location.href;
if (url.indexOf('?showmodal=1') != -1) {
    $("#post-6").modal('show');
}
if (url.indexOf('?showmodal=2') != -1) {
    $("#post-7").modal('show');
}
if (url.indexOf('?showmodal=3') != -1) {
    $("#post-4").modal('show');
}
if (url.indexOf('?showmodal=4') != -1) {
    $("#post-5").modal('show');
}

});
