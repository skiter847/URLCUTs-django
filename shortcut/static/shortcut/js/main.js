$(document).ready(function () {
    $(".copy-link").click(function () {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($('.link').text()).select();
        document.execCommand("copy");
        $temp.remove();
    });
    $(".copy-link-detail").click(function () {
        console.log(1)
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($('.link-detail-url p').text()).select();
        document.execCommand("copy");
        $temp.remove();
    });
});