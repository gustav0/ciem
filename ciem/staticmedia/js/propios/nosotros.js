$(document).ready(function(){
    $("#slideUno").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 230,     // automatically calculated
        height      : 189,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 230,     //  automatically calculated
            height          : 189     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 500
        },
        auto        : {
            play            : true,
            timeoutDuration : 4500,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });
    $("#slideDos").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 230,     // automatically calculated
        height      : 189,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 230,     //  automatically calculated
            height          : 189     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 400
        },
        auto        : {
            play            : true,
            timeoutDuration : 5000,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });
    $("#slideTres").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 230,     // automatically calculated
        height      : 189,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 230,     //  automatically calculated
            height          : 189     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 350
        },
        auto        : {
            play            : true,
            timeoutDuration : 4000,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });


});