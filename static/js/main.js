function get_src() {
    let txt = $('#src-txt').val();
    console.log('get')

    $.ajax({
        type: 'POST',
        url: '/translate',
        data: {src_txt: txt},
        success: function (response) {
            $('dest-txt-google').val(response['google_txt'])
        }
    })
}