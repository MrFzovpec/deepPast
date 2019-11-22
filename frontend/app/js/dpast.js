$(".dpast__content_defined").click(function() {
    parse()
})

function parse() {

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "http://127.0.0.1:5000/?word=222")

    xmlHttp.send();

    alert(xmlHttp.responseText) ;

}
