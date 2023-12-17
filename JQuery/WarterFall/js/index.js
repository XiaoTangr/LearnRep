
class Waterfall {
    el = null;
    Width = 0;
    col_Num = 0;
    ImgArr = [];
    col_Height = {};
    img_length = 0;
    loaded_index = 0;
    lock = false;

    constructor(el, col_Num, Url) {
        this.el = el;
        this.col_Num = col_Num;
        this.url = Url;
        this.LoadData()
        this.CreateCOL()

    }
    GetShortestCOL() {
        let min = this.col_Height[0].height;
        let min_index = 0;
        for (let i = 0; i < this.col_Num; i++) {
            if (this.col_Height[i].height < min) {
                min = this.col_Height[i].height;
                min_index = i;
            }

        }
        return this.col_Height[min_index].el;
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
                self.InsertItem();
                return res
            },
            error: function (err) {
                return -1
            }
        })
    }
    CreateCOL() {
        for (let i = 0; i < this.col_Num; i++) {
            let $WF_COL = `<div class="WF_Col" id="WF_Col_` + i + `"></div>`
            this.el.append($WF_COL)
        }
        this.UpdateHight()
    }


    // let $WF_Item = `
    //     <div class="WF_Item" id="WF_Item_`+ IntoID + ID + `">
    //     <img class="WF_Item_Img" id="WF_Item_Img_`+ IntoID + ID + `" src="` + ImgSrc + `" alt="#">
    //     <p class="WF_Item_P" id="WF_Item_P_`+ IntoID + ID + `">` + Desc + `</p>
    //     </div> `


    InsertItem() {
        if (this.lock === false) {
            for (let i = 0; i < 3 * this.col_Num; i++) {

                let index = this.loaded_index;
                if (this.loaded_index >= this.img_length) {
                    this.lock = true;
                    break;
                }
                let imgsrc = this.ImgArr[index].src;
                let imgdesc = this.ImgArr[index].desc;
                let $WF_Item = `
                    <div class="WF_Item" id="WF_Item_`+ index + `">
                    <img class="WF_Item_Img" id="WF_Item_Img_`+ index + `" src="` + imgsrc + `" alt="#">
                    <p class="WF_Item_P" id="WF_Item_P_`+ index + `">` + imgdesc + `</p>
                    </div> `
                this.UpdateHight()
                $(this.GetShortestCOL()).append($WF_Item)
                this.loaded_index++;
            }
        } else {
            console.log("locked")
        }
    }

    UpdateHight() {
        for (let i = 0; i < this.col_Num; i++) {
            let newdata = {
                "height": $("#WF_Col_" + i).height(),
                "el": "#WF_Col_" + i
            }
            this.col_Height[i] = newdata
        }
    }
}

$(document).ready(function () {
    var WF = new Waterfall($("#WarterFall"),2, "./api/data.json")


    $(window).scroll(function () {
        if ($(window).scrollTop() + $(window).height() >= $(document).height() * 0.45) {
            if (WF.lock === false) {
                WF.InsertItem()
            }
        }
    });
})