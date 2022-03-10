function toggle_sign_up() {
    $("#help-id-login").toggleClass("is-hidden")
    $("#help-password-login").toggleClass("is-hidden")
}


function sign_in() {
    let username = $("#input-username").val()               // id값을 읽어옴.
    let password = $("#input-password").val()               // pw값을 읽어옴.

    if (username == "") {
        $("#help-id-login").text("아이디를 입력해주세요.")     // 아이디의 값들이 빈 값인지 아닌지 검사. -> ""(아이디 창이 비어 있으면) text를 보여줌.
        $("#input-username").focus()
        return;
    } else {
        $("#help-id-login").text("")
    }

    if (password == "") {
        $("#help-password-login").text("비밀번호를 입력해주세요.")   // 비밀번호의 값들이 빈 값인지 아닌지 검사. -> ""(pw 창이 비어 있으면) text를 보여줌.
        $("#input-password").focus()
        return;
    } else {
        $("#help-password-login").text("")
    }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('token', response['token'], {path:'/'});
                window.location.href= '/main'

            } else {
                alert(response['msg'])
            }
        }
    });
}