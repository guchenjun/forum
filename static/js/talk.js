function f(n){
    str = window.location.href;
    if(str.indexOf("post") == -1){
        a ='../../static/arclist/' + n + '.gif';
    }else{
        a ='../../../static/arclist/' + n + '.gif';
    }
    $('#saytext').focus();
    document.execCommand('InsertImage', false, a);
}
function fontw(){
    document.execCommand("Bold",false,null);
}
function xieti(){
    document.execCommand("italic",false,null);
}
function underLine(){
    document.execCommand("Underline",false,null);
}
function chexiao(){
    var o = document.execCommand('undo');;

}
function f1(){
    $('#saytext').html('');
}

$(".picture").click(function(){
    $("#files").click();
})

$('.emotion').click(function(){
    $('.emotion_tab').removeClass('tab_visible');
    $('.transparent').css('display','block');
})
$('.emotion_tab').click(function(){
    $('.emotion_tab').addClass('tab_visible');
})
$('.talk_box').click(function(){
    $('.emotion_tab').addClass('tab_visible');
})
$('.reply-btn').click(function(){
    $.ajax({
        type:"POST",
        url:"../reply/",
        data:{"content": $(".talk_box").html(), "thread_id": $(".thread-id").html(), "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val()},
        error:function (e) {
            alert("回复失败")
        },
        success:function (result) {
            alert("回复成功");
            location.reload()
        }
    })
})




function changeM(){
        var inputJ = $("#files"),
            input  = inputJ[0],
            Con    = $(".talk_box");

        inputJ.change(function(e){
            var files     = e.target.files,//拿到file数组
                thisSrc   = '';//当前的地址

            for(var i = 0; i < files.length; i++ ){
                thisSrc = URL.createObjectURL(files[i]);

                //文件加载成功后渲染
                $('<img>').attr('width','30%').attr('src',thisSrc).load(function(){
                    Con.append( this );
                    URL.revokeObjectURL(thisSrc);//释放内存
                });

            }
        });
    }//
changeM();