$(document).ready(function () {
    comment_container();
})

function comment_container(){
    document.getElementById("comment_container").style.overflowY = "auto";

}

//comment input값을 서버로 보낸다
function comment_post() {
    let comment_input = $('#comment_give').val();
    let db_index = $('#db_index').text();
    let cookie = document.cookie;

    $.ajax({
        type: "POST",
        url: "/community/comment_post",
        data: {comment_give : comment_input , index_give : db_index},
        success: function (response) {
            if(comment_input == ""){
            alert("내용을 입력해주시기 바랍니다!!")
            }else {
            alert(response["msg"])
            window.location.reload()}
        }
    });
}

// function comment_delete() {
//     let test = $('#test').text

//     $.ajax({
//         type: "POST",
//         url: "/community/comment_delete",
//         data: {test_give : test},
//         success: function (response) {
//             alert(response["msg"])
//             window.location.reload()}
//         }
//     });



