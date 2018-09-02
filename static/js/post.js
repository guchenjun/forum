$(init);

function init() {
    $(".post-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"./",
            data:{"title": $(".post-title-ipt").val(), "content": $(".talk_box").html(), "cat_id": $(".cat_id").val(), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val()},
            error:function (e) {
                alert("发帖失败")
            },
            success:function (data) {
                alert(data);
                window.location.href=document.referrer;
            }
        })
    });
}