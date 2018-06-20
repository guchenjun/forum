$(".bk-img-fold-1").click(function(){
	var display = $(".bk-content-1").css('display');
	if(display != 'none'){
		$(".bk-content-1").hide();
	}else{
		$(".bk-content-1").show();
	}
});
$(".bk-img-fold-2").click(function(){
	var display = $(".bk-content-2").css('display');
	if(display != 'none'){
		$(".bk-content-2").hide();
		$(".bk-title-b").css('border','solid 1px #bbb');
	}else{
		$(".bk-content-2").show();
		$(".bk-title-b").css('border','');
	}
});
$(".bk-img-fold-3").click(function(){
	var display = $(".bk-content-3").css('display');
	if(display != 'none'){
		$(".bk-content-3").hide();
	}else{
		$(".bk-content-3").show();
	}
});
