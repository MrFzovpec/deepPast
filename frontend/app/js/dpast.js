



function find(content) {

    $.get("http://127.0.0.1:5000/find?word=" + content,

        function(data) {
            $('#dpast__description').text(data)

            $('#dpast__description').show()
        }
    )

}

function sendHtml() {


    var xmlHttp = new XMLHttpRequest();

    my_url = window.location.href.replace()

    xmlHttp.open("GET", "http://127.0.0.1:5000/parse?url=" + my_url, false)

    xmlHttp.send();

    var words = JSON.parse(xmlHttp.response)['words']

    for (i in words) {
        document.body.innerHTML = document.body.innerHTML.replace(words[i], '<span class="dpast__content__defined">' + words[i] + '</span>');
    }

}
$(document).ready(function() {
    $(".dpast__content__defined").click(function() {
        content = $(this).html()
        info = find(content)
    })

    $('.dpast__description__hide').click(function() {
        $('#dpast__description').hide()
    })
});
