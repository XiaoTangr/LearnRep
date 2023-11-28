var ImgPalyerIndex = 0;
var ImgPalyerImgsTimer = null;
const ImgPalyer_Img_Srcs = [
    "./Assets/Imgs/001.jpg",
    "./Assets/Imgs/002.jpg",
    "./Assets/Imgs/003.jpg",
    "./Assets/Imgs/004.jpg",
];

$(document).ready(function () {
    function ImgPalyer_Auto_Init() {
        ImgPalyerImgsTimer = setInterval(function () {
            if (ImgPalyerIndex < ImgPalyer_Img_Srcs.length) {
                
                $(".ImgPalyer-ImgBox").removeClass("ImgPalyer-Point-NoTr");
            }
            if (ImgPalyerIndex === ImgPalyer_Img_Srcs.length) {
                $(".ImgPalyer-ImgBox").addClass("ImgPalyer-Point-NoTr");
                ImgPalyerIndex = 0;
            }
            ImgPalyer_Set_BG(ImgPalyerIndex);
            $(".ImgPalyer-ImgBox").css({ left: 0 - (ImgPalyerIndex) * 900 });
            $("#ImgPalyer-Point-" + ImgPalyerIndex)
                .addClass("ImgPalyer-Point-Active")
                .siblings().removeClass("ImgPalyer-Point-Active");
            ImgPalyerIndex++;
        }, 2000);
        return ImgPalyerImgsTimer;
    };
    function ImgPalyer_Auto_Stop(){
        ImgPalyerImgsTimer = clearInterval(ImgPalyerImgsTimer);
        intervalId = null;
    }

    function ImgPalyer_Set_BG(index){
        var src = "url(" + ImgPalyer_Img_Srcs[index] + ")";
        $(".ImgPalyer-OutBox").css("background-image",src);
    }

    function ImgPalyer_Init(src) {
        var imgnum = Img_Palyer_Add_Img(src);
        ImgPalyer_Add_Point();
        ImgPalyer_Auto_Init();
        return imgnum;
    }

    function ImgPalyer_Add_Point() {
        for (var index = 0; index < $(".ImgPalyer-ImgBox").children().length; index++) {
            $(".ImgPalyer-PointBox").append("<div class='ImgPalyer-Point' id='ImgPalyer-Point-" + index + "'></div > ");
        }
    }
    function Img_Palyer_Add_Img(src) {
        for (var index = 0; index < src.length; index++) {
            $(".ImgPalyer-ImgBox").append("<img src='" + src[index] + "' class='ImgPalyer-Item' id='ImgPalyer-Img-" + index + "' > ");
        }
        console.log($(".ImgPalyer-ImgBox").children().length);
        return src.length;
    }





    // 轮播图初始化
    var ImgPalyerImgsNum = ImgPalyer_Init(ImgPalyer_Img_Srcs)
    // 菜单样式监听
    $(".Menu-Item").on("mouseenter", function () {
        $(this).find(".Menu-SubItem-Box").slideDown();
        $(this).find(".el-icon,.Menu-Icon,.icon-more").css("transform", "none");
    })
    $(".Menu-Item").on("mouseleave", function () {
        $(this).find(".Menu-SubItem-Box").slideUp();
        $(this).find(".el-icon.Menu-Icon.icon-more").css("transform", "rotate(-90deg)");
    })

    $(".ImgPalyer-Point").on("mouseenter",function(){
        var index = $(this).index();
        $(this).addClass("ImgPalyer-Point-Active")
        .siblings().removeClass("ImgPalyer-Point-Active");
        $(".ImgPalyer-ImgBox").removeClass("ImgPalyer-Point-NoTr");
        ImgPalyer_Set_BG(index)
        $(".ImgPalyer-ImgBox").css({ left: 0 - index * 900 });
        ImgPalyerIndex = index + 1;
        ImgPalyer_Auto_Stop()
    })
    $(".ImgPalyer-Point").on("mouseleave", function () {
        ImgPalyer_Auto_Init();
    })
    $("#ToCMSE").on("click", function(){
        window.open("https://www.cmse.gov.cn/")
    })
    $("#ToSCAVC").on("click", function(){
        window.open("https://www.scavc.com/")
    })
});
