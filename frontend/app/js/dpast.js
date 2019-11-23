
$(".dpast__content_defined").click(function() {
    $('.dpast__description').text('')
    content = $(this).html()
    info = find(content)
    $('.dpast__description').text(info)

    $('.dpast__description').show()
})

$('dpast__description__hide').click(function () {
    $('.dpast__description').hide()
})


function find(content) {

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "http://127.0.0.1:5000/find?word=" + content, false)

    xmlHttp.send();

    return xmlHttp.responseText

}

function sendHtml() {
    var poems = $('.dpast').html()
    alert(poems)
    for (i = 0; i < poems.lenght; i++){
        alert(i)
    }
    // var xmlHttp = new XMLHttpRequest();
    // xmlHttp.open("GET", "http://127.0.0.1:5000/find?word=" + content, false)
    //
    // xmlHttp.send();
    //
    // return xmlHttp.responseText

}
