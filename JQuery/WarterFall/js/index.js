class Waterfall {
    el = null;
    All_Width = 0;
    Each_Width = 0;
    col_Num = 0;
    ImgArr = [];
    img_length = 0;
    loaded_index = 0;
    First_load = 0;
    lock = false;

    constructor(el, col_Num, First_load, Url) {
        this.el = el;
        this.All_Width = $(el).width();
        if (this.All_Width <= 640) {
            this.col_Num = 2;
        } else if (this.All_Width > 640 && this.All_Width <= 960) {
            this.col_Num = 3;
        } else if (this.All_Width > 960 && this.All_Width <= 1280) {
            this.col_Num = 4;
        } else {
            this.col_Num = col_Num;
        }
        this.Each_Width = this.All_Width / this.col_Num;
        this.url = Url;
        this.First_load = First_load;
        this.LoadData()
        this.CreateCOL()

    }
    GetShortestCOL() {
        var min = $("#WF_Col_0").height();
        var min_index = 0;
        for (let i = 0; i < this.col_Num; i++) {
            if ($("#WF_Col_" + i).height() < min) {
                min_index = i;
                min = $("#WF_Col_" + i).height();
            }
        }
        // console.log($("#WF_Col_" + min_index).height())
        return ("#WF_Col_" + min_index)
    }

    LoadData() {
        var self = this;
        $.ajax({
            url: this.url,
            type: "GET",
            dataType: "json",
            success: function (res) {
                self.ImgArr = res.ImgArr;
                self.img_length = res.ImgArr.length;
                self.InsertItem(self.First_load);
                return res
            },
            error: function (err) {
                return err
            }
        })
    }
    CreateCOL() {
        for (let i = 0; i < this.col_Num; i++) {
            let $WF_COL = `<div class="WF_Col" id="WF_Col_` + i + `"></div>`
            this.el.append($WF_COL)
        }
        $(".WF_Col").css("width", this.Each_Width + "px")
    }


    InsertItem(num) {
        if (this.lock === false) {
            var self = this;
            for (let i = 0; i < num; i++) {
                setTimeout(function () {
                    let min_dom_id = self.GetShortestCOL()
                    let index = self.loaded_index;
                    let imgsrc = self.ImgArr[index].src;
                    let imgdesc = self.ImgArr[index].desc;
                    let $WF_Item = `
                    <div class="WF_Item" id="WF_Item_` + index + `">
                    <img class="WF_Item_Img" id="WF_Item_Img_` + index + `" alt="#">
                    <p class="WF_Item_P" id="WF_Item_P_` + index + `">` + imgdesc + `</p>
                    </div> `
                    $(min_dom_id).append($WF_Item)
                    if (self.loaded_index >= self.img_length - 1) {
                        self.lock = true;
                        alert("达到底部。");
                    }
                    $("#WF_Item_Img_" + index).attr("src", imgsrc)
                    self.loaded_index++;
                }, 300 * i)
            }
        } else {
            console.log("locked")
        }
    }
    ResetWidth(int) {
        $(this.el).width(int)
        this.All_Width = $(this.el).width();
        this.Each_Width = this.All_Width / this.col_Num;
        $(".WF_Col").css("width", this.Each_Width + "px")
    }
}
$(document).ready(function () {
    var WF = new Waterfall($("#WarterFall"), 4, 16, "./api/data.json")
    var minAwayBtm = 50; // 距离页面底部的最小距离
    $(window).scroll(function () {
        var awayBtm = $(document).height() - $(window).scrollTop() - $(window).height();
        if (awayBtm <= minAwayBtm) {
            // isbool = false;
            WF.InsertItem(3)
        }
    });
    $(window).resize(function () {
        WF.ResetWidth($(window).width())
    })
})