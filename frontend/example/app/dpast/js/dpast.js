function find(content) {

    $.get("http://127.0.0.1:5000/find?word=" + content,

        function(data) {
            var text = JSON.parse(data)['text']
            title = JSON.parse(data)['title']


            $('#dpast__description__title').text(title)

            $('#dpast__description__content').html(text.replace(/dp-trans/gi, '</br>'))


            $('#chrome_dpast__description__content').html(text.replace(/dp-trans/gi, '</br>'))

            $('#dpast__description').show()
            $('#chrome_dpast__description__content').show()
        }
    )

}

function sendHtml(mode, url) {

    var xmlHttp = new XMLHttpRequest();

    my_url = window.location.href

    if (mode != "chrome") {
        xmlHttp.open("GET", "http://127.0.0.1:5000/parse?url=" + my_url, false)

        xmlHttp.send();

        var words = JSON.parse(xmlHttp.response)['words']

        for (i in words) {

            document.body.innerHTML = document.body.innerHTML.replace(words[i], '<span class="dpast__content__defined">' + words[i] + '</span>');
        }
    } else {
        $('#chrome_analyze__process').toggle()
        $('#chrome_analyze').toggle()


        xmlHttp.open("GET", "http://127.0.0.1:5000/parse_chrome?url=" + url, false)
        xmlHttp.send();
        $('#chrome_analyze__process').toggle()

        var words = JSON.parse(xmlHttp.response)['words']
        for (i in words) {

            $('#chrome_words').append('<span class="chrome_dpast__content__defined">' + words[i] + '</span></br>');


        }
        $('#chrome_words').append('<p id="chrome_dpast__description__content"></p>')

        $('#chrome_words').show()
        $('#chrome_dpast__description__content').show()
        $(".chrome_dpast__content__defined").click(function() {
            content = $(this).html()
            info = find(content)
        })

        $('#chrome__close__dpast__description').click(function() {
            $('#chrome__dpast__description').hide()
        })
    }






}



window.onload = function() {

    $(".dpast__content__defined").click(function() {
        content = $(this).html()
        info = find(content)
    })

    $('#close__dpast__description').click(function() {
        $('#dpast__description').toggle()
    })

    chrome.tabs.query({
        'active': true,
        'lastFocusedWindow': true
    }, function(tabs) {
        urla = tabs[0].url;

        sendHtml("chrome", urla)
        $('#chrome_analyze__process').toggle()
    })
};
