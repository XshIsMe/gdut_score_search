function refresh_verify_code() {
    $.ajax({
        type: 'GET',
        dataType: 'text',
        url: '/refresh_verify_code/',
        success: function (result) {
            $('#verify_code_img').attr("src", result);
        },
    });
}

function print_score(datas) {
    datas = eval('(' + datas + ')');
    for (i = 0; i < datas['rows'].length; i++) {
        kcmc = datas['rows'][i]['kcmc'];
        zcj = datas['rows'][i]['zcj'];
        cjjd = datas['rows'][i]['cjjd'];
        xf = datas['rows'][i]['xf'];

        document.getElementById('score').innerHTML += `
            <tr>
                <td>`+ kcmc + `</td>
                <td>`+ zcj + `</td>
                <td>`+ cjjd + `</td>
                <td>`+ xf + `</td>
            </tr>
        `;
    }
    document.getElementById('avg_score').innerHTML = `
        <button class="btn btn-info" type="button">
            平均绩点：<span class="badge">` + datas['avg_score'] + `</span>
        </button>
    `;
}

$('form').submit(function () {
    $.ajax({
        type: 'POST',
        dataType: 'text',
        url: '/',
        data: $('form').serialize(),
        success: function (result) {
            print_score(result);
            refresh_verify_code();
        },
        error: function (result) {
            alert(result.responseText);
            refresh_verify_code();
        },
    });
    return false;
});

window.onload = function () {
    $('#verify_code_img').click(function () {
        refresh_verify_code();
    });
    refresh_verify_code();
}