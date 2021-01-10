var element = document.getElementById("inbox_msg");

function refresh() {
    $.ajax({
        url: "",
        success: function(data) {
            if ($(".mesgs > div").length == $('.mesgs > div', data).length) {
                element.scrollTop = element.scrollHeight
            } else {
                // if (element.scrollTop != element.scrollHeight) {
                //     $('#inbox_msg').replaceWith($('#inbox_msg', data));
                //     element.scrollTop = element.scrollHeight
                //     console.log("not at the bottom")
                // } else {
                //     $('#inbox_msg').replaceWith($('#inbox_msg', data));
                //     element.scrollTop = element.scrollHeight
                //     console.log("at the bottom")
                // }
                document.getElementById("sessionexpiremodalbutton").click()
                clearInterval(myVar)
            }
        }
    });
}

$(function() {
    myVar = setInterval('refresh()', 1000);
});