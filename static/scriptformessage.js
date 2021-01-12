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

function focusonme() {
    ele = document.getElementById("footer")
    if (screen.width < 800) {
        ele.style.bottom = '-100px'
    }
}

function bluronme() {
    document.getElementById("footer").style.bottom = '0px'
}