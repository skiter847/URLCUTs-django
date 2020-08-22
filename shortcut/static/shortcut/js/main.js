$(document).ready(function () {
    $(".copy-link").click(function () {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($('.link').text()).select();
        document.execCommand("copy");
        $temp.remove();
    });
});