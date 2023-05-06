$(() => {
    const url = "https://www.fourtonfish.com/hellosalut/?"
    $("INPUT#btn_translate").click(() => {
        $.get(url + $.param({lang: $("INPUT#language_code").val()}), (data) => {
            $("DIV#hello").html(data)
        })
    });
    $("NPUT#language_code").submit(() => {
        $.get(url + $.param({lang: $("INPUT#language_code").val()}), (data) => {
            $("DIV#hello").html(data)
        })
    });
})
