function find(content) {

    $.get("http://127.0.0.1:5000/find?word=" + content,

        function(data) {
            var text = JSON.parse(data)['text']
            title = JSON.parse(data)['title']

            $('#dpast__description__title').text(title)
            $('#dpast__description__content').text(text)

            $('#chrome_dpast__description__title').text(title)
            $('#chrome_dpast__description__content').text(text)

            $('#dpast__description').show()
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

        alert(words)

        for (i in words) {

            document.body.innerHTML = document.body.innerHTML.replace(words[i], '<span class="dpast__content__defined">' + words[i] + '</span>');
        }

        $('#chrome_words').toggle()
    }






}



$(document).ready(function() {

    // SDK script
    $(".dpast__content__defined").click(function() {
        content = $(this).html()
        info = find(content)
    })

    $('#close__dpast__description').click(function() {

        $('#dpast__description').toggle()
    })

    //chrome script

    $(".chrome__dpast__content__defined").click(function() {
        content = $(this).html()
        info = find(content)
    })

    $('#chrome__close__dpast__description').click(function() {
        $('#chrome__dpast__description').hide()
    })
    $('#chrome_analyze').click(function() {
        chrome.tabs.query({
            'active': true,
            'lastFocusedWindow': true
        }, function(tabs) {
            url = tabs[0].url;
            sendHtml("chrome", url)

        });


    })

});
