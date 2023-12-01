$(document).ready(function () {
    let Rated = false;
    let RatedLevel = 0;
    $("#ShowImageBtn").on("click", function () {
        $("#myImage").slideToggle();
    });
    $(".star").on("mouseenter", function () {
        let index = $(this).index();

        for (var i = 0; i <= 4; i++) {
            var DomID = "#star" + (i);
            $(DomID).removeClass("star-Active");
        }
        for (var i = 0; i <= index; i++) {
            var DomID = "#star" + (i);
            $(DomID).addClass("star-Active");
        }
    })
    $(".star").on("click", function () {
        Rated = true;
        RatedLevel = $(this).index() + 1;
        console.log(RatedLevel);
        return RatedLevel;
    })
    $(".Rating_Box").on("mouseleave", function () {
        if (Rated == false) {
            for (var i = 0; i <= 4; i++) {
                var DomID = "#star" + (i);
                $(DomID).removeClass("star-Active");
            }
        } else {
            Rated = false;
        }
    })

    $("#Submit_Btn").on("click", function () {
        let MsgText = $("#Text_Input").val();

        if (MsgText) {
            let StarDom = (RatedLevel === 0) ? "未评级 " : "&#9734;".repeat(RatedLevel) + " ";
            let SubmitDom =
                `<div>   <span class="RatedStars"> ` + StarDom + `</span><span>` + MsgText + `</span></div>`
            if ($(".NoDis").length <= 0) {
                $("#Msg_Box").append(SubmitDom);
            } else {
                $("#Msg_Box").html(SubmitDom);
            }
        } else {
            alert("未输入评论！")
        }
        RatedLevel = 0;
        Rated = false;
        $(".star").removeClass("star-Active");
        $("#Text_Input").val("");
    })
    $(".AddMsg").on("click", function () {
        switch ($(this).attr("id")) {
            case "Msg1":
                $("#Text_Input").val("为中国航天事业点赞！");
                RatedLevel = 5;
                break
            case "Msg2":
                $("#Text_Input").val("努力学习，为航天事业尽力！");
                RatedLevel = 5;
                break
            default:
                break
        }
    })
});