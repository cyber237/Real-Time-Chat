
function connection(id) {
    connect = new WebSocket("ws://" + window.location.host + "/" + id + "/timeTable/");
    connect.onmessage(function(message){
        var data=message.data;
        unpackData(data);
    });
}
