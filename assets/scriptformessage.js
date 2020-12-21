function refresh() {
    $.ajax({
        url: "",
        success: function(data) {
            if ($(".mesgs > div").length == $('.mesgs > div', data).length) {} else {
                var element = document.getElementById("inbox_msg");
                if (element.scrollTop != element.scrollHeight) {
                    $('#inbox_msg').replaceWith($('#inbox_msg', data));
                    console.log("not at the bottom")
                } else {
                    $('#inbox_msg').replaceWith($('#inbox_msg', data));
                    element.scrollTop = element.scrollHeight
                    console.log("at the bottom")
                }
            }
        }
    });
}

$(function() {
    setInterval('refresh()', 1000);
});