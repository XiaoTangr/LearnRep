const { createApp, ref } = Vue

axios.get('./api/data.json').then(function (res) {
    var ViewTextDatas = ref()
    ViewTextDatas.value = res.data;
    const app = createApp({
        setup() {
            var ViewID = ref(0)
            const ChangeVID = (index, e) => {
                ViewID.value = index
                console.log(ViewID.value)
            }
            return {
                ChangeVID,
                ViewID,
                ViewTextDatas
            }
        }
    });
    app.mount('#app')
}).catch(function (error) {
    console.log(error)
})
;

