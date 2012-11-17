$(document).ready(function(){
    $("#slideInicio").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 243,     // automatically calculated
        height      : 241,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 243,     //  automatically calculated
            height          : 241     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "crossfade",
            easing          : "swing",
            duration        : 1000
        },
        auto        : {
            play            : true,
            timeoutDuration : 4000,     //  5 * auto.duration
        }
    });
});