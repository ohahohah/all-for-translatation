function autotranslate() {
    let txt = $('#src-txt').val();

    $.ajax({
        type: 'POST',
        url: '/translate',
        data: {src_txt: txt},
        success: function (response) {
            $('#dest-txt-google').text(response['google'])
            $('#dest-txt-papago').text(response['papago'])
        }
    })
}