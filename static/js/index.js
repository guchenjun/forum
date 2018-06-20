$(document).ready(init);

function init() {
    $(".link-login").click(function () {
        $(this).css("color", "lightskyblue");
        $(".link-reg").css("color", "#666");
        $(".login-cnt").removeClass("hidden");
        $(".login-cnt").addClass("show");
        $(".reg-cnt").addClass("hidden");
        $(".reg-cnt").removeClass("show");
    });
    $(".link-reg").click(function () {
        $(this).css("color", "lightskyblue");
        $(".link-login").css("color", "#666");
        $(".reg-cnt").removeClass("hidden");
        $(".reg-cnt").addClass("show");
        $(".login-cnt").addClass("hidden");
        $(".login-cnt").removeClass("show");
    });

    // 注册帐号
    $(".reg-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"../reg/",
            data:$(".reg-form").serialize(),
            error:function (e) {
                alert("注册失败!");
            },
            success:function (data) {
                alert(data);
                if(data == "注册成功!"){
                    window.location.href = "../"
                }
            }
        })
    });

    // 登录帐号
    $(".login-btn").click(function () {
        $.ajax({
            type:"POST",
            url:"../login/",
            data:$(".login-form").serialize(),
            error:function (e) {
                alert("登录失败!");
            },
            success:function (data) {
                alert(data);
                if(data == "登录成功!"){
                    window.location.href = "../forum/"
                }
            }
        })
    })
}