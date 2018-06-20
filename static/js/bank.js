$(init);

function init() {
    $(".deposit-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"./deposit/",
            data:{"deposit_amount": $("#post").val(), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val()},
            error:function (e) {
                alert("存款失败")
            },
            success:function (data) {
                alert(data);
                window.location.reload()
            }
        })
    });

    $(".withdraw-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"./withdraw/",
            data:{"withdraw_amount": $("#get").val(), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val()},
            error:function (e) {
                alert("取款失败")
            },
            success:function (data) {
                alert(data);
                window.location.reload()
            }
        })
    });

    $(".transfer-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"./transfer/",
            data:{"transfer_to": $("#transfer_name").val(), "transfer_amount": $("#transfer_much").val(), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val()},
            error:function (e) {
                alert("转账失败")
            },
            success:function (data) {
                alert(data);
                window.location.reload()
            }
        })
    });
}