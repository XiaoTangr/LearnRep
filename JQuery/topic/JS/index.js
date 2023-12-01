const DEV = true;
// 准备数据
var NowCo;
var ListDirection = "TB";
var Data = {};
var MsgData = [];
// 首次启动的模板数据
var TemplateData = {
    "model": "Dark",
    "datas": [
    ]
};






/**
 * 加载存储的数据
 */
function LoadData() {
    if (localStorage.getItem("data") != null) {
        Data = JSON.parse(localStorage.getItem('data'));
        MsgData = Data.datas;
        if (MsgData.length === 0) {
            console.log("Data Init!")
            InitData()
            LoadColor();
        }
    } else {
        InitData();
        console.log("No Datas!")

    }
}
/**
 * 保存数据到本地
 */
function SaveData() {
    Data.datas = MsgData;
    localStorage.setItem('data', JSON.stringify(Data))
}

/**
 * 数据初始化
 */
function InitData() {
    localStorage.setItem('data', JSON.stringify(TemplateData))
}

/**
 * 删除数据
 */
function DelData() {
    localStorage.removeItem('data')
}


/**
 * 遍历Json对象，创建DOM，加载数据内容
 */
function loadDOM() {
    LoadData();
    $("#text_display_inbox").html("");
    if (ListDirection === "BT") {
        for (var i = MsgData.length - 1; i >= 0; i--) {
            var BaseDOM =
                "<div class=\"text_dis_item\" id=\"item" + i + "\">"
                + MsgData[i].time + "<br>"
                + "@" + MsgData[i].username + "<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                + MsgData[i].usertext
                + "</div>"
                // +"<div class=\"line\"></div>"
                ;
            $("#text_display_inbox").append(BaseDOM);
        }
    } else {
        for (var i = 0; i < MsgData.length; i++) {
            var BaseDOM =
                "<div class=\"text_dis_item\" id=\"item" + i + "\">"
                + MsgData[i].time + "<br>"
                + "@" + MsgData[i].username + "<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                + MsgData[i].usertext
                + "</div>"
                // +"<div class=\"line\"></div>"
                ;
            $("#text_display_inbox").append(BaseDOM);
        }
    }

    if (MsgData.length === 0) {
        $("#text_display_inbox").append("<div class=\"text_dis_item\"><center>暂无留言，从下面添加一条吧~</center></div>");
    }
}


function ChangDirection() {
    if (ListDirection === "BT") {
        ListDirection = "TB";
        $("#Btn_list").text("倒序")
    } else {
        ListDirection = "BT";
        $("#Btn_list").text("正序")
    }
    loadDOM();
}

/**
 * 加载颜色
 */
function LoadColor() {
    NowCo = Data.model;
    $("body").attr("class", NowCo);
    $("#Btn_mod").text(NowCo);
}

/**
 * 改变主题颜色
 */
function ChangeColor() {
    switch (NowCo) {
        case "Dark":
            NowCo = "Light";
            break;
        case "Light":
            NowCo = "Dark";
            break;
        default:
            NowCo = "Light";
            break;
    }
    $("body").attr("class", NowCo);
    $("#Btn_mod").text(NowCo);
    SaveColor();
}

/**
 * 保存颜色主题
 */
function SaveColor() {
    Data.model = NowCo;
    SaveData();
}

/**
 * 撤回上一条留言
 */
function DelLastMsg() {
    $(".alert_outbox").css("display", "none");
    MsgData.pop();
    SaveData();
    loadDOM();
}

/**
 * Ajax方法从Api获取背景，解析后设置背景
 */
function LoadBG() {
    $.ajax({
        type: "GET",
        url: "https://bing.biturl.top",
        data: {
            "resolution": 1920,
            "format": "json",
            "mkt": "zh-CN",
        },
        dataType: "JSON",
        success: function (result) {
            // result = JSON.parse(result);
            $(".BG").css("background-image", "url(" + result.url + ")");
            $("#bg-info").text("背景信息：" + result.copyright)
            window.bg_url = result.copyright_link;
        },
        error: function (result) {
            alert("获取背景失败: "+ result);
        }
    });
}


/**
 * When HTML ok
 */
$(document).ready(function () {
    // 加载DOM、颜色主题、背景图片
    loadDOM();
    LoadColor();
    LoadBG();

    // JQuery方法改变样式，鼠标移入添加样式
    $("#text_display_inbox").on("mouseover", ".text_dis_item", function () {
        printd("%s", MsgData.length - 1);
        $(this).css("background", "var(--EL-NOL_H)")
        $(this).css("border", " 1px solid var(--EL-ACT)");
        $(this).css("backdrop-filter", "blur(1em)");
        $(this).css("-webkit-backdrop-filter", "blur(1em)");
    })

    // JQuery方法改变样式，鼠标移出删除样式
    $("#text_display_inbox").on("mouseout", ".text_dis_item", function () {
        printd("%s", MsgData.length - 1);
        $(this).css("background", "none");
        $(this).css("border", " none");
        $(this).css("backdrop-filter", "none");
        $(this).css("-webkit-backdrop-filter", "none");
    })

    // 留言按钮点击事件
    $("#Btn_pul").on("click", function () {
        var username = $("#user_name_input").val();
        var usertext = $("#user_text_input").val();
        if (username != "" && usertext != "") {
            MsgData.push(
                {
                    "time": new Date().toLocaleString(),
                    "username": username,
                    "usertext": usertext
                }
            );
            SaveData();
            loadDOM();
        } else {
            alert("用户名或留言内容为空！");
        }
        return false;
    })

    // 撤回按钮点击事件
    $("#Btn_del").on("click", function () {
        if (confirm("撤回上一条留言？")) {
            DelLastMsg()
        }
        return false;
    })
    // 切换顺序按钮按下
    $("#Btn_list").on("click", function () {
        ChangDirection()
    });
    // 颜色主题按钮点击事件
    $("#Btn_mod").on("click", function () {
        // DelData();
        ChangeColor();
    })

})

/**
 * 打印重定向
 * @param {*} format 格式化字符串
 * @param  {...any} args 变量序列
 */
function printd(format, ...args) {
    var formattedString = format.replace(/\%s/g, function (match) {
        return args.shift().toString();
    });
    formattedString = formattedString.replace(/\%d/g, function (match) {
        return args.shift();
    });
    if (DEV) {
        console.log(formattedString);
    }

}
function printf(format, ...args) {
    var formattedString = format.replace(/\%s/g, function (match) {
        return args.shift().toString();
    });
    formattedString = formattedString.replace(/\%d/g, function (match) {
        return args.shift();
    });
    console.log(formattedString);
}