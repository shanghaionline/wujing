$(function()
{

$(".topic_list h2").mouseover(function(event) {
$(this).parent().find("p").css({display:"none"});
$(this).next("p").css({display:"block"});
$(this).parent().find("span").removeClass("curr");
$(this).prev("span").addClass("curr");
});

$(".m1").mouseenter(function(event) {
event.preventDefault();
$(".submenu").css({display:"none"});
$(".s1").slideDown(200);
});

$(".s1").mouseleave(function(event) {
event.preventDefault();
$(".s1").slideUp(200);
});

$(".m2").mouseenter(function(event) {
event.preventDefault();
$(".submenu").css({display:"none"});
$(".s2").slideDown(200);
});

$(".s2").mouseleave(function(event) {
event.preventDefault();
$(".s2").slideUp(200);
});

$(".m3").mouseenter(function(event) {
event.preventDefault();
$(".submenu").css({display:"none"});
$(".s3").slideDown(200);
});

$(".s3").mouseleave(function(event) {
event.preventDefault();
$(".s3").slideUp(200);
});

$(".m5").mouseenter(function(event) {
event.preventDefault();
$(".submenu").css({display:"none"});
$(".s5").slideDown(200);
});

$(".s5").mouseleave(function(event) {
event.preventDefault();
$(".s5").slideUp(200);
});

$(".pic_thread").click(function(event) {
event.preventDefault();
$.blockUI({ message: $('.pic_show') });
});

$(".btn_close").click(function(event) {
$.unblockUI();
});

});