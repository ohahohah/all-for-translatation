function autotranslate() {
    let txt = $('#src-txt').val();
    console.log(txt)
    console.log('test function')

    $.ajax({
        type: 'POST',
        url: '/translate',
        data: {src_txt: txt},
        success: function (response) {
            console.log(response['google_txt'])
            $('#dest-txt-google').text(response['google_txt'])
        }
    })

}